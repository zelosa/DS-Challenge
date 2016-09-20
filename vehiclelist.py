
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from sys import argv
import time
import csv
import lxml.html
import unicodedata

def vehiclelist(br):  
    makelist = []
    vehiclemake = []
    vehiclemodel = []
    vehicleclass = []
    tablebody = br.find_element_by_xpath('//*[@id="box-table-a"]/tbody')
    tablerows = tablebody.find_elements_by_tag_name("tr")
    for tablerow in tablerows:
        tablerow_tdcells = tablerow.find_elements_by_tag_name("td")
        #print 'Vehicle:'
        for i, e in enumerate(tablerow_tdcells):
          if i == 0:
            vehiclemake.append(e.text)
          if i == 1:
            vehiclemodel.append(e.text)
          if i == 2:
            vehicleclass.append(e.text)
          #print i, e.text
        for tdcell in tablerow_tdcells: #for each of the  len(tablerow_tdcells) 3
          cells = tdcell.text + '\t'
          makelist.append(cells)
          #print 'element.text: {0}'.format(tdcell.text)      
    f = open('model.csv', 'w') #missing values before 2014...6/13/14
    for i in xrange(len(vehiclemodel)):
        f.write("{}\n".format(vehiclemodel[i]))
    f.close()

    g = open('class.csv', 'w') #missing values before 2014...6/13/14
    for i in xrange(len(vehicleclass)):
        g.write("{}\n".format(vehicleclass[i]))
    g.close()

    h = open('make.csv', 'w') #missing values before 2014...6/13/14
    for i in xrange(len(vehiclemake)):
        h.write("{}\n".format(vehiclemake[i]))
    h.close()

if __name__ == '__main__':
    browser = webdriver.Firefox() 
    browser.get('http://driveubernyc.com/vehicles/full-list/')   
    for i in range(3): 
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    vehiclelist(browser)
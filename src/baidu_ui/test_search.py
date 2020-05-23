# coding = utf-8
import pytest
import xlrd
from selenium import webdriver
from time import sleep, ctime
import os
import sys
sys.path.append("D:\\python3\\项目\\demo\\src\\baidu_ui")
from const import *


class Test_baidu_search():
    def test_search_from_excel(self, EXCEL_DIR=EXCEL_DIR):

        driver = webdriver.Firefox()
        driver.get("http://www.baidu.com")
        excel_file = xlrd.open_workbook(EXCEL_DIR)
        sheet = excel_file.sheet_by_index(0)
        cols = sheet.col_values(0)
        for query in cols:
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(str(query))
            driver.find_element_by_id("su").click()
            sleep(2)
        driver.quit()

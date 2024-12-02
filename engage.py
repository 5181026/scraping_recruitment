import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Engage:

    def scraping_recruitment(self, url_list):
        conpany_sete_exists_list = {}
        conpany_sete_not_exists_list = {}
        for url in url_list:
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            obj = BeautifulSoup(response.text, "html.parser")

    def selenilm_recruitment(self):
        list = []
        # 福岡で建築のURL
        url = "https://en-gage.net/user/search/?from=top&keyword=&companyName=&salary_0=0&span=0&PK=&token=6749b29345e90&area=50&job=500000&distanceIndex=#/"
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(7.0) #サイトを読み込むために待つ
        obj = driver.find_elements(By.CLASS_NAME , "headArea")
        for v in obj:
            print("ループ")
            print(v.find_element(By.CLASS_NAME , "category"))
            print(v.get_attribute("href"))
            list.append(v.get_attribute("href"))
        driver.quit()
        return list


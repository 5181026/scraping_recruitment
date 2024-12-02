import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class dota:
    # def recruitment_test(url):
    #     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    #     print("関数")
    #     for v in url:
    #         cnt=0
    #         response = requests.get(v , headers={"User-Agent": user_agent})
    #         print("リクエスト")
    #         response.encoding = response.apparent_encoding
    #         obj = BeautifulSoup(response.text , "html.parser")
    #         items = obj.findAll("a" , class_="jobSearchDetail-companyOverview__link")
    #         print(items)
    #         time.sleep(3.0)
    #
    #
    #         cnt += 1
    #         if cnt == 10:
    #             break



    def replace_url(self , url):
        return url.replace("-tab__pr", "-tab__jd")

    def recruitment_test(self , url):
        # url = "https://doda.jp/DodaFront/View/JobSearchList/j_pr__40/-preBtn__1/?sid=TopSearch&usrclk=PC_logout_kyujinSearchArea_searchButton_loc"
        # url = "https://doda.jp/"
        url = "https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3011489470/-tab__pr/"
        url = self.replace_url(url)

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        print("開始")
        response = requests.get(url, headers={"User-Agent": user_agent})
        print("リクエスト")
        response.encoding = response.apparent_encoding
        obj = BeautifulSoup(response.text, "html.parser")
        items = obj.findAll("a", class_="jobSearchDetail-companyOverview__link")
        print(items)


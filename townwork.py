import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import urllib.request
import re

# ページ遷移
# https://townwork.net/joSrchRsltList/?jc=036&ac=440&page=2&cursor=ABkAAQAZAAAAAAAAAAAAAAACOPH3XgEAIzfS7shhdulYZmkKFCL4y0plrwgnvkErKQMDopVwpHerS%2FgoY1HS8%2B4CKvhgH6WYKtVd1d70hpi%2FiPwq%2BzIy7JA%3D
# https://townwork.net/joSrchRsltList/?jc=036&ac=440&page=4&cursor=ABkAAgAyAAAAAAAAAAAAAAACOPH3XgEBARQFEDflmCc4lf1IUSFBVOq5JBI6ZWmfESnEDoW4liZzgLYPFFOkh9WOPLz4qHkHNPy2ckfyP7mnwY%2FWm46GTlqAb0iHZAJ%2BagsY65d8DAwXQNNR%2FoE2LEfdY0OM6Bb%2B31iXqB%2FkwopV%2Bbe0VXbCNK6%2B
class TownWork:
    # https: // townwork.net / joSrchRsltList /?jc = 036 & ac = 041
    # https: // townwork.net / joSrchRsltList /?jc = 036 & ac = 440  東京


    def scraping_recruitment_list(self , url_list):
        conpany_sete_exists_list = {}
        conpany_sete_not_exists_list = {}

        # url = "https://townwork.net/joSrchRsltList/?jc=036&ac=440"

        for url in url_list:

            response = requests.get(url)
            response.encoding = response.apparent_encoding
            obj = BeautifulSoup(response.text , "html.parser")
            conpany_url = obj.find("a" , class_="jsc-thumb-link")
            conpany_name = obj.find("h3" , class_="job-detail-ttl-txt").text
            # conpany_tel = obj.find("div" , class_="detail-tel-box").find("p" , class_="detail-tel-ttl").text
            conpany_tel = obj.find("div" , class_="detail-tel-box").text
            conpany_tel = re.search("(\d{2,4})(.*-)(.*)", conpany_tel).group()
            print("＝＝＝＝＝＝＝＝＝URL========")
            print(conpany_url)
            print("＝＝＝＝＝＝＝＝＝TEL========")
            print(conpany_tel)

            if conpany_url is None and not "営業所" in conpany_name:
                print("*************存在しない*****************")
                conpany_sete_not_exists_list[conpany_name] = url

                conpany_name = conpany_name.strip().strip("\t")
                conpany_tel = conpany_tel.strip().strip("\t")
                url = url.strip().strip("\t")
                template = \
f"""
会社名：{conpany_name.strip().strip()}
電話番号：{conpany_tel.strip()}
求人URL：{conpany_url}
"""
                self.export_text(template)
            else:
                conpany_sete_exists_list[conpany_name] = conpany_url
            time.sleep(1.5)

        print("URLが存在する：")
        print(conpany_sete_exists_list)
        print("URL存在しない")
        print(conpany_sete_not_exists_list)



    def scraping_recruitment(self , url):
        # url = "https://townwork.net/joSrchRsltList/?jc=036&ac=440"
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        obj = BeautifulSoup(response.text, "html.parser")
        site = obj.find("a", class_="jsc-thumb-link")
        print(site.text)

    def selenilm_recruitment(self):
        list = []
        url = input()
        try:
            urllib.request.urlopen(url)
        except urllib.request.HTTPError:
            print("URLが無効です")
            exit()

        # url = "https://townwork.net/joSrchRsltList/?jc=036&ac=440"

        # url = "https://townwork.net/joSrchRsltList/?jc=036&ac=440&page=40&cursor=ABkAAQAZAAAAAAAAAAAAAAACOPr7HQEBFwYEix%2F3R9osUDSiSuw6fvdS3h7M4p4Me%2FMYutr39pZlhpCIa%2BmsH8RH%2Bh2LX9Eax8pjIjnckGbFC4TE"
        # url = "https://townwork.net/joSrchRsltList/?jc=036&ac=440&page=39&cursor=ABkAAQAZAAAAAAAAAAAAAAACOPr7HQEBFwYEix%2F3R9osUDSiSuw6fvdS3h7M4p4Me%2FMYutr39pZlhpCIa%2BmsH8RH%2Bh2LX9Eax8pjIjnckGbFC4TE"
        driver = webdriver.Chrome()
        driver.get(url)
        next_flag = True
        cnt = 0
        while next_flag:
            time.sleep(2.0)
            try:
                next_btn = driver.find_element(By.CLASS_NAME, "i-btn-next")
                if not next_btn:
                    next_flag = False

                obj = driver.find_elements(By.CLASS_NAME , "job-lst-main-box-inner")
                for v in obj:
                    print(v.find_element(By.CLASS_NAME , "job-lst-main-ttl-txt").text)
                    print(v.get_attribute("href"))
                    list.append(v.get_attribute("href"))
                next_btn.click()
            except NoSuchElementException:
                break
            # break #テスト用1回で抜け出す
        driver.quit()


        return list

    def export_text(self , template):
        with open("townwork_scraping.txt" , mode="a" , encoding='utf-8') as f:
            f.write(template)
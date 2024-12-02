import urllib.request
#test
import requests
from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HelloWork:
    def scraping_recruitment_list(self , url_list):
        conpany_sete_exists_list = {}
        conpany_sete_not_exists_list = {}

        for url in url_list:
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            obj = BeautifulSoup(response.text , "html.parser")
            conpany_url = obj.find("a" , id="ID_hp")
            conpany_name = obj.find("div" , id="ID_jgshMei").text if obj.find("div" , id="ID_jgshMei") is not None  else "掲載なし"
            conpany_tel =  obj.find("div" , id="ID_ttsTel").text if obj.find("div" , id="ID_ttsTel") is not None else "掲載なし"
            ("＝＝＝＝＝＝＝＝＝企業名========")
            print(conpany_name)
            print("＝＝＝＝＝＝＝＝＝URL========")
            print(conpany_url)
            print("＝＝＝＝＝＝＝＝＝TEL========")
            print(conpany_tel)

            if conpany_url is None and not "営業所" in conpany_name:
                print("*************存在しない*****************")
                conpany_sete_not_exists_list[conpany_name] = url

                conpany_name = conpany_name.strip().strip("\t")
                conpany_tel = conpany_tel.strip().strip("\t")
                conpany_url = url.strip().strip("\t")
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



    def scraping_recruitment(self, url):
        conpany_sete_exists_list = {}
        conpany_sete_not_exists_list = {}


        response = requests.get(url)
        response.encoding = response.apparent_encoding
        obj = BeautifulSoup(response.text, "html.parser")
        conpany_url = obj.find("a", id="ID_hp")
        conpany_name = obj.find("div", id="ID_jgshMei").text if obj.find("div",
                                                                         id="ID_jgshMei") is not None else "掲載なし"
        conpany_tel = obj.find("div", id="ID_ttsTel").text if obj.find("div",
                                                                       id="ID_ttsTel") is not None else "掲載なし"
        ("＝＝＝＝＝＝＝＝＝企業名========")
        print(conpany_name)
        print("＝＝＝＝＝＝＝＝＝URL========")
        print(conpany_url)
        print("＝＝＝＝＝＝＝＝＝TEL========")
        print(conpany_tel)

        if conpany_url is None and not "営業所" in conpany_name:
            print("*************存在しない*****************")
            conpany_sete_not_exists_list[conpany_name] = url

            conpany_name = conpany_name.strip().strip("\t")
            conpany_tel = conpany_tel.strip().strip("\t")
            conpany_url = url.strip().strip("\t")
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




    def selenilm_recruitment(self):
        url_list = []
        next_flag = True
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress" , "127.0.0.1:9222")
        print("chromeドライバに接続してます")
        try:
            driver = webdriver.Chrome(options=chrome_options)
            print("Chromeドライバーに接続成功")
        except Exception as e:
            print(f"Chromeドライバへの接続に失敗しました:{e}")
            exit(1)

        try:
            while next_flag:
                time.sleep(2.0)
                try:
                    next_btn = driver.find_element(By.NAME , "fwListNaviBtnNext")
                    # obj = driver.find_element(By.ID , "ID_dispDetailBtn")
                    obj = driver.find_elements(By.CLASS_NAME , "kyujin")
                    if not next_btn or not next_btn.is_enabled():
                        next_flag = False

                    for v in obj:
                        conpany_name = v.find_element(By.CLASS_NAME , "m13").text
                        url = v.find_element(By.ID , "ID_dispDetailBtn").get_attribute("href")
                        print(conpany_name)
                        print(url)
                        # url_list.append(url)
                        self.scraping_recruitment(url)
                    next_btn.click()
                except NoSuchElementException:
                    break

                #break #テスト用
        except Exception as e:
            print(f"エラーが発生しました: {e}")

        driver.quit()
        return url_list


    def export_text(self , template):
        with open("hellowork_scraping.txt" , mode="a" , encoding='utf-8') as f:
            f.write(template)
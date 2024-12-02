# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from townwork import TownWork
from engage import Engage
from hellowork import HelloWork

def selenilm_test(url):
    list = []
    driver = webdriver.Chrome()
    driver.get(url)
    # obj = driver.find_elements(By.CLASS_NAME , "cardDetail__companyName")
    obj = driver.find_elements(By.CLASS_NAME , "jobCard-header__link")
    for v in obj:
        # print(v.find_element(By.TAG_NAME , "h2").text)
        list.append( replace_url(v.get_attribute("href")))
        # print(v.text)
    driver.quit()
    return list

def replace_url(url):
    return url.replace("-tab__pr" , "-tab__jd")





# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    # url = "https://doda.jp/DodaFront/View/JobSearchList/j_pr__40/-preBtn__1/?sid=TopSearch&usrclk=PC_logout_kyujinSearchArea_searchButton_loc"
    # url = "https://doda.jp/"
    # url = "https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3011489470/-tab__pr/"
    # url = replace_url(url)

    # town.scraping_recruitment()

    # town = TownWork()
    # url_list = town.selenilm_recruitment()
    # town.scraping_recruitment_list(url_list)


    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress" , "127.0.0.1:9222")
    # print("Chromeドライバーに接続しています")
    # try:
    #     driver = webdriver.Chrome(options=chrome_options)
    #     print("Chromeドライバーに接続成功")
    # except Exception as e:
    #     print(f"Chromeドライバーへの接続に失敗しました：{e}")
    #     exit(1)
    #
    # try:
    #     print("指定したURLに移動しています...")
    #     # 指定したURLに移動
    #     # driver.get("https://qiita.com/")
    #     print("URLに移動完了")
    #
    #     print("ページの読み込みを待機しています...")
    #     # ページが完全に読み込まれるまで待機（最大10秒）
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.TAG_NAME, "body"))
    #     )
    #     print("ページの読み込み完了")
    #
    #     # 現在のページのタイトルを取得して表示
    #     print(f"現在のページタイトル: {driver.title}")
    #
    #     # 追加のデバッグ情報
    #     print(f"現在のURL: {driver.current_url}")
    #     print(f"ページソースの長さ: {len(driver.page_source)} 文字")
    #
    # except Exception as e:
    #     print(f"エラーが発生しました: {e}")
    #
    # finally:
    #     print("スクリプトが完了しました。")
    #     # 3秒待機してからスクリプトを終了（状態を確認するため）
    #     time.sleep(3)

    # en = Engage().selenilm_recruitment()

    hello = HelloWork()
    url_list = hello.selenilm_recruitment()
    # hello.scraping_recruitment_list(url_list)




# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください

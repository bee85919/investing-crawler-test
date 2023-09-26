import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537")

def crawler():
    driver = Chrome(options=chrome_options)
    driver.get('https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::a<eq_market_cap;1')
    time.sleep(2)
    
    for i in range(1, 5):  # 예시로 4 페이지까지만 크롤링
        driver.get(f'https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::a<eq_market_cap;{i}')
        
        # 페이지가 로드되는 것을 기다림
        time.sleep(2)
        
        # XPath를 사용하여 data-column-name="viewData.symbol"과 "name_trans"을 가진 요소를 찾음
        symbols = driver.find_elements(By.XPATH, '//td[@data-column-name="viewData.symbol"]')
        names = driver.find_elements(By.XPATH, '//td[@data-column-name="name_trans"]')
        
        for symbol, name in zip(symbols, names):
            print(symbol.text, name.text)  # 각 요소의 텍스트를 쌍으로 출력

if __name__ == "__main__":
    crawler()
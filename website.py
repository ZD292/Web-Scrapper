from cgitb import html, text
from pydoc import classname
from re import search
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
import pandas as pd

Path = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(Path)

driver.get("https://www.grab.com/sg/pay/where-to-use/")
# website that we are accessing to scrap some addresses 
df = pd.read_csv(
    r"C:\Users\zhendong.ong\Desktop\01 Python Web Scrapper\01 steps\01dataset.csv")
lst = df.values.tolist()
# import csv file from excel to load as a list

for i in lst:
    search = driver.find_element(By.CLASS_NAME, "searchbar___2Ut-b")
    search.send_keys(i)
    # .return also can
    driver.find_element(
        By.CSS_SELECTOR, 'button[class="btnSearch___2Q3CK btn___2ZMWx"]').click()
    numberoutlets = driver.find_elements(By.CLASS_NAME, "merchantCard____htHl")
    time.sleep(5)
    # print(len(numberoutlets))
    for j in range(1, len(numberoutlets)+1):
        outlet = driver.find_element(
            By.XPATH, f'/html/body/div[2]/div/div/div/section/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[{j}]/div[2]/div[1]').text
        print(outlet)
        address = driver.find_element(
            By.XPATH, f'/html/body/div[2]/div/div/div/section/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div/div[{j}]/div[2]/div[2]').text
        print(address)
        driver.back()

df1 = pd.DataFrame(lst)
df1.to_excel('infodump.xlsx', sheet_name='me', header=False, index=False)

from cgitb import text
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import html, text

Path = 'C:\chromedriver.exe'
driver = webdriver.Chrome(Path)
#specify the path where driver is located

driver.get('https://free-proxy-list.net/')
# website to get free proxies
j = 1
proxies = []

while len(proxies) < 10:
    j += 1
    https = driver.find_element(
        By.XPATH, f"/html/body/section[1]/div/div[2]/div/table/tbody/tr[{j}]/td[7]").text
    if https == 'no':
        continue
    elif https == 'yes':
        ip = driver.find_element(
            By.XPATH, f'/html/body/section[1]/div/div[2]/div/table/tbody/tr[{j}]/td[1]').text
        proxies.append(ip)
    else:
        continue
driver.quit()
print(proxies)

workingproxy = []
failedproxy = []

# try out the proxies and append the working ones to a list for later use
for i in proxies:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % i)
    chrome_options.add_argument(Path)
    chrome = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='C:\chromedriver.exe')
    try:
        # chrome.get("https://www.google.com")
        # search = driver.find_element(By.NAME, 'q')
        chrome.get("https://www.grab.com/sg/pay/where-to-use/")
        # search = driver.find_element(
        # By.CSS_SELECTOR, 'button[class="btnSearch___2Q3CK btn___2ZMWx"]').click()
        # search.send_keys('hello')
        # search.send_keys(Keys.RETURN)
        workingproxy.append(i)
        print('working', {}.__format__(workingproxy))
    except:
        failedproxy.append(i)
        print('failed', {}.__format__(failedproxy))

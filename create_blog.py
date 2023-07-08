import time
import asset as ast
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


def posting(title, contents):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    chrome_options.add_argument("lang=ko_KR")
    # service = Service("./chromedriver")    
    driver = webdriver.Chrome(options=chrome_options)
    url = ast.blog_url
    driver.get(url)

    id = ast.blog_id
    pw = ast.blog_pw



    driver.find_element(By.XPATH, '//*[@id="wrap"]/header/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id="container"]/aside/div[1]/div[2]/div[2]/div[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="cMain"]/div/div/div/a[2]').click()


    driver.find_element(By.XPATH, '//*[@id="loginKey--1"]').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="password--2"]').send_keys(pw)
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="wrap"]/header/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id="container"]/aside/div[1]/div[2]/div[2]/div[2]/a[2]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="category-btn"]').click()
    driver.find_element(By.XPATH, '//*[@id="category-item-964852"]/span').click()
    driver.find_element(By.XPATH, '//*[@id="editor-mode-layer-btn-open"]').click()
    driver.find_element(By.XPATH, '//*[@id="editor-mode-markdown-text"]').click()
    da = Alert(driver)
    da.accept()

    driver.find_element(By.XPATH, '//*[@id="post-title-inp"]').send_keys(title,Keys.TAB, Keys.TAB)
    iframe=driver.find_element(By.CSS_SELECTOR, 'iframe')
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, 'tinymce').send_keys(contents)
    driver.switch_to.default_content()

    driver.find_element(By.XPATH, '//*[@id="publish-layer-btn"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="publish-btn"]').click()
    
    print(f"{title} 제목으로 블로그 글 작성이 완료되었습니다.")
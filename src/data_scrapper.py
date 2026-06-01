import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import json
import config
import logging

os.makedirs(config.OUTPUT_DIR, exist_ok=True)
logging.basicConfig(
    filename = config.LOG_PATH,
    level = logging.INFO,
    format = '%(asctime)s-%(levelname)s-%(message)ss'

)

def headlines_download(url):
 
    prefs = {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "profile.default_content_setting_values.automatic_downloads": 1,
        "profile.default_content_settings.popups": 0,
        
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--safebrowsing-disable-download-protection")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")
    chrome_options.add_argument("--headless=new")  
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--window-size=1920,1080")
    date_limit = datetime.strptime(config.DATE_LIMIT,"%B %d, %Y")
    driver = None
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    run = True
    i = 7
    content = {}
    while run:
        time.sleep(5)
        articles = driver.find_elements(By.CLASS_NAME, 'styles_container__TFaNi') 
        
        for article in articles:
            date_text =  article.find_element(By.CLASS_NAME,'styles_entry__TF29t').text
            article_date = datetime.strptime(date_text,"%B %d, %Y")
            logging.info(f"extracting article from date: {article_date}")
        
            if article_date>date_limit:
                description = article.find_element(By.CLASS_NAME,'styles_desc__hJut5')
                title = article.find_element(By.CLASS_NAME,"styles_title__1_iL8")
                content.update({title.text:description.text})
            else:
                run = False
                break
        driver.execute_script("document.body.click();")
        next_pg_button = WebDriverWait(driver,30).until(
                   EC.element_to_be_clickable((By.XPATH,f"/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[{i}]")))
        
        
        driver.execute_script("arguments[0].scrollIntoView();", next_pg_button)
        time.sleep(4)
        try:
            next_pg_button.click()
        except Exception as e:
            logging.exception(f"Error during next page navigation : {e}")
            break
        if i<9:
          i+=1                                
    driver.quit()
    logging.info(f"Total articles extracted: {len(content)}")
    return content


url_dict = {"grid":"https://www.mercomindia.com/category/grid","solar":"https://www.mercomindia.com/category/solar","wind":"https://www.mercomindia.com/category/wind"}
path = config.HEADLINES_PATH
content_path = config.SUMMARY_PATH
os.makedirs(config.OUTPUT_DIR, exist_ok=True)
if __name__ == "__main__":

    all_articles = {}
    for category, url in url_dict.items():
        logging.info(f"Starting news extraction for category:{category}")
        try:
            content = headlines_download(url)
            all_articles[category] = content
            
        except Exception as e:
            logging.exception(f"Error during article download: {e}")
    
    with open(path,"w", encoding="utf-8") as file:
        json.dump(all_articles, file, indent=4, ensure_ascii=False)


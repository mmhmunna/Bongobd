from selenium import webdriver
import time

driver = webdriver.Chrome("driver/chromedriver")
driver.maximize_window()
baseurl = "https://bongobd.com/"
driver.get(baseurl)
time.sleep(2)
driver.execute_script("window.scrollBy(0, 650)")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/div[5]/div/div[1]/div/div/div[1]/div[2]/a/button/span[1]').click()
time.sleep(2)
page_url = driver.current_url
for i in range(10):
    i = i + 1
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/div/div/div['+ str(i) +']/div/div/a/div[2]').click()
    time.sleep(8)
    if(driver.current_url == 'https://bongobd.com/register'):
        print("This video is not free")
        print(driver.current_url)
        time.sleep(1)
        #print(page_url)
        driver.get(page_url)
    else:
        print('This video is free')
        print(driver.current_url)
        driver.implicitly_wait(18)
        try:
            print('try')
            time.sleep(1)
            driver.find_element_by_class_name('videoAdUiSkipButtonExperimentalText').click()
        except:
            print('except')
            time.sleep(1)
            if (driver.find_element_by_xpath('//*[@id="vid1"]/div[4]/button[1]/span[2]').text == "Pause"):
                break
            else:
                driver.find_element_by_xpath('//*[@id="vid1"]/div[4]/button[1]').click()
                break
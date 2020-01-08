#!/usr/bin/env python
# coding: utf-8

# # Trivial Hack 

# In[2]:


import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from datetime import date,time,datetime,timedelta


# In[3]:


Today = date.today()
InitialTime = (datetime.now()-timedelta(hours=5, minutes=30)).time()
UTCthreshold = datetime.time(datetime(1999,4,19,19,30))
if(InitialTime > UTCthreshold):
    Today -= timedelta(days=1)
#Today -= timedelta(days=1)
print(Today,InitialTime)
#Today = Today.strftime("%Y-%m-%d")
#TimeRightNow = TimeRightNow.strftime("%H:%M")


# ### Run below cell before new post comes up on page above cell is useless but I don't want to delete it

# #### Fill in your own username and password

# In[7]:


driver = webdriver.Chrome()
actions = ActionChains(driver)

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher');
#id
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
element.click()
driver.find_element_by_css_selector("input[name='username']").send_keys("kneelbefore_me");
#pass
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
element.click()
driver.find_element_by_css_selector("input[name='password']").send_keys("@Uk12d1492");
#login button
driver.find_element_by_css_selector("span#react-root div:nth-child(4)").click()
#goto that page
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.instagram.com/hapiens_tribe/') #name of page   https://www.instagram.com/hapiens_tribe/

topPost = driver.find_element_by_css_selector("span#react-root article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a")
linkToPostCurrent = topPost.get_attribute("href")
linkToPostPrev = linkToPostCurrent

while(linkToPostCurrent == linkToPostPrev):
    topPost = driver.find_element_by_css_selector("span#react-root article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a")
    postedOn = datetime.now()
    linkToPostCurrent = topPost.get_attribute("href")
    if linkToPostCurrent != linkToPostPrev:
        driver.get(linkToPostCurrent)
        element = driver.find_element_by_class_name("Ypffh")
        element.click()
        driver.find_element_by_class_name("Ypffh").send_keys("A")
        driver.find_element_by_css_selector("form > button[type='submit']").click()
        print(datetime.now()-postedOn)
    else:
        print("Waiting for Update")
    driver.refresh()
driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





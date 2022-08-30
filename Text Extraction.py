#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from bs4 import BeautifulSoup


# In[71]:


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("URL")

content = driver.page_source
soup = BeautifulSoup(content)
url = (driver.current_url).replace("/","").replace(":",".")


print(driver.title)
f = open(f'{url}.txt', "w+")
f.write(soup.title.text)
for i in soup.find('div', attrs={'class':'td-post-content'}).children:
    print(i.text)
    text = i.text + '\r\n'
    f.write(text)
f.close()


# In[ ]:





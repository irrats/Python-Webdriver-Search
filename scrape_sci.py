 
  ################. RETRIEVE 3 different ID Numbers for Article

# Import packages
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import appscript

# Specify url
url = appscript.app("Safari").windows.first.current_tab.URL()
time.sleep(1)

browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
browser.implicitly_wait(1)


# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all("a", {'class':'id-link'})
#First ID from strong tag with title
pm = soup.find("strong", title=re.compile("PubMed ID")).text

#Second ID from a tag
for item in a_tags[0:1]:
    pmc = item.text.strip()
#Third id from a tag
for item in a_tags[1:2]:
    doi = item.text.strip()
# Print the URLs to the shell
print(pm, pmc, doi)

default_input = pm
browser.get('https://sci-hub.se')
field = browser.find_element_by_xpath('//*[@name="request"]')
field.send_keys(default_input)
field.send_keys(Keys.ENTER)

default_input = pm
browser.get('https://sci-hub.se')
field = browser.find_element_by_xpath('//*[@name="request"]')
field.send_keys(default_input)

url = browser.current_url

field.send_keys(Keys.ENTER)# press enter key for search

time.sleep(1) # wait for 1 second to check
#while url == browser.current_url:
    
url = browser.current_url
#print(url)

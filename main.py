import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

# https://github.com/manan2412
github_user = input('Github username: ')
url = "https://github.com/" + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
output_url = soup.find("img",{'alt': 'Avatar'})['src']
print(output_url)

driver = webdriver.Chrome()

# Fetching the Url
driver.get(output_url)
file = open("logo.ico", "wb")
file.write(requests.get(output_url).content)
file.close()
print(type(file))
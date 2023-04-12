
from requests.models import Response
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import keys 
import requests
import os
import random

driver = webdriver.Chrome(ChromeDriverManager().install()) 
url1 = 'https://google.com'

def ac1():
  driver.get(url1)
ac1()


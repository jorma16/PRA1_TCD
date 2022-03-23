from src.scrappers.scrapper import Scrapper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class DetailScrapper(Scrapper):
  def __init__(self, urls, headless=False, driver=None):
    super().__init__(headless=headless, driver=driver)

    self.urls = urls

  def fetch_price(self):
    text = self.driver.find_element(by=By.CLASS_NAME, value='re-DetailHeader-price').get_attribute('innerHTML')

    price = text.split(' ')[0]

    return price.replace('.', '')

  def fetch(self):
    list = []
    for url in self.urls:
      print(f'Fetching {url}')
      self.driver.get(url)
      price = self.fetch_price()
      obj = {
        'price': price,
        'link': url
      }

      list.append(obj)
      print(f'{url} Fetched')

    return list

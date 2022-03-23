from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_headers import Headers

class Scrapper:
  def __init__(self, headless=False, driver=None):
    DRIVER_PATH = './chromedriver_macosx'

    if driver is None:
      header = Headers(
        browser='chrome',
        os='win',
        headers=False
      )
      userAgent = header.generate()['User-Agent']
      chrome_options = Options()
      chrome_options.add_argument('--window-size=1920,1080')
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument(f'user-agent={userAgent}')

      if headless:
        chrome_options.add_argument('--headless')

      self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
    else:
      self.driver = driver

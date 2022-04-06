from selenium.webdriver.common.by import By
from time import sleep
from src.scrappers.scrapper import Scrapper


class SearchScrapper(Scrapper):
  def __init__(self, url, output, max_pages=4, headless=False, driver=None):
    super().__init__(headless=headless, driver=driver)

    self.url = url
    self.output = output
    self.max_pages = int(max_pages)

  def fetch(self):
    print(f'Fetching {self.url}')
    self.driver.get(self.url)
    print(f'{self.url} Fetched')
    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    self.driver.implicitly_wait(5)

    return self.driver.page_source

  def get_pages_number_from_header(self):
    print('Getting Pages number from header')
    el = self.driver.find_element(by=By.CLASS_NAME, value='re-SearchTitle-count')
    text = el.get_attribute('innerHTML')
    text = text.replace('.', '')
    n = int(text)
    p = min(self.max_pages, int(n/30))

    print(f'Getted {int(n/30)} pages but going to scrap {p} pages')

    return p

  def fetch_page(self, n):
    url = self.url + f'/{n}'
    print(f'Ready to fetch {url}')
    self.driver.get(url)
    print(f'{url} fetched')
    self.scroll()

    items = self.driver.find_elements_by_tag_name('article')

    list = []
    for item in items:
      i = item.find_element(By.TAG_NAME, 'a')
      href = i.get_attribute('href')
      print(f'Getted ({href})')
      list.append(href)

    return list

  def scrap(self, close=True):
    self.fetch()
    self.pages_number = self.get_pages_number_from_header()

    list = []
    for i in range(1, self.pages_number + 1):
      l = self.fetch_page(i)
      for item in l:
        if 'ad.doubleclick.net' not in item:
          list.append(item)

    print(f'Finished, returning {len(list)} elements')

    if close:
      self.driver.quit()

    return list

  def scroll(self, times=50, time=.05, px=300):
    print('Scrolling...');
    y = px
    for timer in range(0, times):
      self.driver.execute_script("window.scrollTo(0, "+str(y)+")")
      y += px
      sleep(time)
    print('Finish Scroll');


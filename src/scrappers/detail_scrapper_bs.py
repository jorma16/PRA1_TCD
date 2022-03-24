import requests
from bs4 import BeautifulSoup

class DetailScrapper():
  FAKE_HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    */*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "no-cache",
    "dnt": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5\
    37.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
  }

  @staticmethod
  def __fetch_price(url, bs):
    selector = "div > span.re-DetailHeader-price"
    price = bs.select(selector)[0].getText()
    str_replacements = {".": "", "€": "", " ": ""}
    for key, value in str_replacements.items():
      price = price.replace(key, value)

    return price

  @staticmethod
  def __fetch_bedrooms(url, bs):
    bedrooms = ""
    selector = "li.re-DetailHeader-featuresItem"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "habs." in item:
        bedrooms = item.replace(" habs.", "")
      elif "hab." in item:
        bedrooms = item.replace(" hab.", "")

    return bedrooms

  @staticmethod
  def __fetch_bathrooms(url, bs):
    bathrooms = ""
    selector = "li.re-DetailHeader-featuresItem"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "baños" in item:
        bathrooms = item.replace(" baños", "")
      elif "baño" in item:
        bathrooms = item.replace(" baño", "")

    return bathrooms
 
  @staticmethod
  def __fetch_sqm(url, bs):
    sqm = ""
    selector = "li.re-DetailHeader-featuresItem"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "m²" in item:
        sqm = item.replace(" m²", "")

    return sqm

  @staticmethod
  def __fetch_floor(url, bs):
    floor = ""
    selector = "li.re-DetailHeader-featuresItem"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "Planta" in item:
        floor = item.replace("ª Planta", "")

    return floor

  @staticmethod
  def __fetch_type(url, bs):
    type = ""
    selector = "div.re-DetailFeaturesList-featureContent > p.re-DetailFeaturesList-featureLabel"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "Tipo de inmueble" in item:
        type = items[i].nextSibling.getText()

    return type

  @staticmethod
  def __fetch_orientation(url, bs):
    orientation = ""
    selector = "div.re-DetailFeaturesList-featureContent > p.re-DetailFeaturesList-featureLabel"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "Orientación" in item:
        orientation = items[i].nextSibling.getText()

    return orientation
  
  @staticmethod
  def __fetch_condition(url, bs):
    condition = ""
    selector = "div.re-DetailFeaturesList-featureContent > p.re-DetailFeaturesList-featureLabel"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "Estado" in item:
        condition = items[i].nextSibling.getText()

    return condition

  @staticmethod
  def __fetch_hot_water(url, bs):
    hot_water = ""
    selector = "div.re-DetailFeaturesList-featureContent > p.re-DetailFeaturesList-featureLabel"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "Agua caliente" in item:
        hot_water = items[i].nextSibling.getText()

    return hot_water

  @staticmethod
  def __fetch_elevator(url, bs):
    elevator = ""
    selector = "div.re-DetailFeaturesList-featureContent > p.re-DetailFeaturesList-featureLabel"
    items = bs.select(selector)
    for i in range(len(items)):
      item = items[i].getText()
      if "Ascensor" in item:
        elevator = items[i].nextSibling.getText()

    return elevator
  
  @staticmethod
  def fetch(url):
    res = requests.get(url, DetailScrapper.FAKE_HEADER)
    bs = BeautifulSoup(res.content, "html.parser")

    obj = {
      'price': DetailScrapper.__fetch_price(url, bs),
      'bedrooms': DetailScrapper.__fetch_bedrooms(url, bs),
      'bathrooms': DetailScrapper.__fetch_bathrooms(url, bs),
      'sqm': DetailScrapper.__fetch_sqm(url, bs),
      'floor': DetailScrapper.__fetch_floor(url, bs),
      'type': DetailScrapper.__fetch_type(url, bs),
      'orientation': DetailScrapper.__fetch_orientation(url, bs),
      'condition': DetailScrapper.__fetch_condition(url, bs),
      'hot_water': DetailScrapper.__fetch_hot_water(url, bs),
      'elevator': DetailScrapper.__fetch_elevator(url, bs)
    }

    return obj

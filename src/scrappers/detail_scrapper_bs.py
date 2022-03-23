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
    bedrooms = "NA"
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
    bathrooms = "NA"
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
  def fetch(url):
    res = requests.get(url, DetailScrapper.FAKE_HEADER)
    bs = BeautifulSoup(res.content, "html.parser")

    obj = {
      'price': DetailScrapper.__fetch_price(url, bs),
      'bedrooms': DetailScrapper.__fetch_bedrooms(url, bs),
      'bathrooms': DetailScrapper.__fetch_bathrooms(url, bs)
    }

    return obj

url = "https://www.fotocasa.es/es/comprar/vivienda/valencia-capital/aire-acondicionado-calefaccion-parking-ascensor/161495104/d"
url2 = "https://www.fotocasa.es/es/comprar/vivienda/valencia-capital/no-amueblado/162369481/d"
url3 = "https://www.fotocasa.es/es/comprar/vivienda/valencia-capital/ascensor/162793279/d"
    
print(DetailScrapper.fetch(url))
print(DetailScrapper.fetch(url2))
print(DetailScrapper.fetch(url3))

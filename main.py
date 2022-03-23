#!/usr/bin/env python3

import getopt, sys
from src.scrappers.detail_scrapper import DetailScrapper
from src.scrappers.search_scrapper import SearchScrapper
from src.utils.list_to_csv import write

options = 's:o:p:Hh'

long_options = ['search', 'output', 'max_pages', 'headless', 'help']

site = f'https://www.fotocasa.es/es/alquiler/viviendas/valencia/todas-las-zonas/l'
output = 'csv'
max_pages = 3
headless = False

try:
  args = sys.argv[1:]
  arguments, values = getopt.getopt(args, options, long_options)

  for argument, value in arguments:
    if argument in ('-h', '--help'):
      print('Displaying Help')
    elif argument in ('-s', '--search'):
      site = f'https://www.fotocasa.es/es/alquiler/viviendas/{value}/todas-las-zonas/l'
    elif argument in ('-o', '--output'):
      output = value
    elif argument in('-p', '--max_pages'):
      max_pages = value
    elif argument in ('-H', '--headless'):
      headless = True
except getopt.error as err:
  print(str(err))

search = SearchScrapper(url=site, output=output, max_pages=max_pages, headless=headless)
list = search.scrap(close=False)
detail = DetailScrapper(urls=list, driver=search.driver)
objs = detail.fetch()

write(columns=['price', 'link'], data=objs)

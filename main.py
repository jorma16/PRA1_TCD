#!/usr/bin/env python3

import getopt, sys
from src.scrappers.detail_scrapper import DetailScrapper
from src.scrappers.search_scrapper import SearchScrapper
from src.utils.list_to_csv import write

options = 's:o:p:Ha'

long_options = ['search', 'output', 'max_pages', 'headless', 'append_file']

site = f'https://www.fotocasa.es/es/comprar/viviendas/valencia/todas-las-zonas/l'
output = 'csv'
max_pages = 3
headless = False
append_file = False

try:
  args = sys.argv[1:]
  arguments, values = getopt.getopt(args, options, long_options)

  for argument, value in arguments:
    if argument in ('-s', '--search'):
      site = f'https://www.fotocasa.es/es/comprar/viviendas/{value}/todas-las-zonas/l'
    elif argument in ('-o', '--output'):
      output = value
    elif argument in('-p', '--max_pages'):
      max_pages = value
    elif argument in ('-H', '--headless'):
      headless = True
    elif argument in ('-a', '--append_file'):
      append_file = True
except getopt.error as err:
  print(str(err))

search = SearchScrapper(url=site, output=output, max_pages=max_pages, headless=headless)
list = search.scrap(close=True)

rows = []
for url in list:
  rows.append(DetailScrapper.fetch(url))

write(columns=[
  'price',
  'bedrooms',
  'bathrooms',
  'sqm',
  'floor',
  'type',
  'orientation',
  'condition',
  'hot_water',
  'elevator'
], data=rows, write_headers=not append_file)

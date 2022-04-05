import csv

def write(file_name='data.csv', columns=[], data=[], write_headers=True):
  with open(file_name, 'w' if write_headers else 'a',) as csv_file:
    writer = csv.writer(csv_file)
    if write_headers:
      writer.writerow(columns)

    for d in data:
      item = []
      for c in columns:
        item.append(d[c])

      writer.writerow(item)

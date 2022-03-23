import csv

def write(file_name='data.csv', columns=[], data=[]):
  with open(file_name, 'a',) as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(columns)

    for d in data:
      item = []
      for c in columns:
        item.append(d[c])

      writer.writerow(item)

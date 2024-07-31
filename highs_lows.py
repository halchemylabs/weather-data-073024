import csv

file = 'sitka_weather_07-2014.csv'
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Print Header Rows
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    
    print(highs)

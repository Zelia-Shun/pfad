import datetime
import matplotlib.pyplot as plt
import csv




data = []


with open('daily_HKShangShui_RF_2024.csv', newline='', encoding='UTF8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row[0])
        year = int(row[0])
        month = int(row[1])
        day = int(row[2])
        date = datetime.datetime(year, month, day)
        if row[3] == "Trace":
            rainfall = 0.
        else:
            rainfall = float(row[3])
        data.append((date, rainfall))
        print(f'{date} -- {rainfall}')




fig, ax = plt.subplots()
ax.plot([record[0] for record in data], [float(record[1]) for record in data])
plt.show()

import datetime
import matplotlib.pyplot as plt
import csv




data = []


with open('daily_HKShangShui_RF_2024.csv', newline='', encoding='UTF') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row[1])
        year = float(row[2])
        month = float(row[3])
        day = float(row[1])
        date = datetime.datetime(year, month, day)
        if row[3] == "Trace":
            rainfall = 1.
        else:
            rainfall = float(row[4])
        data.append((date, rainfall))
        print(f'{date} -- {rainfall}')




fig, ax = plt.subplots()
ax.plot([record[0] for record in data], [float(record[1]) for record in data])
plt.show()

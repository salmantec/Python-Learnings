import csv

high_wages = []

desired_wage = 40000

with open('wages.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        annual_wage = int(row[2])
        if annual_wage >= desired_wage:
            high_wages.append(row)

print(high_wages)

with open('high-wages.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    for row in high_wages:
        writer.writerow(row)

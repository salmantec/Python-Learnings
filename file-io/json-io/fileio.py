import json

with open('listings.json', 'r') as infile:
    data = json.load(infile)


print(data)

available = [job for job in data if job['available']]

print(available)


with open('available-listings.json', 'w') as outfile:
    json.dump(available, outfile, indent=2)

with open('queries.txt', 'r') as infile:
    content = infile.read()

print(type(content))

print(content)

queries = content.split('\n');

print(queries)

normalized = [query.strip().lower() for query in queries[::2]]

print(normalized)

with open('normalized-queries.txt', 'w') as outfile:
    for query in normalized:
        outfile.write(query + '\n')


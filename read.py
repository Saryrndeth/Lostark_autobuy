tobuy = list()
with open('./list.txt', 'r', encoding='UTF8') as f:
    for line in f:
        tobuy.append((line[:line.find(':')], line[line.find(':') + 1:].strip()))
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 1000 == 0:
            print(len(data))
print('Reading is done, there are', len(data), 'comments')

print(data[0])

# word count
wc = {} # word acount
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc: #if word not in wc:
            wc[word] += 1
        else:
            wc[word] = 1
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])  

print(len(wc))
print

while True:
    word = input('what key word do you search: ')
    if word == 'q':
        break
    if word in wc:
        print(word, 'appears', wc[word], 'times')
    else:
        print('This word is not in the dictionary.')

print('See you!')






sum_len = 0
for dline in data:
    sum_len = sum_len + len(dline) 

print('The average length of comments is', sum_len / len(data), 'digitals')

new = []
for dline in data:
    if len(dline) < 100:
        new.append(dline)
print('There are totally', len(new), 'comments smaller than 100 digitals')
print(new[0])
print(new[1])

#good = []
#for dline in data:
#    if 'good' in dline:
#        good.append(dline)
good = [1 for dline in data if 'good' in dline]
print(good)
#print('There are', len(good), 'comments mentioning good')
#print(good[0])

bad = ['bad' in dline for dline in data]
print(bad)
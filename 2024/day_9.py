data = open('2024/input_9.txt',"r").read().strip()

unzip_data = []

n = 0
for i,x in enumerate(data):
    if i % 2 == 0:
        unzip_data += str(n) * int(x)
        n += 1
    else:
        unzip_data += "." * int(x)

list_unzip = list(unzip_data)
point_indexes = []
num_indexes = []

for i,x in enumerate(list_unzip):
    if x == ".":
        point_indexes.append((i,x))
    else:
        num_indexes.append((i,x))

for p,n in zip(point_indexes,num_indexes[::-1]):
    if n[0] < p[0]:
        break
    list_unzip[p[0]] = n[1]
    list_unzip[n[0]] = '.'
    print((p[0],n[0]))

sum_is = sum(int(x) * i for i, x in enumerate(list_unzip) if x != ".")

print(sum_is)

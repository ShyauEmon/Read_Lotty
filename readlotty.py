pp = ["05 , 15 , 19 , 22 , 30 , 42"]
lotty = []
with open('lotty.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lotty.append(line.strip())  # 從f拿出line放入lotty[]的list裡面
a = 0
b = 0
for x in lotty:
    if pp[0] in x:
        a += 1
    else:
        b += 1
print(a)
print(b)

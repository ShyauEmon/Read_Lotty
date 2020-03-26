num_1 = input("請輸入第一個號碼(由小到大)")
num_2 = input("請輸入第二個號碼(由小到大)")
num_3 = input("請輸入第三個號碼(由小到大)")
num_4 = input("請輸入第四個號碼(由小到大)")
num_5 = input("請輸入第五個號碼(由小到大)")
num_6 = input("請輸入第六個號碼(由小到大)")
# 此為判斷是否出現過輸出格式:["05 , 15 , 19 , 22 , 30 , 42"]
num = [num_1 + " , " + num_2 + " , " + num_3 + " , " + num_4 + " , " + num_5 + " , " + num_6]
lotty = []
with open('lotty.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lotty.append(line.strip())  # 從f拿出line放入lotty[]的list裡面
# 判斷是否有出現過
appear = 0
for x in lotty:
    if num[0] in x:
        appear += 1
print(num, "出現次數為:", appear, "次")

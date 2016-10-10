import sys
import math

n = int(sys.argv[1])
fr = open("D:\\nlp100\\hightemp.txt",encoding="UTF-8")
list = fr.readlines()
fr.close()
list_num = len(list)
split_num = math.floor(list_num / n)
start = 0
print("n split_num start list_num",n,split_num,start,list_num)
for l in range(n):
    if l == n - 1:
        print(len(list[start:]))
    else:
        print(len(list[start:start + split_num]))
    start += split_num
 
    
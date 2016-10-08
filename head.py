import sys

n = int(sys.argv[1])
fr = open("D:\\nlp100\\hightemp.txt",encoding="UTF-8")

for index,l in enumerate(fr):
    if index+1 > n:
        break
    print(l)

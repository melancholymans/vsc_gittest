import sys

n = int(sys.argv[1])
fr = open("D:\\nlp100\\hightemp.txt",encoding="UTF-8")
list = fr.readlines()
fr.close()
for l in list[len(list) - n:]:
    print(l)
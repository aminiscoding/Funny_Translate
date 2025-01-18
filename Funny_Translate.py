n = int(input("Tell me the number of words you want to translate:"))

dic = {}
for i in range(n):
    f, x1, x2, x3 = input("Tell me the original word and three of its translations in different languages:").split()
    dic[x1] = f; dic[x2] = f; dic[x3] = f

phrase = input("What phrase do you want to translate:").split()

trans = []
#
for i in phrase:
    if i in dic:
        trans.append(dic[i])
    else:
        trans.append(i)
print(" ".join(trans))

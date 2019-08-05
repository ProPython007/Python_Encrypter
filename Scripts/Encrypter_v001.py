# Encryptor ver_001

import random

def encrypt(file):
    f1 = open(file,"r")
    data = f1.read()
    f1.close()
    da, en = [], []
    for i in data:
        da.append(i)
    for i in range(97,123):
        en.append(chr(i))
    while len(da)>len(en):
        en = en+en
    random.shuffle(en)
    k = open("key.txt","a")
    key = random.randint(65,122)
    k.write(str(key))
    k.close()
    j = 0
    for i in range(len(da)):
        da[i] = str(ord(da[i])+key)+en[j]
        j+=1
    f2 = open("en_"+file,"a")
    for z in range(len(da)):
        f2.write(da[z])

file = input("Enter the file name in same path to encrypt: ")
encrypt(file)
print("Done !")
print("The encrypted file stored as:","en_"+file)
print("The key stored as:","key.txt")
input()

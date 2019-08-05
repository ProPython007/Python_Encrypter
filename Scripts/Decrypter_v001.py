# Decrypter ver_001

file = input("Enter the file name in same path to decrypt: ")
key = int(input("Enter the key here: "))

def decrypt(file, key):
    f1 = open(file,"r")
    data = f1.read()
    f1.close()
    l, t = [], ""
    for i in data:
        if 97 <= ord(i) <= 122:
            l.append(chr(int(t)-key))
            t=""
        else:
            t+=i
    f2 = open("de_"+file,"a")
    for i in l:
        f2.write(i)
    f2.close()

decrypt(file, key)
print("Done!!!")
print("Data stored at: ","de_"+file)
input()

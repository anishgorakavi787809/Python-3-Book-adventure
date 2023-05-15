#6.2.1
# One way to open files. Flaw is that the programmer has to control when to open and close files
f = open("/Users/anishgorakavi/Desktop/Python 3 Book adventure/Part 1 -> Getting started/Chapter 6 -> Files/names.txt")

for d in f.readlines():
    print(d.strip("\n"))
f.close()

#6.2.2 -> Read file
# Best way is with "with".
dic = {}
with open("/Users/anishgorakavi/Desktop/Python 3 Book adventure/Part 1 -> Getting started/Chapter 6 -> Files/names.txt") as fi:
    for f in fi.readlines():
        f = f.split(" ")
        dic[f[0]] = f[1].strip("\n")

print(dic)
#6.2.3 -> Read file
with open("/Users/anishgorakavi/Desktop/Python 3 Book adventure/Part 1 -> Getting started/Chapter 6 -> Files/wrike.txt","w") as wri:
    
    wri.writelines([f"{di} {dic[di]}\n" for di in dic])
#6.2.1
# One way to open files. Flaw is that the programmer has to control when to open and close files
f = open("/Users/anishgorakavi/Desktop/Python 3 Book adventure/Part 1 -> Getting started/Chapter 6 -> Files/names.txt")

for d in f.readlines():
    print(d.strip("\n"))
f.close()

# Best way is with "with".

with open("/Users/anishgorakavi/Desktop/Python 3 Book adventure/Part 1 -> Getting started/Chapter 6 -> Files/names.txt") as fi:
    pass
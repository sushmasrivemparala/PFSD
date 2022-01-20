'''try:
    klu1 = open("file.txt","w")
    try:
        klu1.write("this is s1 section")
        klu1.write("\ni am sushma")
    finally:
        klu1.close()
except IOError:
    print("the file opened successfully")
    klu1.close() '''
 class B(Exception):
     pass
 class C(B):
     pass
 class D(c):
     pass

 for cls in[B,C,D]:
     try:
         raise cls()
     except D:
         print("D")
     except C:
         print("C")
     except B:
         print("B")



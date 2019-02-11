from Backend import *

def StrListtoIntList(strList):
    for s in range (strList.__len__()):
        strList[s] = int(strList[s])
#Untuk input file
fitext = input("Nama file input : ")
fInput = open(fitext,'r')
#Untuk Output file
fotext = input("Nama File output : ")
fOutput = open(fotext,'w')

#ubah string jadi list of int
data = fInput.readline()
listNumber = data.split()

StrListtoIntList(listNumber)

#Operasi backend
BE = BackEnd(listNumber,[])
Expr, Point = BE.solution(listNumber)

#tulis hasil operasi ke output file
fOutput.write(Expr)
fOutput.write("\nPoint : ")
fOutput.write(str(Point))

#print(Expr)
#print(Point)

fInput.close()
fOutput.close()

from Backend_Kelompok35 import *
import sys

def StrListtoIntList(strList):
    for s in range (strList.__len__()):
        strList[s] = int(strList[s])

#Untuk input file
with open(sys.argv[1], 'r') as fInput:
    data = fInput.readline()

#Untuk Output file
fOutput = open(sys.argv[2],'w')

#ubah string jadi list of int
listNumber = data.split()
StrListtoIntList(listNumber)

#Operasi backend
BE = BackEnd(listNumber,[])
Expr, Point = BE.solution(listNumber)

#tulis hasil operasi ke output file
fOutput.write(Expr)
fOutput.write("\nPoint : ")
fOutput.write(str(Point))

fInput.close()
fOutput.close()

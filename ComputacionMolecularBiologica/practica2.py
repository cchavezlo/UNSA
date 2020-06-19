# -*- coding: utf-8 -*-
from Bio import SeqIO
import matplotlib.pyplot as plt

matSust=[[2,-7,-5,-7],
         [-7,2,-7,-5],
         [-5,-7,2,-7],
         [-7,-5,-7,2]]

gapOpen=0
gapExt=-5


def nuclValNum(nucl1):
    
    if nucl1=='A':
        return 0
    if nucl1=='C':
        return 1
    if nucl1=='G':
        return 2
    else:
        return 3
    

def valorMaximo(nucl1,nucl2,valorDia,valorArr,valorAba):
    
    nucleotNum1=nuclValNum(nucl1)
    nucleotNum2=nuclValNum(nucl2)
    
    valores=[]
    
    valores.append(valorDia+matSust[nucleotNum1][nucleotNum2])
    valores.append(valorArr+gapExt)
    valores.append(valorAba+gapExt)
    
    return (max(valores))
    
def makeMatrix(seq1,seq2):
    
    M = []
    gapinitI=gapOpen
    gapinitJ=gapOpen
    for i in range(len(seq1)+1):
        M.append([])
        
        for j in range(len(seq2)+1):
            if i==0 and j==0:
                M[i].append(gapOpen)
            elif i==0:
                gapinitI+=gapExt
                M[i].append(gapinitI)
            elif j==0:
                gapinitJ+=gapExt
                M[i].append(gapinitJ)
            else:
                M[i].append(valorMaximo(seq1[i-1],seq2[j-1],M[i-1][j-1],M[i-1][j],M[i][j-1]))
    
    print(M)
    return M

alineamiento1=[""]
alineamiento2=[""]
def generarAlineamineto(longitud1,longitud2,seq1,seq2,numAlineaminto2,M):
    
    nucl1=seq1[longitud1-1]
    nucl2=seq2[longitud2-1]
    numAlineaminto=numAlineaminto2
    if longitud1>=0 and longitud2>=0:
        print(longitud1,longitud2,M[longitud1][longitud2],M[longitud1-1][longitud2-1],nuclValNum(nucl1),nuclValNum(nucl2))
        if M[longitud1][longitud2]==M[longitud1-1][longitud2-1]+matSust[nuclValNum(nucl1)][nuclValNum(nucl2)]:
            print(numAlineaminto,"0")
            alineamiento1[numAlineaminto]=nucl1+alineamiento1[numAlineaminto]
            alineamiento2[numAlineaminto]=nucl2+alineamiento2[numAlineaminto]
            generarAlineamineto(longitud1-1,longitud2-1,seq1,seq2,numAlineaminto,M)
            numAlineaminto+=1
        if M[longitud1][longitud2]==M[longitud1-1][longitud2]+gapExt:
            if(numAlineaminto>numAlineaminto2):
                alineamiento1.append("")
                alineamiento2.append("")
            print(numAlineaminto,"1")
            alineamiento1[numAlineaminto]=nucl1+alineamiento1[numAlineaminto]
            alineamiento2[numAlineaminto]='-'+alineamiento2[numAlineaminto]
            generarAlineamineto(longitud1-1,longitud2,seq1,seq2,numAlineaminto,M)
            numAlineaminto+=1
        if M[longitud1][longitud2]==M[longitud1][longitud2-1]+gapExt:
            if(numAlineaminto>numAlineaminto2):
                alineamiento1.append("")
                alineamiento2.append("")
            print(numAlineaminto,"2")
            alineamiento1[numAlineaminto]='-'+alineamiento1[numAlineaminto]
            alineamiento2[numAlineaminto]=nucl2+alineamiento2[numAlineaminto]
            generarAlineamineto(longitud1,longitud2-1,seq1,seq2,numAlineaminto,M)
            numAlineaminto+=1

    
def dinamic(seq1,seq2):
     
    
    M=makeMatrix(seq1,seq2)
    numeroalineamito=0
    longitud1=len(seq1)
    longitud2=len(seq2)
    generarAlineamineto(longitud1,longitud2,seq1,seq2,numeroalineamito,M)
    
    print(alineamiento1)
    print(alineamiento2)
        
sequences = SeqIO.parse("Q8BTM8m.fasta.txt","fasta")
for record in sequences:
    data1=str(record.seq.upper())
    
sequences = SeqIO.parse("P21333.fasta.txt","fasta")
for record in sequences:
    data2=str(record.seq.upper())


data3="AAG"
data4="AGC"



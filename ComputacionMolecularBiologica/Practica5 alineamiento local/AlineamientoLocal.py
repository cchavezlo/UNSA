import sys 
sys.setrecursionlimit(10**6)
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np

matSust=[[1,-1,-1,-1],
         [-1,1,-1,-1],
         [-1,-1,1,-1],
         [-1,-1,-1,1]]

gapOpen=0
gapExt=-5
scoremax=0 

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
    maximo=max(valores)
    if(maximo<0):
        return 0
    return (max(valores))
    
def makeMatrix(seq1,seq2):
    global scoremax
    M = []
    for i in range(len(seq1)+1):
        M.append([])
        
        for j in range(len(seq2)+1):
            
            if i==0:
                M[i].append(0)
            elif j==0:
                M[i].append(0)
            else:
                valor=valorMaximo(seq1[i-1],seq2[j-1], M[i-1][j-1],M[i-1][j],M[i][j-1])
                M[i].append(valor)
                if valor>scoremax:
                    scoremax=valor
                ##print(seq1[i-1],seq2[j-1])
    #print(M)
    return M

alineamientoscad1=[]
alineamientoscad2=[]
def generarAlineamineto(longitud1,longitud2,seq1,seq2,numAlineamiento,M):
    alineamientoActual=numAlineamiento

    nucl1=seq1[longitud1-1]
    nucl2=seq2[longitud2-1]
    if longitud1>=0 and longitud2>=0:
        ##print(longitud1,longitud2,M[longitud1][longitud2],M[longitud1-1][longitud2-1],nuclValNum(nucl1),nuclValNum(nucl2))
        if M[longitud1][longitud2]==M[longitud1-1][longitud2-1]+matSust[nuclValNum(nucl1)][nuclValNum(nucl2)]:
            ##print(alineamientoActual,"0")
            alineamientoscad1[alineamientoActual]=nucl1+alineamientoscad1[alineamientoActual]
            alineamientoscad2[alineamientoActual]=nucl2+alineamientoscad2[alineamientoActual]
            generarAlineamineto(longitud1-1,longitud2-1,seq1,seq2,alineamientoActual,M)
            
            
    
    
def localAligment(seq1,seq2):
     
    alineamientoActual=0
    M=makeMatrix(seq1,seq2)
    
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]==scoremax:
                alineamientoscad1.append("")
                alineamientoscad2.append("")
                generarAlineamineto(i,j,seq1,seq2,alineamientoActual,M)
                alineamientoActual+=1

    print("score maximo: ",scoremax)
    print(np.unique(alineamientoscad1))
    print(np.unique(alineamientoscad2))
    
    
        
sequences = SeqIO.parse("ebola.fasta","fasta")
for record in sequences:
    data1=str(record.seq.upper())
    
sequences = SeqIO.parse("hepatitis_c.fasta","fasta")
for record in sequences:
    data2=str(record.seq.upper())


data3="ATACTGGG"
data4="TGACTGAG"


localAligment(data1,data2)
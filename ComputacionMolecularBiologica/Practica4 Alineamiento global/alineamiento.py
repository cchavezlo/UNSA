# -*- coding: utf-8 -*-
import sys 
sys.setrecursionlimit(10**6)
from Bio import SeqIO
import matplotlib.pyplot as plt

matSust=[[ 1,-1,-1,-1],
         [-1, 1,-1,-1],
         [-1,-1, 1,-1],
         [-1,-1,-1, 1]]

gapOpen=0
gapExt=-1


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
    
    ##print(M)
    return M

alineamientoscad1=[""]
alineamientoscad2=[""]
alineamientoActual=0
def generarAlineamineto(longitud1,longitud2,seq1,seq2,numAlineamiento,M):
    global alineamientoActual
    bifurcacion=False
    nucl1=seq1[longitud1-1]
    nucl2=seq2[longitud2-1]
    if longitud1>=0 and longitud2>=0:
        ##print(longitud1,longitud2,M[longitud1][longitud2],M[longitud1-1][longitud2-1],nuclValNum(nucl1),nuclValNum(nucl2))
        if M[longitud1][longitud2]==M[longitud1-1][longitud2-1]+matSust[nuclValNum(nucl1)][nuclValNum(nucl2)]:
            ##print(alineamientoActual,"0")
            alineamientoscad1[alineamientoActual]=nucl1+alineamientoscad1[alineamientoActual]
            alineamientoscad2[alineamientoActual]=nucl2+alineamientoscad2[alineamientoActual]
            generarAlineamineto(longitud1-1,longitud2-1,seq1,seq2,alineamientoActual,M)
            bifurcacion=True

        if M[longitud1][longitud2]==M[longitud1-1][longitud2]+gapExt:
            if(bifurcacion):
                alineamientoActual+=1
                alineamientoscad1.append("")
                alineamientoscad2.append("")
            ##print(alineamientoActual,"1")
            alineamientoscad1[alineamientoActual]=nucl1+alineamientoscad1[alineamientoActual]
            alineamientoscad2[alineamientoActual]='-'+alineamientoscad2[alineamientoActual]
            generarAlineamineto(longitud1-1,longitud2,seq1,seq2,alineamientoActual,M)
            bifurcacion=True
            
        if M[longitud1][longitud2]==M[longitud1][longitud2-1]+gapExt:
            if(bifurcacion):
                alineamientoActual+=1
                alineamientoscad1.append("")
                alineamientoscad2.append("")
           ## print(alineamientoActual,"2")
            alineamientoscad1[alineamientoActual]='-'+alineamientoscad1[alineamientoActual]
            alineamientoscad2[alineamientoActual]=nucl2+alineamientoscad2[alineamientoActual]
            generarAlineamineto(longitud1,longitud2-1,seq1,seq2,alineamientoActual,M)
            
            
    
    
def globalAligment(seq1,seq2):
     
    
    M=makeMatrix(seq1,seq2)
    longitud1=len(seq1)
    longitud2=len(seq2)
    
    generarAlineamineto(longitud1,longitud2,seq1,seq2,0,M)
    
    ##print(alineamientoscad1)
    ##print(alineamientoscad2)
    
    for i in range (len(alineamientoscad1)-1):
        primera_par=alineamientoscad1[i+1]
        segunda_par=alineamientoscad2[i+1]
        
        if len(alineamientoscad1[i]) > len(primera_par):
            alineamientoscad1[i+1]=alineamientoscad1[i+1]+alineamientoscad1[i][len(primera_par):]
        if len(alineamientoscad2[i]) > len(segunda_par):
            alineamientoscad2[i+1]=alineamientoscad2[i+1]+alineamientoscad2[i][len(segunda_par):]
        


    linea="Impresion de las secuencias \n"
    j=0
    while j<len(alineamientoscad2):
        linea+=alineamientoscad1[j]+"\n"
        linea+=alineamientoscad2[j]+"\n"
        j+=1
    archivo=open("salida.txt","w")
        
    archivo.write(linea)
    ##print("Imprimir linea",linea)
        
sequences = SeqIO.parse("Q8BTM8.fasta.txt","fasta")
for record in sequences:
    data1=str(record.seq.upper())
    
sequences = SeqIO.parse("P21333.fasta.txt","fasta")
for record in sequences:
    data2=str(record.seq.upper())


data3="AAAC"
data4="AGC"


globalAligment(data1,data2)
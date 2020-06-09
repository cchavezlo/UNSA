# -*- coding: utf-8 -*-
from Bio import SeqIO
import matplotlib.pyplot as plt


def compara(seq1,seq2,t):
    auxt=0
    for i in range(len(seq1)):
        if seq1[i]==seq2[i]:
            auxt+=1
    
    if auxt>=t:
        return 1
    else:
        return 0

def makeMatrix(seq1,seq2,w,t):
    

    subseq1=[]
    subseq2=[]
    cadtem=""
    contador=0
    for i in seq1:
        if contador==w:
            subseq1.append(cadtem)
            cadtem=""
            contador=0
        else:
            contador+=1
            cadtem=cadtem+i
    
    cadtem=""
    contador=0
    for i in seq2:
        if contador==w:
            subseq2.append(cadtem)
            cadtem=""
            contador=0
        else:
            contador+=1
            cadtem=cadtem+i
    M = []
    
    for i in range(len(subseq1)):
        M.append([])
        for j in range(len(subseq2)):
            if compara(subseq1[i],subseq2[j],t)==1:
                M[i].append(1)
            else:
                M[i].append(0)
        
    return M

def plotMatrix(M):
    xs=[]
    ys=[]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]==1:
                xs.append(i)
                ys.append(j)
    
    plt.scatter(xs, ys)
    plt.show()

def dotplot(seq1,seq2,w,t):
     
    
    M=makeMatrix(seq1,seq2,w,t)
    plotMatrix(M)



sequences = SeqIO.parse("Q8BTM8.fasta.txt","fasta")
for record in sequences:
    data1=str(record.seq.upper())
    
sequences = SeqIO.parse("Q60FE5.fasta","fasta")
for record in sequences:
    data2=str(record.seq.upper())

threshold=15 #porcentaje
window=50

threshold=threshold*window/100

dotplot(data1,data2,window,threshold)



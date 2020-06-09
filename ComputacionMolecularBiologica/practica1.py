# -*- coding: utf-8 -*-
from Bio import SeqIO
import matplotlib.pyplot as plt
import sys

def delta(x,y):
    return 0 if x == y else 1

def M(seq1,seq2,i,j,k):
    return sum(delta(x,y) for x,y in zip(seq1[i:i+k],seq2[j:j+k]))

def makeMatrix(seq1,seq2,k):
    n = len(seq1)
    m = len(seq2)
    return [[M(seq1,seq2,i,j,k) for j in range(m-k+1)] for i in range(n-k+1)]

def plotMatrix(M,t, seq1, seq2):
    xs=[]
    ys=[]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]<t:
                xs.append(i)
                ys.append(j)
    
    plt.scatter(xs, ys)
    plt.show()

def dotplot(seq1,seq2,k = 10,t = 1):
    M = makeMatrix(seq1,seq2,k)
    plotMatrix(M, t, seq1,seq2) #experiment with character choice



sequences = SeqIO.parse("Q8BTM8m.fasta.txt","fasta")
for record in sequences:
    data1=str(record.seq.upper())
    
sequences = SeqIO.parse("P21333.fasta.txt","fasta")
for record in sequences:
    data2=str(record.seq.upper())

dotplot(data1,data2)



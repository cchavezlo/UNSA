# -*- coding: utf-8 -*-
from Bio import SeqIO

sequences= SeqIO.parse("Q8BTM8m.fasta.txt", "fasta")
for record in sequences:
    data1=str(record.seq.upper())

sequences= SeqIO.parse("Q60FE5.fasta.txt", "fasta")
for record in sequences:
    data2=str(record.seq.upper())
        
print(data1)
print(data2)

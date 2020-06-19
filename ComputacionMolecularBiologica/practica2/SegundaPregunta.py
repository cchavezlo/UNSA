import numpy as np
from Bio import SeqIO
def ini_matriz_ceros():
	global tamano_secu,matriz
	i=0
	while i<tamano_secu:
		sub_lista=[]
		j=0
		while j<tamano_secu:
			sub_lista.append(0)
			j+=1
		i+=1
		matriz.append(sub_lista)

def ini_pri_fila_colu():
	global tamano_secu,matriz, gap
	i=0
	while i<1:
		acumulado=0
		j=0
		while j<tamano_secu:
			if i==j:
				matriz[i][j]=[ [[0,0]],0]
			else:	
				acumulado+=gap
				matriz[i][j]=[ [[i,j-1]],acumulado]
				matriz[j][i]=[ [[j-1,i]],acumulado]
			j+=1
		i+=1


s=[
[2,-7,-5,-7],
[-7,2,-7,-5],
[-5,-7,2,-7],
[-7,-5,-7,2]
]
matriz=[]
tamano_secu=4
gap=-5

ini_matriz_ceros()
ini_pri_fila_colu()
print("Imprimiendo la matriz")
i=0
while i<tamano_secu:
	print(matriz[i])
	i+=1

lista_1="ACGT"
seq_2="AAG"
seq_1="AGC"
cmp_seq=3+1
print("Completando la matriz")
i=1
while i<cmp_seq:
	j=1
	while j<4:
		valor_g=-1
		valor_cmp=seq_1[i-1]+seq_2[j-1]
		print("valor_g",valor_cmp)
		if valor_cmp in ["AA","CC","GG","TT"]:
			valor_g=2
		elif valor_cmp in ["AC","CG","GT","CA","GC","TG","AT","TA"]:
			valor_g=-7
		else:
			valor_g=-5

		primer_val=matriz[i-1][j-1][1]+valor_g
		segun_val=matriz[i-1][j][1]+gap
		tercer_val=matriz[i][j-1][1]+gap
		#print("igualdad",valor_g)
		#print("primer",primer_val)
		#print("segundo",segun_val)
		#print("tercer",tercer_val)
		resultado=[]
		menor=-1
		if primer_val>=segun_val and primer_val>=tercer_val:
			menor=primer_val
			resultado.append([i-1,j-1])
		if segun_val>=primer_val and segun_val>=tercer_val:
			menor=segun_val
			resultado.append([i-1,j])
		if tercer_val>=primer_val and tercer_val>=segun_val:
			resultado.append([i,j-1])
			menor=tercer_val
		matriz[i][j]=[resultado,menor]
		print(matriz[i][j])
			
		j+=1
	
	i+=1

def atras(i,j,respuesta,indice,ind_seq):
	global matriz,seq_1,seq_2
	if i==0 and j==0:
		print("Entra por aca ")
		return 
	print("Posicion_inicial",matriz[i][j][0])
	if len(matriz[i][j][0])==1:
		coor_x_y=matriz[i][j][0][0]
		if coor_x_y[0]==i-1 and coor_x_y[1]==j:
			respuesta[indice+1][ind_seq]='-'
		if coor_x_y[0]==i and coor_x_y[1]==j-1:
			respuesta[indice][ind_seq]="-"
		if coor_x_y[0]==i-1 and coor_x_y[1]==j-1:
			respuesta[indice][ind_seq]=seq_1[i]
			respuesta[indice+1][ind_seq]=seq_2[j]
		i=coor_x_y[0]
		j=coor_x_y[1]
		
		if ind_seq==0:
			print("indice",indice)
			print(respuesta[indice])
			print(respuesta[indice-1])
		ind_seq-=1
		atras(i,j,respuesta,indice,ind_seq)
	else:
		tamano=len(matriz[i][j][0])-1
		anadiendo=0
		while anadiendo<tamano:
			temp_seq1=respuesta[indice]
			temp_seq2=respuesta[indice+1]
			respuesta.append(temp_seq1)
			respuesta.append(temp_seq2)
			anadiendo+=1
		itera=0
		tamano=len(matriz[i][j][0])
		nuevo_indice=indice+2
		while itera<tamano:
			coor_x_y=matriz[i][j][0][itera]
			temp_i=-1
			temp_j=-1
			if coor_x_y==[i-1,j]:
				respuesta[nuevo_indice+1][ind_seq]='-'
				temp_i=i-1
				temp_j=j
			if coor_x_y==[i,j-1]:
				respuesta[nuevo_indice][ind_seq]="-"
				temp_i=i
				temp_j=j-1
			if coor_x_y==[i-1,j-1]:
				respuesta[nuevo_indice][ind_seq]=seq_1[i]
				respuesta[nuevo_indice+1][ind_seq]=seq_2[j]
				temp_i=i-1
				temp_j=j-1
			atras(temp_i,temp_j,respuesta,itera*2,ind_seq-1)
			itera+=1
		return
		
	

print("Matriz Final:")
impri=0
while impri<4:
	print(matriz[impri])
	impri+=1


sequences = SeqIO.parse("Q8BTM8.fasta.txt","fasta")
for record in sequences:
    data1=str(record.seq.upper())
    
sequences = SeqIO.parse("P21333.fasta.txt","fasta")
for record in sequences:
    data2=str(record.seq.upper())

seq_2=data1 ###ojo solo duplico la primera letra 
seq_1=data2

seq_ali1=list(seq_1)
seq_ali2=list(seq_2)
i=tamano_secu-1
indice=0
j=tamano_secu-1
respuesta=[]
respuesta.append(seq_ali1)
respuesta.append(seq_ali2)
#atras(i,j,respuesta,indice)
indice_cmp=tamano_secu-1
ind_seq=tamano_secu-1
atras(i,j, respuesta,indice,ind_seq)
print("Imprimiendo la matriz")
i=0
while i<len(respuesta):
	print("i=",i)
	print(respuesta[i])
	i+=1
'''
#solo funciona para la primera pregunta
while indice<4:
	print("INDICE ###############3",indice_cmp)
	if len(matriz[i][j][0])==1:
		coor_x_y=matriz[i][j][0][0]
	else:
		tamano=len(matriz[i][j][0])
		anadiendo=0
		temp_seq1=respuesta[0]
		temp_seq2=respuesta[1]
		respuesta.append(temp_seq1)
		respuesta.append(temp_seq2)
		indi2=0
		while anadiendo<3:
			coor_x_y=matriz[i][j][0][indi2]
			
			temp_i=-1
			temp_j=-1
			if coor_x_y==[i-1,j]:
				respuesta[anadiendo+1][indice_cmp]='-'
				temp_i=i-1
				temp_j=j
			if coor_x_y==[i,j-1]:
				respuesta[anadiendo][indice_cmp]="-"
				temp_i=i
				temp_j=j-1
				print(respuesta[anadiendo])
			if coor_x_y==[i-1,j-1]:
				respuesta[anadiendo][indice_cmp]=seq_1[i]
				respuesta[anadiendo+1][indice_cmp]=seq_2[j]
				temp_i=i-1
				temp_j=j-1
			
			indice_cmp-=1
			ite_temp1=-1
			ite_temp2=-1

			coor_x_y=matriz[temp_i][temp_j][0]
			if anadiendo==2:
				coor_x_y=matriz[temp_i][temp_j][0][0]
			
			
			if coor_x_y==[temp_i-1,temp_j]:
				respuesta[anadiendo+1][indice_cmp]='-'
				ite_temp1=i-1
				ite_temp2=j				
			if coor_x_y==[temp_i,temp_j-1]:
				respuesta[anadiendo][indice_cmp]="-"
				ite_temp1=i
				ite_temp2=j-1
				
			if coor_x_y==[temp_i-1,temp_j-1]:
				if anadiendo==2:
					temp_i-=1
				respuesta[anadiendo][indice_cmp]=seq_1[temp_i]
				respuesta[anadiendo+1][indice_cmp]=seq_2[temp_i]
				ite_temp1=i-1
				ite_temp2=j-1
				
			indice_cmp+=1
			print(respuesta[anadiendo])
			print(respuesta[anadiendo+1])
			anadiendo+=2
			print("##################")
			indi2+=1

		break
	print("ESTO PRIMERA ITERACIon")
	if coor_x_y[0]==i-1 and coor_x_y[1]==j:
		respuesta[1][indice_cmp]='-'
	if coor_x_y[0]==i and coor_x_y[1]==j-1:
		respuesta[0][indice_cmp]='-'
	if coor_x_y[0]==i-1 and coor_x_y[1]==j-1:
		respuesta[0][indice_cmp]=seq_1[i]
		respuesta[1][indice_cmp]=seq_2[j]
	i=coor_x_y[0]
	j=coor_x_y[1]
	print(respuesta[0])
	print(respuesta[1])
	print("iter",indice)
	indice+=1
	indice_cmp-=1

'''

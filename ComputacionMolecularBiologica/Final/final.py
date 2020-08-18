########i  y j son posiciones 
###largo del fragmento medio ??
##el coverage cantidad de bases sobrepuestas
##Largo del framento medio es de 395
##numero de fragmentos
import random 
import pandas as pd
import numpy as np
from timeit import default_timer 

def encontrar_menor(L):
	global N
	ordenado=sorted(L,key=lambda x: x[-1:])# de menor a mayor
	tmn=len(ordenado)
	print("Ordenado",tmn)
	i=0
	j=1
	igual=True
	print(ordenado[i][-1:])
	escogido=ordenado[i][0]

	if tmn>=2 and ordenado[i][-1:]==ordenado[j][-1:]:
		mejor=ordenado[i]
		while i<tmn and j<tmn and ordenado[i][-1:]==ordenado[j][-1:]:
			if ordenado[j][2]>mejor[2]:
				mejor=ordenado[j]
			i+=1
			j+=1
		print(mejor)
		return mejor[0],mejor[1]
	else:
		return ordenado[0][0],ordenado[0][1]




def generar_inicialSolucion(N):
	s=[]
	i=0
	while i<N:
		alea=random.randint(0,N-1)
		while alea in s:
			alea=random.randint(0,N-1)
		s.append(alea)
		i+=1
	return s



def calculadelta(s,i,j):
	global w,N
	cutoff=30
	dc=0
	df=0
	#df=df-w[s[i-1]][s[i]]-w[s[j]][s[j+1]]
	#df=w[s[i-1]][s[j]]+w[s[i]][s[j+1]]
	
	df=w[s[i-1]][s[j]]+w[s[i]][s[j+1]] #añade el sobre lape de la solucion modificada
	df=df-w[s[i-1]][s[i]]-w[s[j]][s[j+1]] #remover el sobre los actuales soluciones
	#df=w[s[i-1]][s[j]]+ w[s[i]][s[j+1]]
	#df=df - w[s[i-1]][s[i]]- w[s[j]][s[j+1]]
	if w[s[i-1]][s[i]]>cutoff:
		dc=dc+1
	if  w[s[j]][s[j+1]]>cutoff:
		dc=dc+1
	#hace test si dos coting son unidos, y si asi , esto disminuye la cantidad de contints
	if w[s[i-1]][s[j]]>cutoff:
		dc=dc-1
	if w[s[i]][s[j+1]]>cutoff:
		dc=dc-1
	return df,dc

def invierte_posiciones(s1,i,j):
	print("i=",i)
	print("j=",j)
	print("secuencia",s1)
	global N
	tmp=s1[i]
	s1[i]=s1[j]
	s1[j]=tmp
	print("secuencia",s1)
	return s1

df = pd.read_csv('C:/Users/Erika/Documents/biomolecular/ComputacionMolecularBiologica/Final/x60189_6_68/matrix_conservative.csv',sep =",",comment="#")

N=len(df)
print(N)
w=np.asarray(df)
print(w)
s=generar_inicialSolucion(N)

cutoff=30
acumulado=0
cambio=True
df=-1
canti=0
temp=0

#########PALS###############################
inicio = default_timer()
while cambio:
	print("secuencia inicial",s)
	L=[]
	i=0
	while i<N-2:
		j=i+1
		while j<N-1:
			dc,df=calculadelta(s,i,j)
			#print("dc",dc,"df",df)
			if (dc < 0) or (dc == 0 and df > 0):#dc>=0:#dc<0 or (dc==0 and df>0):
				L.append([i,j,df,dc])
			j+=1
		i+=1

	print(len(L))
	if len(L)>0:
		i,j=encontrar_menor(L)
		#acumulado+=dfitnes
		canti+=1
		s=invierte_posiciones(s,i,j)
		print("secuencia final",s)
	else:
		cambio=False
		break
	
	temp+=1
fin = default_timer()
print("Tiempo total obtenido"+str(fin-inicio)+" \n")#calcula el tiempo en segundos
#########PALS###############################
#print("s",s)
#print("esto es df",df)

#print(acumulado/canti)
#print(invierte_posiciones(0,1))
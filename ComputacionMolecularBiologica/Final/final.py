########i  y j son posiciones 
###largo del fragmento medio ??
##el coverage cantidad de bases sobrepuestas
##Largo del framento medio es de 395
##numero de fragmentos
import random 
import pandas as pd
import numpy as np
from timeit import default_timer 

##############################best
def encontrar_menor_best(L):
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
		return mejor[0],mejor[1],mejor[2],mejor[3]
	else:
		return ordenado[0][0],ordenado[0][1],ordenado[0][2],ordenado[0][3]

def encontrar_menor_first(L):
	
	i=0
	while i<len(L):
		if L[i][3]<=0:
			return L[i][0],L[i][1],L[i][2],L[i][3]
		i+=1

def encontrar_menor_random(L):
	alea=random.randint(0,len(L)-1)
	return L[alea][0],L[alea][1],L[alea][2],L[alea][3]

def calculadelta(s,i,j):
	global w,N
	cutoff=30
	dc=0
	df=0
	#df=df-w[s[i-1]][s[i]]-w[s[j]][s[j+1]]
	#df=w[s[i-1]][s[j]]+w[s[i]][s[j+1]]
	
	#df=w[s[i-1]][s[j]]+w[s[i]][s[j+1]] #añade el sobre lape de la solucion modificada
	#df=df-w[s[i-1]][s[i]]-w[s[j]][s[j+1]] #remover el sobre los actuales soluciones
	df = df - w[s[i-1], s[i]] - w[s[j], s[j+1]]
	df = df + w[s[i-1], s[j]] + w[s[i], s[j+1]]

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



#############random
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

#############greedy
def greedy(N,w):
	alea=random.randint(0,N-1)
	lista=[]
	lista.append(alea)

	lista_secuencia=[]
	j=0
	while j<N:
		lista_secuencia.append(j)
		j=j+1

	print("lista_secuencia",lista_secuencia)
	tamano=N-1
	indice=-1
	while len(lista_secuencia)!=0:
		i=0
		menor=100000
		indice_m=-1
		while i<len(lista_secuencia):
			if alea!=lista_secuencia[i]:
				if menor>w[alea][i]:
					menor=w[alea][i]
					indice_m=lista_secuencia[i]
					indice=i
			i+=1
		if len(lista_secuencia):
			lista.append(lista_secuencia[0])
			lista_secuencia.pop(0)		
		else:	
			lista.append(indice_m)
			lista_secuencia.pop(indice)
			

	return lista



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

df = pd.read_csv('C:/Users/Erika/Documents/biomolecular/ComputacionMolecularBiologica/Final/x60189_4/matrix_conservative.csv',sep =",",comment="#")

N=len(df)
print(N)
w=np.asarray(df)
print(w)

tipo="Random"
s=[]
if tipo=="Random":
	s=generar_inicialSolucion(N)
else:
	s=greedy(N,w)

cutoff=30
A_variacion_C=0
A_variacion_F=0
cantidad_cambio=0
cambio=True
df=-1
canti=0


#########PALS###############################
inicio = default_timer()

arreglo_tipos=["Best","First","Random"]
tipo="Random"
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
		if tipo=="Best":
			i,j,df,dc=encontrar_menor_best(L)
		elif tipo=="First":
			i,j,df,dc=encontrar_menor_first(L)
		elif tipo=="Random":
			i,j,df,dc=encontrar_menor_random(L)
		#acumulado+=dfitnes
		canti+=1
		s=invierte_posiciones(s,i,j)
		print("secuencia final",s)
		#A_variacion_C+=dc
		#A_variacion_F+=df
		cantidad_cambio+=1
	else:
		cambio=False
		break
	
fin = default_timer()
print("Tiempo total obtenido"+str(fin-inicio)+" \n")#calcula el tiempo en segundos
promedio_c=A_variacion_C/cantidad_cambio
promedio_f=A_variacion_F/cantidad_cambio
#print("Promedio de variacion de conting"+str(promedio_c))
#print("Promedio de variacion de fitnes"+str(promedio_f)) 


#########PALS###############################
#print("s",s)
#print("esto es df",df)

#print(acumulado/canti)
#print(invierte_posiciones(0,1))
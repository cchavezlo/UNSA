########i  y j son posiciones 
###largo del fragmento medio ??
##el coverage cantidad de bases sobrepuestas
##Largo del framento medio es de 395
##numero de fragmentos
import random 
import pandas as pd
import numpy as np
import time
df = pd.read_csv('C:/Users/ErikaPC/Documents/Cursos2020-1/BioinformaticaMoleculaar/FINAL/x60189_4/matrix_conservative.csv',sep =",",comment="#")
tamano=len(df)
#print(tamano)
w=np.asarray(df)
#print(w)
def encontrar_menor(L):
    # get the posible movement with minimun delta_c
    x = len(L)
    L_temp = np.matrix(L)
    delta_c_list = L_temp[:,3]
    min_delta_c = np.amin(delta_c_list)

    L_with_min_delta_c = []
    for i in range(x):
        if L_temp[i,3] == min_delta_c:
            L_with_min_delta_c.append(np.squeeze(np.asarray(L_temp[i,:])))

       
    # get the posible movement with maximun delta_f
    x = len(L_with_min_delta_c)
    L_temp = np.matrix(L_with_min_delta_c)
    delta_f_list = L_temp[:,2]
    max_delta_f = np.amax(delta_f_list)
    
    L_with_max_delta_f = []
    for i in range(x):
        if L_temp[i,2] == max_delta_f:
            L_with_max_delta_f.append(np.squeeze(np.asarray(L_temp[i,:])))

    L_temp = np.matrix(L_with_max_delta_f)
    
    #print(L_temp.shape)   
    #print(L_temp)
    return int(L_temp[0, 0]), int(L_temp[0, 1])
    """
def encontrar_menor(L):
	global N
	ordenado=sorted(L,key=lambda x: x[-1:])# de menor a mayor
	tmn=len(ordenado)
	print("Ordenado",tmn)
	i=0
	j=1
	igual=True
	print(ordenado[i][-1:])
	if ordenado[i][-1:]==ordenado[j][-1:]:
		mejor=ordenado[i]
		while i<tmn and j<tmn and ordenado[i][-1:]==ordenado[j][-1:]:
			
			if ordenado[j][2]>mejor[2]:
				mejor=ordenado[j]
			i+=1
			j+=1
		print(mejor)
		return mejor[0],mejor[1],mejor[2]
	else:
		return ordenado[0][0],ordenado[0][1],ordenado[0][2]
"""
M=[]


N=tamano
#################inicializar soluciones#####
cutoff=30
s=[]
sequencia=""
i=0
while i<N:
	alea=random.randint(0,N-1)
	while alea in s:
		alea=random.randint(0,N-1)
	s.append(alea)
	i+=1

#print("Orden de la sequencia aleatorioa \n",s)

def calculadelta(s,i,j):
	global w,N
	cutoff=30
	dc=0
	df=0
	df=df-w[s[i-1]][s[i]]-w[s[j]][s[j+1]]
	df=df + w[s[i-1]][s[j]]- w[s[i]][s[j+1]]
	if w[s[i-1]][s[i]]>cutoff:
		dc=dc+1
	if  w[s[j]][s[j+1]]>cutoff:
		dc=dc+1
	if w[s[i-1]][s[j]]>cutoff:
		dc=dc-1
	if w[s[i]][s[j+1]]>cutoff:
		dc=dc-1
	return df,dc

def invierte_posiciones(s1,i,j):
	global N
	tmp=s1[i]
	s1[i]=s1[j]
	s1[j]=tmp
	return s

acumulado=0
cambio=True
df=-1
canti=0
temp=0
while temp<300:
	L=[]
	i=1
	while i<N:
		j=0
		while j<N-1:
			dc,df=calculadelta(s,i,j)
			if dc<0 or (dc==0 and df>0):
				L.append([i,j,df,dc])
			j+=1
		i+=1

	print(len(L))
	if len(L)>0:
		i,j=encontrar_menor(L)
		#acumulado+=dfitnes
		canti+=1
		s=invierte_posiciones(s,i,j)

	else:
		cambio=False
		break
	temp+=1

#print("s",s)
#print("esto es df",df)

#print(acumulado/canti)
#print(invierte_posiciones(0,1))
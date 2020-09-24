#include <iostream>
#include <ctime>
#include <limits>
#include <signal.h>
using namespace std;

 

void ejercicio01 (int MAX){

	double A[MAX][MAX], x[MAX], y[MAX];
	srand(time(NULL));

    for (int fila = 0; fila < MAX; fila++){
    	x[fila] = rand()%10000;
   		y[fila] = 0;
        for (int columna = 0; columna < MAX; columna++){
            A[fila][columna] = rand()%10000;
        }
    }


	clock_t start; 
	double duration; 

	start = std::clock(); 

	for (int i = 0; i < MAX; i++)
	    for (int j = 0; j < MAX; j++)
	        y[i] += A[i][j]*x[j] ;
   
	//raise(SIGINT) ;
	duration = (clock() - start ) / (double) CLOCKS_PER_SEC;
	cout<<"For sin Misses Cache: "<< duration <<endl;

	start = std::clock(); 

	for (int j = 0; j < MAX; j++)
	    for (int i = 0; i < MAX; i++)
	        y[i] += A[i][j]*x[j] ;
   

	duration = (clock() - start ) / (double) CLOCKS_PER_SEC;
	cout<<"For con Misses Cache: "<< duration <<endl;
}


void ejercicio02(int MAX){


	double A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];
	srand(time(NULL));

    for (int fila = 0; fila < MAX; fila++){
        for (int columna = 0; columna < MAX; columna++){
            A[fila][columna] = rand()%10000;
            B[fila][columna] = rand()%10000;
            C[fila][columna] = 0;
        }
    }

	clock_t start; 
	double duration; 

	start = std::clock();     

	for(int i=0;i<MAX;i++){
        for(int j=0;j<MAX;j++){
            for(int k=0;k<MAX;k++){
                C[i][j] = C[i][j] + (A[i][k]*B[k][j]);
            }
        }
    }

    duration = (clock() - start ) / (double) CLOCKS_PER_SEC;
	cout<<"Tiempo consumido con un tam de: "<<MAX << " es: " << duration <<endl;
}


void ejercicio03(int MAX){

	double mat1[MAX][MAX], mat2[MAX][MAX], matres[MAX][MAX];
	srand(time(NULL));

    for (int fila = 0; fila < MAX; fila++){
        for (int columna = 0; columna < MAX; columna++){
            mat1[fila][columna] = rand()%10000;
            mat2[fila][columna] = rand()%10000;
            matres[fila][columna] = 0;
        }
    }
 
 	int bloques = MAX/10; // T a m a o de cada bloque
	
	clock_t start; 
	double duration; 

	start = std::clock();  

	start = clock();
	for(int bi=0; bi<MAX; bi+=bloques){
		for(int bj=0; bj<MAX; bj+=bloques){
			for(int bk=0; bk<MAX; bk+=bloques){
				for(int i=bi; i<bi+bloques; i++){
					for(int j=bj; j<bj+bloques; j++){
						for(int k=bk; k<bk+bloques; k++){
							matres[i][j]+=mat1[i][k]*mat2[k][j];
						}
					}
				}
			}
		}
	}
	duration = (clock() - start ) / (double) CLOCKS_PER_SEC;
	cout<<"Tiempo consumido con un tam de: "<<MAX << " es: " << duration <<endl;
}

int main(int argc, char const *argv[])
{
	//cout << "max(int): " << numeric_limits<int>::max() << endl;

	//cout<< "Actividad 01"<<endl;
	//cout<<"##############################"<<endl;
	//cout<< "Resultados Ejercicio01: "<<endl;
	//ejercicio01(1000);
	


	//cout<<"##############################"<<endl;
	//cout<< "Resultados Ejercicio02: "<<endl;
	//ejercicio02(10);
	//ejercicio02(100);
	//ejercicio02(500);


	//cout<<"##############################"<<endl;
	//cout<< "Resultados Ejercicio03: "<<endl;

	ejercicio03(500);

	//cout<<"##############################"<<endl;

	return 0;
}
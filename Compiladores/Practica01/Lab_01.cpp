#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <cctype>
#include <clocale>
using namespace std;



void ejercicio_04(string file){

	string cadena; 
	string caracter_especial = "+-*/";
	ifstream data(file);
 	
	while (!data.eof()) {
		data >> cadena;
		if(caracter_especial.find(cadena)<=4){ cout<<cadena <<" -> Es un Caracter Especial"<<endl;}
	 	else if(isalpha(char(cadena[0]))){
		 	for (char caracter : cadena){
	   			 if (!isalpha(caracter)){
	   			 	cout<<cadena <<" -> Cadena NO Aceptada"<<endl; 
	   			 	break;
	   			 }
	   		}
	   		cout<<cadena <<" -> Es una PALABRA"<<endl;
   		}
   		else if(isdigit(char(cadena[0]))){
		 	for (char caracter : cadena){
	   			 if (!isdigit(caracter)){
	   			 	cout<<cadena <<" -> Cadena NO Aceptada"<<endl; 
	   			 	break;
	   			 }
	   		}
	   		cout<<cadena <<" -> Es un DIGITO"<<endl;
   		}	 			 
		
		else {cout<<cadena <<" -> Cadena NO Aceptada"<<endl;}
	}
	data.close();
}


void ejercicio_03_cifrado (string file, int rot){

	string cadena;
	string alfabeto= " )(][ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz#_.:<>,1234567890=";

	ifstream data(file);
 	ofstream data_cifrada("descifrar.txt"); 
 
	while (!data.eof()) {
		getline(data,cadena); 
		for(int i=0; i < cadena.length(); i++){
			auto it = alfabeto.find(cadena[i]) ;
			data_cifrada<< alfabeto[ (int(it)+rot) % alfabeto.length() ];  
		}
		data_cifrada<<endl;
 
	}
	data.close();
	data_cifrada.close();
	cout<<"Archivo Cifrado en: descifrar.txt"<<endl;
}

void ejercicio_03_descifrado (string file, int rot){

	string cadena;
	string alfabeto= " )(][ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz#_.:<>,1234567890=";

	

	ifstream data(file);
 	ofstream data_cifrada("descifrar_resultado.txt"); 
 
	while (!data.eof()) {
		getline(data,cadena); 
		for(int i=0; i < cadena.length(); i++){
			auto it = alfabeto.find(cadena[i]);
		
			 
            int nuevaposicion=int(it)-rot;
           if(nuevaposicion<0){ 
            	nuevaposicion=  alfabeto.length() + nuevaposicion;  
            	data_cifrada<< alfabeto[nuevaposicion]; }
          else {data_cifrada<< alfabeto[ nuevaposicion % alfabeto.length() ];  }
           // data_cifrada<< alfabeto[ nuevaposicion % alfabeto.length() ];  
               
		}
		data_cifrada<<endl;
 
	}
	data.close();
	data_cifrada.close();
	cout<<"Archivo Descifrado en: descifrar_resultado.txt"<<endl;
}



void ejercicio_02 (){

	string cadena;
	cout<<"Leer un archivo de texto plano (archivo con un pseudocódigo) y muestre en pantalla letra por letra"<< endl;
	 
	ifstream data("in.txt");
	while (!data.eof()) {
		//data >> cadena; -> Esta instruccion solo obtine hasta encontrar espacio
		getline(data,cadena); 
		 
		for(int i=0; i < cadena.length(); i++)
			cout<<cadena[i]<<endl;
		cout<<endl;
	}
	data.close();
		 
}



void ejercicio_01 (){

	//getchar -> Mediante la función de biblioteca getchar se puede conseguir la entrada de carácteres uno a uno. Devuelve un carácter leído del teclado.
	char cadena;
	cout<<"Leer toda una instrucción por consola (Ejemplo: “int temp;”) y mostrar en pantalla letra por letra"<< endl;
	cout<<"Ingresa la Cadena: "<<endl;
	cin>>cadena;
	
	do{
		cout<<cadena<<endl;
	}while( (cadena = getchar())!= '\n');		
}



int main(){
//ejercicio_01()
//ejercicio_02()
//ejercicio_03_cifrado("cifrar.txt",3);
//ejercicio_03_descifrado("descifrar.txt",3);

ejercicio_04("reconocer_token.txt");
}


#include <signal.h>
#include <stdio.h>
#include <string.h>
int main(){
	char realPassword[20];
	char givenPassword[20];

	strncpy(realPassword, "aaaaaaaa", 20);
	//	fgets(givenPassword,20,stdin);
	gets(givenPassword);
	
	if (0 == strncmp(givenPassword, realPassword, 20)){
		printf("SUCCESS!\n");
	}else{
		printf("FAILURE!\n");
	}
	raise(SIGINT);
	printf("givenPassword: %s\n", givenPassword);
	printf("realPassword: %s\n", realPassword);
	return 0;
}

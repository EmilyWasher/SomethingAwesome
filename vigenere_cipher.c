#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHA 26
#define CODE 10
#define LC_to_UC 'a' - 'A'
#define BUF 1024
//balh
void encode_message(char* message);
void convert_to_lc (char code_word[]);
void create_matrix(char matrix[ALPHA][ALPHA]);

int main (int argc, char* argv[]){
	char matrix[ALPHA][ALPHA];
	char* message = malloc(sizeof(char) * BUF);

	create_matrix(matrix);


	printf("Welcome to the Vigenere cipher\nEnter a code word (<10): ");
	char code_word[CODE]; 
	scanf("%s", &code_word);
	getchar();
	int code_len = strlen(code_word);
	printf("%s\n", code_word);

	convert_to_lc(code_word);

	/*for (int i = 0; i < strlen(code_word); i++){
		//code_word[i] = code_word[i] - 'a';
		//printf ("%d ", code_word[i]);
		printf("%d", code_word[i] );
	}*/

	printf("Enter your message to encode: ");
	
	while (fgets(message, BUF, stdin) != NULL){
		encode_message(message);
		//if (message[strlen(message) - 1] == '\n') break;
	}

	printf("Your endcoded mesage is: %s", message);

	free(message);

	return 0;
}

void encode_message(char* message){
	/*if ('a' <= message[i] && message[i] < ='z'){

	} else if ('A' <= message[i] && message[i] <= 'Z'){
		printf("wassup");
	}*/
	printf("%s\n", message);
}

void convert_to_lc (char code_word[]){	
	for (int i = 0; i <strlen(code_word); i++){
		if ('A' <= code_word[i] && code_word[i] <= 'Z'){
			code_word[i] = code_word[i] + 'a' - 'A';
		}
	}
}

void create_matrix(char matrix[ALPHA][ALPHA]){
	for (int i = 0; i < ALPHA; i++){
		for (int j = 0; j < ALPHA; j++){
			if ('a' + i + j > 'z'){
			 	matrix[i][j] = 'a' + i +j - ALPHA;
			} else {
				matrix[i][j] = 'a' + i + j;
			}
		}	}
}

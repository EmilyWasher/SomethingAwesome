#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHA 26
#define CODE 10
#define BUF 1024

void encode_message(char* message, int code[], int code_len, char matrix[ALPHA][ALPHA]);
void convert_to_num (char code_word[], int code[]);
void create_matrix(char matrix[ALPHA][ALPHA]);

int main (int argc, char* argv[]){
	char matrix[ALPHA][ALPHA];
	char* message = malloc(sizeof(char) * BUF);

	create_matrix(matrix);

	printf("Welcome to the Vigenere cipher\nEnter a code word (<10): ");
	char code_word[CODE]; 
	scanf("%s", &code_word);
	getchar();
	int code_length = strlen(code_word);
	int code[code_length];

	convert_to_num(code_word, code);

	printf("Enter your message to encode: ");
	
	while (fgets(message, BUF, stdin) != NULL){
		encode_message(message, code, code_length, matrix);
		if (message[strlen(message) - 1] == '\n') break;
	}

	printf("Your endcoded mesage is: %s", message);

	free(message);

	return 0;
}

void encode_message(char* message, int code[], int code_len, char matrix[ALPHA][ALPHA]){
	int is_letter = 0;
	for (int i = 0; i < strlen(message); i++){
	    if ('a' <= message[i] && message[i] <='z'){
            message[i] = matrix[code[is_letter % code_len]][message[i] - 'a'];
            is_letter++;
	    } else if ('A' <= message[i] && message[i] <= 'Z'){
		    message[i] = matrix[code[is_letter % code_len]][message[i] - 'A'] - 'a' + 'A';
            is_letter++;
	    }
	}
}

void convert_to_num (char code_word[], int code[]){	
	for (int i = 0; i <strlen(code_word); i++){
		if ('A' <= code_word[i] && code_word[i] <= 'Z'){
			code[i] = code_word[i] - 'A';
		} else if ('a' <=code_word[i] && code_word[i] <= 'z'){
		    code[i] = code_word[i] - 'a';
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
		}	
	}
}

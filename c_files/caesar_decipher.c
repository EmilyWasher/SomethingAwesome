#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 1024

void decode_message(char* message, int key);

int main (int argc, char* argv[]){
    printf("Welcome to the Caesar cipher\n");

    char *message = malloc(sizeof(char) * BUF_SIZE);
    int key = 0;
    
    printf("Enter the key: ");
    scanf("%d", &key);
    if (1 > key || key > 26){
        fprintf(stderr, "Invalid key entered. Please enter a number between 1 and 26\n");
        exit(1);
    }
    getchar(); 

    printf("Enter a message to decode: ");
    
    while (fgets(message, BUF_SIZE, stdin) != NULL){
        decode_message(message, key);
        if (message[strlen(message) - 1] == '\n') break;
    }
       
    printf("Your encoded message is: %s", message);
    free(message);
}

void decode_message(char* message, int key){
    for (int i = 0; i < (int)strlen(message); i++){
        if (message[i] >= 'a' && message[i] <= 'z'){
            if ((message[i] - key) < 'a'){
                message[i] = (message[i] - key + 'z' - 'a' + 1);
            } else {
                message[i] = (message[i] - key); 
            }
        } else if (message[i] >= 'A' && message[i] <= 'Z'){
            if ((message[i] - key) < 'A'){
                message[i] = (message[i] - key + 'Z' - 'A' + 1);
            } else {
                message[i] = (message[i] - key); 
            }
        }
    }
}

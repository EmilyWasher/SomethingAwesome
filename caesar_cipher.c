#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 1024

void encode_message(char* message, int key);

int main (int argc, char* argv[]){
    printf("Welcome to the Caesar cipher\n");
    int key = 0;
    char *message = malloc(sizeof(char) * BUF_SIZE);
   
    printf("Enter a number betrween 1-26: ");
    scanf("%d", &key);
    if (1 > key || key > 26){
        fprintf(stderr, "Invalid key entered. Please enter a number between 1 and 26\n");
        exit(1);
    }
    getchar();

    printf("Enter a message to encode: ");
    while (fgets(message, BUF_SIZE, stdin) != NULL){
        encode_message(message, key);
        if (message[strlen(message) - 1] == '\n') break;
    }
       
    printf("Your encoded message is: %s", message);
    free(message);
}

void encode_message(char* message, int key){
    for (int i = 0; i < (int)strlen(message); i++){
        if (message[i] >= 'a' && message[i] <= 'z'){
            if ((message[i] + key) > 'z'){
                message[i] = (message[i] + key - 'z' + 'a' - 1);
            } else {
                message[i] = (message[i] + key); 
            }
        } else if (message[i] >= 'A' && message[i] <= 'Z'){
            if ((message[i] + key) > 'Z'){
                message[i] = (message[i] + key - 'Z' + 'A' - 1);
            } else {
                message[i] = (message[i] + key); 
            }
        }
    }
}

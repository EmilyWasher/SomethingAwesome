#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 1024

void encode_message(char* message);

int main (int argc, char* argv[]){
    printf("Welocome to the Atbash cipher\n");
    char *message = malloc(sizeof(char) * BUF_SIZE);
    printf("Enter a message to encode: ");
    
    while (fgets(message, BUF_SIZE, stdin) != NULL){
        encode_message(message);
        if (message[strlen(message) - 1] == '\n') break;
    }
       
    printf("Your new message is: %s", message);
    free(message);
}

void encode_message(char* message){
    for (int i = 0; i < (int)strlen(message); i++){
        if ('a' <= message[i] && message[i] <= 'z'){
            message[i] = 'z' + 'a' - message[i];
        } else if ('A' <= message[i] && message[i] <= 'Z'){
            message[i] = 'Z' + 'A' - message[i];
        }

    }
}
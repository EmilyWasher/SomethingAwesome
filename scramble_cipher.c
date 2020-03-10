#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define BUF_SIZE 1024
#define SCRAM_ALPHA 26

void encode_message(char* message, char* lc_scram_alpha, char* uc_scram_alpha);
void scramble(char* lc_scram_alpha, char* uc_scram_alpha);

int main (int argc, char* argv[]){
    printf("Welcome to the Scramble cipher\n");
    int key = 0;
    char *message = malloc(sizeof(char) * BUF_SIZE);
    char* lc_scram_alpha = malloc(sizeof(char) * SCRAM_ALPHA);
    char* uc_scram_alpha = malloc(sizeof(char) * SCRAM_ALPHA);

    scramble(lc_scram_alpha, uc_scram_alpha);

    //printf("lc: %s\nuc: %s\n", lc_scram_alpha, uc_scram_alpha);

    printf("Enter a message to encode: ");
    
    while (fgets(message, BUF_SIZE, stdin) != NULL){
        encode_message(message, lc_scram_alpha, uc_scram_alpha);
        if (message[strlen(message) - 1] == '\n') break;
    }
       
    printf("Your encoded message is: %s", message);
    free(lc_scram_alpha);
    free(uc_scram_alpha);
    free(message);
}

void encode_message(char* message, char* lc_scram_alpha, char* uc_scram_alpha){
    for (int i = 0; i < (int)strlen(message); i++){
        if ('a' <= message[i] && message[i] <= 'z'){
            message[i] = lc_scram_alpha[message[i] - 'a'];   
        } else if ('A' <= message[i] && message[i] <= 'Z'){
            message[i] = uc_scram_alpha[message[i] - 'A'];   
        }
    }
}

void scramble(char* lc_scram_alpha, char* uc_scram_alpha){
    srand(time(NULL));
    for (int i = 0; i < SCRAM_ALPHA; i++){
        char c = 'a' + (rand() % 26);

        if (i == 0) lc_scram_alpha[i] = c;  

        for (int j = 0; j < i; j++){
            //If the letter has been seen before, repeat the ith iteration
            if (lc_scram_alpha[j] == c){ i--; break;}
            else if (j == i - 1){
                lc_scram_alpha[i] = c;
            }
        }
    }
    lc_scram_alpha[SCRAM_ALPHA] = '\0';

    //copy the lower case scrambled alphabet into upper case
    for (int i = 0; i < SCRAM_ALPHA; i++){
        uc_scram_alpha[i] = lc_scram_alpha[i] - ('a' - 'A');
    }
    uc_scram_alpha[SCRAM_ALPHA] = '\0';
}
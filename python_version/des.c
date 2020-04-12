/*
block cipher
takes fixed length string of plaintext 
and converts it to a cipher text of the same length
block size = 64bits
uses a 64 bit key (but only 56 bits are used)
the other 8 bits are used for checking parity
i.e. the ley is stored in 8 bits and the 8th bit is used for error checking 's of odd parity'
decryption works the same way but the leys are used in the reverse order

Copied from Wikipedia
The ⊕ symbol denotes the exclusive-OR (XOR) operation. 
The F-function scrambles half a block together with some of the key. 
The output from the F-function is then combined with the other half of the block, 
and the halves are swapped before the next round. 
After the final round, the halves are swapped; 
this is a feature of the Feistel structure which makes encryption and 
decryption similar processes.


*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){

	return 0;
}

//Generate a 64 bit key
void gen_key(){
	srand(time(0));
	unsigned long key = malloc(sizeof(unsigned long));

}
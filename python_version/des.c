/*
block cipher
takes fixed length string of plaintext 
and converts it to a cipher text of the same length
block size = 64bits
uses a 64 bit key (but only 56 bits are used)
the other 8 bits are used for checking parity
i.e. the key is stored in 8 bits and the 8th bit is used for error checking 's of odd parity'
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
#include <inttypes.h>
#include <time.h>


//Type declarations
typedef union key {
	struct key_s {
		unsigned int k0: 8, k1: 8, k2: 8, k3: 8, k4: 8, k5: 8, k6: 8, k7: 8;
	};
	unsigned int key_a[8];
} Key64;


//Function Declarations
Key64 gen_rand_key();


int main(int argc, char* argv[]){
	Key64 key = gen_rand_key();

	return 0;
}



//Generate a 64 bit key based off the current time
Key64 gen_rand_key(){
	srand(time(0));
	Key64 key;
	for (int i = 0; i < 8; i++){
		key.key_a[i] = rand() % 256;
	}
	return key;
}
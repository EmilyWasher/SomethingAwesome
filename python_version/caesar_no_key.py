# Set up dictionary in Australian English
import enchant
d = enchant.Dict("en_AU")


def get_input():
    print ("Welcome to Caesar cipher.")
    print("I will attempt to crack your secret message without a key")
    message = input("Enter the secret message: ")
    words = message.split()
    return words;
    #might'nt work if there are spelling errors


# Function to decrypt provided ciphertext given a key
def decrypt(message, key):
    cipher = ''
    for c in message:
        if c.isalpha():
            num_c = ord(c) - key
            if num_c < ord('a') and 'a' <= c < 'z':
                num_c += 26
            elif num_c > ord('Z') and 'A' <= c <= 'Z':
                num_c += 26
            cipher += chr(num_c)
        else:
            cipher += c
            
     return cipher;

  
def crack_caesar():
    get_input()
    key = 0
    for w in words:
        print(word)
        '''new_w = decrypt(w, key)
        if d.check(new_w) == True:
            #do something
        else:
            #restart'''

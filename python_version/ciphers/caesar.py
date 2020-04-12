# Read in the input, ensuring to sanitise the choice and key
'''while True:
    choice = int(input("Do you want to encrypt (1) or decrypt (2): "))
    if choice == 1 or choice == 2:
        break
    else:
        print("Invalid option. PLease select a different option.")

message = input("Enter message: ")

while True:
    try:
        key = int(input("Enter your key (<= 26): "))
        if key > 26 or key < 0:
            raise ValueError
    except ValueError:
        print("Invalid key. Please enter a new key.")
        continue
    else:
        break'''

class Caesar:
    def __init__(self, message, key):
        self._message = message
        self._key = key
    
    # Function to encrypt the plain text to cipher text
    def encrypt(self):
        cipher = ''
        for c in self._message:
            if c.isalpha():
                num_c = ord(c) + self._key
                if num_c > ord('z') and 'a' <= c <= 'z':
                    num_c -= 26
                elif num_c > ord('Z') and 'A' <= c <= 'Z':
                    num_c -= 26
                cipher += chr(num_c)
            else:
                cipher += c
        #print("Encoded message is: " + cipher)
        return cipher


    # Function to decrypt provided ciphertext given a key
    def decrypt(self):
        cipher = ''
        for c in self._message:
            if c.isalpha():
                num_c = ord(c) - self._key
                if num_c < ord('a') and 'a' <= c <= 'z':
                    num_c += 26
                elif num_c < ord('A') and 'A' <= c <= 'Z':
                    num_c += 26
                cipher += chr(num_c)
            else:
                cipher += c
       # print("The decoded message is: " + cipher)
        return cipher

'''
# Main body of the program
if choice == 1:
    encrypt(message, key)
elif choice == 2:
    decrypt(message, key)'''

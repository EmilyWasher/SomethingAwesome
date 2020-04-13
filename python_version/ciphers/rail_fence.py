import re

'''
print("Welcome to the rail fence cipher")
# Read in the input, ensuring to sanitise the choice and key
while True:
    choice = int(input("Do you want to encrypt (1) or decrypt (2): "))
    if choice == 1 or choice == 2:
        break
    else:
        print("Invalid option. PLease select a different option.")

message = input("Enter message: ")

while True:
    try:
        key = int(input("Enter the number of rails ( > 0): "))
        if key < 0:
            raise ValueError
    except ValueError:
        print("Invalid number of rails. Please enter a new number.")
        continue
    else:
        break
'''

# Major credit to https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/

class Rail_fence:

    def __init__(self, message, rails):
        self._message = message
        self._rails = rails

        # Function to encrypt the plain text to cipher text
    def encrypt(self):
       # new_message = re.sub("\W", '', self._message)
        rails = [""] * self._rails
        direc = False  # direction we are traverse the array, false is down, true is up
        i = 0
        for ch in self._message:
            rails[i] += ch

            if i == self._rails - 1:
                direc = True
            elif i == 0:
                direc = False

            if direc == True:
                i -= 1
            else:
                i += 1
        return ''.join(rails)


    def create_matrix(self, message):
    	matrix = [['' for i in range(len(message))] for j in range(self._rails)]
    	direc = False # direction we are traverse the array, false is down, true is up
    	row = 0
    	for col in range(len(message)):
            matrix[row][col] = True
            if row == self._rails - 1:
                direc = True
            elif row == 0:
                direc = False

            if direc == True:
                row -= 1
            else:
                row += 1    	
    	return matrix

    # Function to decrypt provided ciphertext given a key
    def decrypt(self):
       # new_message = re.sub(' ', '', self._message)
        matrix = self.create_matrix(self._message)
        plaintext = ''

        ch_index = 0
        for row in range(self._rails):
        	for col in range(len(self._message)):
        		if (matrix[row][col] == True) and (ch_index < len(self._message)):
        			matrix[row][col] = self._message[ch_index]
        			ch_index += 1

        row = 0
        for col in range(len(self._message)):
            plaintext += matrix[row][col] 
            if row == self._rails - 1:
                direc = True
            elif row == 0:
                direc = False

            if direc == True:
                row -= 1
            else:
                row += 1
       
        return plaintext



'''
# Main body of the program
if choice == 1:
    encrypt(message, key)
elif choice == 2:
    decrypt(message, key)
'''

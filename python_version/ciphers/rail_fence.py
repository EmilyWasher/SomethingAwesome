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


class Rail_fence:

    def __init__(self, message, rails):
        self._message = message
        self._rails = rails

        # Function to encrypt the plain text to cipher text
    def encrypt(self):
        new_message = re.sub("\W", '', self._message)
        rails = [""] * self._rails
        direc = False  # direction we are traverse the array, false is down, true is up
        i = 0
        for ch in new_message:
            rails[i] += ch

            if i == self._rails - 1:
                direc = True
            elif i == 0:
                direc = False

            if direc == True:
                i -= 1
            else:
                i += 1

        #print("Your encrypted message is: ", ''.join(rails))

        return ''.join(rails)

    # Function to decrypt provided ciphertext given a key
    def decrypt(self):
        new_message = re.sub(' ', '', self._message)

        return


'''
# Main body of the program
if choice == 1:
    encrypt(message, key)
elif choice == 2:
    decrypt(message, key)
'''

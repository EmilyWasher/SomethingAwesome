'''
Currently does not work if:
you mispell a word
'''

# Set up dictionary in Australian English
import re
import enchant
d = enchant.Dict("en_AU")

# Print welcome message and gain input from the user

'''
def get_input():
    print("Welcome to Caesar cipher.")
    print("I will attempt to crack your secret message without a key.")
    message = input("Enter the secret message: ")
    words = message.split()
    return words
'''

class Caesar_no_key:
    def __init__(self, message):
        self._message = message

    def crack_caesar(self):
        words = self._message.split()
        print(words)
        key = 0
        plaintxt = []

        while key < 26:
            for w in words:
                new_w = self.decrypt(w, key)
                if self.is_word(new_w) == True:
                    plaintxt.append(new_w)
                    if w == words[-1]:
                        print('The key was: ', key)
                        seperator = ' '
                        return seperator.join(plaintxt)
                else:
                    plaintxt = []
                    key += 1
                    break

        return "I couldn't crack your code :("

    # Function to decrypt provided ciphertext given a key
    def decrypt(self, message, key):
        cipher = ''
        for c in message:
            if c.isalpha():
                num_c = ord(c) - key
                if num_c < ord('a') and 'a' <= c <= 'z':
                    num_c += 26
                elif num_c < ord('A') and 'A' <= c <= 'Z':
                    num_c += 26
                cipher += chr(num_c)
            else:
                cipher += c
        return cipher


    def is_word(self, word):
        if word == '':
            return True
        if re.fullmatch(r"\d+\.\d*", word) is not None:
            return True
        new_word = re.sub("[^a-zA-Z']", '', word)
        return d.check(new_word)



'''
text = crack_caesar()
print("Your message is :", text)
'''
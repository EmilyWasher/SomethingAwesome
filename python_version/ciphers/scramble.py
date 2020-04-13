import string
import random
'''
message = input("Enter your message here:" )
key = 'zyxwvutsrqponmlkjihgfedcba'
'''
class Scramble:

	def __init__(self, message, key = None):
		self._message = message
		if key is None:
			alpha = string.ascii_lowercase
			scramble = ''.join(random.sample(alpha, 26))
			self._lc_alpha = scramble
			self._uc_alpha = scramble.upper()
		else:
			self._lc_alpha = key.lower()
			self._uc_alpha = key.upper()


	def get_key(self):
		return self._lc_alpha


	def encrypt(self):
		ciphertext = ''
		for c in self._message:
			if c.isupper():
				ciphertext += self._uc_alpha[ord(c) - ord('A')]
			elif c.islower():
				ciphertext += self._lc_alpha[ord(c) - ord('a')]
			else:
				ciphertext += c
		return ciphertext


	def decrypt(self):
		plaintext = ''
		alpha = string.ascii_lowercase
		for c in self._message:
			if c.isupper():
				plaintext += alpha[self._uc_alpha.index(c)].upper()
			elif c.islower():
				plaintext += alpha[self._lc_alpha.index(c)]
			else:
				plaintext += c
		print(plaintext)

		return plaintext

'''
cipher = Scramble(message, key)
cipher.printing()
cipher.decrypt()
'''

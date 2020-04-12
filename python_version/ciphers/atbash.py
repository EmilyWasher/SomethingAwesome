class Atbash:
	
	def __init__(self, message):
		self._message = message

	def encode(self):
		new_message = ''
		for c in self._message:
			if c.isupper():
				new_message = new_message + chr(ord('Z') + ord('A') - ord(c))
			elif c.islower():
				new_message = new_message + chr(ord('z') + ord('a') - ord(c))
			else:
				new_message = new_message + c
		return new_message
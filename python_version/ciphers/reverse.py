'''
def get_input():
    print("Welcome to the reverse cipher")
    message = input("Enter the message you would like to encode: ")
    return message
    '''

class Reverse:
	def __init__(self, message):
		self._message = message

	def rev_by_word(self, message):
	    return ' '.join(message.split()[::-1])

	def rev_by_letter(self, message):
	    l = list(message)
	    l.reverse()
	    return ''.join(l)

'''
message = get_input()
word = rev_by_word(message)
letter = rev_by_letter(message)

print("By word is: ", word)
print("By letter is: ", letter)
'''
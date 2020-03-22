while True:
    choice = input("Do you want to encrypt (1) or decrypt (2): ")
    if choice == 1 or choice == 2:
        break
    else:
        print ("Invalid option. PLease select a different option.")

message = raw_input("Enter message: ")

while True:
    try:
        key = int(raw_input("Enter your key (<= 26): "))
        if key > 26 or key < 0:
            raise ValueError
    except ValueError:
        print("Invalid key. Please enter a new key.")
        continue
    else:
        break


def encrypt(message, key):
    cipher = ''
    for c in message:
        if c.isalpha():
            num_c = ord(c) + key
            if num_c > ord('z') and 'a' <= c <= 'z':
                num_c -= 26
            elif num_c > ord('Z') and 'A' <= c <= 'Z':
                num_c -= 26
            cipher += chr(num_c)
        else:
            cipher += c

    print "Encdoded message is: " + str(cipher)


def decrypt(message, key):
    cipher = ''
    for c in message:
        if c.isalpha():
            cipher += chr(ord(c) - key)
        else:
            cipher += c

    print "The decoded message is: " + cipher


while (choice >= 0):
    if choice == 1:
        encrypt(message, key)
        choice = -1
    elif choice == 2:
        decrypt(message, key)
        choice = -1
    else:
        print "Invalid option"
        choice = input("Do you want to encrypt (1) or decrpyt (2): ")

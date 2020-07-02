import random

def encrypting(string_input, key):
    """Encryption function, returning an encrypted string in hexadecimal encoding format separated by a comma"""
    if len(string_input) == 0 or len(key) == 0: raise Exception("You must put a minimum one symbol for 'plain text' or 'key' ")
    if len(string_input) > len(key): raise Exception("The KEY must be longer than STRING")
    array_input = list(string_input) # Seperate the incoming string in array
    key = list(key) 
    cipher_output = []
    for i in range(len(key)): # We use the length of the key because we don't want to show the original length of the message
        if i >= len(array_input):
            cipher_output.append(0 + ord(key[i])) # When the message characters are ended, we continue to encrypt None element
        else:
            cipher_output.append(ord(array_input[i]) + ord(key[i])) # In any character, we add a key and change the original character
        cipher_output[i] = format((cipher_output[i] % 128), 'x') # mod(128) becouse we want to use only ASCII 128
    cipher_text = ",".join(cipher_output) # convert array to string
    return cipher_text

def decrypting(cipher_text_input, key):
    """Decrypting function, return decrypted string. 
    For cipher string have to be encrypted with 'encrypting' and the generated key for this message."""
    cipher_text_input = cipher_text_input.split(",")
    if len(cipher_text_input) > len(key): raise Exception("The KEY must be longer than STRING")
    decrypted_symbols = []
    decrypted_string = ""
    key_symbols = list(key)
    for i in range(len(cipher_text_input)):
        decrypted_symbols.append(chr((int(cipher_text_input[i], 16) - ord(key_symbols[i])) % 128)) # decrypt each character with the corresponding symbol key
    return decrypted_string.join(decrypted_symbols)

def key_generator(length = 100): 
    """Pseudo randomly generated key N characters"""
    #pre_generated_key = [] # in combination with #print("###In decimal:"...... used more than one time make the OTP-system insecure
    #return pre_generated_key
    key_array = [random.randint(33,126) for i in range(length)] # 33-126 use symbols which we can show
    key_string = ""
    for symbol in key_array:
        key_string += chr(symbol)
    return key_string

ans = True
RED = "\033[1;31m" # Bold Red Text
BLUE = "\033[1;34m"
BLACK ="\033[1;30m"
ENDC = '\033[m' # reset to the defaults
while ans:
    print ("""
---ONE TIME PAD---\n1.Encrypting - Enter a plain text message \n2.Decrypting - Enter a ciphertext message and а key\n3.Generate a key - for one time use\n4.Encrypting with a custom key - Enter a plain text message and a key\n0.Exit/Quit
    """)
    #print (RED + "Das ist es!" , ENDC)
    ans=input("Encrypt or Decrypt - Which is your choice?: ")
    if ans=="1":
        plaint_text = input("Type your plain text (up to a hundred ASCII-128 symbols): ")
        key = key_generator()
        print("###Key for decryption:")
        print(BLACK, end = "")
        print(key, ENDC)
        print("###Encrypted/ciphertext:")
        print(RED, end = "")
        print(encrypting(plaint_text, key), ENDC)
    elif ans=="2":
        cipher_text = input("Type your cipher text:")
        key = input("Type cipher key:")
        print("###Decrypted message:")
        print(BLUE, end = "")
        print(decrypting(cipher_text, key), ENDC)
    elif ans=="3":
        print("###Key for decryption and encription - only for one time use:")
        print(BLACK, end = "")
        print(key_generator(), ENDC)
    elif ans=="4":
        plaint_text = input("Type your plain text (use up to a hundred ASCII-128 symbols): ")
        key = input("Put your key for encryption: ")
        print("###Encrypted/ciphertext:")
        print(RED, end = "")
        print(encrypting(plaint_text, key), ENDC)
    elif ans=="0":
        print("\n Goodbye")
        break
    elif ans !="":
        print("\n Not Valid Choice Try again")
    #ans = False
import random 
import sys

def readFileContent(filePath):
    file_content = None
    with open(filePath, "r") as f:
        print("reading file: ", filePath)
        file_content = f.read()
    return file_content

def writeFileContent(filePath, fileContent):
    with open(filePath, "w") as f:
        f.write(fileContent)
    return

def generateKey(keySize):
    key = []
    for i in range(keySize):
        key.append(chr(random.randrange(26)+ord('A')))
    return("" . join(key))

def generateKeyFile(filePath, keySize):
    key = generateKey(keySize)
    writeFileContent(filePath, key)
    return key

def encrypt(plainText, key):
    cipher_text = ""
    key_len = len(key)
    key_point = 0
    for i in range(len(plainText)):
        x = ord(plainText[i])
        shifts = ord(key[key_point % key_len]) - ord('A')
        offset_point = ord('A') if plainText[i]>='A' and plainText[i]<='Z' else ord('a')
        if (plainText[i]>='A' and plainText[i]<='Z') or (plainText[i]>='a' and plainText[i]<='z'):
            key_point += 1     
            x = ((ord(plainText[i])-offset_point) + shifts) % 26 + offset_point
        cipher_text += chr(x)
    return cipher_text

def encryptFile(filePath, keyPath):
    key = readFileContent(keyPath).strip()
    plaintext = readFileContent(filePath)
    ciphertext = encrypt(plaintext, key)
    outfilepath = filePath[:filePath.rfind(".")] + "_enc"+filePath[filePath.rfind("."):]
    writeFileContent(outfilepath, ciphertext)
    return ciphertext, outfilepath

def decrypt(cipherText, key):
    plain_text = ""
    key_len = len(key)
    key_point = 0
    for i in range(len(cipherText)):
        x = ord(cipherText[i])
        shifts = ord(key[key_point % key_len]) - ord('A')
        offset_point = ord('A') if cipherText[i]>='A' and cipherText[i]<='Z' else ord('a')
        if (cipherText[i]>='A' and cipherText[i]<='Z') or (cipherText[i]>='a' and cipherText[i]<='z'):
            key_point += 1     
            x = ((ord(cipherText[i])-offset_point) - shifts) % 26 + offset_point
        plain_text += chr(x)
    return plain_text

def decryptFile(filePath, keyPath):
    key = readFileContent(keyPath).strip()
    cipher_text = readFileContent(filePath)
    plain_text = decrypt(cipher_text, key)
    outfilepath = filePath[:filePath.rfind(".")] + "_dec"+filePath[filePath.rfind("."):]
    writeFileContent(outfilepath, plain_text)
    return plain_text, outfilepath

def help():
    print ('''Commands are in form of [command action] [parameters]:
        keygen  keysize keypath
        encrypt keypath filepath
        decrypt keypath filepath
    ''')
   
print(len(sys.argv))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Wrong number of commandline args. Use help to see the detail.")
        sys.exit(1)
   
    command_action =  sys.argv[1]
    if command_action == "help":
        help()
        sys.exit(0)     

    if command_action == "keygen":
        if len(sys.argv) != 4:
            help()
            sys.exit(1)
        else:
            generateKeyFile(sys.argv[3], int(sys.argv[2]))
            sys.exit(0) 
    elif  command_action == "encrypt":
        if len(sys.argv) != 4:
            help()
            sys.exit(1)
        else:
            print(sys.argv[3], sys.argv[2])
            encryptFile(sys.argv[3], sys.argv[2])
            sys.exit(0) 
    elif  command_action == "decrypt":
        if len(sys.argv) != 4:
            help()
            sys.exit(1)
        else:
            print(sys.argv[3], sys.argv[2])
            decryptFile(sys.argv[3], sys.argv[2])
            sys.exit(0) 
    else:
        print ("Invalid command.")
        help()
        sys.exit(1)
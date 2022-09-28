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
    print("key_len:", key_len)

    for i in range(len(plainText)):
        x = ord(plainText[i])
        if plainText[i]>='A' and plainText[i]<='Z':
            shifts = ord(key[i%key_len]) - ord('A')
            print(shifts)
            x = ((ord(plainText[i])-ord('A')) + ord(key[i%key_len]) - ord('A')) % 26 + ord('A')
        cipher_text += chr(x)
    return cipher_text

def encryptFile(filePath, keyPath):
    key = readFileContent(keyPath).strip()
    plaintext = readFileContent(filePath)
    print("file content:", plaintext)
    print("key content:" + key + "--")
    ciphertext = encrypt(plaintext, key)
    outfilepath = filePath[:filePath.rfind(".")] + "_enc"+filePath[filePath.rfind("."):]
    writeFileContent(outfilepath, ciphertext)
    return ciphertext, outfilepath

def decrypt(ciphertext, key):
    plaintext = ""
    return plaintext

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

    if int(sys.argv[1]) < 1:
        print ("Keysize should be 0<")
        sys.exit(1)
    print (generateKey(int(sys.argv[1])))
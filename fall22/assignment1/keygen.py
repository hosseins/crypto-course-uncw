import random 
import sys

def generateKey(keySize):
    key = []
    for i in range(keySize):
        key.append(chr(random.randrange(26)+ord('A')))
    return("" . join(key))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(len(sys.argv))
        print ("Wrong number of commandline arg. Command format is: python keygen keysize")
        sys.exit(1)
    if int(sys.argv[1]) < 1:
        print ("Keysize should be 0<")
        sys.exit(1)
    print (generateKey(int(sys.argv[1])))
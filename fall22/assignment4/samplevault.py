import os
import base64

def setEnvVar():
    os.environ["VAULT_ADDR"] = "http://127.0.0.1:8200"
    os.environ["VAULT_TOKEN"] = "hvs.UiC8YM6sXNJOE8eoKsbPAZFz"

def enableTransitEngine():
    try:
        os.system("vault secrets enable transit")
    except:
        print("The transit engine is already being enabled.")

def createKey():
    keyname = "mykey"
    os.system("vault write -f transit/keys/{}".format(keyname))

def decodeMessage(cipher):
    return

def encryptMessage(plain, key):
    b = base64.b64encode(bytes(plain, 'utf-8'))
    print(str(b))
    os.system("vault write transit/encrypt/{} plaintext={}".format(key, b.decode('utf-8')))
    return


setEnvVar()
encryptMessage("Hello secret world!", "emilyskey")

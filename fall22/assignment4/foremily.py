import base64
import json
import hvac

def init_server(client):
    print("Initializing server and checking client authentication: {client.is_authenticated()}")

def write_secret(client):
    create_response = client.secrets.kv.v2.create_or_update_secret(path='hello', secret=dict(foo="bar"))
    print(create_response)

def read_secret(client):
    read_responce = client.secrets.kv.v2.read_secret_version(path='hello')
    print(read_response)
    
def create_key(client):
    client.secrets.transit.create_key(name='my_python_key', key.type='aes256-gcm96')   #I noticed terrance used my_python_key instead
                                                                                    ## of hvac-key so I used it throughout in place of hvac-key, should I've?
def read_key(client):                                                                           
    read_key_response = client.secrets.transit.read_key(name='my_python_key')
    latest_version = read_key_response['data']['lastest_version']
    print('Latest version for key "my_python_key" is: , {ver}'.format(ver=latest_version))

def base64ify():                            #Dont really know how to set this one up
    
def transit_encrypt(client, plain_text):
    #text_bytes = plain_text.encode("utf-8")
    #json_str = json.dumps(text_bytes.decode("utf-8"))
    encrypt_data_response = client.secrets.transit.encrypt_data(name='my_phyton_key', plaintext=json_str.encode())
    ciphertext = encrypt_data_response['data']['ciphertext']
    print('Encrypted plaintext ciphertext is: {cipher}'.format(cipher=ciphertext))

def transit_decrypt(client, ciphertext, decrypt_key="my.python_key"): 
    decrypt_data_response = client.secrets.transit.decrypt_data(name=decrypt_key, ciphertext=ciphertext)
    return str(base64.b64decode(decrypt_data_response['data']['plaintext']), "utf-8")

if __name__==__main__:                  #Am I setting my driver up correctly?
    clt = hvac.Client(url='https://localhost:8200')
    init_server(clt)
    write_secret(clt)
    read_secret(clt)
    create_key(clt)
    read_key(clt)
    transit_encrypt(clt, "This is the plaintext to be encrypted")  #Would this be where I enter the plaintext to be encrypted?
    transit_decrypt(clt, )                #Dont know what to enter for 2nd or 3rd parameter
main()
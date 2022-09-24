from Crypto import Random
from Crypto.PublicKey import RSA

def generarLlaves ():
    random_generator = Random.new().read

    rsas= RSA.generate(1024,random_generator)

    ClavePrivada = rsas.export_key()
    with open('clvp.txt','wb') as f:
        f.write(ClavePrivada)

    ClavePublica = rsas.public_key().export_key()
    with open('clvpu.txt','wb') as f:
        f.write(ClavePublica)

    print(ClavePrivada)
    print(ClavePublica)
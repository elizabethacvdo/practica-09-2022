from hmac import digest
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs_1_v1_5
from Crypto.PublicKey import RSA
import base64

def verificar(mensaje,firma):
    with open('clvpu.txt') as f:
        key = f.read()
        rsaKey = RSA.import_key(key)
        verifier = Signature_pkcs_1_v1_5.new(rsaKey)
        digest  = SHA.new()

        digest.update(mensaje)
        print(digest.hexdigest())
        is_verify = verifier.verify(digest,base64.b64decode(firma))
    
    if is_verify:
        print("----------------------Documento no alterado------------------------")

    else:
        print("----------------mensaje alterado--------------------------")


with open("datos.txt",'r') as f1:
    mensaje = f1.read()

with open('firma.txt','r') as f2:
    firma = f2.read()

mensaje = mensaje.encode()
verificar(mensaje,firma)
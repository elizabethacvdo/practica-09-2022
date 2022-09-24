import base64
from inspect import signature
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs_1_v1_5
from Crypto.PublicKey import RSA

def firmar(mensaje):
    with open('clvp.txt') as f:
        key = f.read()
        rsaKey= RSA.import_key(key)
        signer = Signature_pkcs_1_v1_5.new(rsaKey)
        digest  = SHA.new()
        digest.update(mensaje)
        print(mensaje)
        print(digest.hexdigest())
        sing = signer.sign(digest)
        signature = base64.b64encode(sing)
    
    with open('firma.txt','wb') as fp1:
        fp1.write(signature)
        fp1.close()
        print(signature)
        
    return signature

with open('datos.txt','r') as f1:
    mensaje = f1.read()
mensaje = mensaje.encode()
signature = firmar(mensaje)
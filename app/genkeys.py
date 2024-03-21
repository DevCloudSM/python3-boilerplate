from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives import serialization  
from cryptography.hazmat.primitives.asymmetric import rsa

class Genkeys:
	"""docstring for Genkeys"""
	def __init__(self):
		super(Genkeys, self).__init__()

		def save_file(filename, content):  
		   f = open(filename, "wb")  
		   f.write(content)
		   f.close()  
		  
		  
		# generate private key & write to disk  
		private_key = rsa.generate_private_key(  
		    public_exponent=65537,  
		    key_size=4096,  
		    backend=default_backend()  
		)  
		pem = private_key.private_bytes(  
		    encoding=serialization.Encoding.PEM,  
		    format=serialization.PrivateFormat.PKCS8,  
		    encryption_algorithm=serialization.NoEncryption()  
		)
		# DEV:
		#save_file("./data/private.pem", pem)
		# PROD:
		save_file("/var/lib/NOM_APPLI/data/private.pem", pem)  
		  
		# generate public key  
		public_key = private_key.public_key()  
		pem = public_key.public_bytes(  
		    encoding=serialization.Encoding.PEM,  
		    format=serialization.PublicFormat.SubjectPublicKeyInfo  
		)
		# DEV:
		#save_file("./shared/private.pem", pem)
		# PROD:
		save_file("/var/lib/NOM_APPLI/shared/jwt_rsa.pem", pem)  
from cryptography.fernet import Fernet
key = Fernet.generate_key()
c = Fernet(key)
pw = c.encrypt("pass")
print(pw)

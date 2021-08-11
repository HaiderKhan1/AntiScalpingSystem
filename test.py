from cryptography.fernet import Fernet
import random
# we will be encryting the below string.
message = "hello geeks"

print(random.randint(100000000000,999999999999))
  
# generate a key for encryptio and decryption
# You can use fernet to generate 
# the key or use random key generator
# here I'm using fernet to generate key
  
key = '1kzTkTXWNjrV3wHfAZUKIJI8CkvzwB0nmVH_S10lpe0='
  
# Instance the Fernet class with the key
  
fernet = Fernet(key)
  
# then use the Fernet class instance 
# to encrypt the string string must must 
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())
  
print("original string: ", message)
print("encrypted string: ", encMessage)
  
# decrypt the encrypted string with the 
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methos
decMessage = fernet.decrypt(encMessage).decode()
  
print("decrypted string: ", decMessage)
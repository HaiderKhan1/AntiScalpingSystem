from cryptography.fernet import Fernet

key = "1kzTkTXWNjrV3wHfAZUKIJI8CkvzwB0nmVH_S10lpe0="
fernet = Fernet(key)

# cc = "5460837053669256"

# cc_encrypted = fernet.encrypt(cc.encode())
# char_cc = list(cc_encrypted.decode())
# char_cc.insert(0,"'")
# char_cc.insert(len(char_cc), "'")
# cc_encrypted = ''.join(char_cc)

# print(cc_encrypted)

cc = "gAAAAABhGD4i9NVlmD-ZorxeeulvoGYtPVD6tJ9kfamDs6ZZDVeRSzz9skgRYcs9o0dBJ3HYRD2JhCV9cuBlm5iU5ufXbyrCerxksk7qY0DntT9e46YxcSk="
decMessage = fernet.decrypt(cc.encode()).decode()
  
print( decMessage)

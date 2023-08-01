import hashlib
hashList=['md5 ','sha1 ','sha224 ', 'sha256 ', 'sha334 ', 'sha512 ' ]
print("")
print("Avalaible Hashes to encode")
print("______________________________________________")
print(''.join(hashList))
print("----------------------------------------------")
print("")
word = input("Enter the password: ")
algoritm = input("Enter the name of algoritm: ")
if algoritm == "md5" or "sha1" or "sha224" or "sha256" or "sha384" or "sha512":
    coders = hashlib.new(algoritm)
if word == any:
    coders.update.__str__(word)
print()
print("hash:",coders.hexdigest())

import hashlib

hashList=['md5 ','sha1 ','sha224 ', 'sha256 ', 'sha384 ', 'sha512 ' ]
print("")
print("Avalaible Hashes to encode")
print("______________________________________________")
print(''.join(hashList))
print("----------------------------------------------")
print("")

word = input("Enter the password: ")
algoritm = input("Enter the name of algoritm: ")

convert = hashlib.new(algoritm)
convert.update(word.encode()) 
print("")
print("hash:",convert.hexdigest())

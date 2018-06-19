import random
import string
#from Crypto.Cipher import AES 
#from Crypto import Random
import os 
import sys
'''class Encryption:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + "\0" * (AES.block_size - len(s) % AES.block_size)
    def decrypt(self,cipherText,key):
        iv=cipherText[:AES.block_size]
        cipher=AES.new(key,AES.MODE_CBC,iv)
        data=cipher.decrypt(cipherText[AES.block_size:])
        return data.rstrip(b"\0")
    def decrypt_file(self,filename):
        with  open(filename,"rb") as fp:
            cipherText=fp.read()
        dec=self.decrypt(cipherText,self.key)
        with open(filename[:-4],"wb") as fp:
            fp.write(dec)
    
key1=b'\xa4\xe4\xfe\xef7\xfe\xab\xd1\x92\x86\xa7\xfc\x9eM\xbe\xeb'
enc=Encryption(key1)'''



originaltxt=''
def key(word,key):
    global originaltxt
    originaltxt+=word[int(key)]
    

#start

#enc.decrypt_file(sys.argv[1])


f=open("output_random.txt","r")
d=f.read()
x=d.split()
with open("key.txt") as fp:
    keyval=fp.read()
keys=keyval.split()

cnt=0
for i in (keys):
    k=i.split("/")
    for j in range(int(k[1])):
        try:
            key(x[cnt],int(k[0]))
            cnt+=1
        except Exception as e:
            print("word="+x[cnt],e.message)
            pass
    originaltxt+=" "
print("original text====",originaltxt)



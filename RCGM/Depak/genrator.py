import random
import string
#from Crypto.Cipher import AES 
#from Crypto import Random
import os 
z=0
b=''
def goalWord(y):  
    n=len(y)
    entxt=''
    z=random.randint(0,n)
    with open("key.txt","a") as fp:
        fp.write(" "+str(z)+"/"+str(n))
    
    for i in range(n):   
            try: 
                with open("words.txt","r") as wordbook:
                    words = (line.rstrip('\n') for line in wordbook)
                    
                    large_words = [word for word in words if len(word)>z]
                    large_words1= [word for word in large_words if word[z]==y[i]]
                    entxt+=random.choice(large_words1)+" "
            except Exception as e:
                print("word="+y,e.message)
                pass

    return entxt

    #expand  data
def  expand():
    txt=''
    f=open("index.txt", "r")
    g=f.read()
    g=g.lower()
    da=g.split()

    for i in da:

        # calling the method of goalword
       txt+=' '+goalWord(i)
    return txt

txt=expand()

with open('output_random.txt', 'w+') as fout:
        #print(fout)
            for char in txt:
            #print(char,type(char))
                    fout.write(char) 

# creating new  random file
'''def newfile(txt):
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase

    d=s1+s2
    global  b
    for i in range(0,random.randint(0,5)):
      
      b+= random.choice(d)
    b+=".txt"
    f= open(b,"w+")
    f.write(txt)'''
        
'''     #aes encryption
class Encryption:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + "\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, msg, key, key_size=256):
        msg = self.pad(msg)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv+cipher.encrypt(msg)

    def encrypt_file(self, filename):
        with open(filename, 'rb') as fp:
            data = fp.read()
        enc = self.encrypt(data, self.key)
        with open(filename+".enc", "wb") as fp:
            fp.write(enc)

   #key  

key = b'\xa4\xe4\xfe\xef7\xfe\xab\xd1\x92\x86\xa7\xfc\x9eM\xbe\xeb'
enc = Encryption(key)
 '''



#start 



#enc.encrypt_file(b)
# deleteing the .txt file 

#os.remove(b)



#deleting the data in text file

#f = open('index.txt', 'r+')
#f.truncate()



















    



   
    

#GET DATA FROM PREINDEX
msg=open("preindex.txt", "r")
txt=msg.read()


convert=str(txt)
b=''

#CONVERTING THE VALUE
x={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h'}
for i in convert:
        b+=x.get(i)

cnt=0
for i in range(len(b)):    
    if cnt==6:
        #to accesingf string character 
        b=b[:i]+" "+b[i:]
        cnt=0
    cnt+=1

f= open("index.txt","w+")
f.write(b)






    






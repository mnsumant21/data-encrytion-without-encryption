from tkinter import *
import random
from PIL import Image as img

from tkinter import filedialog

def EPressed():                          #function
                                 #main window
    button1 = Button(root, text = 'Input file', command = Input)
    button1.pack(pady=20, padx = 20)

def DPressed():                          #function
                                #main window
    button1 = Button(root, text = 'Encrypted file', command = Output)
    button1.pack(pady=20, padx = 20)


def Input():

    #function

    list=[]
    list_bcd=[]
    lib_ch=[]
    lib_final=[]
    count=0
    lib_final2=''
    lib_final_list=[]
    rand_list=['00','01','10','11']
    root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/SUMANTH/Desktop/",title = "Select file")
    #print(root.filename)
    file_obj = open(root.filename,"r")
    z = file_obj.read()
    s = [ord(c) for c in z]
    #print(s)

    
    #s=input("Enter the input:")
    def ascii_conv(s):
            for c in s:
                    #integer=ord(c)
                    integerstr=str(c).zfill(3)
                    #print(integerstr)
                    list.extend(integerstr)
                    #print(list)
            return list
    ascii_conv(s)
    #print(list)
    #print('over')
    
    
    for li in list:
            if li=='0':
                    list_bcd.append('0000')
            elif li=='1':
                    list_bcd.append('0001')
            elif li=='2':
                    list_bcd.append('0010')
            elif li=='3':
                    list_bcd.append('0011')
            elif li=='4':
                    list_bcd.append('0100')
            elif li=='5':
                    list_bcd.append('0101')
            elif li=='6':
                    list_bcd.append('0110')
            elif li=='7':
                    list_bcd.append('0111')
            elif li=='8':
                    list_bcd.append('1000')
            elif li=='9':
                    list_bcd.append('1001')



    
    

    

    
    def add_bits(list_bcd):       
            for lib in list_bcd:
                    lib=random.choice(rand_list)+lib
                    lib_ch.append(lib)
                    

    
    

    ascii_conv(s)
    add_bits(list_bcd)
    
    #print(lib_ch)      
    

    

    length=int((len(lib_ch))/3)
    #print(length)

    while(count<=length-1):
     

            lib_final.append(lib_ch[:3])
            #print(lib_final)
            #print("\n")
            lib_ch=lib_ch[3:]
            #print(lib_ch)
            count=count+1
    

    

    #print(lib_final)
    #print(lib_ch)

    

    for i in range(0,length):
            for j in range(0,3):
                    lib_final2=lib_final2+lib_final[i][j]
            #print(lib_final2)
            lib_final_list.append(lib_final2)
            lib_final2=''
    #print(lib_final_list)


    s=[]
    final_list=[]

    for i in lib_final_list:
            while i:
                    s.append(i[:2])
                    i=i[2:]
            final_list.append(s)
            s=[]
    #print(final_list)


                                 #main window
    button1 = Button(root, text = 'Pattern to encrypt', command = lambda: Pattern_to_encrypt(final_list))
    button1.pack(pady=20, padx = 20)

    


    

def Pattern_to_encrypt(final_list):
    
    root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/SUMANTH/Desktop/",title = "Select file")
    #print(root.filename)
    im = img.open(root.filename)
    width, height = im.size
    img_string = im.tobytes()
    with open('outfile.txt', 'w+') as fout:
        #print(fout)
            for char in img_string:
            #print(char,type(char))
                    fout.write( format(char,'02x')) 

    
    inputFile = open('outfile.txt', 'r').read()    #Open test.txt file in read mode
    #print inputFile
    count_of_0=0 
    count_of_1=0 
    count_of_2=0 
    count_of_3=0 
    count_of_4=0 
    count_of_5=0
    count_of_6=0 
    count_of_7=0 
    count_of_8=0 
    count_of_9=0 
    count_of_a=0 
    count_of_b=0 
    count_of_c=0 
    count_of_d=0 
    count_of_e=0 
    count_of_f=0 
    for i in inputFile:
            if(i=='0'):
                    count_of_0=count_of_0+1	
            elif(i=='1'):
                    count_of_1=count_of_1+1
            elif(i=='2'):
                    count_of_2=count_of_2+1
            elif(i=='3'):
                    count_of_3=count_of_3+1
            elif(i=='4'):
                    count_of_4=count_of_4+1
            elif(i=='5'):
                    count_of_5=count_of_5+1
            elif(i=='6'):
                    count_of_6=count_of_6+1
            elif(i=='7'):
                    count_of_7=count_of_7+1
            elif(i=='8'):
                    count_of_8=count_of_8+1
            elif(i=='9'):
                    count_of_9=count_of_9+1
            elif(i=='a'):
                    count_of_a=count_of_a+1
            elif(i=='b'):
                    count_of_b=count_of_b+1
            elif(i=='c'):
                    count_of_c=count_of_c+1
            elif(i=='d'):
                    count_of_d=count_of_d+1
            elif(i=='e'):
                    count_of_e=count_of_e+1
            elif(i=='f'):
                    count_of_f=count_of_f+1
                    
                    
    '''print("Number of '0' are:",count_of_0)		
    print("Number of '1' are:",count_of_1)		
    print("Number of '2' are:",count_of_2)	
    print("Number of '3' are:",count_of_3)	
    print("Number of '4' are:",count_of_4)
    print("Number of '5' are:",count_of_5)
    print("Number of '6' are:",count_of_6)
    print("Number of '7' are:",count_of_7)
    print("Number of '8' are:",count_of_8)
    print("Number of '9' are:",count_of_9)
    print("Number of 'a' are:",count_of_a)
    print("Number of 'b' are:",count_of_b)
    print("Number of 'c' are:",count_of_c)
    print("Number of 'd' are:",count_of_d)
    print("Number of 'e' are:",count_of_e)
    print("Number of 'f' are:",count_of_f)'''

    a=[count_of_0,count_of_1,count_of_2,count_of_3,count_of_4,count_of_5,count_of_6,count_of_7,count_of_8,count_of_9,count_of_a,count_of_b,count_of_c,count_of_d,count_of_e,count_of_f]
    index=[]
    #print(a)

    x=0
    for i in a:
            while i:
                    x = i%10
                    if x not in index:
                            index.append(x)
                            break
                    else:
                            i=int(i/10)
    #print(index)

    
    
    
    #print(list)
    #print(index)
    
    #index=[8, 1, 4, 7, 5, 2, 3, 6,9,0]
    index.remove(9)

    final_list2=[]
    main_list=[]
    length=len(final_list)
    #print(length)

    for i in range(0,length):
        new_list=[final_list[i][j] for j in index]
        final_list2=final_list2+new_list
    #print(final_list2)

    leng=len(final_list2)   
    for i in range(0,leng):
        for j in range(0,2):
            main_list=main_list+[final_list2[i][j]]
    #print(main_list)

    leng=int(len(main_list))

    super_final=[]




    for i in range(0,leng,3):
        super_final=super_final+[main_list[i]+main_list[i+1]+main_list[i+2]]

        
    #print(super_final)
    code=''
    for i in range(0,len(super_final)):
        code=code+str((int(super_final[i],2)))

    #print(code)

    with open('code.txt', 'w+') as fout:
            for char in code:
            #print(char,type(char))
                    fout.write(char)

    print("Encryption done")

    root.destroy()
            


    
def Output():
    list_bcd=[]
    main_list=[]
    mainn_list=[]
    last_list=[]
    llist=[]
    data=''
    ori_data=''
    #input=input("Enter the value")
    
    root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/SUMANTH/Desktop/",title = "Select file")
    #print(root.filename)
    input_file = open(root.filename,"r")
    #print(input)
    for i in input_file.read():
        if i=='0':
            list_bcd.append('000')
        elif i=='1':
            list_bcd.append('001')
        elif i=='2':
            list_bcd.append('010')
        elif i=='3':
            list_bcd.append('011')
        elif i=='4':
            list_bcd.append('100')
        elif i=='5':
            list_bcd.append('101')
        elif i=='6':
            list_bcd.append('110')
        elif i=='7':
            list_bcd.append('111')
    #print(list_bcd)

    leng=len(list_bcd)
    for i in range(0,leng):
        for j in range(0,3):
            main_list=main_list+[list_bcd[i][j]]
    #print(main_list)
                            
            
    lengt=len(main_list)       
    for i in range(0,lengt-1,2):
            temp=main_list[i]+main_list[i+1]
            last_list.append(temp)
    
    #print(last_list)
    
    #index=[8, 1, 4, 7, 5, 2, 3, 6,0]
    
    #print(length3)
    #print(index)
    
    

    
    #print(super_list)

                                #main window
    button1 = Button(root, text = 'Pattern to decrypt', command = lambda: Pattern_to_decrypt(last_list,leng))
    button1.pack(pady=20, padx = 20)


def Pattern_to_decrypt(last_list,leng):

    length3=len(last_list)
    super_list=[0]*length3
    
    root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/SUMANTH/Desktop/",title = "Select file")
    #print(root.filename)
    #file_obj = open(root.filename,"r")
    #z = file_obj.read()
    im = img.open(root.filename)
    width, height = im.size
    img_string = im.tobytes()
    with open('outfile.txt', 'w+') as fout:
        #print(fout)
            for char in img_string:
            #print(char,type(char))
                    fout.write( format(char,'02x')) 

    
    inputFile = open('outfile.txt', 'r').read()    #Open test.txt file in read mode
    #print inputFile
    count_of_0=0 
    count_of_1=0 
    count_of_2=0 
    count_of_3=0 
    count_of_4=0 
    count_of_5=0
    count_of_6=0 
    count_of_7=0 
    count_of_8=0 
    count_of_9=0 
    count_of_a=0 
    count_of_b=0 
    count_of_c=0 
    count_of_d=0 
    count_of_e=0 
    count_of_f=0 
    for i in inputFile:
            if(i=='0'):
                    count_of_0=count_of_0+1	
            elif(i=='1'):
                    count_of_1=count_of_1+1
            elif(i=='2'):
                    count_of_2=count_of_2+1
            elif(i=='3'):
                    count_of_3=count_of_3+1
            elif(i=='4'):
                    count_of_4=count_of_4+1
            elif(i=='5'):
                    count_of_5=count_of_5+1
            elif(i=='6'):
                    count_of_6=count_of_6+1
            elif(i=='7'):
                    count_of_7=count_of_7+1
            elif(i=='8'):
                    count_of_8=count_of_8+1
            elif(i=='9'):
                    count_of_9=count_of_9+1
            elif(i=='a'):
                    count_of_a=count_of_a+1
            elif(i=='b'):
                    count_of_b=count_of_b+1
            elif(i=='c'):
                    count_of_c=count_of_c+1
            elif(i=='d'):
                    count_of_d=count_of_d+1
            elif(i=='e'):
                    count_of_e=count_of_e+1
            elif(i=='f'):
                    count_of_f=count_of_f+1
                    
                    
    '''print("Number of '0' are:",count_of_0)		
    print("Number of '1' are:",count_of_1)		
    print("Number of '2' are:",count_of_2)	
    print("Number of '3' are:",count_of_3)	
    print("Number of '4' are:",count_of_4)
    print("Number of '5' are:",count_of_5)
    print("Number of '6' are:",count_of_6)
    print("Number of '7' are:",count_of_7)
    print("Number of '8' are:",count_of_8)
    print("Number of '9' are:",count_of_9)
    print("Number of 'a' are:",count_of_a)
    print("Number of 'b' are:",count_of_b)
    print("Number of 'c' are:",count_of_c)
    print("Number of 'd' are:",count_of_d)
    print("Number of 'e' are:",count_of_e)
    print("Number of 'f' are:",count_of_f)'''

    a=[count_of_0,count_of_1,count_of_2,count_of_3,count_of_4,count_of_5,count_of_6,count_of_7,count_of_8,count_of_9,count_of_a,count_of_b,count_of_c,count_of_d,count_of_e,count_of_f]
    index=[]
    #print(a)

    x=0
    for i in a:
            while i:
                    x = i%10
                    if x not in index:
                            index.append(x)
                            break
                    else:
                            i=int(i/10)
    #print(index)

    
    
    
    #print(list)
    #print(index)
    
    #index=[8, 1, 4, 7, 5, 2, 3, 6,9,0]
    index.remove(9)


    def shuffle(last_list,super_list,index):
        
        k=0
        for i in index:
            
            super_list[i]=last_list[k]
        
            k=k+1

        return last_list,super_list,index

    times=int(length3/9)
    for i in range(0,times):
        shuffle(last_list,super_list,index)
    
    
        last_list=last_list[9:]
        index=[x +9 for x in index]
    

    

    '''print("FROMHERE")    
    print(last_list)
    print(super_list)
    print(index)'''

    length2=len(super_list)
    #print(length2)
    for i in range(0,length2):
        if i%3==0:
            super_list[i]='none'

    #print(super_list)

    super_list=[i for i in super_list if i not in('none')]
    #print(super_list)
    
    
    
    
    
    mainn_list=[]
    llist=[]
    data=''
    ori_data=''
    
    for i in range(0,leng):
        for j in range(0,2):
            mainn_list=mainn_list+[super_list[i][j]]
    #print(mainn_list)

    length4=len(mainn_list)       
    for i in range(0,length4-1,4):
            temp=mainn_list[i]+mainn_list[i+1]+mainn_list[i+2]+mainn_list[i+3]
            llist.append(temp)

    #print(llist)

    for i in llist:
        if i=='0000':
            data=data+'0'
        elif i=='0001':
            data=data+'1'
        elif i=='0010':
            data=data+'2'
        elif i=='0011':
            data=data+'3'
        elif i=='0100':
            data=data+'4'
        elif i=='0101':
            data=data+'5'
        elif i=='0110':
            data=data+'6'
        elif i=='0111':
            data=data+'7'
        elif i=='1000':
            data=data+'8'
        elif i=='1001':
            data=data+'9'
        '''elif i=='1010':
            data=data+'a'
        elif i=='1011':
            data=data+'b'
        elif i=='1100':
            data=data+'c'
        elif i=='1101':
            data=data+'d'
        elif i=='1110':
            data=data+'e'
        elif i=='1111':
            data=data+'f'''

    #print(data)

   


    
    data_len=len(data)
    
    #print(data_len)

    for i in range(0,data_len-2,3):
        
        tempor=data[i]+data[i+1]+data[i+2]
        #print(tempor)
        ori_data=ori_data+chr(int(tempor))
        #print(ori_data)
        
    

    with open('original.txt', 'w+') as fout:
        #print(fout)
            for char in ori_data:
            #print(char,type(char))
                    fout.write(char)

    print("Decryption done")

    root.destroy()

    
root = Tk()
root.title('PROJECT RCMG')
root.geometry('1100x350+500+300')
root.configure(background='grey')
button1 = Button(root, text = 'Encrypt', command = EPressed)#,width=100, bg ='yellow', fg='red', activebackground='violet', activeforeground='black')
button1.pack(pady=20, padx = 20)
button2 = Button(root, text = 'Decrypt', command = DPressed)
button2.pack(pady=20, padx = 20)


root.mainloop()

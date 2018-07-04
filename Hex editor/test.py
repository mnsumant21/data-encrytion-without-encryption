from tkinter import *
from tkinter import filedialog
import binascii

root=Tk()
input("Press enter to input a file")
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/SUMANTH/Desktop/",title = "Select file")
with open(root.filename, "rb") as file_obj:
	content = file_obj.read()
	b = binascii.hexlify(content)

print(b)
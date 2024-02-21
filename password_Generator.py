import string 
import tkinter as tk
import random
import pyperclip

    
def password_generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation
    
    total=small_alphabets+capital_alphabets+numbers+special_characters
    
    password_length=int(length_Box.get())
    
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
        
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    
    if choice.get()==3:
        passwordField.insert(0,random.sample(total,password_length))
    
 
def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
    
root=tk.Tk()
root.config(bg='black')
choice=tk.IntVar()
Font=('arial',13,'bold')

passwordLabel=tk.Label(root, text='Password Generator', font=('times new roman',20,'bold'),bg='gray',fg='white')
passwordLabel.grid(pady=10)

weak_radioButton=tk.Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weak_radioButton.grid(pady=5)

medium_radioButton=tk.Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
medium_radioButton.grid(pady=5)

strong_radioButton=tk.Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strong_radioButton.grid(pady=5)

lengthLabel=tk.Label(root, text='Password Length', font=('times new roman',20,'bold'),bg='gray',fg='white')
lengthLabel.grid(pady=5)

length_Box=tk.Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generate_Button=tk.Button(root,text='Generate',font=Font,command=password_generator)
generate_Button.grid(pady=5)

passwordField=tk.Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

copyButton=tk.Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)

root.mainloop()

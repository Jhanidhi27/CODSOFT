import tkinter as tk 

calculation=""

def insert_to_calculator(symbol):    #Adding numbers to calculator for performing calculations.
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    
    
def perform_calculations():  #to solve any expression.
    global calculation
    print(calculation)
    try:
        result=str(eval(calculation))
        calculation=""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear_display()
        text_result.insert(1.0,"ERROR")
    

def clear_display():      #to clear the display board.
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

root=tk.Tk()
root.geometry("300x275")

text_result=tk.Text(root,height=2,width=16,font=("Arial",24) )
text_result.grid(columnspan=5)

button_1=tk.Button(root,text="1", command=lambda: insert_to_calculator(1),width=5,font=("Arial",15))
button_1.grid(row=2,column=1)

button_2=tk.Button(root,text="2", command=lambda: insert_to_calculator(2),width=5,font=("Arial",15))
button_2.grid(row=2,column=2)

button_3=tk.Button(root,text="3", command=lambda: insert_to_calculator(3),width=5,font=("Arial",15))
button_3.grid(row=2,column=3)

button_4=tk.Button(root,text="4", command=lambda: insert_to_calculator(4),width=5,font=("Arial",15))
button_4.grid(row=3,column=1)

button_5=tk.Button(root,text="5", command=lambda: insert_to_calculator(5),width=5,font=("Arial",15))
button_5.grid(row=3,column=2)

button_6=tk.Button(root,text="6", command=lambda: insert_to_calculator(6),width=5,font=("Arial",15))
button_6.grid(row=3,column=3)

button_7=tk.Button(root,text="7", command=lambda: insert_to_calculator(7),width=5,font=("Arial",15))
button_7.grid(row=4,column=1)

button_8=tk.Button(root,text="8", command=lambda: insert_to_calculator(8),width=5,font=("Arial",15))
button_8.grid(row=4,column=2)

button_9=tk.Button(root,text="9", command=lambda: insert_to_calculator(9),width=5,font=("Arial",15))
button_9.grid(row=4,column=3)

button_0=tk.Button(root,text="0", command=lambda: insert_to_calculator(0),width=5,font=("Arial",15))
button_0.grid(row=5,column=2)

button_add=tk.Button(root,text="+", command=lambda: insert_to_calculator("+"),width=5,font=("Arial",15))
button_add.grid(row=2,column=4)

button_sub=tk.Button(root,text="-", command=lambda: insert_to_calculator("-"),width=5,font=("Arial",15))
button_sub.grid(row=3,column=4)

button_multiply=tk.Button(root,text="*", command=lambda: insert_to_calculator("*"),width=5,font=("Arial",15))
button_multiply.grid(row=4,column=4)

button_division=tk.Button(root,text="/", command=lambda:insert_to_calculator("/"),width=5,font=("Arial",15))
button_division.grid(row=5,column=4)

button_p_open=tk.Button(root,text="(", command=lambda: insert_to_calculator("("),width=5,font=("Arial",15))
button_p_open.grid(row=5,column=1)

button_p_close=tk.Button(root,text=")", command=lambda: insert_to_calculator(")"),width=5,font=("Arial",15))
button_p_close.grid(row=5,column=3)

button_equal_to=tk.Button(root,text="=", command=perform_calculations,width=11,font=("Arial",15))
button_equal_to.grid(row=6,column=3, columnspan=2)

button_clear=tk.Button(root,text="C", command=clear_display ,width=11,font=("Arial",15))
button_clear.grid(row=6,column=1,columnspan=2)

root.mainloop()


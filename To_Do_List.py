import tkinter as tk 
import tkinter.messagebox as tmsg
import random

root=tk.Tk()

root.configure(bg="white")

root.title("To-Do-List")

root.geometry("325x275")

tasks=[]

# tasks=["grocery","sleep","study"]

def insert_tasks():
    clear_tasks()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_tasks():
    lb_tasks.delete(0,"end")


def add_task():
    task=task_input.get()
    if task !="":
        tasks.append(task)
        insert_tasks()
    else:
        tmsg.showwarning("Warning","Please enter a task !")
    task_input.delete(0,"end")

def delete_all():
    Confirmed=tmsg.askyesno("Please Confirm","Do you want to delete all?")
    if Confirmed==True:
        global tasks
        tasks=[]
        insert_tasks()
    

def delete_one():
    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    insert_tasks()
        
def sort_asc():
    tasks.sort()
    insert_tasks()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    insert_tasks()

def Choose_random():
    task=random.choice(tasks)
    display["text"]=task

def Number_Of_Task():
    number_of_task=len(tasks)
    msg="Number of Tasks: %s" %number_of_task
    display["text"]=msg





display=tk.Label(root, text="",bg="white")
display.grid(row=0,column=1)

task_input=tk.Entry(root, width=15)
task_input.grid(row=1,column=1)

add_task=tk.Button(root, text="Add task",fg="green",bg="white",command=add_task)
add_task.grid(row=1,column=0)

delete_all=tk.Button(root, text="Delete All",fg="green",bg="white",command=delete_all)
delete_all.grid(row=2,column=0)

Delete_one=tk.Button(root, text="Delete",fg="green",bg="white",command=delete_one)
Delete_one.grid(row=3,column=0)

sort_asc=tk.Button(root, text="Sort(ASC)",fg="green",bg="white",command=sort_asc)
sort_asc.grid(row=4,column=0)

sort_desc=tk.Button(root, text="Sort(DESC)",fg="green",bg="white",command=sort_desc)
sort_desc.grid(row=5,column=0)

Choose_random=tk.Button(root, text="Choose Random",fg="green",bg="white",command=Choose_random)
Choose_random.grid(row=6,column=0)

Number_Of_Task=tk.Button(root, text="Number Of Tasks",fg="green",bg="white",command=Number_Of_Task)
Number_Of_Task.grid(row=7,column=0)

Exit=tk.Button(root, text="Exit",fg="green",bg="white",command=exit)
Exit.grid(row=8,column=0)


lb_tasks=tk.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)

root.mainloop()
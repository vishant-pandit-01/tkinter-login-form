from tkinter import *
root=Tk()
root.geometry("300x200")
root.title("my first page")
root.config(background="pink")
def show_data():
    a=lab1_entry.get()
    b=lab2_entry.get()
    
    label.config(text=f" Username:-{a}\nPassword:-{b}")

lab1=Label(root,text="username",bg="pink",bd=1,relief="raised")
lab1.grid(row=1,column=0,padx=10,pady=10)
lab1_entry=Entry(root,bg="pink")
lab1_entry.grid(row=1,column=1,padx=10,pady=10)

lab2=Label(root,text="password",bg="pink",bd=1,relief="raised")
lab2.grid(row=2,column=0,padx=10,pady=10)
lab2_entry=Entry(root,bg="pink")
lab2_entry.grid(row=2,column=1,padx=10,pady=10)

btn=Button(root,text="press",bg="red",foreground="black",command=show_data)
btn.grid(row=3,column=1)

label=Label(root,text="",background="pink",foreground="black")
label.grid(row=4,column=1)

root.mainloop()

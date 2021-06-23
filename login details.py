from tkinter import *
from PIL import ImageTk #pip install pillow
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)


        #background image
        self.bg=ImageTk.PhotoImage(file="logo3.png")#file name jpg file acceptable
        self.bg.image=Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #login frame
        Frame_login =Frame(self.root,bg = "white")
        Frame_login.place(x=330,y=150 , width=500,height=400)

        #title & subtitle
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="black",bg="white").place(x=90,y=30)
        subtitle = Label(Frame_login, text="Member Login Area", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90,y=100)
        #Username
        lbl_title =Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90,y=140)
        self.username = Entry(Frame_login,  font=("Goudy old style", 15), fg="gray")
        self.username.place(x=90, y=170)

        # password
        lbl_password =Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), fg="gray")
        self.password.place(x=90, y=240,width=320,height=35)

        #button
        forget=Button(Frame_login, text="Forget Password ?",bd=0,cursor="hand2", font=("Goudy old style", 12), fg="gray", bg="white").place(x=90, y=280)
        #submib button
        submit =Button(Frame_login,command=self.check_function,cursor="hand2", text="Login", bd=1,font = ("Goudy old style", 15), fg = "gray", bg = "white").place(x=90, y=320,width=180,height=40)

    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent= self.root)
        elif self.username.get()!="akshay9555" or self.password.get()!="akshay9555":
            messagebox.showerror("Error", "Invalid username or password", parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"welcome {self.username.get()}")


root = Tk()
obj = Login(root)
root.mainloop()

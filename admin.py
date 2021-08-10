from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox 
from main import *

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin login")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        self.bg=ImageTk.PhotoImage(file="C:\\Users\\bipan\\Desktop\\Awfr\\img\\uni.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=130,height=380,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Admin Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        self.txt_user.get()

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)
        self.txt_pass.get()
 
        login_btn=Button(Frame_login,text="Login",bg="#d77337",fg="white",font=("times new roman",15),command=self.login_admin).place(x=150,y=290,width=200,height=40)

    def login_admin(self):
        if self.txt_user.get()=="admin" and self.txt_pass.get()=="admin123":
            self.new_window=Toplevel(self.root)
            self.app=face_recognition_system(self.new_window)

        elif self.txt_user.get()=="" and self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            messagebox.showerror("Error","Invalid Username or Password",parent=self.root) 

if __name__=="__main__":
    root = Tk()
    obj = login(root)
    root.mainloop()



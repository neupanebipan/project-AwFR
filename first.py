from tkinter import *
from PIL import Image, ImageTk
from admin import *
from user import *



class Window1:
    def __init__(self, root):
        self.root = root
        self.root.title("AwFR")
        self.root.geometry("1199x600+100+50")

        Label(root, text="ATTENDANCE  SYSTEM  WITH  FACE  RECOGNITION", font="FORTE 20 bold", bd=1,
              bg="azure2").pack (padx=30, pady=20)


        img4 = Image.open("img/user.jpg")
        img4 = img4.resize((210, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(image=self.photoimg4,cursor="hand2",command=self.user_page)
        b1.place(x=350,y=150,width=210,height=210)
        b1_1=Button(text="User",cursor="hand2",font=("times new roman",14,"bold"),bg="azure2",fg="black",command=self.user_page)
        b1_1=b1_1.place(x=350,y=350,width=210,height=40)


        img5 = Image.open("img/admin.jpg")
        img5 = img5.resize((210, 210), Image.ANTIALIAS)
        self.photoimg5= ImageTk.PhotoImage(img5)

        b1=Button(image=self.photoimg5,cursor="hand2",command=self.login_admin)
        b1.place(x=700,y=150,width=210,height=210)
        b1_1=Button(text="Admin",cursor="hand2",font=("times new roman",14,"bold"),bg="azure2",fg="black",command=self.login_admin)
        b1_1=b1_1.place(x=700,y=350,width=210,height=40)


    def login_admin(self):
        self.new_window=Toplevel(self.root)
        self.app=login(self.new_window)

    def user_page(self):
        self.new_window=Toplevel(self.root)
        self.app=user(self.new_window)




if __name__=="__main__":
    root = Tk()
    obj = Window1(root)
    root.mainloop()
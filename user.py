from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import messagebox


class user:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x800+0+0")
        self.root.title("face recogniton system ")

# -----------------------------------------------------------------------------------------------
        img=Image.open("img/k1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
# ------------------------------------------------------------------------------------------------
        img1 = Image.open("img/a.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
# ------------------------------------------------------------------------------------------------
        img2 = Image.open("img/ku.jpeg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)
# ------------------------------------------------------------------------------------------------
        img3 = Image.open("img/bg2.jpg")
        img3 = img3.resize((1400, 800), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, bg="azure2")
        bg_img.place(x=0, y=130, width=1400, height=800)
# -----------------------------------------------------------------------------------------------
        title=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",20,"bold"),bg="white",fg="#234512")
        title.place(x=0,y=0,width=1400,height=40)


# ----------------------Detector Button------------------------------------------------------------------------------

        img5 = Image.open("img/face_detector1.jpg")
        img5 = img5.resize((210, 210), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, command=self.face_data,image=self.photoimg5, cursor="hand2")
        b2.place(x=250, y=250, width=210, height=210)
        b2_2 = Button(bg_img,command=self.face_data ,text="face recognize", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b2_2 = b2_2.place(x=250, y=450, width=210, height=40)

# ----------------------Attendance Face Button------------------------------------------------------------------------------

        img6 = Image.open("img/at.png")
        img6 = img6.resize((210, 210), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6,command=self.attendance, cursor="hand2")
        b3.place(x=550, y=250, width=210, height=210)
        b3_3 = Button(bg_img, text="Attendance",command=self.attendance, cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b3_3 = b3_3.place(x=550, y=450, width=210, height=40)

# ----------------------help face Button------------------------------------------------------------------------------

        img7 = Image.open("img/help.jpg")
        img7 = img7.resize((210, 210), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=850, y=250, width=210, height=210)
        b4_4 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b4_4 = b4_4.place(x=850, y=450, width=210, height=40)


     











    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendance(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)








if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
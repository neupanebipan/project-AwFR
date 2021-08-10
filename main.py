from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import messagebox


class face_recognition_system:
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

# -----------------studentsButton--------------------------------------------------------------------
        img4 = Image.open("img/ii.jpg")
        img4 = img4.resize((210, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=210,height=210)
        b1_1=Button(bg_img,text="studentDetails",command=self.student_details,cursor="hand2",font=("times new roman",14,"bold"),bg="azure2",fg="black")
        b1_1=b1_1.place(x=150,y=300,width=210,height=40)

# ----------------------Detector Button------------------------------------------------------------------------------

        img5 = Image.open("img/face_detector1.jpg")
        img5 = img5.resize((210, 210), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, command=self.face_data,image=self.photoimg5, cursor="hand2")
        b2.place(x=450, y=100, width=210, height=210)
        b2_2 = Button(bg_img,command=self.face_data ,text="face recognize", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b2_2 = b2_2.place(x=450, y=300, width=210, height=40)

# ----------------------Attendance Face Button------------------------------------------------------------------------------

        img6 = Image.open("img/at.png")
        img6 = img6.resize((210, 210), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6,command=self.attendance, cursor="hand2")
        b3.place(x=750, y=100, width=210, height=210)
        b3_3 = Button(bg_img, text="Attendance",command=self.attendance, cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b3_3 = b3_3.place(x=750, y=300, width=210, height=40)

# ----------------------help face Button------------------------------------------------------------------------------

        img7 = Image.open("img/help.jpg")
        img7 = img7.resize((210, 210), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1050, y=100, width=210, height=210)
        b4_4 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b4_4 = b4_4.place(x=1050, y=300, width=210, height=40)

# ----------------------Train face Button------------------------------------------------------------------------------

        img8 = Image.open("img/datatrain.png")
        img8 = img8.resize((210, 210), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, command=self.train_data,image=self.photoimg8, cursor="hand2")
        b5.place(x=150, y=360, width=210, height=210)
        b5_5 = Button(bg_img,command=self.train_data ,text="Train Data", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b5_5 = b5_5.place(x=150, y=560, width=210, height=40)

# -------------------------Photos--------------------------------------------------------------------------------
        img9 = Image.open("img/photos.jpg")
        img9 = img9.resize((210, 210), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_image)
        b6.place(x=450, y=360, width=210, height=210)
        b6_6 = Button(bg_img,command=self.open_image ,text="photos", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b6_6 = b6_6.place(x=450, y=560, width=210, height=40)

# ----------------------------------Developer---------------------------------------------------------------------

        img10 = Image.open("img/dev.jpg")
        img10 = img10.resize((210, 210), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=750, y=360, width=210, height=210)
        b7_7 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b7_7 = b7_7.place(x=750, y=560, width=210, height=40)

# ------------------------------------Exit-------------------------------------------------------------

        img11 = Image.open("img/exit.jpg")
        img11 = img11.resize((210, 210), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img,command=self.Exit, image=self.photoimg11, cursor="hand2")
        b8.place(x=1050, y=360, width=210, height=210)
        b8_8 = Button(bg_img, text="Exit",command=self.Exit, cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="azure2", fg="black")
        b8_8 = b8_8.place(x=1050, y=560, width=210, height=40)



    def open_image(self):
        os.startfile("data")



    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)



    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendance(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

    def Exit(self):
        self.iExit=messagebox.askyesno("if You Want To Exit ")
        if self.iExit>0:
            self.root.destroy()

        else:
            return






if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
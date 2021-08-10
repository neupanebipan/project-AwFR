from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x800+0+0")
        self.root.title("face recogniton system ")

        title = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 20, "bold"),
                  bg="#6e89cc", fg="#070beb")
        title.place(x=0, y=0, width=1400, height=52)

        img_top = Image.open("img/ttt.jpg")
        img_top = img_top.resize((1400, 357), Image.ANTIALIAS)
        self.phototop = ImageTk.PhotoImage(img_top)
        top_img = Label(self.root, image=self.phototop)
        top_img.place(x=0, y=48, width=1400, height=357)



        img_bottom = Image.open("img/tt1.jpg")
        img_bottom = img_bottom.resize((1400, 325), Image.ANTIALIAS)
        self.photobottom = ImageTk.PhotoImage(img_bottom)
        bottom_img = Label(self.root, image=self.photobottom)
        bottom_img.place(x=0, y=440, width=1400, height=325)


        b1_1=Button(self.root,command=self.train_classifier,text="Train Data",cursor="hand2",font=("times new roman",30,"bold"),bg="#948491",fg="white")
        b1_1=b1_1.place(x=0,y=380,width=1400,height=60)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert("L")
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("training",imageNP)
            cv2.waitKey(1)==13

        ids=np.array(ids)


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set Completed!!!")







if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
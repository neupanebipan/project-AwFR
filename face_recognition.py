from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import cv2
from datetime import datetime



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x800+0+0")
        self.root.title("face recogniton system ")

        title = Label(self.root, text="FACE ROCOGNITION", font=("times new roman", 20, "bold"),
                  bg="#6e89cc", fg="#070beb")
        title.place(x=0, y=0, width=1400, height=52)

        img_top = Image.open("img/f2.jpg")
        img_top = img_top.resize((620, 700), Image.ANTIALIAS)
        self.phototop = ImageTk.PhotoImage(img_top)
        top_img = Label(self.root, image=self.phototop)
        top_img.place(x=0, y=55, width=620, height=700)

        img_bottom = Image.open("img/f1.png")
        img_bottom = img_bottom.resize((950, 700), Image.ANTIALIAS)
        self.photobottom = ImageTk.PhotoImage(img_bottom)
        bottom_img = Label(self.root, image=self.photobottom)
        bottom_img.place(x=620, y=55, width=950, height=700)

        b1_1=Button(bottom_img,command=self.face_recog,text="Face Recognition",cursor="hand2",font=("times new roman",17,"bold"),bg="#e3c710",fg="#940f96")
        b1_1=b1_1.place(x=350,y=550,width=200,height=40)

    def mark_attendance(self,r,n):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if(r not in name_list ) and (n not in name_list ) :
                now=datetime.now()
                dstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{r},{dstring}")





    def face_recog(self):
            def draw_boundry(img,classifier,scalefactor,minneighbours,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scalefactor,minneighbours)
                coord=[]
                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    conn = mysql.connector.connect(host="localhost", user="root", password="",
                                                   database="face")
                    my_curser = conn.cursor()
                    my_curser.execute("select student_name from students where student_id="+str(id))
                    n=my_curser.fetchone()
                    n="+".join(n)

                    my_curser = conn.cursor()
                    my_curser.execute("select roll_no from students where student_id="+str(id))
                    r=my_curser.fetchone()
                    r="+".join(r)




                    if confidence>85:

                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendance(r,n)

                    else:
                        cv2.rectangle(img,(x, y), (x + w, y + h), (0, 255, 0), 3)
                        cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,h]
                return coord

            def recognize(img,clf,faceCascade):
                coord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                return img
            face_Cascade=cv2.CascadeClassifier("C:\\Users\\bipan\\Desktop\\Awfr\\haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("C:\\Users\\bipan\\Desktop\\Awfr\\classifier.xml")

            video_cap=cv2.VideoCapture("C:\\Users\\bipan\\Desktop\\Awfr\\VIDEOS\\finals.mp4")
            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,face_Cascade)
                cv2.imshow("Welcome to Face Recognizition",img)
                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()




if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
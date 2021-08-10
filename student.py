from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x800+0+0")
        self.root.title("face recogniton system ")

#------------------variables----------------------------------------------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_SID=StringVar()
        self.var_student_name=StringVar()
        self.var_class_division=StringVar()
        self.var_rollno=StringVar()
        self.var_photo=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()





# -----------------------------------------------------------------------------------------------
        img=Image.open("img/real.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
# ------------------------------------------------------------------------------------------------
        img1 = Image.open("img/real.png")
        img1 = img1.resize((450, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=450, height=130)
# ------------------------------------------------------------------------------------------------
        img2 = Image.open("img/real.png")
        img2 = img2.resize((450, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=950, y=0, width=450, height=130)
# ------------------------------------------------------------------------------------------------

        img3 = Image.open("img/real.png")
        img3 = img3.resize((1400, 800), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1400, height=800)
# -----------------------------------------------------------------------------------------------
        title = Label(bg_img, text="studentsMANAGEMENT SYSTEM", font=("times new roman", 20, "bold"),
                  bg="azure2", fg="black")
        title.place(x=0, y=0, width=1400, height=40)
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=0,width=1400,height=800)

        left_frame=LabelFrame(main_frame,bd=3,bg="azure",relief=RIDGE,text="REGISTRATION", font=("times new roman", 20, "bold"), fg="black")
        left_frame.place(x=10,y=10,width=690,height=600)


        img_left = Image.open("img/white.jpg")
        img_left = img_left.resize((690, 130), Image.ANTIALIAS)
        self.photoleft = ImageTk.PhotoImage(img_left)
        left_img = Label(left_frame, image=self.photoleft)
        left_img.place(x=5, y=0, width=690, height=130)


        level_frame = LabelFrame(left_frame, bd=3, bg="azure2", relief=RIDGE, text="Course Information", width=14,
                        font=("times new roman", 15, "bold"), fg="black")
        level_frame.place(x=5, y=135, width=670, height=160)

        dept_label=Label(level_frame,text="Department", font=("times new roman", 13, "bold"), fg="black",width=14)
        dept_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(level_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"]=("Select Department","CS & CE","CIVIl & ARCHITECT","MECHANICAL","ENVIRONMENTAL","MATHEMATICS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        course_label=Label(level_frame,text="Course", font=("times new roman", 13, "bold"), fg="black")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(level_frame,textvariable=self.var_course,  font=("times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"]=("Select course","COMP.SCIENCE","COMP.ENGINEERING","CIVIL.ENGINEERING","MECHANICAL.ENGINEERING","ENVIRONMENT.SCIENCE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)



        yr_label=Label(level_frame,text="Year", font=("times new roman", 13, "bold"), fg="black")
        yr_label.grid(row=1,column=0,padx=10,sticky=W)

        yr_combo=ttk.Combobox(level_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly", width=14)
        yr_combo["values"]=("select-year","1st","2nd","3rd","4th")
        yr_combo.current(0)
        yr_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        sem_label=Label(level_frame,text="Semester", font=("times new roman", 13, "bold"), fg="black")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(level_frame , textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="readonly", width=14)
        sem_combo["values"]=("select semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        class_frame = LabelFrame(left_frame, bd=3, bg="azure2", relief=RIDGE, text="Students Information", width=14,
                        font=("times new roman", 15, "bold"), fg="black")
        class_frame.place(x=5, y=295, width=670, height=250)

        sID_label = Label(class_frame, text="Student_Id", font=("times new roman", 13, "bold"), fg="black")
        sID_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)
        sID_entry=ttk.Entry(class_frame,textvariable=self.var_SID,width=20,font=("times new roman", 13, "bold"))
        sID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        sname_label = Label(class_frame, text="studentsName", font=("times new roman", 13, "bold"), fg="black")
        sname_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)
        sname_entry=ttk.Entry(class_frame,textvariable=self.var_student_name,width=20,font=("times new roman", 13, "bold"))
        sname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        division_label = Label(class_frame, text="Class Division", font=("times new roman", 13, "bold"), fg="black")
        division_label.grid(row=1, column=0, padx=10, pady=5,sticky=W)
       # division_entry=ttk.Entry(class_frame,textvariable=self.var_class_division,width=20,font=("times new roman", 13, "bold"))
       # division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        division_combo=ttk.Combobox(class_frame , textvariable=self.var_class_division, font=("times new roman", 12, "bold"), state="readonly", width=14)
        division_combo["values"]=("A","B","c")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        roll_label = Label(class_frame, text="Roll No:", font=("times new roman", 13, "bold"),fg="black")
        roll_label.grid(row=1, column=2, pady=5,padx=10, sticky=W)
        roll_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_rollno,font=("times new roman", 13, "bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        radio_button1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Take sample photo",value="yes")
        radio_button1.grid(row=2,column=0)

        radio_button2 = ttk.Radiobutton(class_frame,variable=self.var_radio2, text="No sample photo", value="No")
        radio_button2.grid(row=2, column=2)

        btn_frame=Frame(class_frame,bd=3,relief=RIDGE,bg="azure2")
        btn_frame.place(x=0,y=100,width=669,height=60)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman", 13, "bold"),bg="azure2",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame ,command=self.update_data,text="Update",width=16,font=("times new roman", 13, "bold"),bg="azure2",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=16,font=("times new roman", 13, "bold"),bg="azure2",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset,text="Reset",width=16,font=("times new roman", 13, "bold"),bg="azure2",fg="black")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_frame,bd=3,relief=RIDGE,bg="azure2")
        btn_frame1.place(x=0,y=160,width=660,height=30)

        take_photo_sample=Button(btn_frame1,command=self.generate_dataset,width=34,text="Take Photo Sample",font=("times new roman", 13, "bold"),bg="azure2",fg="black")
        take_photo_sample.grid(row=0,column=0)

        update_photo_sample=Button(btn_frame1,width=34,text="Update Photo Sample",font=("times new roman", 13, "bold"),bg="azure2",fg="black")
        update_photo_sample.grid(row=0,column=1)

        right_frame = LabelFrame(main_frame, bd=3, bg="azure2", relief=RIDGE, text="STUDENT DETAILS",
                             font=("times new roman", 20, "bold"), fg="black")
        right_frame.place(x=690, y=10, width=670, height=600)

        img_right = Image.open("img/white.jpg")
        img_right = img_right.resize((690, 130), Image.ANTIALIAS)
        self.photoright = ImageTk.PhotoImage(img_right)
        img_right = Label(right_frame, image=self.photoright)
        img_right.place(x=5, y=0, width=670, height=130)


        Search_frame = LabelFrame(right_frame, bd=3, bg="azure2", relief=RIDGE, text="Search System", width=12,
                        font=("times new roman", 15, "bold"), fg="black")
        Search_frame.place(x=5, y=140, width=670, height=100)


        search_label = Label(Search_frame, text="Search By", font=("times new roman", 13, "bold"), fg="black")
        search_label.grid(row=0, column=0,padx=10,pady=5, sticky=W)
        search_combo=ttk.Combobox(Search_frame ,  font=("times new roman", 10, "bold"), state="readonly", width=14)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        delete_btn=Button(Search_frame,text="Search",width=13,font=("times new roman", 11, "bold"),bg="azure2",fg="black")
        delete_btn.grid(row=0,column=2)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman", 11, "bold"))
        search_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        Show_btn=Button(Search_frame,text="Show All",width=13,font=("times new roman", 11, "bold"),bg="azure2",fg="black")
        Show_btn.grid(row=0,column=4)

        table_frame = LabelFrame(right_frame, bd=3, bg="azure2", relief=RIDGE, text="Registered Students", width=12,
                        font=("times new roman", 15, "bold"), fg="black")
        table_frame.place(x=5, y=230, width=660, height=345)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("SID","dep","course","year","sem","student_name","class_division","Rollno","radio1"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("SID",text="SID")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Sem")
        self.student_table.heading("student_name",text="Student_Name")
        self.student_table.heading("class_division",text="Class_Division")
        self.student_table.heading("Rollno",text="Roll_no")
        self.student_table.heading("radio1",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("SID",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("student_name",width=100)
        self.student_table.column("class_division",width=100)
        self.student_table.column("Rollno",width=100)
        self.student_table.column("radio1",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_curser)
        self.fetch_data()

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_SID.get()=="" :
             messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                up=messagebox.askyesno("Do You Want To Update",parent=self.root)
                if up>0:
                        conn = mysql.connector.connect(host="localhost", user="root", password="",
                                                                                           database="face")
                        my_curser = conn.cursor()
                        my_curser.execute("update students set dep=%s,course=%s,year=%s,sem=%s,student_name=%s,class_division=%s,roll_no=%s,photo_sample=%s where student_id=%s",(
                                                      self.var_dep.get(),
                                                      self.var_course.get(),
                                                      self.var_year.get(),
                                                      self.var_sem.get(),
                                                      self.var_student_name.get(),
                                                      self.var_class_division.get(),
                                                      self.var_rollno.get(),
                                                      self.var_radio1.get(),
                                                      self.var_SID.get()



                                                                                                        ))

                else:
                    if not up:
                      return
                messagebox.showinfo("Success","student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()


            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)



    def delete_data(self):
        if self.var_SID.get()=="":
            messagebox.showerror("Error","student ID must be required",parent=self.root)

        else:
            try:
                delete=messagebox.askyesno("Do You Want to Delete",parent=self.root)
                if delete>0:
                  conn = mysql.connector.connect(host="localhost", user="root", password="",
                                           database="face")
                  my_curser = conn.cursor()
                  sql="delete from students where student_id=%s"
                  val=(self.var_SID.get(),)
                  my_curser.execute(sql,val)
                else:
                    if not  delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted students details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)





    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_SID.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
             try:
                  conn=mysql.connector.connect(host="localhost",user="root",password="",database="face")
                  my_curser=conn.cursor()
                  my_curser.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                               self.var_SID.get(),
                                                               self.var_dep.get(),
                                                               self.var_course.get(),
                                                               self.var_year.get(),
                                                               self.var_sem.get(),
                                                               self.var_student_name.get(),
                                                               self.var_class_division.get(),
                                                               self.var_rollno.get(),
                                                               self.var_radio1.get(),
                                                               
                                                                                  ))

                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("Success","students details has been added successfully",parent=self.root)

             except Exception as es :
                 messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    def fetch_data(self):
       conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
       my_curser = conn.cursor()
       my_curser.execute("select * from students")
       data=my_curser.fetchall()

       if len(data)!=0:
           self.student_table.delete(*self.student_table.get_children())
           for i in data:
               self.student_table.insert("",END,values=i)
           conn.commit()
       conn.close()


    def get_curser(self,event=""):
        curser_focus=self.student_table.focus()
        content=self.student_table.item(curser_focus)
        data=content["values"]

        self.var_SID.set(data[0])
        self.var_dep.set(data[1])
        self.var_course.set(data[2])
        self.var_year.set(data[3])
        self.var_sem.set(data[4])
        self.var_student_name.set(data[5])
        self.var_class_division.set(data[6])
        self.var_rollno.set(data[7])
        self.var_radio1.set(data[8])

    def reset(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select course")
        self.var_year.set("Select year")
        self.var_sem.set("Select semester ")
        self.var_student_name.set("")
        self.var_class_division.set("B")
        self.var_rollno.set("")
        self.var_SID.set("")
        self.var_radio1.set("")


    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_SID.get()=="" :
             messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:

               conn = mysql.connector.connect(host="localhost", user="root", password="",
                                                               database="face")
               my_curser = conn.cursor()
               my_curser.execute("select * from students")
               myresult=my_curser.fetchall()
               id=0
               for x in myresult:
                   id+=1
               my_curser.execute(
                "update students set dep=%s,course=%s,year=%s,sem=%s,student_name=%s,class_division=%s,roll_no=%s,photo_sample=%s where student_id=%s",
                 (
                       self.var_dep.get(),
                      self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_student_name.get(),
                    self.var_class_division.get(),
                    self.var_rollno.get(),
                    self.var_radio1.get(),
                    self.var_SID.get()

                 ))

               conn.commit()
               self.fetch_data()
               self.reset()
               conn.close()

               face_classifier=cv2.CascadeClassifier("C:\\Users\\bipan\\Desktop\\Awfr\\haarcascade_frontalface_default.xml")

               def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces=face_classifier.detectMultiScale(gray,1.3,5)
                   for (x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped

               cap=cv2.VideoCapture('C:\\Users\\bipan\\Desktop\\Awfr\\VIDEOS\\bishal.mp4')
               img_id=0
               while True:
                   ret,my_frame=cap.read()
                   if face_cropped(my_frame) is not None:
                       img_id+=1
                       face=cv2.resize(face_cropped(my_frame),(450,450))
                       face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                       file_name_path="C:\\Users\\bipan\\Desktop\\Awfr\\data\\user."+str(id)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name_path,face)
                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       if cv2.waitKey(1)==13 or int(img_id)==50:
                           break
               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Result","Generating dataset completed ")

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


















if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
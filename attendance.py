from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x800+0+0")
        self.root.title("face recogniton system ")

        self.var_atten_name=StringVar()
        self.var_atten_roll=StringVar()
        self.var_time=StringVar()




        # -----------------------------------------------------------------------------------------------
        img = Image.open("img/aaa.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # ------------------------------------------------------------------------------------------------
        img1 = Image.open("img/sssr.jpg")
        img1 = img1.resize((900, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=450, height=130)
        # ------------------------------------------------------------------------------------------------
        img2 = Image.open("img/iii.jpg")
        img2 = img2.resize((900, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=450, height=130)
    # ------------------------------------------------------------------------------------------------

        img3 = Image.open("img/bg2.jpg")
        img3 = img3.resize((1400, 800), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, bg="#db88e3")
        bg_img.place(x=0, y=130, width=1400, height=800)
# -----------------------------------------------------------------------------------------------
        title=Label(bg_img,text="STUDENT ATTENDANCE SYSTEM ",font=("times new roman",20,"bold"),bg="white",fg="#234512")
        title.place(x=0,y=0,width=1400,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1400,height=800)


        left_frame=LabelFrame(main_frame,bd=3,bg="#d4cbb4",relief=RIDGE,text="Student Attendance", font=("times new roman", 15, "bold"), fg="darkgreen")
        left_frame.place(x=10,y=10,width=690,height=570)

        img_left = Image.open("img/Sanskrit-lessons.jpg")
        img_left = img_left.resize((690, 130), Image.ANTIALIAS)
        self.photoleft = ImageTk.PhotoImage(img_left)
        left_img = Label(left_frame, image=self.photoleft)
        left_img.place(x=5, y=0, width=690, height=130)

        class_frame = LabelFrame(left_frame, bd=3, bg="#d4cbb4", relief=RIDGE, text="class student info", width=14,
                        font=("times new roman", 20, "bold"), fg="darkgreen")
        class_frame.place(x=5, y=150, width=670, height=250)

        sID_label = Label(class_frame, text="Name:", font=("times new roman", 13, "bold"), fg="darkgreen")
        sID_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)
        sID_entry=ttk.Entry(class_frame,textvariable=self.var_atten_name,width=20,font=("times new roman", 13, "bold"))
        sID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        sname_label = Label(class_frame, text="Roll No:", font=("times new roman", 13, "bold"), fg="darkgreen")
        sname_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)
        sname_entry=ttk.Entry(class_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman", 13, "bold"))
        sname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        roll_label = Label(class_frame, text="Time:", font=("times new roman", 13, "bold"),fg="darkgreen")
        roll_label.grid(row=1, column=0, pady=5,padx=10, sticky=W)
        roll_entry=ttk.Entry(class_frame,textvariable=self.var_time,width=20,font=("times new roman", 13, "bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)




        btn_frame=Frame(class_frame,bd=3,relief=RIDGE)
        btn_frame.place(x=0,y=150,width=677,height=50)

        save_btn=Button(btn_frame,command=self.ImportCsv,text="Import",width=16,font=("times new roman", 13, "bold"),bg="#383945",fg="#d5d7f2")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame ,text="Export",command=self.exportcsv,width=16,font=("times new roman", 13, "bold"),bg="#383945",fg="#d5d7f2")
        update_btn.grid(row=0,column=3)








        right_frame = LabelFrame(main_frame, bd=3, bg="#bdcfa9", relief=RIDGE, text="student Details",
                             font=("times new roman", 15, "bold"), fg="darkgreen")
        right_frame.place(x=690, y=10, width=670, height=600)

        img_right = Image.open("img/Data.jpg")
        img_right = img_right.resize((690, 130), Image.ANTIALIAS)
        self.photoright = ImageTk.PhotoImage(img_right)
        img_right = Label(right_frame, image=self.photoright)
        img_right.place(x=5, y=0, width=670, height=130)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("name","roll","time"),xscrollcommand=scroll_x,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)



        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("time",text="Time")



        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_curser)

        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("time",width=50)



    def fetchData(self,rows):
          self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
          for i in rows:
              self.AttendanceReportTable.insert("",END,values=i)

    def ImportCsv(self):
            global mydata
            mydata.clear()
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="OPEN CSV",
                                               filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)

            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)


    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data ","No data Found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                               filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)

            with open(fln, mode='w',newline="") as myfile:
              exp_write = csv.writer(myfile, delimiter=",")
              for i in mydata:
                exp_write.writerow(i)
              messagebox.showinfo("Data Export","Your Data exported to "+os.path.basename(fln)+"successfully")



        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def get_curser(self,event=""):
       curser_row=self.AttendanceReportTable.focus()
       content=self.AttendanceReportTable.item(curser_row)
       rows=content['values']
       self.var_atten_name.set(rows[0])
       self.var_atten_roll.set(rows[1])
       self.var_time.set(rows[2])


    def reset_data(self):
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_time.set("")














if __name__ == "__main__":
            root = Tk()
            obj = Attendance(root)
            root.mainloop()
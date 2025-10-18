from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
import sqlite3
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management Systme")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
       
       
       #===icons=====
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        #===title=====
        title=Label(self.root,text="Student Result Management Systme",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        # #====Menu=====#
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)


        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Students",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1120,y=5,width=200,height=40)


        
        #=====content_window====
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,height=350)
        
        
        #====update_details====
        self.lbl_course=Label( self.root,text="Total Courses\n[ 0 ]",font=("goudy oid style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label( self.root,text="Total Student\n[ 0 ]",font=("goudy oid style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label( self.root,text="Total Result\n[ 0 ]",font=("goudy oid style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        

        # ===== Clock Label =====
        self.lbl = Label(self.root,text="\nWebCode Clock",font=("Book Antique",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10, y=180, height=450, width=350)
        # Start clock
        self.working()
    
        #===footer====#
        footer=Label(self.root,text="SRMS-Student Result Management Systme\ncontact Us for any Technical Issue: 7970945863",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
        #======================================================
    
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[ {len(cr)} ]")
            

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[ {len(cr)} ]")


            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[ {len(cr)} ]")
            
           
           
            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")        
    
    
    def working(self):
        now = datetime.now()
        h, m, s = now.hour, now.minute, now.second

        hr = (h % 12 + m / 60) * 30
        min_ = (m + s / 60) * 6
        sec_ = s * 6

        clock_img = self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(clock_img)
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)


    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        # Background clock face image
        try:
            bg = Image.open("images/c.png")
            bg = bg.resize((300, 300), Image.Resampling.LANCZOS)
            clock.paste(bg, (50, 50))
        except:
            pass  

        cx, cy = 200, 200

        # Hour hand
        hx = cx + 50 * sin(radians(hr))
        hy = cy - 50 * cos(radians(hr))
        draw.line((cx, cy, hx, hy), fill="#DF005E", width=4)

        # Minute hand
        mx = cx + 80 * sin(radians(min_))
        my = cy - 80 * cos(radians(min_))
        draw.line((cx, cy, mx, my), fill="white", width=3)

        # Second hand
        sx = cx + 100 * sin(radians(sec_))
        sy = cy - 100 * cos(radians(sec_))
        draw.line((cx, cy, sx, sy), fill="yellow", width=2)

        # Center circle
        draw.ellipse((195, 195, 205, 205), fill="#1AD5D5")

        return clock   


    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)    
    
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)  
    

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
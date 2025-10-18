from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
import sqlite3
import os
from tkinter import messagebox

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        


        # ===== Background Labels =====
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # ===== Login Frame =====
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2")
        title.place(x=250, y=50)

        email_label = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white", fg="gray")
        email_label.place(x=250, y=150)
        self.text_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.text_email.place(x=250, y=180, width=350, height=35)

        pass_label = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="gray")
        pass_label.place(x=250, y=250)
        self.text_pass_ = Entry(login_frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.text_pass_.place(x=250, y=280, width=380, height=35)

        btn_reg= Button(login_frame, cursor="hand2",command=self.register_window, text="Register new Account?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857")
        btn_reg.place(x=250, y=320)

        btn_forget= Button(login_frame, cursor="hand2",command=self.forget_password_window, text="Forget Password?", font=("times new roman", 14), bg="white", bd=0, fg="red")
        btn_forget.place(x=450, y=320)

        
        btn_login = Button(login_frame, text="Login",command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2")
        btn_login.place(x=250, y=380, width=180, height=40)

        # ===== Clock Label =====
        self.lbl = Label(self.root,text="\nWebCode Clock",font=("Book Antique",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        

        

        # Start clock
        self.working()
    
    def reset(self):
        self.cmb_quest.current(0)
        self.text_new_pass.delete(0,END)
        self.text_answer.delete(0,END)
        self.text_pass_.delete(0,END)
        self.text_email.delete(0,END)
    
    
    def forget_password(self):
        if self.text_email.get()=="Select" or self.text_answer.get()=="" or self.text_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.text_email.get(),self.cmb_quest.get(),self.text_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.text_new_pass.get(),self.text_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()
            except  Exception as es:
               messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
              



    def forget_password_window(self):
        if self.text_email.get()=="":
            
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.text_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root) 
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
        
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                    #====================Forget Password==========
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
       
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    self.text_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.text_answer.place(x=50,y=210,width=250)
        
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.text_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.text_new_pass.place(x=50,y=290,width=250)

                    btn_change_Password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
               
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
            
            
        
            
         
    
    def register_window(self):
        self.root.destroy()
        import register   
    

    def login(self):
        if self.text_email.get()==""or self.text_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.text_email.get(),self.text_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalild USERNAME & PASSWORD",parent=self.root) 
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.text_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python display.py")
                con.close()    
            except Exception as es:
                    messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
    
    
        
   
   
   
   
   
   
   
   
    # ===== Clock Image Function =====
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

    # ===== Update Clock =====
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


# ===== Run App =====
root = Tk()
obj = Login_window(root)
root.mainloop()

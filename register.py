from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
from turtle import update, width
import os
import mysql.connector
import Tracker





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register Form")
        self.root.geometry('1200x900+0+0')
        self.root.state('zoomed')
        root.resizable(False,False)
        self.root.wm_iconbitmap("icn.ico")
        # root.resizable(False,False)
        
        self.var_fname = StringVar()
        self.var_uname = StringVar()
        self.var_pass = StringVar()
        self.var_repass = StringVar()
        self.var_type = StringVar()

        root.title('login Page')
        root.geometry('1300x900+0+0')
        root.configure(bg="#fff")

        img=Image.open(r"bg\\l22.png")
        img=img.resize((500,500),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        # img = PhotoImage(file="bg/l22.png")
        Label(root,image=self.photoimg,bg='white').place(x=80,y=90)

        frame = Frame(root,width=500,height=500,bg='white')
        frame.place(x=700,y=80)

        heading = Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Arial',18,'bold'))
        heading.place(x=200,y=50)
        
        dep_combo = ttk.Combobox(frame,textvariable=self.var_type,font=("Times new roman",12,"bold"),width= 15)
        dep_combo["values"]=("Select Department","Admin","Stock","Master_Creation","qr_code","Transport","Delevery","Orders","Return")
        dep_combo.current(0)
        dep_combo.place(x=170,y=100)

        # user Name ----------------------------------------------

        def on_enter(e):
            fname.delete(0,'end')
                    
        def on_leave(e):
            name=fname.get()
            if name=='':
                fname.insert(0,'Enter Your Name')

        fname = Entry(frame,width= 35,textvariable=self.var_fname,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
        fname.place(x=80,y=140)
        fname.insert(0,'Enter Your Name')
        fname.bind('<FocusIn>',on_enter)
        fname.bind('<FocusOut>',on_leave)
        Frame(frame,width=315,height=2,bg='#57a1f8').place(x=80,y=165)

        def on_enter(e):
            user.delete(0,'end')
                    
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')

        user = Entry(frame,width= 35,textvariable=self.var_uname,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
        user.place(x=80,y=200)
        user.insert(0,'Username')
        user.bind('<FocusIn>',on_enter)
        user.bind('<FocusOut>',on_leave)
        Frame(frame,width=315,height=2,bg='#57a1f8').place(x=80,y=225)




                # Passwaord----------------------------------------------------

        def on_enter(e):
            pwd1.delete(0,'end')
                    
        def on_leave(e):
            name=pwd1.get()
            if name=='':
                pwd1.insert(0,'Password')
        
        global pwd1                  
        pwd1 = Entry(frame,width= 35,show="*",textvariable=self.var_pass,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
        pwd1.place(x=80,y=260)
        pwd1.insert(0,'Password')
        pwd1.bind('<FocusIn>',on_enter)
        pwd1.bind('<FocusOut>',on_leave)
        Frame(frame,width=315,height=2,bg='#57a1f8').place(x=80,y=285)
        check_button = Checkbutton(frame,text='show password',command=self.show_pass).place(x=300,y=260)
    
        def on_enter(e):
            repwd.delete(0,'end')
                    
        def on_leave(e):
            name=repwd.get()
            if name=='':
                repwd.insert(0,'Confirm Password')
            
            
        global repwd            
        repwd = Entry(frame,width= 35,show="*",fg='black',textvariable=self.var_repass,border=0,bg='white',font=('Microsoft YaHei UI Light',13))
        repwd.place(x=80,y=320)
        repwd.insert(0,'Confirm Password')
        repwd.bind('<FocusIn>',on_enter)
        repwd.bind('<FocusOut>',on_leave)
        Frame(frame,width=315,height=2,bg='#57a1f8').place(x=80,y=345)

        check_button = Checkbutton(frame,text='show password',command=self.show_repass).place(x=300,y=320)


        # Button-------------------------------------------------
        Button(frame,width=30,pady=7,text='Sign Up',command=self.sign_up,bg="#57a1f8",fg='white',border=0).place(x=125,y=380)
        # label=Label(frame,text="Do You Have Already Account?",fg='black',bg='white',font=('Arial',8))
        # label.place(x=120,y=440)


        # sign_in =Button(frame,width=8,text='Sign In',command=self.login,border=0,bg='white',cursor='hand2',fg='#57a1f8')
        # sign_in.place(x=290,y=440)

    def show_pass(self):
        if pwd1.cget('show') == '*':
            pwd1.config(show='')
                
        else:
            pwd1.config(show='*')
            
    def show_repass(self):
        if repwd.cget('show') == '*':
            repwd.config(show='')
                
        else:
            repwd.config(show='*')
    
    def sign_up(self):
        if self.var_fname.get() == "Enter Your Name" or self.var_type.get() == "Select Department" or self.var_uname.get() == "Username" or self.var_pass.get() == "Password" or self.var_repass.get() == "Confirm Password":
            messagebox.showerror("Error","All Fields are Required",parent = self.root)
            
              
        # elif self.var_fname.get() <= "A" or self.var_fname.get() >= "Z" and self.var_fname.get() <= "a" or self.var_fname.get() >= "z":
        #     messagebox.showinfo('Correct'," Valid User Name")  
            
        elif self.var_pass.get() != self.var_repass.get():
            messagebox.showerror("Error","Password and Confirm Password Must Be Same",parent = self.root)
            
            
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute('''INSERT INTO login(f_name,id,pwd,type) values(%s,%s,%s,%s)''',(self.var_fname.get(),
                                                                                                                self.var_uname.get(),
                                                                                                                self.var_pass.get(),
                                                                                                                self.var_type.get()
                                                                                                                
                                                                                                            ))
                    
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Sucess","Registered Successfully",parent = self.root)
                self.var_fname.set("Enter Your Name")
                self.var_uname.set("Username")
                self.var_pass.set("Password")
                self.var_pass.set("Select Department")
                self.var_repass.set("Confirm Password") 
                
            except Exception as ex:
                messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)

    # def login(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app = login1.Login(self.new_window)  
    #     # root.destroy()
  
if __name__ == "__main__":
    root=Tk()
    boj=Register(root)
    root.mainloop()

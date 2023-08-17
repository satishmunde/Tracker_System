from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
from turtle import update, width
import main
# from mysql.connector.locales.eng import client_error
import mysql
from forgetpass import Forget
import qrgenp
import stock
import delevery
import trasport
import master_creation
import returns
from order import Order



class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry('1325x900+0+0')
        self.root.state('zoomed')
        self.root.wm_iconbitmap("icn.ico")
        root.resizable(False,False)
        
        self.var_Uname = StringVar()
        self.var_pass = StringVar()
        self.var_type = StringVar()
        self.stage = StringVar()
        self.id = StringVar()
        
         #=======Bg Image===============
        root.title('login Page')
        root.geometry('1325x650+0+0')
        root.configure(bg="#fff")

        img3=Image.open(r"bg\\l22.png")
        img3=img3.resize((500,500),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        # img = PhotoImage(file="bg/l22.png")
        Label(root,image=self.photoimg3,bg='white').place(x=80,y=90)

        frame = Frame(root,width=500,height=460,bg="white")
        frame.place(x=650,y=80)

        heading = Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=('Arial',18,'bold'))
        heading.place(x=200,y=80)

        # user Name ----------------------------------------------

        def on_enter(e):
            user.delete(0,'end')
            
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')

      
        dep_combo = ttk.Combobox(frame,textvariable=self.var_type,font=("Times new roman",12,"bold"),width= 15)
        dep_combo["values"]=("Select Department","Admin","Stock","Master_Creation","Orders","qr_code","Transport","Delevery","Return")
        dep_combo.current(0)
        dep_combo.place(x=170,y=130)
        
   
        
        user = Entry(frame,width= 35,textvariable=self.var_Uname,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
        user.place(x=80,y=170)
        user.insert(0,'Username')
        user.bind('<FocusIn>',on_enter)
        user.bind('<FocusOut>',on_leave)

        Frame(frame,width=315,height=2,bg='#57a1f8').place(x=80,y=195)


        # Passwaord----------------------------------------------------

        def on_enter(e):
            pwd.delete(0,'end')
            
        def on_leave(e):
            name=pwd.get()
            if name=='':
                pwd.insert(0,'Password')
                
        global pwd     
        pwd = Entry(frame,width= 35,show="*",textvariable=self.var_pass,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
        pwd.place(x=80,y=230)
        pwd.insert(0,'Password')
        pwd.bind('<FocusIn>',on_enter)
        pwd.bind('<FocusOut>',on_leave)

        Frame(frame,width=315,height=2,bg='#57a1f8').place(x=80,y=255)

        
            
        # Button-------------------------------------------------
        
        check_button = Checkbutton(frame,text='show password',command=self.show_pass).place(x=300,y=260)

        

        Button(frame,width=30,pady=7,text='Sign In',command=self.search_stage,bg="#57a1f8",fg='white',border=0).place(x=125,y=300)
        
        
        Button(frame,text="Forget Password?", command= self.forget,font=("Arial",8),bg="#57a1f8",fg="black",width=20).place(x=250,y=350)
        
        
        # label=Label(frame,text="Don't have an Account?",fg='black',bg='white',font=('Arial',8))
        # label.place(x=135,y=370)


        # sign_up =Button(frame,width=8,text='Sign Up',command=self.register1,border=0,bg='white',cursor='hand2',fg='#57a1f8')
        # sign_up.place(x=260,y=370)
        
    def login_function(self):
        if self.var_Uname.get()=="Username" or self.var_pass.get()=="Password":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_Uname.get()!="Username" or self.var_pass.get()!="Password":
            conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
            my_cursor = conn.cursor()
            lid = self.var_Uname.get()
            pwd = self.var_pass.get()
            
            my_cursor.execute("select id,pwd from login where  id= %s and pwd = %s and type = %s ",[(lid),(pwd),(self.id)])
            result = my_cursor.fetchall()
            global re1
            re1 = result
            
            if result:
                # messagebox.showinfo("Sucess","Sucessfully Logined In")
                
                Update = messagebox.askyesno( "Sucess","Do you want to Enter in Page",parent=self.root)
                
                if Update == 1:
                    if self.id == "Admin":
                        Login.main(self)
                        self.var_Uname.set("Username")
                        self.var_pass.set("Password")

                    elif self.id == "Stock":
                        Login.estock(self)
                        self.var_Uname.set("Username")
                        self.var_pass.set("Password")

                    elif self.id == "Orders":
                        Login.orders(self)
                        self.var_Uname.set("Username")
                        self.var_pass.set("Password")
                    
                    elif self.id == "qr_code":
                        Login.qrcode1(self)
                        self.var_Uname.set("Username")
                        self.var_pass.set("Password")
                        
                    elif self.id == "Transport":
                        Login.transport(self)
                        self.var_Uname.set("Username")
                        self.var_pass.set("Password")
                        
                    elif self.id == "Delevery":
                        Login.delevery(self)
                        self.var_Uname.set("Username")
                        self.var_pass.set("Password")
                        
                    elif self.id == "Master_Creation":
                        Login.master(self)
                        self.var_Uname.set("Username")
                        self.var_pass.set("Password")
                        
                    elif self.id == "Return":
                        Login.returns(self)
                        self.var_Uname.set("Username")
                        self.var_pass.set("Password")
                        
                        
                conn.close()  
            
            else:
                messagebox.showerror("Error","Incorrect User_Name Or Password")
        
    def search_stage(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        self.id = self.var_type.get() 
        my_cursor = conn.cursor()    
        my_cursor.execute("select * from login where type = %s",[(self.id)])
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            Login.login_function(self)
        
        conn.commit()
        conn.close()    

    def show_pass(self):
        if pwd.cget('show') == '*':
            pwd.config(show='')
                
        else:
            pwd.config(show='*')
    
    def main(self):
        self.new_window=Toplevel(self.root)
        self.app = main.Admin(self.new_window)  
        
    def forget(self):
        self.new_window=Toplevel(self.root)
        self.app = Forget(self.new_window)
    
    def qrcode1(self):
        self.new_window=Toplevel(self.root)
        self.app =qrgenp.Genpr(self.new_window)
     
    def estock(self):
        self.new_window=Toplevel(self.root)
        self.app =stock.Stock(self.new_window)
        
    def orders(self):
        self.new_window=Toplevel(self.root)
        self.app =Order(self.new_window)
    
    def transport(self):
        self.new_window=Toplevel(self.root)
        self.app =trasport.Transport(self.new_window)

    def delevery(self):
        self.new_window=Toplevel(self.root)
        self.app =delevery.Delever(self.new_window)
    
    
    def master(self):
        self.new_window=Toplevel(self.root)
        self.app =master_creation.Master(self.new_window)
        
    def returns(self):
        self.new_window=Toplevel(self.root)
        self.app =returns.Return(self.new_window)
        
if __name__ == "__main__":
    root=Tk()
    boj=Login(root)
    root.mainloop()

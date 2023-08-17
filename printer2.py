from tkinter import *
import win32api

from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
from datetime import datetime

class Printer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x900+300+50")
        self.root.title("Printing")
        root.resizable(False,False)
        root.configure(bg="PeachPuff")
        self.root.wm_iconbitmap("icn.ico")
        self.root.state('zoomed')
        
        self.id = StringVar()
        self.data = StringVar()
        
        
       
        
        gen_id = ttk.Entry(self.root,width=20,textvariable=self.id,font=("Times new roman",10,"bold"))
        gen_id.place(x=60,y=120,width=280,height=40)
        
        b1_2=Button(self.root,text="Check",cursor="hand2",command=self.checker,font=("Times New Roman",13,"bold"),bg="PaleVioletRed",fg="Black") 
        b1_2.place(x=120,y=185,width=150,height=40)

        Button(root, text="Print QR Code ",bg="PaleVioletRed",font=("Times New Roman",13,"bold"),command=self.print).place(x=80,y=570,width=200,height=50)

            
        # table Frame---------------------------------
            
        table_frame = LabelFrame(self.root,bd=4,relief=RIDGE,bg="DeepSkyBlue")
        table_frame.place(x=350,y=70,width=920,height=620)
            
            
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
            
        self.status_table=ttk.Treeview(table_frame,column=("QR_Code_ID","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
            
        scroll_y.config(command=self.status_table.xview)
        scroll_x.config(command=self.status_table.yview)
            
        self.status_table.heading("QR_Code_ID",text="QR_Code_Id")
        self.status_table.heading("Date",text="Date")
        self.status_table.heading("Status",text="Status")
        
        self.status_table["show"]="headings"
            
        
            
        self.status_table.column("QR_Code_ID",width=100)
        self.status_table.column("Date",width=100)
        self.status_table.column("Status",width=100)
            
        self.status_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute(''' select * from qr_code_details where Status = "Printed"''')
        data=my_cursor.fetchall()
            
        if len(data)!=0:
            self.status_table.delete(*self.status_table.get_children())
            for i in data:
                self.status_table.insert("",END,values=i)
            conn.commit
            
    def checker(self):
        
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
            my_cursor = conn.cursor() 
            my_cursor.execute('''select qr_code_id from qr_code_details where Status="Generated" limit 1''')
            self.data=my_cursor.fetchone()
                            
            str1 = ''
            i=0
            
            for item in self.data:
                str1 = item
                    
                
                self.data = str1
            Printer.id_show(self)
           
            img3=Image.open(fr"QRCode\\{self.data}.png")
            img3=img3.resize((300,300),Image.LANCZOS)
            self.photoimg3=ImageTk.PhotoImage(img3)
            bg_img=Label(self.root,image=self.photoimg3)
            bg_img.place(x=40,y=250,width=300,height=300)
            # Printer.status(self)
            
    
        except Exception as ex:
            conn.rollback()
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)
            
    def print(self):       
        try:
            img = f"QRCode\\{self.data}.png"
            if img:
        
                # Print Hard Copy of File
                win32api.ShellExecute(0,              # NULL since it's not associated with a window
                    "print",        # execute the "print" verb defined for the file type
                    img,  # path to the document file to print
                    None,           #no parameters, since the target is a document file
                    ".",            #current directory, same as NULL here
                    0)              # SW_HIDE passed to app associated with the file type                   
            
        except Exception as ex:
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)
            
        try: 
            conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
            my_cursor = conn.cursor()
            now = datetime.now()
            tString = now.strftime('%H:%M:%S')
            dString = now.strftime('%d:%m:%y')
                    
        
                  
            my_cursor.execute("update qr_code_details set Date =%s, Date = %s,Status = %s where QR_Code_ID =%s",((dString),(tString),("Printed"),(self.data)))                      
                                        
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess","QR Code Updated Successfully",parent = self.root)
            Printer.fetch_data(self)
        except Exception as ex:
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)
    
    def id_show(self):
        self.id.set(self.data)    
  
if __name__ == "__main__":
    root=Tk()
    obj=Printer(root)
    root.mainloop()

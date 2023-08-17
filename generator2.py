from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import update, width
from PIL import Image,ImageTk
from PIL import ImageFont
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
from datetime import datetime
import mysql.connector

class Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("850x600+200+50")
        self.root.title("Generator")
        root.resizable(False,False)
        root.configure(bg="Crimson")
        self.root.state('zoomed') 
        self.root.wm_iconbitmap("icn.ico")

    
        self.id = StringVar()
        self.data = StringVar()
        
        
        
        id_lbl=Label(self.root,text="Generate Barcode Id",font=("Times New Roman",15),bg="light skyblue",fg="Black")
        id_lbl.place(x=50,y=70,width=200,height=25)
        
        gen_id = ttk.Entry(self.root,width=20,textvariable=self.id,font=("Times new roman",10,"bold"))
        gen_id.place(x=50,y=115,width=200,height=30)
        
    
        b1_1=Button(self.root,text="QR Code Generator",cursor="hand2",command=self.generate,font=("Times New Roman",13,"bold"),bg="DarkOrange",fg="Black") 
        b1_1.place(x=50,y=230,width=200,height=30)

        b1_2=Button(self.root,text="Check",cursor="hand2",command=self.checker,font=("Times New Roman",13,"bold"),bg="DarkSalmon",fg="Black") 
        b1_2.place(x=60,y=170,width=165,height=30)

        
        # table Frame---------------------------------
            
        table_frame = LabelFrame(self.root,bd=4,relief=RIDGE,bg="yellow")
        table_frame.place(x=300,y=40,width=950,height=650)
            
            
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
    
    def checker(self):
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
            my_cursor = conn.cursor() 
            my_cursor.execute('''select qr_code_id from qr_code_details ORDER BY QR_Code_ID DESC limit 1''')
            self.data=my_cursor.fetchone()
                            
            str1 = ''
            for item in self.data:
                str1 = item
                
            str1+=1
            self.data = str1
            Generator.id_show(self)
            
            
                            
        except Exception as ex:
            conn.rollback()
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)
    
    def generate(self):
        qr=qrcode.QRCode(
        version = 15,
        box_size = 10,
        border=5
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        img=qr.make_image(fill="black" ,back_color = "white")
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
            my_cursor = conn.cursor()
            now = datetime.now()
            dString = now.strftime('%d:%m:%y')
            str2  = "Generated"
                  
            my_cursor.execute('''INSERT INTO qr_code_details (QR_Code_ID,Date,Status) VALUES (%s,%s,%s)''',((self.data),(dString),(str2)))  
                                       
            conn.commit()
            conn.close()
                # messagebox.showinfo("Sucess","Details had  Been Updated Successfully",parent = self.root)
        except Exception as ex:
            conn.rollback()
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)

        img.save(f"QRCode\\{self.data}.png")
        messagebox.showinfo("Success",f"ID of QR Code is {self.data} Generated Successfully",parent=self.root)
        self.fetch_data()
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute('''select * from qr_code_details where Status = "Generated"''')
        data=my_cursor.fetchall()
            
        if len(data)!=0:
            self.status_table.delete(*self.status_table.get_children())
            for i in data:
                self.status_table.insert("",END,values=i)
            conn.commit
       
    def id_show(self):
        self.id.set(self.data)

if __name__ == "__main__":
    root = Tk()
    obj = Generator(root)
    root.mainloop()
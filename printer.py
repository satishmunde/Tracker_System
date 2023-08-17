from tkinter import *
from docxtpl import DocxTemplate,InlineImage
import glob
from docx.shared import Inches
from tkinter import *
from tkinter.messagebox import showerror
import os
from tkinter import messagebox

from tkinter import ttk
import mysql.connector
from datetime import datetime

class Printer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x900+300+50")
        self.root.title("Printing")
        self.root.resizable(False,False)
        self.root.configure(bg="MediumOrchid")
        self.root.wm_iconbitmap("icn.ico")
        self.root.state('zoomed')
        

        self.id = StringVar()
        self.data = StringVar()
        
        
        
                    
        
        
        gen_id = ttk.Entry(self.root,width=20,textvariable=self.id,font=("Times new roman",10,"bold"))
        gen_id.place(x=60,y=120,width=280,height=40)
        
        b1_2=Button(self.root,text="Check",cursor="hand2",command=self.checker,font=("Times New Roman",13,"bold"),bg="DarkOrchid",fg="Black") 
        b1_2.place(x=120,y=185,width=150,height=40)

        
        Button(root, text="Print QR Code ",bg="MediumPurple",command=self.print).place(x=80,y=570,width=200,height=50)

            
        # table Frame---------------------------------
            
        table_frame = LabelFrame(self.root,bd=4,relief=RIDGE,bg="yellow")
        table_frame.place(x=400,y=70,width=800,height=600)
            
            
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
            
        except Exception as ex:
            conn.rollback()
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)
           
    def print(self):
                   
        doc = DocxTemplate("demo.docx")
        


        qr_id = []
        for k in glob.glob(f"QRCode/{self.data}.png"):
            img = InlineImage(doc,k,width=Inches(3),height=Inches(3))
            qr_id.append(img)


        doc.render({
                    "id":self.data,
                    "images":qr_id
                    })
        doc.save(f"demo\\{self.data}.docx")
        file = f".\\demo\\{self.data}.docx"

        if os.path.exists(file):
            try:
                os.startfile(file, "print")
                    
            except Exception as e:
                showerror('Error',message='printing Error',detail=e)
        else:
            showerror('Printing Error',message='Please Select a file to print.')
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
            my_cursor = conn.cursor()
            now = datetime.now()
           
            dString = now.strftime('%d:%m:%y')
                    
                  
            my_cursor.execute("update qr_code_details set Date =%s ,Status = %s where QR_Code_ID =%s",((dString),("Printed"),(self.data)))                      
                                        
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess","Details had  Been Updated Successfully",parent = self.root)
            self.fetch_data()
        except Exception as ex:
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)
            conn.rollback()
        
 
    
    def id_show(self):
        self.id.set(self.data)    
  
if __name__ == "__main__":
    root=Tk()
    obj=Printer(root)
    root.mainloop()

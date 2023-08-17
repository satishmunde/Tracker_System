from tkinter import*
from PIL import Image,ImageTk
from turtle import update, width
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
from tkinter import messagebox,ttk
from datetime import datetime
import mysql.connector

# C:\Users\munde\AppData\Local\Programs\Tracker System\


class Delever:
    def __init__(self,root):
        self.root=root
        self.root.title("Home Page")
        self.root.geometry('1530x790')
        self.root.state('zoomed')
        self.root.wm_iconbitmap("icn.ico")
        
    
        # root.resizable(False,False)
        img3=Image.open(r"img\\bg.jpg")
        img3=img3.resize((1530,810),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1300,height=750)
 
 
        
        title_lbl1=Label(self.root,text="Global Gesses India PVT. LTD.",font=("Franklin Gothic Heavy",28),fg="Navy")
        title_lbl1.place(x=0,y=50,width=1300,height=45)
 
        b1_2=Button(bg_img,text="Entry to Delever",cursor="hand2",command=self.delevery,font=("Times New Roman",16,"bold"),bg="LightGreen",fg="Black") 
        b1_2.place(x=85,y=150,width=220,height=40)
        
        self.search = StringVar()
        self.stage = StringVar()
        
        search_frame = LabelFrame(bg_img,bd=2,text="Search System",relief=RIDGE,bg="aqua")
        search_frame.place(x=450,y=100,width=780,height=575)
            
        search_label = Label(search_frame,text="Search By :",font=("Times new roman",13,"bold"),width=10,bg="SpringGreen",fg="Purple")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
            
            
        search_combo = Label(search_frame,text="QR Code ID",font=("Times new roman",12,"bold"),width= 10)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
 
        
        global info_entry
            
        info_entry = ttk.Entry(search_frame,width=20,textvariable=self.search,font=("Times new roman",10,"bold"))
        info_entry.grid(row=0,column=2,padx=10,pady=1,sticky=W)
            
            
        search_btn = Button(search_frame,text="Search",width=10,command=self.search_data,font=("Times new roman",8,"bold"),bg="PowderBlue",fg="Purple")
        search_btn.grid(row=0,column=3,padx=10)
        
        showAll_btn = Button(search_frame,text="Show All",width=10,command=self.fetch_data,font=("Times new roman",8,"bold"),bg="PowderBlue",fg="Purple")
        showAll_btn.grid(row=0,column=5,padx=10)
            
            
        # table Frame---------------------------------
            
        table_frame = LabelFrame(search_frame,bd=4,relief=RIDGE,bg="yellow")
        table_frame.place(x=2,y=50,width=775,height=500)
            
            
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
            
        self.status_table=ttk.Treeview(table_frame,column=("Tank_Id","Date","Time","Status"),xscrollcommand=scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
            
        scroll_y.config(command=self.status_table.xview)
        scroll_x.config(command=self.status_table.yview)
            
        self.status_table.heading("Tank_Id",text="QR_Code_Id")
        self.status_table.heading("Date",text="Date")
        self.status_table.heading("Time",text="Time")
        self.status_table.heading("Status",text="Status")
        
        self.status_table["show"]="headings"
            
        
            
        self.status_table.column("Tank_Id",width=100)
        self.status_table.column("Date",width=100)
        self.status_table.column("Time",width=100)
        self.status_table.column("Status",width=100)
            
        self.status_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
    
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        id = self.search.get()
        
        my_cursor = conn.cursor()    
        my_cursor.execute("select * from tank_details where QR_Code_ID = %s",[(id)])
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.status_table.delete(*self.status_table.get_children())
            for row in rows:
                self.status_table.insert('',END,values= row)    
                
            conn.commit()
        conn.close()
        
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Tank_Details where status= 'Delevered'")
        data=my_cursor.fetchall()
            
        if len(data)!=0:
            self.status_table.delete(*self.status_table.get_children())
            for i in data:
                self.status_table.insert("",END,values=i)
            conn.commit
    
        
        

    def delevery(self):
        def decoder(image):
            gray_img = cv2.cvtColor(image,0)
            barcode = decode(gray_img)
            
            for obj in barcode:
                points = obj.polygon
                (x,y,w,h) = obj.rect
                pts = np.array(points, np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(image, [pts], True, (0, 255, 0), 3)

                barcodeData = obj.data.decode("utf-8")
                barcodeType = obj.type
               
              
                
              
                result = messagebox.askokcancel("Success",f"Barcode: {barcodeData}",parent=self.root)
                if result >0:
                    try:
                        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
                        my_cursor = conn.cursor()
                        now = datetime.now()
                        tString = now.strftime('%H:%M:%S')
                        dString = now.strftime('%d:%m:%y')
                    
                        data = barcodeData
                  
                        my_cursor.execute("update tank_details set Date =%s, Time = %s,Status = %s where QR_Code_ID =%s",((dString),(tString),("Delevered"),(data)))                      
                                        
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Sucess","Tank Has Been Delevered Successfully",parent = self.root)
                    except Exception as ex:
                        messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)

              
                    
                    
        cap = cv2.VideoCapture(1)

        while True:
            ret, frame = cap.read()
            decoder(frame)
            cv2.imshow('Image', frame)
            code = cv2.waitKey(10)
            if code == 13:
                break


    

if __name__ == "__main__":
    root=Tk()
    obj=Delever(root)
    root.mainloop()

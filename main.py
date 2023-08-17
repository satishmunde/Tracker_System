from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter import Frame
from PIL import Image,ImageTk
import mysql.connector
import register
from master_creation import Master



class Admin:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("ONGC Admin")
        self.root.state('zoomed')
        root.resizable(False,False)
        self.root.wm_iconbitmap("icn.ico")
       
    # Main Page
       
        self.search = StringVar()
        self.stage = StringVar()
     
        img3=Image.open(r"img\\bg.jpg")
        img3=img3.resize((1530,790),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1300,height=750)

        title_lbl=Label(bg_img,text="Global Gasses India PVT.LTD.",font=("Bahnschrift SemiBold Condensed",25),bg="Lavender",fg="Black")
        title_lbl.place(x=0,y=15,width=1300,height=50)

    
    #Status
       
        b1_1=Button(bg_img,text="Status",cursor="hand2",command=self.status,font=("Agency FB",15,"bold"),bg="SpringGreen",fg="Black") 
        b1_1.place(x=30,y=15,width=150,height=50)
        
        b1_4=Button(bg_img,text="Master Database",cursor="hand2",command=self.master,font=("Agency FB",13,"bold"),bg="SpringGreen",fg="Black") 
        b1_4.place(x=210,y=15,width=150,height=50)

        b1_2=Button(bg_img,text="Register",cursor="hand2",command=self.register1,font=("Agency FB",15,"bold"),bg="SpringGreen",fg="Black") 
        b1_2.place(x=950,y=15,width=150,height=50)
        
    #Exit

        b1_3=Button(bg_img,text="logout",cursor="hand2",command=self.Exit,font=("Agency FB",15,"bold"),bg="SpringGreen",fg="Black") 
        b1_3.place(x=1120,y=15,width=150,height=50)
             
    def status(self):

        Right_frame=LabelFrame(self.root,text="Status",bd=10,relief=RIDGE,bg='MediumTurquoise',fg="yellow")
        Right_frame.place(x=60,y=80,width=1150,height=600) 
                
        search_frame = LabelFrame(Right_frame,bd=2,text="Search System",relief=RIDGE,bg="aqua")
        search_frame.place(x=2,y=0,width=975,height=570)
            
        search_label = Label(search_frame,text="Search By :",font=("Times new roman",13,"bold"),width=10,bg="SpringGreen",fg="Purple")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
            
            
        search_combo = Label(search_frame,text="QR Code ID",font=("Times new roman",12,"bold"),width= 10)
        
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
 
        
        global info_entry
            
        info_entry = ttk.Entry(search_frame,width=20,textvariable=self.search,font=("Times new roman",10,"bold"))
        info_entry.grid(row=0,column=2,padx=10,pady=1,sticky=W)
            
            
        search_btn = Button(search_frame,text="Search",width=10,command=self.search_data,font=("Times new roman",8,"bold"),bg="PowderBlue",fg="Purple")
        search_btn.grid(row=0,column=3,padx=10)
            
        
            
            
            
            
            
            
        #   ==================================================================================================================================== 
        search_label1 = Label(Right_frame,text="Search By :",font=("Times new roman",13,"bold"),width=10,bg="SpringGreen",fg="Purple")
        search_label1.place(x=1000,y=80,width=100,height=40) 
            
            
        search_combo1 = ttk.Combobox(Right_frame,textvariable=self.stage,font=("Times new roman",10,"bold"),width= 10)
        search_combo1["values"]=("Select Status","Stock","In Transist","Delevered")
        search_combo1.current(0)
        search_combo1.place(x=1000,y=150,width=100,height=30) 
        
        show_btn = Button(Right_frame,text="Show",width=10,command=self.search_stage,font=("Times new roman",8,"bold"),bg="PowderBlue",fg="Purple")
        show_btn.place(x=1000,y=200,width=100,height=30) 
            
            
        showAll_btn = Button(Right_frame,text="Show All",width=10,command=self.fetch_data,font=("Times new roman",8,"bold"),bg="PowderBlue",fg="Purple")
        showAll_btn.place(x=1000,y=520,width=100,height=30) 
            
            
        # table Frame---------------------------------
            
        table_frame = LabelFrame(Right_frame,bd=4,relief=RIDGE,bg="yellow")
        table_frame.place(x=2,y=70,width=975,height=500)
            
            
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
            
        self.status_table=ttk.Treeview(table_frame,column=("Tank_Id","Order_ID","Customer_Name","Number","Date","Gas Type","Status"),xscrollcommand=scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
            
        scroll_y.config(command=self.status_table.xview)
        scroll_x.config(command=self.status_table.yview)
            
        self.status_table.heading("Tank_Id",text="QR_Code_Id")
        self.status_table.heading("Order_ID",text="Order_ID")
        self.status_table.heading("Customer_Name",text="Customer_Name")
        self.status_table.heading("Number",text="Number")
        self.status_table.heading("Date",text="Date")
        self.status_table.heading("Gas Type",text="Gas Type")
        self.status_table.heading("Status",text="Status")
        
        
        self.status_table["show"]="headings"
            
        
            
        self.status_table.column("Tank_Id",width=80)
        self.status_table.column("Order_ID",width=80)
        self.status_table.column("Customer_Name",width=80)
        self.status_table.column("Number",width=80)
        self.status_table.column("Date",width=80)
        self.status_table.column("Gas Type",width=80)
        self.status_table.column("Status",width=80)
                
        self.status_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
    
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        id = self.search.get()
        
        my_cursor = conn.cursor()    
        my_cursor.execute("select tank_details.QR_Code_ID, orders.Order_id, orders.Customer_Name, orders.Number, orders.date, orders.type ,tank_details.Status from tank_details left JOIN orders ON tank_details.QR_Code_ID = orders.Tank_id and tank_details.Status !='Stock' where QR_Code_ID = %s",[(id)])
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.status_table.delete(*self.status_table.get_children())
            for row in rows:
                self.status_table.insert('',END,values= row)    
                
            conn.commit()
        conn.close()
        
    def search_stage(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        id = self.stage.get()
        
        my_cursor = conn.cursor()    
        my_cursor.execute("select tank_details.QR_Code_ID, orders.Order_id, orders.Customer_Name, orders.Number, orders.date, orders.type ,tank_details.Status from tank_details left JOIN orders ON tank_details.QR_Code_ID = orders.Tank_id and tank_details.Status !='Stock' where Status = %s",[(id)])
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
        my_cursor.execute('''SELECT tank_details.QR_Code_ID, orders.Order_id, orders.Customer_Name, orders.Number, orders.date, orders.type ,tank_details.Status
                                            FROM tank_details
                                            LEFT JOIN orders ON tank_details.QR_Code_ID = orders.Tank_id and tank_details.Status !='Stock'
                                            ORDER BY orders.Tank_id;
                                            ''')
        
        data=my_cursor.fetchall()
            
        if len(data)!=0:
            self.status_table.delete(*self.status_table.get_children())
            for i in data:
                self.status_table.insert("",END,values=i)
            conn.commit
            
    def Exit(self):
        iExit=messagebox.askyesno("ONGC Admin ","Are You want to Exit",parent=self.root) 
        if iExit >0:
            self.root.destroy()
        else:
            return
    
    def register1(self):
        self.new_window=Toplevel(self.root)
        self.app = register.Register(self.new_window)
    
    def master(self):
        self.new_window=Toplevel(self.root)
        self.app = Master(self.new_window)
    
               
if __name__ == "__main__":
    root=Tk()
    obj=Admin(root)
    root.mainloop()

from PIL import Image,ImageTk
from tkinter import messagebox,ttk
from turtle import update, width
import os
from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from turtle import update, width
from tkinter.font import BOLD
from mysql.connector.locales.eng import client_error
import mysql.connector
from datetime import datetime


class Master:
    def __init__(self,root):
        self.root=root
        self.root.title("Master Creation Database")
        self.root.geometry('1530x790')
        self.root.state('zoomed')
        self.root.wm_iconbitmap("icn.ico")
        
        self.var_phone = StringVar()
        self.var_name = StringVar()
        self.var_date = StringVar()
        self.var_quantity = StringVar()
        self.var_search = StringVar()
        
        img3=Image.open(r"img\\bg.jpg")
        img3=img3.resize((1530,790),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1300,height=750)
        
        title_lbl = Label(self.root,text ="Vender Data Entry",font = ("Franklin Gothic Heavy",30,"bold"),bg = "Coral",fg = "black")
        title_lbl.place(x=0,y=20,width=1300,height=45)

        
    # -------------- Left Label Frame ----------------
        Left_frame=LabelFrame(self.root,text="Vender Details",fg = "DarkRed",bd=10,relief=RIDGE,bg='lightblue')
        Left_frame.place(x=5,y=100,width=570,height=500) 
        
        
    # Current cource------------------
        # current_cource_frame=LabelFrame(self.root,text="Current Cource",bd=6,relief=RIDGE,bg='aqua')
        # current_cource_frame.place(x=20,y=120,width=535,height=120) 
        
    # Department----------------------
        
        # dep_label = Label(current_cource_frame,text = "Department",font=("Times new roman",12,"bold"))
        # dep_label.grid(row=0,column= 0,padx=10)
        
        # dep_combo = ttk.Combobox(current_cource_frame,font=("Times new roman",12,"bold"),width= 15)
        # dep_combo["values"]=("Select Department","BCS","BCA","Bio Tech","Bio Info","Msc CS","Msc BT")
        # dep_combo.current(0)
        # dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
   
        
    # vender Information -----------------------------------
        
        vender_frame=LabelFrame(self.root,text="Vender Info",bd=0,relief=RIDGE,bg='HotPink')
        vender_frame.place(x=20,y=160,width=540,height=420)
        
    # Vender --------------------------------
        
        Vender_label = Label(vender_frame,text = "Name",font=("Times new roman",12,"bold"))
        Vender_label.grid(row=0,column= 0,padx=8,sticky=W)
        
        Vender_entry = ttk.Entry(vender_frame,textvariable=self.var_name,width=20,font=("Times new roman",12,"bold"))
        Vender_entry.grid(row=0,column=1,padx=5,sticky=W)
        
        
    # vender Name ----------------------------
        
        date_label = Label(vender_frame,text = "Date",font=("Times new roman",12,"bold"))
        date_label.grid(row=0,column= 2,padx=8,pady = 8,sticky=W)
   
        now = datetime.now()
       
        date = now.strftime('%d/%m/%y')
        self.var_date.set(date)
        
        
        date_entry = ttk.Entry(vender_frame,textvariable=self.var_date,width=20,font=("Times new roman",12,"bold"))
        date_entry.grid(row=0,column=3,padx=8,pady = 8,sticky=W)
 
    # Class Division ------------------------------------
        
        phone_label = Label(vender_frame,text = "Phone No",font=("Times new roman",12,"bold"))
        phone_label.grid(row=1,column= 0,padx=8,pady = 8,sticky=W)
        
        phone_entry = ttk.Entry(vender_frame,textvariable=self.var_phone,width=20,font=("Times new roman",12,"bold"))
        phone_entry.grid(row=1,column=1,padx=8,pady=5,sticky=W)
        
        qua_label = Label(vender_frame,text = "Quantity",font=("Times new roman",12,"bold"))
        qua_label.grid(row=1,column= 2,padx=8,pady = 8,sticky=W)
        
        qua_entry = ttk.Entry(vender_frame,textvariable=self.var_quantity,width=20,font=("Times new roman",12,"bold"))
        qua_entry.grid(row=1,column=3,padx=8,pady=5,sticky=W)

    
    # Buttons ----------------------------------------------
        
        # btn_frame = Frame(vender_frame,bd=2,relief=RIDGE,bg="white")
        # btn_frame.place(x=5,y=206,width=500,height=70)
        
        save_btn = Button(vender_frame,text="Save",command=self.add_data,bd=3,width=25,font=("Times new roman",15,"bold"),bg="Turquoise",fg="black")
        # save_btn.grid(row=0,,column=0,padx=2)
        save_btn.place(x=60,y=200,width=150,height=40)
        
        
        update_btn = Button(vender_frame,text="Update",command=self.update_data,width=25,font=("Times new roman",15,"bold"),bg="Turquoise",fg="black")
        # update_btn.grid(row=1,column=0,padx=2)
        update_btn.place(x=300,y=200,width=150,height=40)
        
        delete_btn = Button(vender_frame,text="Delete",command=self.delete_data,width=25,font=("Times new roman",15,"bold"),bg="Turquoise",fg="black")
        # delete_btn.grid(row=0,column=1,padx=2)
        delete_btn.place(x=60,y=250,width=150,height=40)
        
        reset_btn = Button(vender_frame,text="Reset",command=self.reset_data,width=25,font=("Times new roman",15,"bold"),bg="Turquoise",fg="black")
        # reset_btn.grid(row=1,column=1,padx=2)
        reset_btn.place(x=300,y=250,width=150,height=40)
        
    
        
        
        # -------------- Right Label Frame ----------------
        
        Right_frame=LabelFrame(self.root,text="Database",bd=10,relief=RIDGE,bg='grey',fg="DarkRed")
        Right_frame.place(x=600,y=100,width=650,height=500) 
        
    # # Search  System----------------------------------
        
        search_frame = LabelFrame(Right_frame,bd=2,text="Search System",relief=RIDGE,bg="BurlyWood")
        search_frame.place(x=2,y=0,width=615,height=80)
        
        search_label = Label(search_frame,text="Search By :",font=("Times new roman",13,"bold"),width=10,bg="Cyan",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        
        search_combo = Label(search_frame,text="Vender Name",font=("Times new roman",13,"bold"),width=10,bg="Cyan",fg="black")
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        global info_entry
        
        info_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("Times new roman",10,"bold"))
        info_entry.grid(row=0,column=2,padx=10,pady=1,sticky=W)
        
        
        search_btn = Button(search_frame,text="Search",command=self.search_data,width=10,font=("Times new roman",8,"bold"),bg="Khaki",fg="black")
        search_btn.grid(row=0,column=3,padx=10)
        
        showAll_btn = Button(search_frame,text="Show All",command=self.fetch_data,width=10,font=("Times new roman",8,"bold"),bg="Khaki",fg="black")
        showAll_btn.grid(row=0,column=4,padx=10)
        
        
        # table Frame---------------------------------
        
        table_frame = LabelFrame(Right_frame,bd=4,relief=RIDGE,bg="LightSeaGreen")
        table_frame.place(x=2,y=70,width=620,height=400)
        
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.vender_table=ttk.Treeview(table_frame,column=("Phone","Name","date","Quantity"),xscrollcommand=scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.vender_table.xview)
        scroll_x.config(command=self.vender_table.yview)
    
        self.vender_table.heading("Phone",text="Phone")
        self.vender_table.heading("Name",text="Name")
        self.vender_table.heading("date",text="date")
        self.vender_table.heading("Quantity",text="Quantity")
       
        self.vender_table["show"]="headings"
        
       

        self.vender_table.column("Phone",width=100)
        self.vender_table.column("Name",width=100)
        self.vender_table.column("date",width=100)
        self.vender_table.column("Quantity",width=100)
      
        self.vender_table.pack(fill=BOTH,expand=1)
        self.vender_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from master_creation") 
        data=my_cursor.fetchall()
            
        if len(data)!=0:
            self.vender_table.delete(*self.vender_table.get_children())
            for i in data:
                self.vender_table.insert("",END,values=i)
            conn.commit()
        conn.close()            
        
    def add_data(self):
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
            my_cursor = conn.cursor()
            my_cursor.execute('''INSERT INTO master_creation(phone,name,date,quantity)
                              VALUES(%s,%s,%s,%s)''',(self.var_phone.get(),
                                                                                                            
                                                                                                            self.var_name.get(),
                                                                                                            self.var_date.get(),
                                                                                                            self.var_quantity.get()
                                                                                                        ));                                                                                                             
                                                                                                                    
                                                                                                                    
                                                            
            conn.commit()
            self.fetch_data()
                
            conn.close()
            messagebox.showinfo("Sucess","vender Details had  Been Added Successfully",parent = self.root)
         
        except Exception as ex:
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent = self.root)
    
    def reset_data(self):
        self.var_name.set("")
        self.var_phone.set("")
        self.var_quantity.set("")
        
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
        id = self.var_search.get()
        
        my_cursor = conn.cursor()    
        my_cursor.execute("select * from master_creation where name = %s",[(id)])
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.vender_table.delete(*self.vender_table.get_children())
            for row in rows:
                self.vender_table.insert('',END,values= row)    
                
            conn.commit()
        conn.close()
    
    def delete_data(self):
        try:
            delete = messagebox.askyesno("Vender delete page","Do you want to delete this Vender",parent=self.root)
            if delete>0:
                conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
                my_cursor = conn.cursor()
                sql="delete from master_creation where name=%s"
                val = (self.var_name.get(),)
                my_cursor.execute(sql,val)
            else:
                if not delete:
                    return
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete","Successfully Deleted the Vender Details",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Due to : {str(ex)}",parent=self.root)
                
    def update_data(self):
                                                                                                                            
        try:
            Update = messagebox.askyesno( "Update","Do you want to update Vender Details",parent=self.root)
            if Update>0:
                    
                conn = mysql.connector.connect(host="localhost",username="root",password = "Pass@1234",database = 'ongc',auth_plugin = 'mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("update master_creation set phone = %s,quantity= %swhere name=%s",(
                            
                                    self.var_phone.get(),
                                    self.var_quantity.get(),
                                    self.var_name.get()
                                    ))
                if not Update:
                    return
            messagebox.showinfo("Success","Vender Details updated successfully",parent=self.root)
            conn.commit()  
            self.fetch_data()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.root)
    
    def get_cursor(self,event=""):
            cursor_focus=self.vender_table.focus()
            content = self.vender_table.item(cursor_focus)
            data= content["values"]
            self.var_name.set(data[1]),
            self.var_phone.set(data[0]),
            self.var_date.set(data[2]),
            self.var_quantity.set(data[3])
    
    
if __name__ == "__main__":
    root=Tk()
    obj=Master(root)
    root.mainloop()



       
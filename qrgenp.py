
from tkinter import*
from PIL import Image,ImageTk
from PIL import Image
from pyzbar.pyzbar import decode

from generator import Generator
from printer import Printer


class Genpr:
    def __init__(self,root):
        self.root=root
        self.root.title("QR_CODE Sector")
        self.root.state('zoomed')     
        # self.root.geometry('132x900+0+0')
        root.resizable(False,False)
        self.root.wm_iconbitmap("icn.ico")
        
        
         
        img3=Image.open(r"img\\bg.jpg")
        img3=img3.resize((1330,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1330,height=700)

        title_lbl=Label(bg_img,text="Global Gasses India PVT. LTD.",font=("Arial Rounded MT Bold",20),bg="MistyRose",fg="Black")
        title_lbl.place(x=0,y=70,width=1300,height=45)

        b1_1=Button(bg_img,text="QR Code Generator",cursor="hand2",command=self.generator,font=("Times New Roman",13,"bold"),bg="MediumSpringGreen",fg="Black") 
        b1_1.place(x=200,y=300,width=250,height=40)
        
        b1_5=Button(bg_img,text="QR Code Printer",cursor="hand2",command=self.printer,font=("Times New Roman",13,"bold"),bg="MediumSpringGreen",fg="Black") 
        b1_5.place(x=650,y=300,width=250,height=40)
        
        
      
    def generator(self):
        self.new_window=Toplevel(self.root)
        self.app = Generator(self.new_window)
        
    def printer(self):
        self.new_window=Toplevel(self.root)
        self.app = Printer(self.new_window)
            
    
if __name__ == "__main__":
    root=Tk()
    obj=Genpr(root)
    root.mainloop()



       
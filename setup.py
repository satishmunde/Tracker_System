import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\\Users\\munde\\AppData\\Local\\Programs\\Python\\Python310\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\\Users\\munde\\AppData\\Local\\Programs\\Python\\Python310\\tcl\\tk8.6"


executables = [cx_Freeze.Executable("Tracker.py", base=base, icon="icn.ico")]


cx_Freeze.setup(
    name = "Tracker System",
    options = {"build_exe": {"packages":["tkinter","os","docxtpl","glob","docx.shared","turtle","PIL","mysql","mysql.connector","pyzbar","cv2","numpy","qrcode","datetime","sys","win32api"], "include_files":["icn.ico","demo.docx",'tcl86t.dll','tk86t.dll','img',"demo",'QRCode','bg','database']}},
    version = "1.0",
    description = "Tracker System | Developed By Satish Munde And Team",
    executables = executables
    )

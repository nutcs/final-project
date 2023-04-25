from tkinter import *
from tkinter import ttk
import style.font as font
import style.color as color
from tkinter import messagebox


root = Tk()
def mainWindow():
    root.title(font.nameTitle)
    # root.geometry("1340x660")
    root.geometry("1200x800")
    root.configure(bg="#fff")
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.option_add('*font','Garamond 16 bold')
    return root

def showPay():
    show_slip.grid(row=0,column=0,sticky=N)
    show_slip.rowconfigure((0,1,2,3),weight=1)
    show_slip.columnconfigure((0,1),weight=1)

    Label(show_slip,text='\nรายละเอียดราคา').grid(row=0,columnspan=2)
    Label(show_slip,image=slip).grid(row=1,columnspan=2,pady=10)
    
    Label(show_slip,text='ราคารวม').grid(row=2,column=0)
    Label(show_slip,text='THB 7,163.67').grid(row=2,column=1)

    Button(show_slip,text='ยกเลิก').grid(row=3,column=0,pady=20)
    Button(show_slip,text='ชำระเงิน',bg='lightgreen',command=paid).grid(row=3,column=1,pady=20)
    
def paid():
    show_slip.grid_forget()
    messagebox.showinfo("Admin:","จองที่พักเสร็จเรียบร้อย")


root = mainWindow()
show_slip = Frame(root, borderwidth=2, relief="groove")
slip = PhotoImage(file="image/slip.png").subsample(2,2)
showPay()
root.mainloop()
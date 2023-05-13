from tkinter import *




def mainwindow() : #หน้าแรก
    root = Tk()
    root.geometry("1200x800")
    root.config(bg='white')
    root.title("Login")
    root.option_add('*font',"Calibri 16 bold")
    root.rowconfigure(0,weight=1)
    root.columnconfigure((0),weight=1)
    return root

def check_outNut():
    # กำหนด layout เป็น Frameหลัก คุมทั้งหน้าจอ
    mainFrame_checkout.grid(row=0,column=0,sticky='news')
    mainFrame_checkout.rowconfigure((0),weight=3)
    mainFrame_checkout.rowconfigure((1,2,3,4,5,6,7,8,9,10,11),weight=1)
    mainFrame_checkout.columnconfigure((0,1),weight=1)

    # Fram Logo บนสุด
    FrameLogoBu.grid(row=0,columnspan=2,sticky='news')
    FrameLogoBu.rowconfigure(0,weight=1)
    FrameLogoBu.columnconfigure(0,weight=1)


   
    #img
    Label(FrameLogoBu,image=logo,bg='#0194f3').grid(row=0,sticky=W)
    Label(FrameLogoBu,text='BURangsit',bg='#0194f3',font="Calibri 32 bold").grid(row=0,sticky=E,padx=25)

    # FrameLogoBu_detail = Frame(FrameLogoBu)
    # FrameLogoBu_detail.grid(row=0,columnspan=2)
    # FrameLogoBu_detail.rowconfigure(0,weight=1)
    # FrameLogoBu_detail.columnconfigure(0,weight=1)
    #infomation 
    Label(mainFrame_checkout,text='Thaks Annซ๋า').grid(row=1,column=0,sticky=W,padx=25)
    Label(mainFrame_checkout,text='Your booking in kiev is confirmed',font="Calibri 20 bold").grid(row=2,column=0,sticky=W,padx=25)
    Label(mainFrame_checkout,text="Gar'is Kyiv Factory Hostel",font="Calibri 20 bold",fg='blue').grid(row=3,column=0,sticky=W,padx=25)
    Label(mainFrame_checkout,image=img_test).grid(row=4,columnspan=2,pady=20)

    #detel
    Label(mainFrame_checkout,text='Your reservation').grid(row=5,column=0,sticky=W,padx=25)
    Label(mainFrame_checkout,text=f'{1} night, {1} dormitory bed').grid(row=5,column=1,sticky=E,padx=25)
    
    Label(mainFrame_checkout,text='check-in').grid(row=6,column=0,sticky=W,padx=25)
    Label(mainFrame_checkout,text=f'13/5/23').grid(row=6,column=1,sticky=E,padx=25)
    
    Label(mainFrame_checkout,text='Check out').grid(row=7,column=0,sticky=W,padx=25)
    Label(mainFrame_checkout,text='14/5/23').grid(row=7,column=1,sticky=E,padx=25)
    
    Label(mainFrame_checkout,text='Prepayment').grid(row=8,column=0,sticky=W,padx=25)
    Label(mainFrame_checkout,text='You will charged a prepayment of the total price at any time').grid(row=8,column=1,sticky=E,padx=25)

    Button(mainFrame_checkout,text='Cancel your booking',bg='orange',fg='white').grid(row=9,columnspan=2)

    Label(mainFrame_checkout,text='').grid(row=10)
    Label(mainFrame_checkout,text='').grid(row=11)




    





root = mainwindow()

logo = PhotoImage(file="image/logo.png")

img_test = PhotoImage(file="image/p1.png").subsample(5,5)
mainFrame_checkout = Frame(root)
FrameLogoBu = Frame(mainFrame_checkout,bg='#0194f3')

check_outNut()

root.mainloop()


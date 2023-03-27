from tkinter import *
from tkinter import ttk
import style.font as font
import style.color as color

root = Tk()
def mainWindow():
    root.title(font.nameTitle)
    root.geometry("1340x660")
    root.configure(bg="#fff")
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.option_add('*font','Garamond 16 bold')
    return root

def search_hostels(root):
    global Frame_search_hostels,Room_ui2,Room_ui1,Room_ui
    #frame ตัวสีเทา
    Frame_search_hostels = Frame(root,bg=color.bg_behind)

    Frame_search_hostels.grid(row=0,column=0,sticky='news')
    Frame_search_hostels.rowconfigure((0,2),weight=1)
    Frame_search_hostels.rowconfigure((1),weight=2)

    Frame_search_hostels.columnconfigure((0,1,2),weight=1)

    #frame ตัวสีขาว
    data_hostel = Frame(Frame_search_hostels,bg=color.white)
    data_hostel.grid(row=1,column=1,sticky="news")

    data_hostel.rowconfigure((0,2),weight=1)
    data_hostel.rowconfigure((1),weight=3)
    
    data_hostel.columnconfigure((0,2),weight=1)
    data_hostel.columnconfigure((1),weight=3)

    # content ตัวหนังสือ,button,input ต่างๆ *************************************************
    content = Frame(data_hostel,bg="#fff")
    content.grid(row=1,column=1,sticky="news")

    content.rowconfigure((0,1,2,3,4,5,6),weight=1)
    content.columnconfigure((1,2,3),weight=1)
    content.columnconfigure((0,4),weight=2)

    #name title
    name_title = Label(content,text="ค้นหาที่พักในรังสิต",bg=color.white)
    name_title.grid(row=0,columnspan=5,sticky=S)

    #search
    search_var = StringVar()
    search_name = Entry(content,width=50,borderwidth=2, relief="groove",textvariable=search_var)
    search_var.set('รังสิต')
    search_name.grid(row=1,columnspan=5)

    #check in-out
    #column 0
    checkin_title = Label(content,text="Check in",bg=color.white)
    checkin_title.grid(row=2,column=1,sticky=W,padx=40)

    checkin_ui = Label(content,text=f"Wed, {22} Mar {2023}",bg=color.white) #ต้องมีแสดง calenda **********************
    checkin_ui.grid(row=3,column=1,sticky=NW,padx=40)

    #column 1
    duration_title = Label(content,text="Duration",bg=color.white)
    duration_title.grid(row=2,column=2,sticky=W)

    duration_ui = ttk.Combobox(content,values=["1 night","2 night","3 night"])
    duration_ui.set('1 night')
    duration_ui.grid(row=3,column=2,sticky=NW)

    #column 2
    checkout_title = Label(content,text="check-out",bg=color.white)
    checkout_title.grid(row=2,column=3,sticky=W)

    checkout_ui = Label(content,text=f"Thu, {23} Mar {2023}",bg=color.white)
    checkout_ui.grid(row=3,column=3,sticky=NW)

    #เลือกจำนวณคน และ ห้อง
    Room_title = Label(content,text="Guest and Room",bg=color.white)
    Room_title.grid(row=4,columnspan=2,column=1,sticky=W,padx=40)

    Room_ui = Label(content,width=35,textvariable=Roomtext)
    Roomtext.set(f"ผู้ใหญ่ {1} คน, {1} ห้อง")
    Room_ui.grid(row=5,columnspan=2,column=1,sticky=W,padx=38)

    RoomFrame = Frame(content,bg=color.white)
    RoomFrame.grid(row=6,columnspan=2,column=1,sticky="news")
    RoomFrame.rowconfigure(0,weight=1)
    RoomFrame.columnconfigure((0,1,2,3,4),weight=1)

    people_title = Label(RoomFrame,text="ผู้ใหญ่ :",bg=color.white)
    people_title.grid(row=0,column=0,sticky=NE)
    
    Room_ui1 = ttk.Combobox(RoomFrame,values=['1','2','3','4','5'],width=5)
    Room_ui1.set('1')
    Room_ui1.bind("<<ComboboxSelected>>", changeRoom1)
    Room_ui1.grid(row=0,column=1,sticky=N)

    room_title = Label(RoomFrame,text="จำนวณห้อง :",bg=color.white)
    room_title.grid(row=0,column=2,sticky=N)
    
    
    Room_ui2 = ttk.Combobox(RoomFrame,values=['1','2','3','4','5'],width=5)
    Room_ui2.current(0)
    Room_ui2.bind("<<ComboboxSelected>>", changeRoom2)
    Room_ui2.grid(row=0,column=3,sticky=NW)


    #search button
    search_bt = Button(content,text="Search",bg=color.green,width=15,command=deleteFrame)
    search_bt.grid(row=5,column=3,sticky=NW)

    # content ตัวหนังสือ,button,input ต่างๆ *************************************************

def deleteFrame():
    Frame_search_hostels.grid_forget()
    
def changeRoom2(event):
    # print(Room_ui2.get())
    Roomtext.set(f"ผู้ใหญ่ {Room_ui1.get()} คน, {Room_ui2.get()} ห้อง") 
def changeRoom1(event):
    # print(Room_ui1.get())
    Roomtext.set(f"ผู้ใหญ่ {Room_ui1.get()} คน, {Room_ui2.get()} ห้อง") 

root = mainWindow()
Roomtext = StringVar()

search_hostels(root)

root.mainloop()
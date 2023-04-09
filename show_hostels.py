from tkinter import *
from tkinter import ttk
import style.font as font
import style.color as color

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

def show_hostels(root):
    global Frame_hostel
    Frame_hostel = Frame(root)
    Frame_hostel.grid(row=0,sticky='news')
    Frame_hostel.rowconfigure(0,weight=1)
    Frame_hostel.rowconfigure((1),weight=6)
    Frame_hostel.columnconfigure((1),weight=1)
    Frame_hostel.columnconfigure((2),weight=5)


    #Frame ทั้งหมด 3 ตัว
#-------------------------------------------------------------------------------------------
    #Tab menu ด้านบนสุด 
    Frame_menu = Frame(Frame_hostel,bg=color.tab_menu)
    Frame_menu.grid(row=0,columnspan=3,sticky='news')

    #screening ตัวคัดกรอง ด้านซ้าย 
    Frame_screening = Frame(Frame_hostel, borderwidth=2, relief="groove")
    Frame_screening.grid(row=1,column=0,ipady=20,sticky='n',ipadx=20,pady=10,padx=10)

    # list hostels
    Frame_list_hostel = Frame(Frame_hostel,bg="green")
    Frame_list_hostel.grid(row=1,columnspan=2,column=1,sticky="news")
    Frame_list_hostel.rowconfigure(0,weight=1)
    Frame_list_hostel.columnconfigure(0,weight=1)
#-------------------------------------------------------------------------------------------


    # Create A Main Frame
    main_frame = Frame(Frame_list_hostel)
    main_frame.pack(fill=BOTH, expand=1,)
    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)
    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    # Layout of โรงแรม
    show_card(second_frame)
    show_setting(Frame_screening)
    showTab_menubar(Frame_menu)
    
    
# Layout of โรงแรม
def show_card(second_frame):
    for thing in range(15):
        hostel_content = Frame(second_frame, borderwidth=2, relief="groove")
        hostel_content.grid(row=thing,column=0, pady=10, padx=10,ipadx=20)
        hostel_content.columnconfigure((0,2),weight=5)
        hostel_content.columnconfigure((1),weight=1)
        hostel_content.rowconfigure((0,1,2,3,4),weight=1)

        Frame_img = Frame(hostel_content, borderwidth=2, relief="groove")
        Frame_img.grid(rowspan=5,column=0,sticky='news')
        Frame_img.rowconfigure(0,weight=0)
        
        #img
        Label(Frame_img,image = p1).grid(row=0,sticky=SE)
        
        #Name hostel
        Label(hostel_content,text="Rangsit Grand Condo").grid(row=0,column=1,sticky=W)

        # แสดงคะแนน ดาว ของโรงแรม
        Frame_star = Frame(hostel_content)
        Frame_star.grid(row=1,column=1,sticky="W")
        Frame_star.columnconfigure((0,1,2,3,4),weight=1)
        Frame_star.columnconfigure((5),weight=15)
        Frame_star.rowconfigure((0),weight=1)
        for i in range(5):#star
            Label(Frame_star,image=star).grid(row=0,column=i,sticky=N)

        # แสดง service ต่างๆ
        input_fac = '1,2,3,4,5,6,7'
        list_fac = input_fac.split(',')
        list_service = ['เครื่องปรับอากาศ','สระว่ายน้ำ','ร้านอาหาร','แผนกต้อนรับ 24 ชม.','ที่จอดรถ','ลิฟท์','Wifi']
        
        Frame_service = Frame(hostel_content)
        Frame_service.grid(row=2,column=1,padx=5)
        Frame_service.columnconfigure((0,1,2,3,4),weight=1)
        Frame_service.rowconfigure((0,1),weight=1)

        row_service2 = Frame(Frame_service)
        row_service2.grid(row=1,column=0,columnspan=4,sticky='news')
        row_service2.columnconfigure((0,1,2,3,4),weight=1)
        row_service2.rowconfigure((0),weight=1)
        for index,item in enumerate(list_fac):
            # ถ้า service มากกว่า 4 ตัว จะใส่ลง row ถัดไป
            if index >= 4:
                row_service2.grid(row=1,columnspan=4,sticky=W)
                row_service2.columnconfigure((0,1,2,3,4),weight=1)
                Label(row_service2,text=list_service[int(item)-1],font=("Arial", 12), borderwidth=2, relief="groove").grid(row=0,column=index-4,pady=5,sticky=NW,padx=3,ipadx=5,ipady=5)
            else:
                Label(Frame_service,text=list_service[int(item)-1],font=("Arial", 12), borderwidth=2, relief="groove").grid(row=0,column=index,pady=5,sticky=N,padx=3,ipadx=5,ipady=5)


        #Frame review and price
        Frame_3 = Frame(hostel_content, borderwidth=2, relief="groove")
        Frame_3.grid(rowspan=5,row=0,column=2,sticky="news")
        Frame_3.rowconfigure((0,1),weight=1)
        Frame_3.columnconfigure((0,1),weight=1)

        #review
        Label(Frame_3,text="ดีมาก 7.7 คะแนน").grid(row=0,columnspan=2,sticky=NE,pady=10,padx=30)
        Label(Frame_3,text="1,000 reviews",font=("Arial", 12)).grid(row=0,columnspan=2,sticky=NE,pady=40,padx=30)

        #price
        Label(Frame_3,text="฿ 1,000").grid(row=0,columnspan=2,sticky=SE,padx=30)
        Button(Frame_3,text="เลือกห้องพัก",bg='darkcyan',fg="white").grid(row=1,columnspan=2,sticky=NE,padx=30,pady=10)


def show_setting(Frame_screening):
    #setting Frame
    Frame_screening.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
    Frame_screening.rowconfigure((10),weight=10)
    Frame_screening.columnconfigure((0,1),weight=1)

    Label(Frame_screening,text="ราคา/ห้อง/คืน").grid(row=1,columnspan=2)

    #min
    Scale(Frame_screening,from_=0,to=100,orient='horizontal',bg='darkcyan',fg="white",length=100).grid(row=2,column=0,sticky=S)
    Label(Frame_screening,text="min").grid(row=3,column=0,sticky=S)
    Entry(Frame_screening,width=10,borderwidth=2, relief="groove").grid(row=4,column=0,sticky=N)
    #max
    Scale(Frame_screening,from_=0,to=100,orient='horizontal',bg='#b70994',fg="white",length=100).grid(row=2,column=1,sticky=S)
    Label(Frame_screening,text="max").grid(row=3,column=1,sticky=S)
    Entry(Frame_screening,width=10,borderwidth=2, relief="groove").grid(row=4,column=1,sticky=N)

    # เลือก Checkbutton stars
    for i in range(5):
        Checkbutton(Frame_screening,variable=stars[i]).grid(row=i+5,column=0,sticky=NW,padx=20)
        Frame_star = Frame(Frame_screening)
        Frame_star.grid(row=i+5,columnspan=2,sticky=NW,pady=10,padx=60)
        Frame_star.rowconfigure(0,weight=1)
        Frame_star.columnconfigure((0,1,2,3,4,5,6),weight=1)
        for time_star in range(i+1): #start  stop  step 
            Label(Frame_star,image=star).grid(row=0,column=time_star)

def showTab_menubar(Frame_menu):
    Frame_menu.rowconfigure(0,weight=1)
    Frame_menu.columnconfigure((0,1,2,3,4,5),weight=1)

    Entry(Frame_menu,width=40).grid(row=0,columnspan=2,column=0)
    Label(Frame_menu,text="30 Mar 2023").grid(row=0,column=2,sticky=W)

    Label(Frame_menu,text="ผู้ใหญ่ :").grid(row=0,column=3,sticky=E,padx=100)
    people = ttk.Combobox(Frame_menu,values=['1','2','3','4','5'],width=5,justify='center')
    people.current(0)
    people.grid(row=0,column=3,sticky=E,padx=20)
    
    Label(Frame_menu,text="ห้อง :").grid(row=0,column=4,sticky=W)
    people = ttk.Combobox(Frame_menu,values=['1','2','3','4','5'],width=5,justify='center')
    people.current(0)
    people.grid(row=0,column=4,sticky=W,padx=60)

    Button(Frame_menu,image=search_icon,width=60).grid(row=0,column=4,sticky=E)



p1 = PhotoImage(file="image/book1.png")
star = PhotoImage(file="image/star.png").subsample(40,40)
search_icon = PhotoImage(file="image/search_bold.png").subsample(20,20)

root = mainWindow()

stars = [IntVar() for i in range(5)]
show_hostels(root)

root.mainloop()

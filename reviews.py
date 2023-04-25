from tkinter import *
import style.font as font
from tkinter import ttk



root = Tk()
def mainWindow():
    root.title(font.nameTitle)
    # root.geometry("1340x660")
    root.geometry("1200x800")
    root.configure(bg="#fff")
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.option_add('*font','areal 14 bold')
    # root.option_add('*font','areal 14 bold')
    return root

def delete_FrameReviews():
    #Layout_reviews()
    Review_Frame.grid_forget()
    menu_review_Frame.grid_forget()
    showHostel_review_Frame.grid_forget()
    comment_review_Frame.grid_forget()

    #Layout comment review ขวา-ล่าง
    scrollbar_review.grid_forget()
    second_frame2.grid_forget()
    average.grid_forget()
    comment.grid_forget()

    #Layout Show data of hostel (ด้านซ้าย กลาง)
    Frame_star.grid_forget()
    Frame_service.grid_forget()
    row_service2.grid_forget()

def Layout_reviews():
    global Review_Frame, menu_review_Frame, showHostel_review_Frame, comment_review_Frame
    #Layout เต็มหน้าจอ
    Review_Frame = Frame(root)
    Review_Frame.grid(row=0,column=0,sticky='news')
    Review_Frame.rowconfigure(0,weight=1)
    Review_Frame.rowconfigure(1,weight=10)
    Review_Frame.columnconfigure((0),weight=1)
    Review_Frame.columnconfigure((1),weight=3)

    #Layout Menu (บนสุด)
    menu_review_Frame = Frame(Review_Frame,bg="gray")
    menu_review_Frame.grid(row=0,columnspan=2,sticky='news')
    menu_review_Frame.rowconfigure(0,weight=1)
    menu_review_Frame.columnconfigure(0,weight=1)

    #Layout Show data of hostel (ด้านซ้าย กลาง)
    showHostel_review_Frame = Frame(Review_Frame)
    showHostel_review_Frame.grid(row=1,column=0,sticky='nw',pady=10,padx=20,ipady=20)
    showHostel_review_Frame.rowconfigure((0,1,2,3,7),weight=1)
    showHostel_review_Frame.rowconfigure((4,5,6),weight=2)
    #หน้าว่าง
    showHostel_review_Frame.rowconfigure((8),weight=3)
    #column
    showHostel_review_Frame.columnconfigure((0),weight=3)
    showHostel_review_Frame.columnconfigure((1),weight=1)

    #Layout comment
    comment_review_Frame = Frame(Review_Frame)
    comment_review_Frame.grid(row=1,column=1,sticky='news')
    comment_review_Frame.columnconfigure(0,weight=1)
    comment_review_Frame.rowconfigure(0,weight=1)

#Layout Menu (บนสุด)
def menu_review():
    Button(menu_review_Frame,text="กลับไปหน้าหลัก",bg='lightgreen',command=delete_FrameReviews).grid(row=0,sticky=W,ipadx=10,padx=20,ipady=5,pady=10)
    #tap login
    Button(menu_review_Frame,text=' เข้าสู่ระบบ',image=user_login_img,compound='left',command=delete_FrameReviews).grid(row=0,sticky=E,ipadx=10,padx=160,ipady=3)
    Button(menu_review_Frame,text='ลงทะเบียน',bg='#FFCB44',command=delete_FrameReviews).grid(row=0,sticky=E,ipadx=10,padx=30,ipady=2)


#Layout comment review ขวา-ล่าง
def reviews_scrollbar():
    global scrollbar_review,second_frame2,average,comment
    # Create A Main Frame
    scrollbar_review = Frame(comment_review_Frame)
    scrollbar_review.pack(fill=BOTH, expand=1,)
    # Create A Canvas
    my_canvas2 = Canvas(scrollbar_review)
    my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)
    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(scrollbar_review, orient=VERTICAL, command=my_canvas2.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configure The Canvas
    my_canvas2.configure(yscrollcommand=my_scrollbar.set)
    my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion = my_canvas2.bbox("all")))
    # Create ANOTHER Frame INSIDE the Canvas
    second_frame2 = Frame(my_canvas2)
    # Add that New frame To a Window In The Canvas
    my_canvas2.create_window((0,0), window=second_frame2, anchor="nw")

    #หน้าสรุปจำนวนคนรีวิว
    average = Frame(second_frame2, borderwidth=2, relief="groove")
    average.grid(row=0,column=0, pady=5,sticky=NW)
    average.rowconfigure((0,1,2,3,4),weight=1)
    average.columnconfigure((0,1,2),weight=1)

###########################################################################################################
    # คะแนนเฉลี่ย 
    Label(average,text='4.4',font='areal 64 bold').grid(rowspan=3,column=0)
    # จำนวนคนรีวิว
    Label(average,text='ทั้งหมด 15 ความคิดเห็น',font='areal 12').grid(row=3,column=0,padx=20)

    number = ['1','2','3','4','5']
    point = [10,2,1,1,1]
    for i in range(5):
        # number
        Label(average,text=number[i]).grid(row=i,column=1,sticky=E)
        # หลอดพลัง พื้นหลังสีเทา
        Label(average,width=15,bg='gray').grid(row=i,column=2,sticky=W,pady=10,padx=20)
        # คะแนนหลอดพลัง สีเขียว
        Label(average,width=point[i],bg='green').grid(row=i,column=2,sticky=W,pady=10,padx=20)
###########################################################################################################



    # รีวิวทั้งหมด
    for thing in range(15):
        rowComment = thing + 1

        comment = Frame(second_frame2, borderwidth=2, relief="groove")
        comment.grid(row=rowComment,column=0, pady=5,sticky=NW)
        comment.rowconfigure((0,1,2,3,4),weight=1)
        comment.columnconfigure(0,weight=3)
        comment.columnconfigure(1,weight=1)

        #day
        Label(comment,text="14 JAN 2023",font='areal 12').grid(row=1,column=1,sticky=E,ipadx=20,pady=10)
        #Name
        Label(comment,text="Nutthapon Salangsing").grid(row=1,column=0,sticky=W,ipadx=20,pady=10)
        #Point
        Label(comment,text='9.7/10',font='areal 12',bg='lightgreen').grid(row=2,column=0,sticky=W,ipadx=10,padx=20)
        #comment
        Label(comment,text='สะอาด บรรยากาศดี คุ้มราคามาก',font='areal 12').grid(row=3,column=0,sticky=W,ipadx=20,pady=10)

        # พื้นที่หน้าว่างด้านล่าง
        if(thing == 14):
            Label(second_frame2,text='\n\n').grid(row=rowComment+1,column=0, pady=5,sticky=NW)
            

#Layout Show data of hostel (ด้านซ้าย กลาง)
def main_hostel_review():
    global Frame_star,Frame_service,row_service2
    #name hostel
    Label(showHostel_review_Frame,text='โนโวเทล กรุงเทพ ฟิวเจอร์พาร์ค รังสิต',font='areal 24 bold').grid(row=1,columnspan=2,sticky=W)
    
    #star
    Frame_star = Frame(showHostel_review_Frame)
    Frame_star.grid(row=2,column=0,sticky="W")
    Frame_star.columnconfigure((0,1,2,3,4),weight=1)
    Frame_star.columnconfigure((5),weight=15)
    Frame_star.rowconfigure((0),weight=1)
    for i in range(5):#star
        Label(Frame_star,image=star).grid(row=0,column=i,sticky=N)
    
    #address
    name_address = '114 ถ.พหลโยธิน, ต.ประชาธิปัตย์, รังสิต, อำเภอธัญบุรี, ปทุมธานี, ประเทศไทย, 12130'
    Label(showHostel_review_Frame,text=f' {name_address}',font='areal 12',image=placeholder,compound='left').grid(row=3,columnspan=2,sticky=W)

    #img
    Label(showHostel_review_Frame,image=p1, borderwidth=2, relief="groove").grid(row=4,columnspan=2,pady=10)

    #service
    # แสดง service ต่างๆ
    input_fac = '1,2,3,4,5,6,7'
    list_fac = input_fac.split(',')
    list_service = ['เครื่องปรับอากาศ','สระว่ายน้ำ','ร้านอาหาร','แผนกต้อนรับ 24 ชม.','ที่จอดรถ','ลิฟท์','Wifi']
    
    Frame_service = Frame(showHostel_review_Frame)
    Frame_service.grid(row=5,column=0,padx=5)
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
    

    #button ปุ่มเข้าเลือกห้องพัก
    Button(Frame_service,text='เลือกห้องพัก',bg='#FFCB44',command=delete_FrameReviews).grid(row=1,column=4,sticky=NE,ipadx=10,ipady=5,pady=20)



root = mainWindow()

user_login_img = PhotoImage(file="image/user_login.png").subsample(20,20)
p1 = PhotoImage(file="image/p1.png").subsample(3,3)
star = PhotoImage(file="image/star.png").subsample(40,40)
placeholder = PhotoImage(file="image/placeholder.png").subsample(20,20)

# Photos = [PhotoImage(file=f"image/{img}.png") for i in range(10)]

Layout_reviews()
menu_review()
main_hostel_review()
reviews_scrollbar()

root.mainloop()
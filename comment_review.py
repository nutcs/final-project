from tkinter import *
from tkinter import ttk
from tkinter import messagebox



def mainwindow() : #หน้าแรก
    root = Tk()
    root.geometry("1200x800")
    root.config(bg='white')
    root.title("Login")
    root.option_add('*font',"Calibri 16 bold")
    root.rowconfigure(0,weight=1)
    root.columnconfigure((0),weight=1)
    return root

def treeview0() :
    comment_mainFrame.grid(row=0,column=0,sticky='news')
    comment_mainFrame.rowconfigure((0),weight=2)
    comment_mainFrame.rowconfigure((1,2,3,4,5),weight=1)
    comment_mainFrame.columnconfigure((0,1,2),weight=1)

    Label(comment_mainFrame,text="เลือกรีวิวห้องพักของคุณ",bg=bg_comment,font="Calibri 24 bold",fg=fg_comment).grid(row=0,columnspan=3,pady=20,padx=20,sticky=N)
    ################ Treeview
    global mytree,comment_entry,name_comment
    mytree= ttk.Treeview(comment_mainFrame,columns= ("col1","col2","col3") )
    mytree.grid(row=0,columnspan=3,pady=20,padx=20,sticky=S)
    mytree.heading("#0",text="Name")
    mytree.heading("col1",text="Username")
    mytree.heading("col2",text="Check-in")
    mytree.heading("col3",text="Ceck-out")

    mytree.column("#0", width=0, minwidth=0)
    mytree.column("col1", width=500, minwidth=200)
    mytree.column("col2", width=150, minwidth=100) 
    mytree.column("col3", width=150, minwidth=100) 

    data = [
        ['nnnn1','13/555','14/555',0],
        ['nnnn2','13/555','14/555',0],
        ['nnnn3','13/555','14/555',0]
        ]
    for i,record in enumerate(data):
        mytree.insert('','end',values=record)
    ################

    #name
    name_comment = Label(comment_mainFrame,bg=bg_comment,font="Calibri 20 bold",fg=fg_comment,text='none')#,textvariable=ntbasic
    name_comment.grid(row=1,columnspan=3)

    #ให้คะแนน
    Label(comment_mainFrame,text="ให้คะแนนที่พักของคุณ: ",bg=bg_comment,fg=fg_comment).grid(row=2,column=0,pady=20,padx=20,sticky=E)
    star_comment = ttk.Combobox(comment_mainFrame,values=['1','2','3','4','5'],width=5)
    star_comment.set('1')
    star_comment.grid(row=2,column=1,sticky=W)
    Label(comment_mainFrame,text="ดาว",bg=bg_comment,fg=fg_comment).grid(row=2,column=1,columnspan=2,sticky=W,padx=100)

    #input entry
    Label(comment_mainFrame,text="รีวิวห้องพัก: ",bg=bg_comment,fg=fg_comment).grid(row=3,column=0,sticky=E,padx=10)
    comment_entry = Entry(comment_mainFrame,width=50, borderwidth=2, relief="groove",font="Calibri 16")
    comment_entry.grid(row=3,columnspan=2,column=1,sticky=W)

    Button(comment_mainFrame,width=20,text='add comment').grid(row=4,column=0,sticky=E)
    Button(comment_mainFrame,width=20,text='Edit').grid(row=4,column=1)
    Button(comment_mainFrame,width=20,text='Delete').grid(row=4,column=2,sticky=W)
    mytree.bind('<Double-1>',treeviewclick)

def treeviewclick(e) :
    global clickdata,ntbasic
    selectrow = mytree.selection() #Mytree selection ->  ('I002',)
    print("Mytree selection -> ",selectrow)
    clickdata = mytree.item(mytree.selection(),'values') #Clickdata ('2', 'CS318', 'Object-Oriented Programming', 'Tue', 'RA4507')
    print("Clickdata",clickdata)
    # setEntry = [enAdd,enUpdate,enDelete,enClear]
    ntbasic = clickdata[0]
    name_comment['text'] = clickdata[0]


# def addCourse():
#     if(comment_entry.get() == ''):
#         messagebox.showinfo("Admin","กรุณากรอก comment")
#     else: 
#         print(number_course)
#         sql = '''
#         INSERT INTO course (id, course_code, course_name, day, room)
#         VALUES (?,?,?,?,?);
#         '''
#         cursor.execute(sql, [number_course + 1, enAdd.get(),enUpdate.get(),enDelete.get(),enClear.get()] )
#         conn.commit()
#         mytree.insert('','end',values=[number_course + 1, enAdd.get(),enUpdate.get(),enDelete.get(),enClear.get()])



    
# def updateCourse():
#     if(comment_entry.get() == ''):
#         messagebox.showinfo("Admin","กรุณากรอก comment")
#     else: 
#         sql = 'update course set course_code=?, course_name=?, day=?, room=? where id=?'
#         cursor.execute(sql,[comment_entry.get(),enUpdate.get(),enDelete.get(),enClear.get(), clickdata[0]])
#         conn.commit()
#         # delete mytree
#         for item in mytree.get_children():
#             mytree.delete(item)
#         insertMyTree()

# def deleteCourse():
#     sql = 'delete from course where id=?;'
#     cursor.execute(sql,[clickdata[0]])
#     conn.commit()
#     for item in mytree.get_children():
#         mytree.delete(item)
#     insertMyTree()

# def insertMyTree():
#     global number_course
#     sql = 'select * from course'
#     cursor.execute(sql)
#     course_data = cursor.fetchall()
#     number_course = len(course_data)
#     for i,record in enumerate(course_data):
#         mytree.insert('','end',values=record)



root = mainwindow()

comment_mainFrame = Frame(root,bg='#0194f3')

ntbasic = [StringVar()]
bg_comment = '#0194f3'
fg_comment = 'white'

treeview0()
root.mainloop()

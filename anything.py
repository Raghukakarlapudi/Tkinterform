from tkinter import *
from tkinter import ttk
import pymysql

class StudentData:
    def __init__(self,root):
        self.root=root
        self.root.title('Data')
        self.root.geometry('1400x700')

        title=Label(self.root,
                    text='Students Data',
                    bd=10,
                    relief=FLAT,
                    bg='DodgerBlue2',fg='white',font=('times new roman',15,'bold'))
        # title=Frame(self.root,bg='DodgerBlue2',bd=10,relief=GROOVE)
        self.roll_no_var=StringVar()
        self.first_name_var=StringVar()
        self.last_name_var=StringVar()
        self.course_var=StringVar()
        self.fee_var=StringVar()
        self.email_var=StringVar()
        self.mobile_var=StringVar()
        self.gender_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        title.pack(fill=X, side=TOP,pady=10,padx=10)
### --------------Dataframe--------------------######

        DataEntryFrame = Frame(self.root, bg='DodgerBlue2', bd=10, relief=FLAT)
        DataEntryFrame.place(x=10,y=80,width=400,height=600)

        title = Label(DataEntryFrame, text='Students Details Entry', relief=FLAT,bg='DodgerBlue2',fg='white',font=('times new roman', 15,'bold'))
        title.grid(row=0, columnspan=2,padx=90,pady=5)

#--------------Roll No ----------------#

        roll_no =Label(DataEntryFrame,text="Roll No :", font=('times new roman',15,'bold'),bg='DodgerBlue2',fg='white')
        roll_no.grid(row=1,column=0,sticky=W)

        roll_no_entry=Entry(DataEntryFrame,textvariable=self.roll_no_var,font=('times new roman',15,'bold'),)
        roll_no_entry.grid(row=1,column=1,padx=10,pady=20)

#---------------First Name--------------#
        first_name=Label(DataEntryFrame,text="First name :", font=('times new roman',15,'bold'),bg='DodgerBlue2',fg='white')
        first_name.grid(row=2,column=0,sticky=W)

        first_name_entry=Entry(DataEntryFrame,textvariable=self.first_name_var,font=('times new roman',15,'bold'),)
        first_name_entry.grid(row=2,column=1,padx=10,pady=10)

#------------Last Name--------------------#

        last_name = Label(DataEntryFrame, text="Last name :", font=('times new roman', 15, 'bold'), bg='DodgerBlue2',fg='white')
        last_name.grid(row=3, column=0, sticky=W)

        last_name_entry = Entry(DataEntryFrame,textvariable=self.last_name_var, font=('times new roman', 15, 'bold'), )
        last_name_entry.grid(row=3, column=1, padx=10, pady=10)

#-------------course--------------------#

        course = Label(DataEntryFrame, text="Course :", font=('times new roman', 15, 'bold'), bg='DodgerBlue2', fg='white')
        course.grid(row=4, column=0, sticky=W)

        course_entry = Entry(DataEntryFrame,textvariable=self.course_var, font=('times new roman', 15, 'bold'), )
        course_entry.grid(row=4, column=1, padx=10, pady=10)

#-----------------fee------------#

        fee = Label(DataEntryFrame, text="Fee :", font=('times new roman', 15, 'bold'), bg='DodgerBlue2',fg='white')
        fee.grid(row=5, column=0, sticky=W)

        fee_entry= Entry(DataEntryFrame,textvariable=self.fee_var, font=('times new roman', 15, 'bold'), )
        fee_entry.grid(row=5, column=1, padx=10, pady=10)

            #-----------------email--------------#

        email = Label(DataEntryFrame, text="Email  :", font=('times new roman', 15, 'bold'),bg='DodgerBlue2',fg='white')
        email.grid(row=6, column=0, sticky=W)

        email_entry= Entry(DataEntryFrame,textvariable=self.email_var, font=('times new roman', 15, 'bold'), )
        email_entry.grid(row=6, column=1, padx=10, pady=10)

        #------------------Mobile------------#

        mobile=Label(DataEntryFrame,text='Mobile : ',font=('times new roman',15,'bold'),bg='DodgerBlue2',fg='white')
        mobile.grid(row=7, column=0, sticky=W)


        mobile_entry= Entry(DataEntryFrame, textvariable=self.mobile_var,font=('times new roman', 15, 'bold'), )
        mobile_entry.grid(row=7, column=1, padx=10, pady=10)

    #------------------Gender------------#
        gender = Label(DataEntryFrame, text='Gender : ', font=('times new roman', 15, 'bold'), bg='DodgerBlue2',fg='white')
        gender.grid(row=8, column=0, sticky=W)

        gender_entry = Entry(DataEntryFrame,textvariable=self.gender_var, font=('times new roman', 15, 'bold'), )
        gender_entry.grid(row=8, column=1, padx=10, pady=10)

        ##--------Button Frame--------------#

        btn_space=Frame(DataEntryFrame,bd=4,relief=FLAT,bg='DodgerBlue2')
        btn_space.place(x=30,y=500,width=300,height=50)

        add_button=Button(btn_space,text='ADD',command=self.adding_data,bd=3,bg='blue',fg='white',relief=FLAT,width=6)
        add_button.grid(row=0,column=0,padx=10,pady=10)

        update_button = Button(btn_space,command=self.update_data, text='UPDATE', bd=3, bg='green', fg='white', relief=FLAT)
        update_button.grid(row=0,column=1,padx=10, pady=10)

        delete_button = Button(btn_space,command=self.delete_data, text='DELETE', bd=3, bg='red', fg='white', relief=FLAT)
        delete_button.grid( row=0,column=2,padx=10, pady=10)

        clear_button = Button(btn_space,command=self.clear, text='CLEAR', bd=3, bg='yellow', fg='white', relief=FLAT,width=6)
        clear_button.grid( row=0,column=3,padx=10, pady=10)


        DataEntryFrame = Frame(self.root, bg='DodgerBlue2', bd=10, relief=FLAT)
        DataEntryFrame.place(x=420, y=80, width=1100, height=600)

        search_by = Label(DataEntryFrame, text='Search by ', width=15, bg='DodgerBlue2',font=('times new roman', 15, 'bold'))
        search_by.grid(row=0, column=0, padx=20, pady=10, sticky=E)

        combo_search = ttk.Combobox(DataEntryFrame,textvariable=self.search_by, font=('times new roman', 15, 'bold'), width=20)
        combo_search['values'] = ('course', 'fee', 'gender')
        combo_search.grid(row=0, column=1)

        txt_search = Entry(DataEntryFrame,textvariable=self.search_txt, font=('times new roman', 15, 'bold'))
        txt_search.grid(row=0, column=2, padx=20)

        btnSearch = Button(DataEntryFrame, command=self.search_data,bg='blue',text='Search', font=('times new roman', 15, 'bold'), relief=FLAT,width=8)
        btnSearch.grid(row=0, column=3,padx=6)

        btnShowAll=Button(DataEntryFrame,command=self.fetch_data,bg='Green',text='Show All',font=('times new roman',15,'bold'),width=8)
        btnShowAll.grid(row=0,column=4,padx=10)

        #--------------TABLE FRAME-------------#

        table_Frame=Frame(DataEntryFrame,relief=FLAT)
        table_Frame.place(x=10,y=60,width=1065,height=500)

        self.Student_Table=ttk.Treeview(table_Frame,columns=('roll_no','first_name','last_name','course','fee','email','mobile','gender'))
        self.Student_Table.heading('roll_no',text='Roll No')
        self.Student_Table.heading('first_name', text='First Name')
        self.Student_Table.heading('last_name', text='Last Name')
        self.Student_Table.heading('course', text='Course')
        self.Student_Table.heading('fee', text='Fee')
        self.Student_Table.heading('email', text='Email')
        self.Student_Table.heading('mobile', text='Mobile')
        self.Student_Table.heading('gender', text='Gender')
        self.Student_Table['show']='headings'

        self.Student_Table.column('roll_no',width=70,anchor=CENTER)
        self.Student_Table.column('first_name', width=200,anchor=CENTER)
        self.Student_Table.column('last_name', width=200,anchor=CENTER)
        self.Student_Table.column('course', width=100,anchor=CENTER)
        self.Student_Table.column('fee', width=100,anchor=CENTER)
        self.Student_Table.column('email', width=200,anchor=CENTER)
        self.Student_Table.column('mobile', width=100,anchor=CENTER)
        self.Student_Table.column('gender', width=100,anchor=CENTER)

        self.Student_Table.pack()
        # self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor())

        self.fetch_data()
        self.update_data()


        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)

    def get_cursor(self, var):
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.roll_no_var.set(row[0])
        self.first_name_var.set(row[1])
        self.last_name_var.set(row[2])
        self.course_var.set(row[3])
        self.fee_var.set(row[4])
        self.email_var.set(row[5])
        self.mobile_var.set(row[6])
        self.gender_var.set(row[7])


    def adding_data(self):
        connection = pymysql.connect(host='localhost', user='raghu', password='1234', db='studentdatadb')
        cursor = connection.cursor()
        cursor.execute('insert into studentinfo values(%s,%s,%s,%s,%s,%s,%s,%s)',
                        (self.roll_no_var.get(),
                        self.first_name_var.get(),
                        self.last_name_var.get(),
                        self.course_var.get(),
                        self.fee_var.get(),
                        self.email_var.get(),
                        self.mobile_var.get(),
                        self.gender_var.get()
                    ))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def fetch_data(self):
        connection=pymysql.connect(host='localhost',user='raghu',password='1234',db='studentdatadb')
        cursor=connection.cursor()
        cursor.execute('select * from studentinfo')
        rows=cursor.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            connection.commit()
        connection.close()

    def update_data(self):
        connection = pymysql.connect(host='localhost', user='raghu', password='1234', db='studentdatadb')
        cursor = connection.cursor()
        cursor.execute('update studentinfo set first_name=%s, '
                       'last_name=%s, '
                       'course=%s, '
                       'fee=%s,'
                       'email=%s,'
                       'mobile=%s, '
                       'gender=%s where roll_no=%s',
                       (self.first_name_var.get(),
                        self.last_name_var.get(),
                        self.course_var.get(),
                        self.fee_var.get(),
                        self.email_var.get(),
                        self.mobile_var.get(),
                        self.gender_var.get(),
                        self.roll_no_var.get()
                        ))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def delete_data(self):
        connection = pymysql.connect(host='localhost', user='raghu', password='1234', db='studentdatadb')
        cursor = connection.cursor()
        cursor.execute('delete from studentinfo where roll_no = %s',
                       (self.roll_no_var.get()))

        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def clear(self):
        self.roll_no_var.set(' ')
        self.first_name_var.set(' ')
        self.last_name_var.set(' ')
        self.course_var.set(' ')
        self.fee_var.set(' ')
        self.email_var.set(' ')
        self.mobile_var.set(' ')
        self.gender_var.set(' ')

    def search_data(self):
        connection = pymysql.connect(host='localhost', user='raghu', password='1234', db='studentdatadb')
        cursor = connection.cursor()
        cursor.execute("select * from studentinfo "
                       "where "+str(self.search_by.get())+" like '%"+str(self.search_txt.get())+"%'")
        rows=cursor.fetchall()

        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            connection.commit()
        connection.close()


root =Tk()
obj=StudentData(root)
root.mainloop()

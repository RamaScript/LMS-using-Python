from tkinter import *
from tkinter import ttk

bgColor = 'cyan'
fgColor = 'red'
normalFontColor = 'black'
class LMS:
    def __init__(self,root):
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1550x800+0+0')

        labtitle = Label(self.root,text='LIBRARY MANANGEMENT SYSTEM',bg=bgColor,fg=fgColor,bd=10,relief=RIDGE,font=('times new roman',40),padx=5,pady=5)
        labtitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=5,bg=bgColor)
        frame.place(x=0,y=100,width=1530,height=400)

        # Data Framne Left

        DataFrameLeft=LabelFrame(frame,text='Library Membership Information',bg=bgColor,fg=fgColor,bd=5,relief=RIDGE,font=('arial',15,'bold'))
        DataFrameLeft.place(x=10,y=5,width=900,height=350)

        # ----------------------person info

        lblMember = Label(DataFrameLeft,text='Member Type : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblMember.grid(column=0,row=0,sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,font=('arial',12),width=27,state='readonly')
        comMember['value']=('Admin Staff','Student','Faculty')
        comMember.grid(row=0,column=1)

        lblCRN = Label(DataFrameLeft,text='CRN No. : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblCRN.grid(row=1,column=0,sticky=W)
        txtCRN = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtCRN.grid(row=1,column=1)

        lblBranch = Label(DataFrameLeft,text='Branch : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblBranch.grid(row=2,column=0,sticky=W)
        comBranch = ttk.Combobox(DataFrameLeft,font=('arial',12),width=27,state='readonly')
        comBranch['value']=('BCA','BBA','B.Tech','MBA','MCA')
        comBranch.grid(row=2,column=1)

        lblRollNo = Label(DataFrameLeft,text='Roll No. : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblRollNo.grid(row=3,column=0,sticky=W)
        txtRollNo = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtRollNo.grid(row=3,column=1)  

        lblFName = Label(DataFrameLeft,text='First Name : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblFName.grid(row=4,column=0,sticky=W)
        txtFName = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtFName.grid(row=4,column=1) 
        
        lblLName = Label(DataFrameLeft,text='Last Name : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblLName.grid(row=5,column=0,sticky=W)
        txtLName = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtLName.grid(row=5,column=1) 

        lblAddress = Label(DataFrameLeft,text='Address : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblAddress.grid(row=6,column=0,sticky=W)
        txtAddress = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtAddress.grid(row=6,column=1) 

        lblPostalCode = Label(DataFrameLeft,text='Postal Code : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblPostalCode.grid(row=7,column=0,sticky=W)
        txtPostalCode = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtPostalCode.grid(row=7,column=1) 

        lblMobile = Label(DataFrameLeft,text='Mobile No. : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtMobile.grid(row=8,column=1)  


        # ----------------------Book info

        lblBID = Label(DataFrameLeft,text='Book ID : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblBID.grid(row=0,column=3,sticky=W)
        txtBID = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtBID.grid(row=0,column=4) 

        lblBTitle = Label(DataFrameLeft,text='Book Title : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblBTitle.grid(row=1,column=3,sticky=W)
        txtBTitle = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtBTitle.grid(row=1,column=4) 

        lblBAuthor = Label(DataFrameLeft,text='Author Name : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblBAuthor.grid(row=2,column=3,sticky=W)
        txtBAuthor = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtBAuthor.grid(row=2,column=4) 

        lblDateBorrowed = Label(DataFrameLeft,text='Date Borrowed : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=3,sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtDateBorrowed.grid(row=3,column=4) 

        lblDateDue = Label(DataFrameLeft,text='Due Date : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblDateDue.grid(row=4,column=3,sticky=W)
        txtDateDue = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtDateDue.grid(row=4,column=4) 

        lblDaysOnBook = Label(DataFrameLeft,text='Days on Book : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=3,sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtDaysOnBook.grid(row=5,column=4) 

        lblLateReturnFine = Label(DataFrameLeft,text='Late Return Fine : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=3,sticky=W)
        txlLateReturnFine = Entry(DataFrameLeft,font=('arial',12),width=29)
        txlLateReturnFine.grid(row=6,column=4) 

        lblDateOverDue = Label(DataFrameLeft,text='Date Over Due : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=3,sticky=W)
        txtDateOverDue = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtDateOverDue.grid(row=7,column=4) 

        lblActualPrice = Label(DataFrameLeft,text='Actual Price : ',bg=bgColor,fg=normalFontColor,font=('arial',12),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=3,sticky=W)
        txtActualPrice = Entry(DataFrameLeft,font=('arial',12),width=29)
        txtActualPrice.grid(row=8,column=4) 

        #  Data Frame Right 

        DataFrameRight=LabelFrame(frame,text='Book Details',bg=bgColor,fg=fgColor,bd=5,relief=RIDGE,font=('arial',15),padx=5,pady=5)
        DataFrameRight.place(x=920,y=5,width=540,height=350)

        self.txtBox = Text(DataFrameRight,font=('arial',12),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky='ns')

        listBooks = ["Code", "Clean Code", "Effective Java", "Refactoring", "Deep Learning","Introduction to Algorithms", "Python Crash Course", "Effective Python", "Clean Architecture", "JavaScript: The Good Parts", "Design Patterns","Computer Systems", "Head First Design Patterns", "You Don't Know JS", "The Art of Computer Programming", "The C Programming Language", "The Pragmatic Programmer", "Algorithm Design Manual", "Introduction to the Theory of Computation", "Automate the Boring Stuff with Python"]

        listBox = Listbox(DataFrameRight,font=('arial',12,'bold'),width=20,height=15)
        listBox.grid(row=0,column=0,padx=4)

        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        # Btns Frame

        frameBtn=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg=bgColor)
        frameBtn.place(x=0,y=500,width=1530,height=75)

        btnAddData = Button(frameBtn,text='ADD Data',bg='yellow',fg='black',bd=5,font=('arial',15),width=20)
        btnAddData.grid(row=0,column=0)

        btnShowData = Button(frameBtn,text='Show Data',bg='yellow',fg='black',bd=5,font=('arial',15),width=20)
        btnShowData.grid(row=0,column=1)

        btnUpdate = Button(frameBtn,text='Update',bg='yellow',fg='black',bd=5,font=('arial',15),width=20)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(frameBtn,text='Delete',bg='yellow',fg='black',bd=5,font=('arial',15),width=20)
        btnDelete.grid(row=0,column=3)

        btnReset = Button(frameBtn,text='Reset',bg='yellow',fg='black',bd=5,font=('arial',15),width=20)
        btnReset.grid(row=0,column=4)

        btnExit = Button(frameBtn,text='Exit',bg='yellow',fg='black',bd=5,font=('arial',15),width=20)
        btnExit.grid(row=0,column=5)

        # Informaton frame

        frameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=5,bg=bgColor)
        frameDetails.place(x=0,y=570,width=1530,height=225)

        table_frame = Frame(frameDetails,bd=6,relief=RIDGE,bg=bgColor)
        table_frame.place(x=0,y=0,width=1460,height=190)

        self.library_table=ttk.Treeview(table_frame,column=('membertype','prnno','title','firstname','lastname','address','postalcode','mobile','bookid','booktitle','author','dateborrowed','datedues','days','latereturnfine','dateoverdue','finalprice'))

root = Tk()
obj = LMS(root)

root.mainloop()
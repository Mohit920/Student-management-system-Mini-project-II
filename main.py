


######################################TIme and slider function###################
def Time():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%y")
    clock_label.config(text='Date:'+date_string+'\n'+'Time:'+time_string)
    clock_label.after(200,Time)

def Intro_label():
    global count,text
    if count>=len(ss):
        count=-1
        text=''
        slider_label.config(text=text)
    else:
        text+=ss[count]
        slider_label.config(text=text)
    count+=1
    slider_label.after(200,Intro_label)

######################################################
import random

colour=['red','green','blue','violet','cyan','brown','skyblue','yellow','pink','gold2','red2']
def Into_label_colour():
    fg=random.choice(colour)
    slider_label.config(fg=fg)
    slider_label.after(100,Into_label_colour)


##################Connection of database#######################
global con,mycursor
def connect_db():
    def submit_db():
        global con,mycursor
        host=host_value.get()
        user=user_value.get()
        password=password_value.get()

        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect!Try again')
            return
        try:
            strr='create database studentmanagementsystem'
            mycursor.execute(strr)
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            strr='create table studentdata(id int,name varchar(20),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(2),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'Database created.You are connected to Database', parent=dbroot)


        except:
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('notification','Now you are connected to Database',parent=dbroot)
        dbroot.destroy()

    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry("470x250+800+230")
    dbroot.iconbitmap("C:\\Users\\Dell\\PycharmProjects\\student management\\images\\database.ico")
    dbroot.title('Connect to Database')
    dbroot.config(bg='grey')
    dbroot.resizable(False,False)

    ###############connect database label########################################
    id_label=Label(dbroot,text='Enter host:',font="times 15 bold",relief=GROOVE,borderwidth=3,width=12,bg='green',fg='white')
    id_label.place(x=10,y=20)


    user_label=Label(dbroot,text='Username:',font="times 15 bold",relief=GROOVE,borderwidth=3,width=12,bg='green',fg='white')
    user_label.place(x=10, y=80)

    password_label=Label(dbroot,text='Password:',font="times 15 bold",relief=GROOVE,borderwidth=3,width=12,bg='green',fg='white')
    password_label.place(x=10,y=140)

    ####################Entry boxes of connect db########################
    host_value=StringVar()

    host_entry=Entry(dbroot,font='roman 15 bold',bd=3,width=25,textvariable=host_value)
    host_entry.place(x=190,y=18)

    user_value = StringVar()
    user_entry = Entry(dbroot, font='roman 15 bold', bd=3, width=25,textvariable=user_value)
    user_entry.place(x=190, y=78)

    password_value = StringVar()
    password_entry = Entry(dbroot, font='roman 15 bold', bd=3, width=25,textvariable=password_value)
    password_entry.place(x=190, y=138)

    submit_button=Button(dbroot,text="Sumbit",command=submit_db,bd=6,width=18,font="roman 15 bold italic",fg='black',bg='lightgreen',activebackground='blue',activeforeground='white')
    submit_button.place(x=150,y=190)

    dbroot.mainloop()
########################### data entry frame button functions###################
def add_student():
    ###########################################Add button func###############
    def add_button_fun():
        id=enterid_value.get()
        name=entername_value.get()
        mobile=entermobile_value.get()
        emai=email_value.get()
        addres=address_value.get()
        gen=gender_value.get()
        dob=dob_value.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%D/%M/%Y")
        try:
            strr='insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            con.cursor().execute(strr,(id,name,mobile,emai,addres,gen,dob,addedtime,addeddate))
            con.commit()
            res=messagebox.askyesnocancel('notification','Id {} Name {} Added successfully..do you want to clear form'.format(id,name),parent=addroot)
            if res==True:
                enterid_value.set('')
                entername_value.set('')
                entermobile_value.set('')
                email_value.set('')
                address_value.set('')
                gender_value.set('')
                dob_value.set('')
        except:
            messagebox.showerror('error','Id already exits..\nTry another Id',parent=addroot)

        strr = "select * from studentdata"

        (con.cursor()).execute(strr)
        info=(con.cursor()).fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in info:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot=Toplevel(master=data_entry_frame)
    addroot.grab_set()
    addroot.title("add student")
    addroot.geometry('470x400+220+220')
    addroot.resizable(False,False)
    addroot.config(bg="grey")
    #addroot.iconbitmap()

    ############## Add student label ########

    enterid_label = Label(addroot, text='Enter Id:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,bg='green', fg='white')
    enterid_label.place(x=10, y=20)
    ####################Entry boxe of enterid label########################
    enterid_value=StringVar()
    enterid_entry=Entry(addroot,font='roman 15 bold',bd=3,width=25,textvariable=enterid_value)
    enterid_entry.place(x=190,y=18)

    entername_label = Label(addroot, text='Name:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12, bg='green', fg='white')
    entername_label.place(x=10, y=65)
    ####################Entry boxe of enterid label########################
    entername_value = StringVar()
    entername_entry = Entry(addroot, font='roman 15 bold', bd=3, width=25, textvariable=entername_value)
    entername_entry.place(x=190, y=63)

    entermobile_label = Label(addroot, text='Mobile No.:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12, bg='green', fg='white')
    entermobile_label.place(x=10, y=110)
    ####################Entry boxe of mobile label########################
    entermobile_value = StringVar()
    entermobile_entry = Entry(addroot, font='roman 15 bold', bd=3, width=25, textvariable=entermobile_value)
    entermobile_entry.place(x=190, y=108)

    email_label = Label(addroot, text='Email:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,bg='green', fg='white')
    email_label.place(x=10, y=155)
    ####################Entry boxe of email label########################
    email_value = StringVar()
    email_entry = Entry(addroot, font='roman 15 bold', bd=3, width=25, textvariable=email_value)
    email_entry.place(x=190, y=153)

    address_label = Label(addroot, text='Address:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,bg='green', fg='white')
    address_label.place(x=10, y=200)
    ####################Entry boxe of address label########################
    address_value = StringVar()
    address_entry = Entry(addroot, font='roman 15 bold', bd=3, width=25, textvariable=address_value)
    address_entry.place(x=190, y=198)

    gender_label = Label(addroot, text='Gender:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,bg='green', fg='white')
    gender_label.place(x=10, y=245)
    ####################Entry boxe of gender label########################
    gender_value = StringVar()
    gender_entry = Entry(addroot, font='roman 15 bold', bd=3, width=25, textvariable=gender_value)
    gender_entry.place(x=190, y=243)

    dob_label = Label(addroot, text='Date of Birth:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,bg='green', fg='white')
    dob_label.place(x=10, y=290)
    ####################Entry boxe of dob label########################
    dob_value = StringVar()
    dob_entry = Entry(addroot, font='roman 15 bold', bd=3, width=25, textvariable=dob_value)
    dob_entry.place(x=190, y=288)

    ##########Add buton#

    add_button = Button(addroot, text="Add ",command=add_button_fun ,bd=6, width=18, font="roman 15 bold italic", fg='black',bg='cyan', activebackground='blue', activeforeground='white')
    add_button.place(x=150, y=345)

    addroot.mainloop()


def student_search():
    def search_button_fun():
        pass
    searchroot = Toplevel(master=data_entry_frame)
    searchroot.grab_set()
    searchroot.title("Search student")
    searchroot.geometry('470x470+220+220')
    searchroot.resizable(False, False)
    searchroot.config(bg="grey")
    # addroot.iconbitmap()

    ############## Search student label ########

    s_idlabel = Label(searchroot, text='Enter Id:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                          bg='green', fg='white')
    s_idlabel.place(x=10, y=20)
    ####################Entry boxe of enterid label########################
    s_id_value = StringVar()
    s_id_entry = Entry(searchroot, font='roman 15 bold', bd=3, width=25, textvariable=s_id_value)
    s_id_entry.place(x=190, y=18)

    s_name_label = Label(searchroot, text='Name:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                            bg='green', fg='white')
    s_name_label.place(x=10, y=65)
    ####################Entry boxe of enterid label########################
    s_name_value = StringVar()
    s_name_entry = Entry(searchroot, font='roman 15 bold', bd=3, width=25, textvariable=s_name_value)
    s_name_entry.place(x=190, y=63)

    s_mobile_label = Label(searchroot, text='Mobile No.:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                              bg='green', fg='white')
    s_mobile_label.place(x=10, y=110)
    ####################Entry boxe of mobile label########################
    s_mobile_value=StringVar()
    s_mobile_entry = Entry(searchroot, font='roman 15 bold', bd=3, width=25, textvariable=s_mobile_value)
    s_mobile_entry.place(x=190, y=108)

    s_email_label = Label(searchroot, text='Email:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                        bg='green', fg='white')
    s_email_label.place(x=10, y=155)
    ####################Entry boxe of email label########################
    s_email_value = StringVar()
    s_email_entry = Entry(searchroot, font='roman 15 bold', bd=3, width=25, textvariable=s_email_value)
    s_email_entry.place(x=190, y=153)

    s_address_label = Label(searchroot, text='Address:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                          bg='green', fg='white')
    s_address_label.place(x=10, y=200)
    ####################Entry boxe of address label########################
    s_address_value = StringVar()
    s_address_entry = Entry(searchroot, font='roman 15 bold', bd=3, width=25, textvariable=s_address_value)
    s_address_entry.place(x=190, y=198)

    s_gender_label = Label(searchroot, text='Gender(M/F):', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                         bg='green', fg='white')
    s_gender_label.place(x=10, y=245)
    ####################Entry boxe of gender label########################
    s_gender_value = StringVar()
    s_gender_entry = Entry(searchroot, font='roman 15 bold', bd=3, width=25, textvariable=s_gender_value)
    s_gender_entry.place(x=190, y=243)

    sdob_label = Label(searchroot, text='Date of Birth:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                      bg='green', fg='white')
    sdob_label.place(x=10, y=290)
    ####################Entry boxe of dob label########################
    sdob_value = StringVar()
    sdob_entry = Entry(searchroot, font='roman 15 bold', bd=3, width=25, textvariable=sdob_value)
    sdob_entry.place(x=190, y=288)

    date_label = Label(searchroot, text='Date :', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                       bg='green', fg='white')
    date_label.place(x=10, y=335)
    ####################Entry boxe of dob label########################
    date_value = StringVar()
    date_entry = Entry(searchroot, font='roman 15 bold', bd=3, width=25, textvariable=date_value)
    date_entry.place(x=190, y=333)

    ##########searchbuton#

    search_button = Button(searchroot, text="search", command=search_button_fun, bd=6, width=18, font="roman 15 bold italic", fg='black', bg='cyan', activebackground='blue', activeforeground='white')
    search_button.place(x=150, y=380)



    searchroot.mainloop()

def update_student():
    def update_button_fun():
        pass
    uproot = Toplevel(master=data_entry_frame)
    uproot.grab_set()
    uproot.title("Update student")
    uproot.geometry('470x480+220+220')
    uproot.resizable(False, False)
    uproot.config(bg="grey")
    # addroot.iconbitmap()

    ############## Search student label ########

    updateidlabel = Label(uproot, text='Update Id:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                      bg='green', fg='white')
    updateidlabel.place(x=10, y=20)
    ####################Entry boxe of enterid label########################
    updateid_value = StringVar()
    updateid_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=updateid_value)
    updateid_entry.place(x=190, y=18)

    updatename_label = Label(uproot, text='Change Name:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                         bg='green', fg='white')
    updatename_label.place(x=10, y=65)
    ####################Entry boxe of enterid label########################
    updatename_value = StringVar()
    updatename_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=updatename_value)
    updatename_entry.place(x=190, y=63)

    updatemobile_label: Label = Label(uproot, text='Update Mobile.:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                           bg='green', fg='white')
    updatemobile_label.place(x=10, y=110)
    ####################Entry boxe of mobile label########################
    updatemobile_value = StringVar()
    updatemobile_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=updatemobile_value)
    updatemobile_entry.place(x=190, y=108)

    update_email_label = Label(uproot, text='Update Email:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                          bg='green', fg='white')
    update_email_label.place(x=10, y=155)
    ####################Entry boxe of email label########################
    update_email_value = StringVar()
    update_email_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=update_email_value)
    update_email_entry.place(x=190, y=153)

    up_address_label = Label(uproot, text='Update Address:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                            bg='green', fg='white')
    up_address_label.place(x=10, y=200)
    ####################Entry boxe of address label########################
    up_address_value = StringVar()
    up_address_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=up_address_value)
    up_address_entry.place(x=190, y=198)

    up_gender_label = Label(uproot, text='Gender(M/F):', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                           bg='green', fg='white')
    up_gender_label.place(x=10, y=245)
    ####################Entry boxe of gender label########################
    up_gender_value = StringVar()
    up_gender_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=up_gender_value)
    up_gender_entry.place(x=190, y=243)

    up_dob_label = Label(uproot, text='Update DOB:', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                       bg='green', fg='white')
    up_dob_label.place(x=10, y=290)
    ####################Entry boxe of dob label########################
    up_dob_value = StringVar()
    up_dob_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=up_dob_value)
    up_dob_entry.place(x=190, y=288)

    up_date_label = Label(uproot, text='Update Date :', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                       bg='green', fg='white')
    up_date_label.place(x=10, y=335)
    ####################Entry boxe of date label########################
    up_date_value = StringVar()
    up_date_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=up_date_value)
    up_date_entry.place(x=190, y=333)

    up_time_label = Label(uproot, text='Update Time :', font="times 15 bold", relief=GROOVE, borderwidth=3, width=12,
                          bg='green', fg='white')
    up_time_label.place(x=10, y=380)
    ####################Entry boxe of update time label########################
    up_time_value = StringVar()
    up_time_entry = Entry(uproot, font='roman 15 bold', bd=3, width=25, textvariable=up_time_value)
    up_time_entry.place(x=190, y=378)

    ##########updatebuton#

    update_button = Button(uproot, text="update", command=update_button_fun, bd=6, width=18,
                           font="roman 15 bold italic", fg='black', bg='cyan', activebackground='blue',
                           activeforeground='white')
    update_button.place(x=150, y=420)

    uproot.mainloop()

def delete_student():
    pass

def show():
    pass
def export_data():
    pass

def exit():
    response=messagebox.askyesnocancel('notification','Do you really want to exit?')
    if response==True:
        root.destroy()



#########################Dimension settings and starting of program#################
from tkinter import *
import time
from tkinter import Toplevel, messagebox, Label
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql

root=Tk()
root.title("Student Management System")
root.config(bg='grey')
root.geometry("1174x700+200+50")
root.iconbitmap('C:\\Users\\Dell\\PycharmProjects\\student management\\images\\main_icon.ico')
root.resizable(False,False)
##################Frames##########

data_entry_frame=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
data_entry_frame.place(x=10,y=80,width=250,height=600)
    ############# Data entry Frames labels and Button #####
front_label=Label(data_entry_frame,text="**Welcome Admin!!! ",width=30,font='arial 15 italic',bg='white',fg='red')
front_label.pack(side=TOP,anchor='n',expand=True)

add_student_button=Button(data_entry_frame,text='1.Add Student',command=add_student,font="aerial 12 bold",bd=5,width=21,bg='red',fg='white',activebackground='blue',activeforeground='white')
add_student_button.pack(side=TOP,anchor='n',expand=True)

search_student_button=Button(data_entry_frame,text='2.Search Student',command=student_search,font="aerial 12 bold",bd=5,width=21,bg='red',fg='white',activebackground='blue',activeforeground='white')
search_student_button.pack(side=TOP,anchor='n',expand=True)

delete_student_button=Button(data_entry_frame,text='3.Delete Student',command=delete_student,font="aerial 12 bold",bd=5,width=21,bg='red',fg='white',activebackground='blue',activeforeground='white')
delete_student_button.pack(side=TOP,anchor='n',expand=True)

update_student_button=Button(data_entry_frame,text='4.Update Entry',command=update_student,font="aerial 12 bold",bd=5,width=21,bg='red',fg='white',activebackground='blue',activeforeground='white')
update_student_button.pack(side=TOP,anchor='n',expand=True)

show_all_button=Button(data_entry_frame,text='5.Show All',command=show,font="aerial 12 bold",bd=5,width=21,bg='red',fg='white',activebackground='blue',activeforeground='white')
show_all_button.pack(side=TOP,anchor='n',expand=True)

export_data_button=Button(data_entry_frame,text='6.Export Data',command=export_data,font="aerial 12 bold",bd=5,width=21,bg='red',fg='white',activebackground='blue',activeforeground='white')
export_data_button.pack(side=TOP,anchor='n',expand=True)

exit_button=Button(data_entry_frame,text='7.Exit',command=exit,font="aerial 12 bold",bd=5,width=21,bg='red',fg='white',activebackground='blue',activeforeground='white')
exit_button.pack(side=TOP,anchor='n',expand=True)

################################################################################################################
show_data_frame=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
show_data_frame.place(x=325,y=80,width=830,height=600)
##############show database###########
style=ttk.Style()
style.configure('Treeview.headings',font="aerial 20 bold",fg='blue')
style.configure('Treeview',font="times 15 bold",background='cyan',foreground='black')
scroll_x=Scrollbar(show_data_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(show_data_frame,orient=VERTICAL)
studenttable=Treeview(show_data_frame,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,columns=('Student Id','Name','Mobile NO.','Date of Birth','Gender','Email','Address','Added Date','Added Time'))

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Student Id',text="student Id")
studenttable.heading('Name',text="Name")
studenttable.heading('Mobile NO.',text='Mobile No.')
studenttable.heading('Date of Birth',text="Date Of Birth")
studenttable.heading('Gender',text="Gender")
studenttable.heading('Email',text="Email")
studenttable.heading('Address',text="Address")
studenttable.heading('Added Date',text="Added Date")
studenttable.heading('Added Time',text="Added Time")

studenttable['show']='headings'
studenttable.column('Student Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile NO.',width=200)
studenttable.column('Date of Birth',width=200)
studenttable.column('Gender',width=150)
studenttable.column('Email',width=300)
studenttable.column('Address',width=400)
studenttable.column('Added Date',width=200)
studenttable.column('Added Time',width=200)


studenttable.pack(expand=1,fill=BOTH)






################Labels##########
ss="Graphic Era Student Management System"
count=0
text=''
####################silder label####################
slider_label=Label(root,text=ss,relief=RIDGE,borderwidth=4,font=('chiller',26,'italic bold'),fg='red',bg='cyan',width=35)
slider_label.place(x=330,y=3)
Intro_label()
Into_label_colour()
######clock label######################
clock_label=Label(root,text='Time',relief=RIDGE,borderwidth=4,font=('chiller',15,'bold'),fg='red',bg='lightgreen',width=20)
clock_label.place(x=2,y=3)
Time()

#####################Connect database Button################

connect_button=Button(root,text="Conenct Database",width=20,relief=RIDGE,borderwidth=4,font=('chiller',20,'bold'),fg='red',bg='lightgreen',activebackground='blue',activeforeground='white',command=connect_db)
connect_button.place(x=934,y=3)

root.mainloop()
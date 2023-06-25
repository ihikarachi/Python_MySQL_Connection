from tkinter import *
import my_db_class as db
from tkinter import messagebox
from tkinter import ttk


def MyTextBox(txt):
    t = Entry(
        font=fnt,
        background='skyblue',
        foreground='blue',
        width=25,
    )

    l = Label(
        text = txt,
        font=fnt,
        background='white',
        foreground='black',
        width=12,
        anchor = 'nw'
    )
    return  (t,l)

def get_full_class_name(obj):
    module = obj.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return obj.__class__.__name__
    return module + '.' + obj.__class__.__name__


def saveData():
    try:
        gender = ''
        if  (opt_status.get() == 1):
            gender = 'Male'
        else:
            gender = 'Female'
        str_shift = ''
        if (ch_status1.get()):
            str_shift = 'Morning,'
        if (ch_status2.get()):
            str_shift += 'Evening,'
        if (ch_status3.get()):
            str_shift += 'Night,'
        print(txt1.get(),txt2.get(),txt3.get())
        id = txt1.get()
        en = txt2.get()
        dp = txt3.get()
        sl = txt4.get()
        sql = f"insert into tbl_emp (ID,salary,emp_name,depart,shift,gender) values ({id}, {sl},'{en}', '{dp}','{str_shift}' , '{gender}' )"
        db.MyExecute(sql)
        messagebox.showinfo('CRUD App Message', 'Successfully Save Data')
            # txt2.delete(0,END)
        # txt2.insert(INSERT,'Hello DAta')
    except Exception as e:
    #     print ('Error')
        messagebox.showinfo ('CRUD App Message', e)
win = Tk()
fnt = ('Arial',20)
win.geometry('900x700')
win.title ('It is My GUI Data')
btn = Button (
    text = 'Save Data',
    background = 'yellow',
    foreground = 'blue',
    font = fnt,
    command = saveData
    )
btn.place (x=50 , y = 600)

txt1,lbl1 = MyTextBox('Enter ID')
txt1.place (x=250,y=100)
lbl1.place (x=10,y=100)

txt2,lbl2 = MyTextBox('Enter Name')
txt2.place (x=250,y=150)
lbl2.place (x=10,y=150)

DTx = db.MyRead('Select DPT_Name from tbl_depart')
# print(DTx)
lst = ['Select and Deaprt']
for i in DTx:
    # print (i[0])
    lst.append(i[0])


txt3 = ttk.Combobox(
        value = lst,
        stat = 'readonly',
        font = fnt
        )
txt3.current(0)
#txt3, lbl3 = MyTextBox('Enter Depart')
txt3.place (x=250,y=200)
#lbl3.place (x=10,y=200)

txt4, lbl4 = MyTextBox('Enter Salary')
txt4.place (x=250,y=250)
lbl4.place (x=10,y=250)

ch_status1 = BooleanVar()
ch_status2 = BooleanVar()
ch_status3 = BooleanVar()

chk1 = Checkbutton (text = 'Morning',font = fnt,var = ch_status1)
chk2 = Checkbutton (text = 'Evening',font = fnt,var = ch_status2)
chk3 = Checkbutton (text = 'Night',font = fnt,var = ch_status3)
chk1.place (x=250, y = 300)
chk2.place (x=500, y = 300)
chk3.place (x=750, y = 300)

opt_status = IntVar()
opt1 = Radiobutton (text = 'Male' , value = 1, font = fnt,variable = opt_status)
opt2 = Radiobutton (text = 'Female' ,  value = 2, font = fnt,variable = opt_status)
opt1.place (x=250, y = 350)
opt2.place (x=500, y = 350)


win.mainloop()

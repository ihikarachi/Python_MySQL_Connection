from tkinter import *
import my_db_class as db

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

def saveData():
    print(txt1.get(),txt2.get(),txt3.get())
    id = txt1.get()
    en = txt2.get()
    dp = txt3.get()
    sl = txt4.get()
    sql = f"insert into tbl_emp (ID,salary,emp_name) values ({id}, {sl},'{en}')"
    db.MyExecute(sql)
    # txt2.delete(0,END)
    # txt2.insert(INSERT,'Hello DAta')

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

txt3, lbl3 = MyTextBox('Enter Depart')
txt3.place (x=250,y=200)
lbl3.place (x=10,y=200)

txt4, lbl4 = MyTextBox('Enter Salary')
txt4.place (x=250,y=250)
lbl4.place (x=10,y=250)


win.mainloop()

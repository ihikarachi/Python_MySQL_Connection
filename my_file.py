import my_db_class as iHi

def InsertData():
    id = input('Enter Emp ID: ')
    en = input('Enter Emp Name: ')
    sl = input('Enter Emp Salary: ')
    sql = f"insert into tbl_emp (ID,salary,emp_name) values ({id}, {sl},'{en}')"
    iHi.MyExecute(sql)

def DeleteData():
    print( ' ::: Student Assignment ::: ' )

def UpdateData():
    id = input('Enter Emp ID: ')
    en = input('Enter Emp Name: ')
    sl = input('Enter Emp Salary: ')
    sql = f"Update tbl_emp set emp_name = '{en}' , salary = {sl} where id = {id}"
    iHi.MyExecute(sql)

def ReadData():
    en = input('Enter Emp Name: ')
    DT = iHi.MyRead("Select * From tbl_emp")
    for i in DT:
        print(i)


while (True):
    print('1) Insert')
    print('2) Update')
    print('3) Delete')
    print('4) Find')
    print('5) Exit')
    uin = input('----- ?')
    if (uin == '1'):
        InsertData()
    elif (uin == '2'):
        UpdateData()
    elif (uin == '3'):
        DeleteData()
    elif  (uin == '4'):
        ReadData()
    elif (uin == '5'):
        iHi.MyClose()
        break


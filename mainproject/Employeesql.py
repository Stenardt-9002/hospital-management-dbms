import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = "Additional",
    database = "test123",
)

my_cursor = mydb.cursor()
def getdata(firstna,lastna,emp_id,DOB,Gender,b_id,d_id):
    l_id = []
    my_cursor.execute("SELECT emp_id FROM Employee")
    for i in my_cursor:
        l_id.append(i[0])



    if emp_id in l_id:
        print("Id already in use")
        return -1,l_id


    lb_id = []
    my_cursor.execute("SELECT b_id FROM Branch")
    for i in my_cursor:
        lb_id.append(i[0])

    print(lb_id)
    if b_id not in lb_id:
        print("wrong branch id")
        return -2,lb_id


    ld_id = []
    my_cursor.execute("SELECT dept_id FROM Department")
    for i in my_cursor:
        ld_id.append(i[0])

    print(ld_id)

    if d_id not in ld_id:
        print("wrong Department id")
        return -3, ld_id

    cmd = "INSERT INTO Employee VALUES(%s,%s,%s,%s,%s,%s,%s)"
    record = [(firstna,lastna,emp_id,DOB,Gender,b_id,d_id)]
    my_cursor.executemany(cmd,record)
    mydb.commit()

    return 0,ld_id

# getdata("Jon","snow",4,"1978-3-2",'M',1,1)



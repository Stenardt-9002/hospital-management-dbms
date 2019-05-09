import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = "Additional",
    database = "test123",
)

my_cursor = mydb.cursor()
def getdata(firstna,lastna,p_id,DOB,Gender,b_id,diagnose):
    l_id = []
    my_cursor.execute("SELECT p_id FROM Patient")
    for i in my_cursor:
        l_id.append(i[0])



    if p_id in l_id:
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




    cmd = "INSERT INTO Patient VALUES(%s,%s,%s,%s,%s,%s,%s)"
    record = [(firstna,lastna,p_id,DOB,Gender,diagnose,b_id)]
    my_cursor.executemany(cmd,record)
    mydb.commit()

    return 0,lb_id

# getdata("Jon","snow",4,"1978-3-2",'M',1,1)



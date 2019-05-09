import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = "Additional",
    database = "test123",
)

my_cursor = mydb.cursor()

def getdaat():
    l =[]
    my_cursor.execute("SELECT * FROM Employee")

    name = []
    las_t = []
    emp_id = []
    DOB = []
    Gender = []
    b_id = []
    d_id = []
    emp_id2 = []
    x =  my_cursor.fetchall()
    for o in x:
        # print(o[0])
        name.append(o[0])
        las_t.append(o[1])
        emp_id.append(o[2])
        emp_id2 = []
        for i in emp_id:
            i = (str)(i)
            emp_id2.append(i)
        DOB.append(o[3])
        Gender.append(o[4])
        b_id.append(o[5])
        d_id.append(o[6])



    print(name)
    print(las_t)
    print(emp_id2)
    print(DOB)
    print(Gender)
    print(b_id)
    print(d_id)
    # print(x[0])
    # command = "INSERT INTO Employee VALUES(%s,%s)"
    # record = [(name,id)]
    # my_cursor.executemany(command,record)
    # mydb.commit()
    return name,las_t,emp_id2,Gender,b_id,d_id

def delete(id):
    id1,ane = id.split(",")
    id = id1

    # cmd = "Delete from Employee where emp_id = %s"
    record = [(id)]
    print(id)
    my_cursor.execute("Delete from Employee where emp_id = "+id)
    # my_cursor.executemany(cmd,record)
    mydb.commit()
# getdaat("ritvik",12)
# x = getdaat()
# print(type(x))
# print(x)
# delete('0')
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
    my_cursor.execute("SELECT * FROM Department")

    name = []

    d_id = []

    x =  my_cursor.fetchall()
    for o in x:
        # print(o[0])
        name.append(o[1])

        d_id.append(o[0])

        d_id2 = []
        for i in d_id:
            i = (str)(i)
            d_id2.append(i)




    print(d_id2)
    # print(x[0])
    # command = "INSERT INTO Employee VALUES(%s,%s)"
    # record = [(name,id)]
    # my_cursor.executemany(command,record)
    # mydb.commit()
    return d_id2,name

def delete(id):
    id1,ane = id.split(",")
    id = id1

    # cmd = "Delete from Employee where emp_id = %s"
    record = [(id)]
    print(id)
    my_cursor.execute("Delete from Department where dept_id = "+id)
    # my_cursor.executemany(cmd,record)
    mydb.commit()
# getdaat("ritvik",12)
# x = getdaat()
# print(type(x))
# print(x)
# delete('0')
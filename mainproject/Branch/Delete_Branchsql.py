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
    my_cursor.execute("SELECT * FROM Branch")

    name = []

    id = []
    id2 = []
    x =  my_cursor.fetchall()
    for o in x:
        # print(o[0])
        id.append(o[0])
        name.append(o[1])

        id2 = []
        for i in id:
            i = (str)(i)
            id2.append(i)

    print(name)

    # print(x[0])
    # command = "INSERT INTO Employee VALUES(%s,%s)"
    # record = [(name,id)]
    # my_cursor.executemany(command,record)
    # mydb.commit()
    return id2,name

def delete(id):

    print(id)
    # cmd = "Delete from Employee where emp_id = %s"
    x,y = id.split(",")
    x = (str)(x)
    # y = (str)(y)
    y = "'" + y + "'"


    # x = "'"+x+"'"
    # print(x,end='')
    print(y)
    my_cursor.execute("Delete from Branch where b_id ="+x)
    # my_cursor.executemany(cmd,record)
    mydb.commit()
# getdaat("ritvik",12)
# x = getdaat()
# print(type(x))
# print(x)
# delete(Geeta)
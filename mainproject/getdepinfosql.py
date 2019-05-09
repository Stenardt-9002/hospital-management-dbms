


def getdaat():
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost',
        user="root",
        password="Additional",
        database="test123",
    )
    my_cursor = mydb.cursor()
    l =[]
    my_cursor.execute("SELECT * FROM Department")

    name = []

    d_id = []
    d_id2 = []
    x =  my_cursor.fetchall()
    for o in x:
        # print(o[0])
        name.append(o[1])

        d_id.append(o[0])

        d_id2 = []
        for i in d_id:
            i = (str)(i)
            d_id2.append(i)


    # print(x[0])
    # command = "INSERT INTO Employee VALUES(%s,%s)"
    # record = [(name,id)]
    # my_cursor.executemany(command,record)
    mydb.commit()
    return d_id2,name

def search(name):
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost',
        user="root",
        password="Additional",
        database="test123",
    )
    my_cursor = mydb.cursor()
    l = []
    name = "'"+name+"%'"
    print("WE r here")
    print(name)
    my_cursor.execute("SELECT * FROM Department where dept_name LIKE"+name)

    name = []

    d_id = []
    d_id2 = []
    x = my_cursor.fetchall()
    for o in x:
        # print(o[0])
        name.append(o[1])

        d_id.append(o[0])

        d_id2 = []
        for i in d_id:
            i = (str)(i)
            d_id2.append(i)
    mydb.commit()
    print(d_id2)
    print(name)
    return d_id2, name

# getdaat("ritvik",12)
# x = getdaat()
# print(type(x))
# print(x)
# delete('0')
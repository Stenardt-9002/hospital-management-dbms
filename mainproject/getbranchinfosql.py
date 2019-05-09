
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
    mydb.commit()
    return id2,name

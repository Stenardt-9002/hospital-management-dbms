import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    password="Additional",
    database="test123",
)

my_cursor = mydb.cursor()


def getdaat(id, name):
    l = []
    my_cursor.execute("SELECT b_id FROM Branch")
    # rsult = my_cursor.fetchall()
    # print(rsult[0])
    for i in my_cursor:
        l.append(i[0])
    # print(l)
    # print(" id " );print(id);
    # z = input(" dept sql ")
    try:
        id = (int)(id)


    except:
        pass

    if id in l:
        print("error id not allowed")
        return 1, l


    else:
        command = "INSERT INTO Branch VALUES(%s,%s)"
        record = [(id, name)]
        my_cursor.executemany(command, record)
        mydb.commit()
        return 0, l


# x = getdaat(12,"12")


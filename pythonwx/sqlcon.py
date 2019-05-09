import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = "Additional",
    database = "test123",
)

my_cursor = mydb.cursor()

def getdaat(name,id):
    l =[]
    my_cursor.execute("SELECT id FROM Employee")
    # rsult = my_cursor.fetchall()
    # print(rsult[0])
    for i in my_cursor:
        l.append(i[0])
    print(l)
    if id in l:
        print("error")
        pass
    else:
        command = "INSERT INTO Employee VALUES(%s,%s)"
        record = [(name,id)]
        my_cursor.executemany(command,record)
        mydb.commit()




getdaat("ritvik",12)
# getdaat("ritvik",12)



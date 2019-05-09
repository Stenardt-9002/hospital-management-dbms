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
    my_cursor.execute("SELECT * FROM Patient")

    name = []
    las_t = []
    p_id = []
    DOB = []
    Gender = []
    diagnose = []
    b_id = []
    p_id2 = []
    x =  my_cursor.fetchall()
    for o in x:
        # print(o[0])
        name.append(o[0])
        las_t.append(o[1])
        p_id.append(o[2])
        p_id2 = []
        for i in p_id:
            i = (str)(i)
            p_id2.append(i)
        DOB.append(o[3])
        Gender.append(o[4])
        diagnose.append(o[5])
        b_id.append(o[6])




    print(name)
    print(las_t)
    print(p_id2)
    print(DOB)
    print(Gender)
    print(b_id)
    print(diagnose)
    # print(x[0])
    # command = "INSERT INTO Employee VALUES(%s,%s)"
    # record = [(name,id)]
    # my_cursor.executemany(command,record)
    # mydb.commit()
    return p_id2,name,las_t,Gender,b_id,diagnose


# getdaat("ritvik",12)
# x = getdaat()
# print(type(x))
# print(x)
# delete('0')
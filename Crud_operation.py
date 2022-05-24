import psycopg2
#Define Connection String

conn = psycopg2.connect( host ="localhost",database="Crud_operation", user ="postgres",password ="Postgresql")

cur = conn.cursor()
def getData(sqldbConn):
    print("Read")
    cur=conn.cursor();
    cur.execute("select *from Crud_Operation")
    conn.commit()
    for row in cur:
        print(f'{row}')

getData(conn)

#Read Data
def getData(conn):
    print("Read")
    cur=conn.cursor();
    cur.execute("select *from Crud_Operation")
    for row in cur:
        print(f'{row}')

#insert From Data
def insertData(conn):
    print("Insert")
    cur=conn.cursor();
    cur.execute(
        'insert into Crud_Operation(Product_Name,Cost,Profit,Sales) Values (?,?,?,?)',
         ('M','170000','10000','3'))
    conn.commit()

#update From Data
def updateData(conn):
    print("update")
    cur=conn.cursor();
    cur.execute(
        'update Crud_Operation Set Product_Name =?,cost=? where id=?',
         ('Macbook','170000','3'))
    conn.commit()

#Delete from item
def deleteData(sqldbconn):
    print("delete")
    cur=conn.cursor();
    cur.execute(
        'delete from Crud_Operation where id=?',(1006))
    sqldbconn.commit()

#insertData(conn)
getData(conn)
cur.close()

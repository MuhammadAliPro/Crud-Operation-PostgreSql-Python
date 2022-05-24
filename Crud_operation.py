import pyodbc
#Define Connection String

sqldbconn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-KEQKIQO;DATABASE=Crud_Operation;Trusted_Connection=yes;')

cursor = sqldbconn.cursor()
def getData(sqldbConn):
    print("Read")
    cursor=sqldbConn.cursor();
    cursor.execute("select *from Crud_Operation")
    for row in cursor:
        print(f'{row}')

getData(sqldbconn)

#Read Data
def getData(sqldbconn):
    print("Read")
    cursor=sqldbconn.cursor();
    cursor.execute("select *from Crud_Operation")
    for row in cursor:
        print(f'{row}')

#insert From Data
def insertData(sqldbconn):
    print("Insert")
    cursor=sqldbconn.cursor();
    cursor.execute(
        'insert into Crud_Operation(Product_Name,Cost,Profit,Sales) Values (?,?,?,?)',
         ('MacBook','170000','10000','3'))
    sqldbconn.commit()

#update From Data
def updateData(sqldbconn):
    print("update")
    cursor=sqldbconn.cursor();
    cursor.execute(
        'update Crud_Operation Set Product_Name =?,cost=? where id=?',
         ('Macbook','170000','3'))
    sqldbconn.commit()

#Delete from item
def deleteData(sqldbconn):
    print("delete")
    cursor=sqldbconn.cursor();
    cursor.execute(
        'delete from Crud_Operation where id=?',(1006))
    sqldbconn.commit()

insertData(sqldbconn)
getData(sqldbconn)
 
import sqlite3
conn=sqlite3.connect('example.db')
cursor=conn.cursor()
sql="CREATE TABLE IF NOT EXISTS EMPLOY030(EMPID CHAR(10) PRIMARY KEY,EMPNAME CHAR(20) NOT NULL,DEPTNAME char(20))"
cursor.execute(sql)
print("EMployee table created successfully....")
conn.commit()

print("Database Operation")
print("1.insert into Table")
print("2.Display contents from Table")
print("3.Upadte contents of Table")
print("4.Exit")
while (True):
    ch=int(input("Enetr Your choice:"))
    if(ch==1):
        eid=input("enter empid:")
        ename=input("Enter EMPName:")
        dname=input("Enter DeptName:")
        sql="INSERT INTO EMPLOY030(EMPID,EMPNAME,DEPTNAME)VALUES(?,?,?)"
        vargs=(eid,ename,dname)
        cursor.execute(sql,vargs)
        print("Record inserted Successfully...")
        conn.commit()
    elif(ch==2):
        sql="SELECT * FROM EMPLOY030"
        cursor.execute(sql)
        result=cursor.fetchall()
        print("EMPLOY Tables has")
        for x in result:
            print(x)
    elif(ch==3):
        eid=input("Enter Empid to be upadted:")
        newname=input("Enter updated name:")
        sql="UPDATE EMPLOY030 SET EMPNAME=?WHERE EMPID=?"
        vargs=(newname,eid)
        cursor.execute(sql,vargs)
        print("record updated successfully...")
        conn.commit()
    elif (ch==4):
        conn.close()
        exit()
    else:
        print("Invalid choice")

#导入SQLite驱动
import sqlite3
#连接到SQLite数据库
# conn = sqlite3.connect('test.db')
#
# cursor = conn.cursor()
#
# cursor.execute('Create table user(id varchar(20) primary key,name varchar(20))')
#
# cursor.execute('insert into user(id,name) values (\'1\',\'Michael\')')
#
# print(cursor.rowcount)
#
# cursor.close()
#
# conn.commit()
#
# conn.close()


conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('select * from user where id = ?',('1',))

values = cursor.fetchall()
print(values)

cursor.close()

conn.close()


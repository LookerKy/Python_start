import sqlite3

conn = sqlite3.connect('/Users/ino/Project/python3/python_basic/src/resource/database.db', isolation_level=None)

c = conn.cursor()

c.execute("update users set username =? where id = ?", ('niceman', 2))
conn.commit()

c.execute("update users set username =:name where id =:id", {"name": "goodman", "id": 5})

c.execute("update users set username = '%s' where id ='%s'" % ("badman", 3))

for user in c.execute("select * from users"):
    print(user)

c.execute("delete from users where id =? ", (2,))
c.execute("delete from users where id =:id ", {"id": 5})
c.execute("delete from users where id ='%s' " % 4)

print()

for user in c.execute("select * from users"):
    print(user)


print("users db deleted", conn.execute("delete from users").rowcount)

conn.commit()

conn.close()



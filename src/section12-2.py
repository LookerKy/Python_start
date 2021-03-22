import sqlite3

conn = sqlite3.connect('/Users/ino/Project/python3/python_basic/src/resource/database.db', isolation_level=None)

c = conn.cursor()

c.execute("select * from users")

# 커서 위치변경
# 1개 row 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=3))

# 전체 로우 선택
# print("All-> \n", c.fetchall())
# 커서가 이동하며 다음 데이터 위치를 가져옴 마지막 까지 가면 none이 나옴

# 순회 1
# rows = c.fetchall()
# for row in rows:
#     print("retrieve1 > ", row)

# 순회 2
# for row in c.fetchall():
#     print("retrieve1 > ", row)

# 순회 3
# for row in c.execute('select * from users order by id desc'):
#     print("retrieve1 > ", row)

print()

# Where retrieve1
param1 = (3,)
c.execute('select * from users where id=?', param1)
print('param1 :', c.fetchone())
print('param1 :', c.fetchall())

# Where retrieve2
param2 = (4,)
c.execute('select * from users where id="%s"' % param2)
print('param2 :', c.fetchone())
print('param2 :', c.fetchall())

# Where retrieve3
c.execute('select * from users where id=:Id', {"Id": 5})
print('param3 :', c.fetchone())
print('param3 :', c.fetchall())

# Where retrieve4
param4 = (3, 5)
c.execute("select * from users where id in(?,?)", param4)
print('param4:', c.fetchall())

# Where retrieve5
c.execute("select * from users where id in('%d','%d')" % (3, 4))
print('param5:', c.fetchall())

# Where retrieve6
c.execute("select * from users where id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param6:', c.fetchall())

# Dump 출력
with conn:
    with open('/Users/ino/Project/python3/python_basic/src/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.close(), conn.close()

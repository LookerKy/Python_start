# section12-1
# 파이썬 데이터 베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3 as lite
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print('now Date Time : ', nowDateTime)

print('sqlite.version', lite.version)
print('sqlite.sqite_version :', lite.sqlite_version)

# DB 생성 & Auto Commit <-> Rollback
conn = lite.connect('/Users/ino/Project/python3/python_basic/src/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()

# Table create (Data Type: TEXT, Numeric Integer REAL BLOB)
c.execute("create table if not exists users(id INTEGER PRIMARY KEY, username text, email text,"
          " phone text, website text, regdate text)")

# insert
c.execute("insert into users values(1, 'Lee', 'nagaraz07@gmail.com', '010-7777-9999', "
          "'www.naver.com', ?)", (nowDateTime,))
c.execute("insert into users(id, username, email, phone, website, regdate) values(?,?,?,?,?,?)",
          (2, 'Park', 'Park@naver.com', '010-1111-1111', 'www.naver.com', nowDateTime))

# many 삽입 (튜플, 리스트)
userList = ((3, 'Lee', 'Lee@naver.com', '010-2222-3333', 'Lee.com', nowDateTime),
            (4, 'choi', 'choi@naver.com', '010-2423-5433', 'Choi.com', nowDateTime),
            (5, 'joo', 'joo@naver.com', '010-2324-2342', 'joo.com', nowDateTime),
            )

c.executemany("insert into users(id, username, email, phone, website, regdate) values(?,?,?,?,?,?)", userList)

# 데이터 삭제
# c.execute("delete from users")
# print("users db deleted : ", conn.execute("delete from users").rowcount)

# commit & rollback
# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋)


# conn.rollback()

# 접속해제
conn.close()

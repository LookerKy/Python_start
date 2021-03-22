BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Lee','nagaraz07@gmail.com','010-7777-9999','www.naver.com','2021-03-22 13:57:40');
INSERT INTO "users" VALUES(2,'Park','Park@naver.com','010-1111-1111','www.naver.com','2021-03-22 13:57:40');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-3333','Lee.com','2021-03-22 13:57:40');
INSERT INTO "users" VALUES(4,'choi','choi@naver.com','010-2423-5433','Choi.com','2021-03-22 13:57:40');
INSERT INTO "users" VALUES(5,'joo','joo@naver.com','010-2324-2342','joo.com','2021-03-22 13:57:40');
COMMIT;

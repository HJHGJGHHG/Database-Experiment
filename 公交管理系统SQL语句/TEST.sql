USE ��������ϵͳ;
SELECT * FROM ��Ա��Ϣ;
--DELETE FROM ��Ա��Ϣ;
--SELECT name FROM SysUsers WHERE islogin='1';

/*
DROP LOGIN ��ΰ��;
DROP USER ��ΰ��;
DROP LOGIN ����׿;
DROP USER ����׿;
DROP LOGIN л����;
DROP USER л����;
*/

--SELECT CURRENT_USER;
--ALTER LOGIN л���� WITH PASSWORD=N'29597';
--UPDATE �û���Ϣ SET ����='29597' WHERE �û��� IN (SELECT ���� FROM ��Ա��Ϣ WHERE ����='л����');

--ALTER LOGIN ����׿ WITH PASSWORD=N'71720';
--UPDATE �û���Ϣ SET ����='71720' WHERE �û��� IN (SELECT ���� FROM ��Ա��Ϣ WHERE ����='����׿');


--DELETE  FROM ���ӱ�;
--INSERT INTO ���ӱ� VALUES('M01','10010',3);

/*
INSERT INTO ��Ա��Ϣ VALUES ('10010','л����','Ů',25,'2016-11-04','M01','L01','�ӳ�');
INSERT INTO �û���Ϣ(�û���,����) VALUES('10010','29597');
CREATE LOGIN л���� WITH PASSWORD='29597', DEFAULT_DATABASE=��������ϵͳ;
USE ��������ϵͳ;
CREATE USER л���� FOR LOGIN л���� WITH DEFAULT_SCHEMA=dbo;
EXEC SP_ADDROLEMEMBER 'db_owner', л����;

INSERT INTO ��Ա��Ϣ VALUES ('10011','����׿','��',43,'2019-12-19','M01','L01','·�ӳ�');
INSERT INTO �û���Ϣ(�û���,����) VALUES('10011','71720');
CREATE LOGIN ����׿ WITH PASSWORD='71720', DEFAULT_DATABASE=��������ϵͳ;
USE ��������ϵͳ;
CREATE USER ����׿ FOR LOGIN ����׿ WITH DEFAULT_SCHEMA=dbo;
EXEC SP_ADDROLEMEMBER 'db_owner', ����׿;

INSERT INTO ��Ա��Ϣ VALUES ('10012','��ΰ��','��',33,'2018-3-10','M01','L01','˾��');
INSERT INTO �û���Ϣ(�û���,����) VALUES('10012','99461');
CREATE LOGIN ��ΰ�� WITH PASSWORD='99461', DEFAULT_DATABASE=��������ϵͳ;
USE ��������ϵͳ;
CREATE USER ��ΰ�� FOR LOGIN ��ΰ�� WITH DEFAULT_SCHEMA=dbo;
EXEC SP_ADDROLEMEMBER 'db_owner', ��ΰ��;
*/

--INSERT INTO ��·�� VALUES ('L03','M01');

--INSERT INTO ��·��Ա�� VALUES('10011','L01','·�ӳ�');
--INSERT INTO ��·��Ա�� VALUES('10012','L01','˾��');

--UPDATE ��Ա��Ϣ SET ���Ӻ�='M01';
UPDATE ��Ա��Ϣ SET ��·��='L01',ְλ='·�ӳ�' WHERE ����=10011;

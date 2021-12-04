USE 公交管理系统;

/*
DROP TABLE 违章记录表;
DROP TABLE 线路成员表;
DROP TABLE 线路公交表;
DROP TABLE 用户信息;
DROP TABLE 车队表;
DROP TABLE 线路表;
DROP TABLE 站点表;
DROP TABLE 成员信息;
*/

/*
CREATE TABLE 成员信息(
	工号 CHAR(5),
	姓名 VARCHAR(10) NOT NULL,
	性别 CHAR(2) NOT NULL CHECK (性别 IN ('男','女')),
	年龄 INT NOT NULL CHECK (年龄 >= 18 AND 年龄 <=50),
	入职时间  DATE NOT NULL,
	车队号 VARCHAR(4) NOT NULL,
	线路号 VARCHAR(4),
	职位 VARCHAR(6) NOT NULL CHECK (职位 IN ('司机','路队长','队长')),
	PRIMARY KEY (工号),
	);

CREATE TABLE 用户信息(
	用户名 CHAR(5),
	密码 VARCHAR(8) NOT NULL,
	PRIMARY KEY (用户名),
	FOREIGN KEY (用户名) REFERENCES 成员信息(工号),
);

CREATE TABLE 车队表(
	车队号 VARCHAR(4),
	车队长工号 CHAR(5),
	队员数量 INT NOT NULL,
	PRIMARY KEY (车队号),
	FOREIGN KEY (车队长工号) REFERENCES 成员信息(工号),
	CHECK (车队号 LIKE 'M%'),
);
--ALTER TABLE 成员信息 ADD 	FOREIGN KEY (车队号) REFERENCES 车队表(车队号);

CREATE TABLE 线路表(
	线路号 CHAR(4),
	车队号 VARCHAR(4),
	PRIMARY KEY (线路号),
	--FOREIGN KEY (车队号) REFERENCES 车队表(车队号),
	CHECK (线路号 LIKE 'L%'),
);
--ALTER TABLE 成员信息 ADD FOREIGN KEY (线路号) REFERENCES 线路表(线路号);

CREATE TABLE 站点表(
	站点名 VARCHAR(8),
	线路号 CHAR(4),
	PRIMARY KEY (站点名),
	--FOREIGN KEY (线路号) REFERENCES 线路表(线路号),
);


CREATE TABLE 线路成员表(
	工号 CHAR(5),
	线路号 CHAR(4),
	职位 VARCHAR(6),
	FOREIGN KEY (工号) REFERENCES 成员信息(工号),
	FOREIGN KEY (线路号) REFERENCES 线路表(线路号),
);

CREATE TABLE 线路公交表(
	车牌号 CHAR(5),
	线路号 CHAR(4),
	座位数 INT NOT NULL CHECK (座位数>0),
	品牌 VARCHAR(10) NOT NULL,
	车龄 INT NOT NULL CHECK (车龄>0 AND 车龄<8),
	PRIMARY KEY (车牌号),
	FOREIGN KEY (线路号) REFERENCES 线路表(线路号),
);

CREATE TABLE 违章记录表(
	违章编号 CHAR(5),
	违章者工号 CHAR(5) REFERENCES 成员信息(工号),
	违章内容 VARCHAR(10) NOT NULL,
	所在线路 CHAR(4),
	违章时间 DATE NOT NULL,
	记录人工号 CHAR(5) REFERENCES 成员信息(工号),
	PRIMARY KEY (违章编号),
	FOREIGN KEY (所在线路) REFERENCES 线路表(线路号),
);
*/
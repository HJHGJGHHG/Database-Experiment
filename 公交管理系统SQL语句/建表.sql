USE ��������ϵͳ;

/*
DROP TABLE Υ�¼�¼��;
DROP TABLE ��·��Ա��;
DROP TABLE ��·������;
DROP TABLE �û���Ϣ;
DROP TABLE ���ӱ�;
DROP TABLE ��·��;
DROP TABLE վ���;
DROP TABLE ��Ա��Ϣ;
*/

/*
CREATE TABLE ��Ա��Ϣ(
	���� CHAR(5),
	���� VARCHAR(10) NOT NULL,
	�Ա� CHAR(2) NOT NULL CHECK (�Ա� IN ('��','Ů')),
	���� INT NOT NULL CHECK (���� >= 18 AND ���� <=50),
	��ְʱ��  DATE NOT NULL,
	���Ӻ� VARCHAR(4) NOT NULL,
	��·�� VARCHAR(4),
	ְλ VARCHAR(6) NOT NULL CHECK (ְλ IN ('˾��','·�ӳ�','�ӳ�')),
	PRIMARY KEY (����),
	);

CREATE TABLE �û���Ϣ(
	�û��� CHAR(5),
	���� VARCHAR(8) NOT NULL,
	PRIMARY KEY (�û���),
	FOREIGN KEY (�û���) REFERENCES ��Ա��Ϣ(����),
);

CREATE TABLE ���ӱ�(
	���Ӻ� VARCHAR(4),
	���ӳ����� CHAR(5),
	��Ա���� INT NOT NULL,
	PRIMARY KEY (���Ӻ�),
	FOREIGN KEY (���ӳ�����) REFERENCES ��Ա��Ϣ(����),
	CHECK (���Ӻ� LIKE 'M%'),
);
--ALTER TABLE ��Ա��Ϣ ADD 	FOREIGN KEY (���Ӻ�) REFERENCES ���ӱ�(���Ӻ�);

CREATE TABLE ��·��(
	��·�� CHAR(4),
	���Ӻ� VARCHAR(4),
	PRIMARY KEY (��·��),
	--FOREIGN KEY (���Ӻ�) REFERENCES ���ӱ�(���Ӻ�),
	CHECK (��·�� LIKE 'L%'),
);
--ALTER TABLE ��Ա��Ϣ ADD FOREIGN KEY (��·��) REFERENCES ��·��(��·��);

CREATE TABLE վ���(
	վ���� VARCHAR(8),
	��·�� CHAR(4),
	PRIMARY KEY (վ����),
	--FOREIGN KEY (��·��) REFERENCES ��·��(��·��),
);


CREATE TABLE ��·��Ա��(
	���� CHAR(5),
	��·�� CHAR(4),
	ְλ VARCHAR(6),
	FOREIGN KEY (����) REFERENCES ��Ա��Ϣ(����),
	FOREIGN KEY (��·��) REFERENCES ��·��(��·��),
);

CREATE TABLE ��·������(
	���ƺ� CHAR(5),
	��·�� CHAR(4),
	��λ�� INT NOT NULL CHECK (��λ��>0),
	Ʒ�� VARCHAR(10) NOT NULL,
	���� INT NOT NULL CHECK (����>0 AND ����<8),
	PRIMARY KEY (���ƺ�),
	FOREIGN KEY (��·��) REFERENCES ��·��(��·��),
);

CREATE TABLE Υ�¼�¼��(
	Υ�±�� CHAR(5),
	Υ���߹��� CHAR(5) REFERENCES ��Ա��Ϣ(����),
	Υ������ VARCHAR(10) NOT NULL,
	������· CHAR(4),
	Υ��ʱ�� DATE NOT NULL,
	��¼�˹��� CHAR(5) REFERENCES ��Ա��Ϣ(����),
	PRIMARY KEY (Υ�±��),
	FOREIGN KEY (������·) REFERENCES ��·��(��·��),
);
*/
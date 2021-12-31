import random

if __name__ == '__main__':
    names = []
    with open('中文名.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            name = line[:-1]
            names.append(name)
    position = ['队长', '路队长', '司机']
    for i in range(2):
        print(
            "INSERT INTO 成员信息 VALUES ('100{7}','{0}','男',{1},'{2}-{3}-{4}','M0{5}','{6}');\nINSERT INTO 用户信息(用户名,密码) VALUES('100{7}','{8}');\nCREATE LOGIN {0} WITH PASSWORD='{8}', DEFAULT_DATABASE=公交管理系统;\nUSE 公交管理系统;\nCREATE USER {0} FOR LOGIN {0} WITH DEFAULT_SCHEMA=dbo;\nEXEC SP_ADDROLEMEMBER 'db_owner', {0};\n".format(
                names[random.randint(0, len(names))],
                random.randint(20, 50),
                random.randint(2015, 2021),
                random.randint(1, 12),
                random.randint(1, 30),
                random.randint(1, 1),
                position[random.randint(0, 2)],
                i + 10,
                random.randint(1000, 100000)
            
            ))

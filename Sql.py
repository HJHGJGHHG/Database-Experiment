import pyodbc


def Sql(user, password, sql, isSelect):
    """
    登录并执行一条SQL语句
    :param user: 用户名
    :param password: 密码
    :param sql: SQL语句
    :param isSelect: 是否为查询语句
    :return: 若为查询语句，返回结果
    """
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-38ACSOA2;DATABASE=公交管理系统;UID=' + user + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute(str(sql))
    if isSelect:
        ans = cursor.fetchall()
    cursor.commit()
    cursor.close()
    if isSelect:
        return ans


if __name__ == '__main__':
    sql = 'SELECT * FROM 用户信息'
    print(Sql('谢阳霁', '29597', sql, isSelect='SELECT' in sql))

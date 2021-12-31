import tkinter as tk
from Sql import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from prettytable import PrettyTable


class MyDialog(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 password: str,
                 name: str,
                 position: str,
                 function: int,
                 cnxn_admin,
                 cnxn
                 ):
        """
        :param job_number: 工号
        :param password:密码
        :param name:姓名
        :param position: 职位
        :param function: 功能
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.function = function
        self.name = name
        self.password = password
        
        self.cnxn_admin = cnxn_admin
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        if function == 1:  # 修改密码
            self.title("修改密码")
            self.newp = tk.StringVar()
            self.lab1 = tk.Label(self.frame, text="请输入新密码:", pady=10)
            self.lab1.grid(row=0, column=0)
            self.ent1 = tk.Entry(self.frame, textvariable=self.newp)
            self.ent1.grid(row=0, column=1)
            self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
            self.bo1.grid(row=1, column=0)
            self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
            self.exit.grid(row=1, column=1)
            self.geometry('300x80')
        if function == 2:  # 查看、修改信息
            if self.position == '队长':  # 队长可以查看自己车队所有成员的个人信息
                self.title("查询车队成员信息")
                sql = "SELECT * FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 姓名='" + self.name + "');"
                data = Sql(self.cnxn, sql, isSelect=True)
                self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                          "入职时间", "车队号", "线路号", "职位"])
                self.table.add_rows(data)
                self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
                self.lab1.grid(row=0, column=0)
                self.bo1 = tk.Button(self.frame, text="修改信息", command=self.UpdateInfo)
                self.bo1.grid(row=1, column=0)
                self.exit = tk.Button(self.frame, text="确认", command=self.cancel2)
                self.exit.grid(row=1, column=2)
                self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
                self.bo2.grid(row=1, column=1)
                self.geometry('500x300')
            elif self.position == '路队长':  # 路队长可以看到同一条线路的人员信息
                self.title("查询路线成员信息")
                sql = "SELECT 信息2.* FROM 成员信息 信息1,成员信息 信息2 WHERE 信息1.工号=" + self.job_number + " AND 信息1.车队号=信息2.车队号 AND 信息1.线路号=信息2.线路号;"
                data = Sql(self.cnxn, sql, isSelect=True)
                self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                          "入职时间", "车队号", "线路号", "职位"])
                self.table.add_rows(data)
                self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
                self.lab1.grid(row=0, column=0)
                self.bo1 = tk.Button(self.frame, text="修改信息", command=self.UpdateInfo)
                self.bo1.grid(row=1, column=0)
                self.exit = tk.Button(self.frame, text="确认", command=self.cancel2)
                self.exit.grid(row=1, column=2)
                self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
                self.bo2.grid(row=1, column=1)
                self.geometry('500x300')
            else:  # 司机只能查看自己的信息
                self.title("查询个人信息")
                sql = "SELECT * FROM 成员信息 WHERE 工号=" + self.job_number + ";"
                data = Sql(self.cnxn, sql, isSelect=True)
                self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                          "入职时间", "车队号", "线路号", "职位"])
                self.table.add_rows(data)
                self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
                self.lab1.grid(row=0, column=0)
                self.exit = tk.Button(self.frame, text="确认", command=self.cancel2)
                self.exit.grid(row=1, column=0)
                self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
                self.bo2.grid(row=1, column=1)
                self.geometry('500x300')
        if function == 3:  # 录入信息
            if self.position == '队长':
                self.title("录入车队成员信息")
                self.lab1 = Label(self.frame, text="工号:", pady=10)
                self.lab1.grid(row=0, column=0, sticky=W)
                self.ent1 = Entry(self.frame)
                self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)
                
                self.lab2 = Label(self.frame, text="登录密码:", pady=10)
                self.lab2.grid(row=1, column=0, sticky=W)
                self.ent2 = Entry(self.frame)
                self.ent2.grid(row=1, column=1, columnspan=2, sticky=W)
                
                self.lab3 = Label(self.frame, text="姓名:", pady=10)
                self.lab3.grid(row=2, column=0, sticky=W)
                self.ent3 = Entry(self.frame)
                self.ent3.grid(row=2, column=1, columnspan=2, sticky=W)
                
                self.lab4 = Label(self.frame, text="性别:", pady=10)
                self.lab4.grid(row=3, column=0, sticky=W)
                self.ent4 = Entry(self.frame)
                self.ent4.grid(row=3, column=1, columnspan=2, sticky=W)
                
                self.lab5 = Label(self.frame, text="年龄:", pady=10)
                self.lab5.grid(row=4, column=0, sticky=W)
                self.ent5 = Entry(self.frame)
                self.ent5.grid(row=4, column=1, columnspan=2, sticky=W)
                
                self.lab6 = Label(self.frame, text="入职年份:", pady=10)
                self.lab6.grid(row=5, column=0, sticky=W)
                self.ent6 = Entry(self.frame)
                self.ent6.grid(row=5, column=1, columnspan=2, sticky=W)
                self.lab7 = Label(self.frame, text="入职月份:", pady=10)
                self.lab7.grid(row=6, column=0, sticky=W)
                self.ent7 = Entry(self.frame)
                self.ent7.grid(row=6, column=1, columnspan=2, sticky=W)
                self.lab8 = Label(self.frame, text="入职日期:", pady=10)
                self.lab8.grid(row=7, column=0, sticky=W)
                self.ent8 = Entry(self.frame)
                self.ent8.grid(row=7, column=1, columnspan=2, sticky=W)
                
                self.lab9 = Label(self.frame, text="车队号:", pady=10)
                self.lab9.grid(row=8, column=0, sticky=W)
                self.ent9 = Entry(self.frame)
                self.ent9.grid(row=8, column=1, columnspan=2, sticky=W)
                
                self.lab10 = Label(self.frame, text="线路号:", pady=10)
                self.lab10.grid(row=9, column=0, sticky=W)
                self.ent10 = Entry(self.frame)
                self.ent10.grid(row=9, column=1, columnspan=2, sticky=W)
                
                self.lab11 = Label(self.frame, text="职位:", pady=10)
                self.lab11.grid(row=10, column=0, sticky=W)
                self.ent11 = Entry(self.frame)
                self.ent11.grid(row=10, column=1, columnspan=2, sticky=W)
                
                self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm1)
                self.bo1.grid(row=11, column=0)
                self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
                self.exit.grid(row=11, column=1)
                
                self.geometry('400x500')
            elif self.position == '路队长':
                self.title("录入路线成员信息")
                self.lab1 = Label(self.frame, text="工号:", pady=10)
                self.lab1.grid(row=0, column=0, sticky=W)
                self.ent1 = Entry(self.frame)
                self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)
                
                self.lab2 = Label(self.frame, text="登录密码:", pady=10)
                self.lab2.grid(row=1, column=0, sticky=W)
                self.ent2 = Entry(self.frame)
                self.ent2.grid(row=1, column=1, columnspan=2, sticky=W)
                
                self.lab3 = Label(self.frame, text="姓名:", pady=10)
                self.lab3.grid(row=2, column=0, sticky=W)
                self.ent3 = Entry(self.frame)
                self.ent3.grid(row=2, column=1, columnspan=2, sticky=W)
                
                self.lab4 = Label(self.frame, text="性别:", pady=10)
                self.lab4.grid(row=3, column=0, sticky=W)
                self.ent4 = Entry(self.frame)
                self.ent4.grid(row=3, column=1, columnspan=2, sticky=W)
                
                self.lab5 = Label(self.frame, text="年龄:", pady=10)
                self.lab5.grid(row=4, column=0, sticky=W)
                self.ent5 = Entry(self.frame)
                self.ent5.grid(row=4, column=1, columnspan=2, sticky=W)
                
                self.lab6 = Label(self.frame, text="入职年份:", pady=10)
                self.lab6.grid(row=5, column=0, sticky=W)
                self.ent6 = Entry(self.frame)
                self.ent6.grid(row=5, column=1, columnspan=2, sticky=W)
                self.lab7 = Label(self.frame, text="入职月份:", pady=10)
                self.lab7.grid(row=6, column=0, sticky=W)
                self.ent7 = Entry(self.frame)
                self.ent7.grid(row=6, column=1, columnspan=2, sticky=W)
                self.lab8 = Label(self.frame, text="入职日期:", pady=10)
                self.lab8.grid(row=7, column=0, sticky=W)
                self.ent8 = Entry(self.frame)
                self.ent8.grid(row=7, column=1, columnspan=2, sticky=W)
                
                self.lab9 = Label(self.frame, text="车队号:", pady=10)
                self.lab9.grid(row=8, column=0, sticky=W)
                self.ent9 = Entry(self.frame)
                self.ent9.grid(row=8, column=1, columnspan=2, sticky=W)
                
                self.lab10 = Label(self.frame, text="线路号:", pady=10)
                self.lab10.grid(row=9, column=0, sticky=W)
                self.ent10 = Entry(self.frame)
                self.ent10.grid(row=9, column=1, columnspan=2, sticky=W)
                
                self.lab11 = Label(self.frame, text="职位:", pady=10)
                self.lab11.grid(row=10, column=0, sticky=W)
                self.ent11 = Entry(self.frame)
                self.ent11.grid(row=10, column=1, columnspan=2, sticky=W)
                
                self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm2)
                self.bo1.grid(row=11, column=0)
                self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
                self.exit.grid(row=11, column=1)
                
                self.geometry('400x500')
            else:
                messagebox.showinfo('提示', '操作失败！\n司机无录入信息权限！')
                self.destroy()
    
    def confirm(self):
        new_password = str(self.newp.get())
        if not new_password:
            messagebox.showinfo('提示', '修改失败！\n 新密码不能为空！')
            self.destroy()
        else:
            sql = 'ALTER LOGIN ' + self.name + ' WITH PASSWORD=' + "'" + new_password + "'" + ';'
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "UPDATE 用户信息 SET 密码='" + new_password + "' WHERE 工号 IN (SELECT 工号 FROM 成员信息 WHERE 姓名='" + self.name + "');"
            Sql(self.cnxn, sql, isSelect=False)
            messagebox.showinfo('提示', '修改成功！\n 新密码为：' + new_password)
            self.destroy()
    
    def confirm1(self):
        job_number = self.ent1.get()
        password = self.ent2.get()
        name = self.ent3.get()
        sex = self.ent4.get()
        age = self.ent5.get()
        year = self.ent6.get()
        month = self.ent7.get()
        date = self.ent8.get()
        chedui = self.ent9.get()
        xianlu = self.ent10.get()
        position = self.ent11.get()
        
        # 非空判断
        if job_number == '':
            messagebox.showinfo('提示', '操作失败！\n工号不能为空！')
            self.destroy()
            return
        elif password == '':
            messagebox.showinfo('提示', '操作失败！\n登录密码不能为空！')
            self.destroy()
            return
        elif name == '':
            messagebox.showinfo('提示', '操作失败！\n姓名不能为空！')
            self.destroy()
            return
        elif sex == '':
            messagebox.showinfo('提示', '操作失败！\n性别不能为空！')
            self.destroy()
            return
        elif age == '':
            messagebox.showinfo('提示', '操作失败！\n年龄不能为空！')
            self.destroy()
            return
        elif year == '' or month == '' or date == '':
            messagebox.showinfo('提示', '操作失败！\n入职时间不能为空！')
            self.destroy()
            return
        elif chedui == '':
            messagebox.showinfo('提示', '操作失败！\n车队号不能为空！')
            self.destroy()
            return
        elif position == '':
            messagebox.showinfo('提示', '操作失败！\n职位不能为空！')
            self.destroy()
            return
        
        # 完整性判断
        # 工号不应已存在
        sql = "SELECT 工号 FROM 成员信息;"
        job_numbers = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        if job_number in job_numbers:
            messagebox.showinfo('提示', '操作失败！\n工号已存在！')
            self.destroy()
            return
        # 性别需为 男 或 女
        if sex not in ('男', '女'):
            messagebox.showinfo('提示', '操作失败！\n性别需为男或女！')
            self.destroy()
            return
        # 年龄需在18到50岁之间
        try:
            age = int(age)
        except ValueError:
            messagebox.showinfo('提示', '操作失败！\n请检查年龄是否输入正确！')
            self.destroy()
            return
        if age < 18 or age > 50:
            messagebox.showinfo('提示', '操作失败！\n年龄需在18到50岁之间！')
            self.destroy()
            return
        # 入职时间
        try:
            month = int(month)
            date = int(date)
        except ValueError:
            messagebox.showinfo('提示', '操作失败！\n请检查入职时间是否输入正确！')
            self.destroy()
            return
        if month < 1 or month > 13 or date < 1 or date > 31:
            messagebox.showinfo('提示', '操作失败！\n请检查入职时间是否输入正确！')
            self.destroy()
            return
        ruzhishijian = str(year) + str(month) + str(date)  # 入职时间
        # 只能录入本车队的成员信息
        if chedui[0] != 'M':
            messagebox.showinfo('提示', '操作失败！\n请检查车队号是否输入正确！')
            self.destroy()
            return
        sql = "SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.job_number + ";"
        self.chedui = Sql(self.cnxn, sql, isSelect=True)[0][0]
        if chedui != self.chedui:
            messagebox.showinfo('提示', '操作失败！\n队长只能录入本车队成员的信息！')
            self.destroy()
            return
        # 职位
        if position not in ('队长', '路队长', '司机'):
            messagebox.showinfo('提示', '操作失败！\n请检查职位是否输入正确！')
            self.destroy()
            return
        # 线路号必须在本车队下
        if position != '队长':
            if xianlu[0] != 'L':
                messagebox.showinfo('提示', '操作失败！\n请检查线路号是否输入正确！')
                self.destroy()
                return
            sql = "SELECT 线路号 FROM 线路信息 WHERE 车队号='" + self.chedui + "'; "
            inLine = False
            for line in Sql(self.cnxn, sql, isSelect=True):
                if xianlu in line[0]:
                    inLine = True
                    break
            if not inLine:
                messagebox.showinfo('提示', '操作失败！\n线路号不存在或不在本车队下！')
                self.destroy()
                return
        
        sql = "SELECT * FROM 成员信息 WHERE 车队号='" + chedui + "' AND 职位=N'队长';"
        have_duizhang = True if Sql(self.cnxn, sql, isSelect=True) else False  # 录入人员所在车队是否有队长
        sql = "SELECT * FROM 成员信息 WHERE 线路号='" + xianlu + "' AND 职位=N'路队长';"
        have_luduizhang = True if Sql(self.cnxn, sql, isSelect=True) else False  # 录入人员所在线路是否有路队长
        if position == '队长':
            if have_duizhang:
                messagebox.showinfo('提示', '操作失败！\n所在车队已有队长！')
                self.destroy()
                return
            else:
                sql = "INSERT INTO 成员信息 VALUES ('{0}','{1}','{2}',{3},'{4}','{5}',NULL,'队长');".format(
                    job_number, name, sex, age, ruzhishijian, chedui
                )
                Sql(self.cnxn, sql, isSelect=False)
                sql = "INSERT INTO 用户信息(姓名,工号,密码) VALUES('{0}','{1}','{2}');".format(
                    name, job_number, password
                )
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "CREATE LOGIN {0} WITH PASSWORD='{1}', DEFAULT_DATABASE=公交管理系统;".format(
                    name, password
                )
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "USE 公交管理系统;"
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "CREATE USER {0} FOR LOGIN {0} WITH DEFAULT_SCHEMA=dbo;".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "EXEC SP_ADDROLEMEMBER 'db_datareader', {0};".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "EXEC SP_ADDROLEMEMBER 'db_datawriter', {0};".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                messagebox.showinfo('提示', '操作成功！\n成功录入车队{0}队长{1}相关信息！\n登录密码为{2}。'.format(
                    chedui, name, password
                ))
                self.destroy()
                return
        elif position == '路队长':
            if have_luduizhang:
                messagebox.showinfo('提示', '操作失败！\n所在线路已有路队长！')
                self.destroy()
                return
            else:
                sql = "INSERT INTO 成员信息 VALUES ('{0}','{1}','{2}',{3},'{4}','{5}','{6}','路队长');".format(
                    job_number, name, sex, age, ruzhishijian, chedui, xianlu
                )
                Sql(self.cnxn, sql, isSelect=False)
                sql = "INSERT INTO 用户信息(姓名,工号,密码) VALUES('{0}','{1}','{2}');".format(
                    name, job_number, password
                )
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "CREATE LOGIN {0} WITH PASSWORD='{1}', DEFAULT_DATABASE=公交管理系统;".format(
                    name, password
                )
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "USE 公交管理系统;"
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "CREATE USER {0} FOR LOGIN {0} WITH DEFAULT_SCHEMA=dbo;".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "EXEC SP_ADDROLEMEMBER 'db_datareader', {0};".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "EXEC SP_ADDROLEMEMBER 'db_datawriter', {0};".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                messagebox.showinfo('提示', '操作成功！\n成功录入线路{0}路队长{1}相关信息！\n登录密码为{2}。'.format(
                    xianlu, name, password
                ))
                self.destroy()
        else:  # 录入司机信息
            sql = "INSERT INTO 成员信息 VALUES ('{0}','{1}','{2}',{3},'{4}','{5}','{6}','司机');".format(
                job_number, name, sex, age, ruzhishijian, chedui, xianlu
            )
            Sql(self.cnxn, sql, isSelect=False)
            sql = "INSERT INTO 用户信息(姓名,工号,密码) VALUES('{0}','{1}','{2}');".format(
                name, job_number, password
            )
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "CREATE LOGIN {0} WITH PASSWORD='{1}', DEFAULT_DATABASE=公交管理系统;".format(
                name, password
            )
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "USE 公交管理系统;"
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "CREATE USER {0} FOR LOGIN {0} WITH DEFAULT_SCHEMA=dbo;".format(name)
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "EXEC SP_ADDROLEMEMBER 'db_datareader', {0};".format(name)
            Sql(self.cnxn_admin, sql, isSelect=False)
            messagebox.showinfo('提示', '操作成功！\n成功录入线路{0}司机{1}相关信息！\n登录密码为{2}。'.format(
                xianlu, name, password
            ))
            self.destroy()
    
    def confirm2(self):
        job_number = self.ent1.get()
        password = self.ent2.get()
        name = self.ent3.get()
        sex = self.ent4.get()
        age = self.ent5.get()
        year = self.ent6.get()
        month = self.ent7.get()
        date = self.ent8.get()
        chedui = self.ent9.get()
        xianlu = self.ent10.get()
        position = self.ent11.get()
        
        # 非空判断
        if job_number == '':
            messagebox.showinfo('提示', '操作失败！\n工号不能为空！')
            self.destroy()
            return
        elif password == '':
            messagebox.showinfo('提示', '操作失败！\n登录密码不能为空！')
            self.destroy()
            return
        elif name == '':
            messagebox.showinfo('提示', '操作失败！\n姓名不能为空！')
            self.destroy()
            return
        elif sex == '':
            messagebox.showinfo('提示', '操作失败！\n性别不能为空！')
            self.destroy()
            return
        elif age == '':
            messagebox.showinfo('提示', '操作失败！\n年龄不能为空！')
            self.destroy()
            return
        elif year == '' or month == '' or date == '':
            messagebox.showinfo('提示', '操作失败！\n入职时间不能为空！')
            self.destroy()
            return
        elif chedui == '':
            messagebox.showinfo('提示', '操作失败！\n车队号不能为空！')
            self.destroy()
            return
        elif position == '':
            messagebox.showinfo('提示', '操作失败！\n职位不能为空！')
            self.destroy()
            return
        
        # 完整性判断
        # 工号不应已存在
        sql = "SELECT 工号 FROM 成员信息;"
        job_numbers = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        if job_number in job_numbers:
            messagebox.showinfo('提示', '操作失败！\n工号已存在！')
            self.destroy()
            return
        # 性别需为 男 或 女
        if sex not in ('男', '女'):
            messagebox.showinfo('提示', '操作失败！\n性别需为男或女！')
            self.destroy()
            return
        # 年龄需在18到50岁之间
        try:
            age = int(age)
        except ValueError:
            messagebox.showinfo('提示', '操作失败！\n请检查年龄是否输入正确！')
            self.destroy()
            return
        if age < 18 or age > 50:
            messagebox.showinfo('提示', '操作失败！\n年龄需在18到50岁之间！')
            self.destroy()
            return
        # 入职时间
        try:
            month = int(month)
            date = int(date)
        except ValueError:
            messagebox.showinfo('提示', '操作失败！\n请检查入职时间是否输入正确！')
            self.destroy()
            return
        if month < 1 or month > 13 or date < 1 or date > 31:
            messagebox.showinfo('提示', '操作失败！\n请检查入职时间是否输入正确！')
            self.destroy()
            return
        ruzhishijian = str(year) + str(month) + str(date)  # 入职时间
        # 只能录入本车队的成员信息
        if chedui[0] != 'M':
            messagebox.showinfo('提示', '操作失败！\n请检查车队号是否输入正确！')
            self.destroy()
            return
        sql = "SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.job_number + ";"
        self.chedui = Sql(self.cnxn, sql, isSelect=True)[0][0]
        if chedui != self.chedui:
            messagebox.showinfo('提示', '操作失败！\n路队长只能录入本车队本线路下成员的信息！')
            self.destroy()
            return
        # 职位
        if position not in ('队长', '路队长', '司机'):
            messagebox.showinfo('提示', '操作失败！\n请检查职位是否输入正确！')
            self.destroy()
            return
        # 线路号必须在与路队长管辖线路一致
        if position != '队长':
            if xianlu[0] != 'L':
                messagebox.showinfo('提示', '操作失败！\n请检查线路号是否输入正确！')
                self.destroy()
                return
            sql = "SELECT 线路号 FROM 成员信息 WHERE 工号='" + self.job_number + "'; "
            data = Sql(self.cnxn, sql, isSelect=True)[0][0]
            if xianlu != data:
                messagebox.showinfo('提示', '操作失败！\n线路号不存在或超出路队长管辖范围！')
                self.destroy()
                return
        
        sql = "SELECT * FROM 成员信息 WHERE 车队号='" + chedui + "' AND 职位=N'队长';"
        have_duizhang = True if Sql(self.cnxn, sql, isSelect=True) else False  # 录入人员所在车队是否有队长
        sql = "SELECT * FROM 成员信息 WHERE 线路号='" + xianlu + "' AND 职位=N'路队长';"
        have_luduizhang = True if Sql(self.cnxn, sql, isSelect=True) else False  # 录入人员所在线路是否有路队长
        if position == '队长':
            if have_duizhang:
                messagebox.showinfo('提示', '操作失败！\n所在车队已有队长！')
                self.destroy()
                return
            else:
                sql = "INSERT INTO 成员信息 VALUES ('{0}','{1}','{2}',{3},'{4}','{5}',NULL,'队长');".format(
                    job_number, name, sex, age, ruzhishijian, chedui
                )
                Sql(self.cnxn, sql, isSelect=False)
                sql = "INSERT INTO 用户信息(姓名,工号,密码) VALUES('{0}','{1}','{2}');".format(
                    name, job_number, password
                )
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "CREATE LOGIN {0} WITH PASSWORD='{1}', DEFAULT_DATABASE=公交管理系统;".format(
                    name, password
                )
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "USE 公交管理系统;"
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "CREATE USER {0} FOR LOGIN {0} WITH DEFAULT_SCHEMA=dbo;".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "EXEC SP_ADDROLEMEMBER 'db_datareader', {0};".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                sql = "EXEC SP_ADDROLEMEMBER 'db_datawriter', {0};".format(name)
                Sql(self.cnxn_admin, sql, isSelect=False)
                messagebox.showinfo('提示', '操作成功！\n成功录入车队{0}队长{1}相关信息！\n登录密码为{2}。'.format(
                    chedui, name, password
                ))
                self.destroy()
                return
        elif position == '路队长':
            messagebox.showinfo('提示', '操作失败！\n所在线路已有路队长！')
            self.destroy()
        else:  # 录入司机信息
            sql = "INSERT INTO 成员信息 VALUES ('{0}','{1}','{2}',{3},'{4}','{5}','{6}','司机');".format(
                job_number, name, sex, age, ruzhishijian, chedui, xianlu
            )
            Sql(self.cnxn, sql, isSelect=False)
            sql = "INSERT INTO 用户信息(姓名,工号,密码) VALUES('{0}','{1}','{2}');".format(
                name, job_number, password
            )
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "CREATE LOGIN {0} WITH PASSWORD='{1}', DEFAULT_DATABASE=公交管理系统;".format(
                name, password
            )
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "USE 公交管理系统;"
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "CREATE USER {0} FOR LOGIN {0} WITH DEFAULT_SCHEMA=dbo;".format(name)
            Sql(self.cnxn_admin, sql, isSelect=False)
            sql = "EXEC SP_ADDROLEMEMBER 'db_denydatawriter', {0};".format(name)
            Sql(self.cnxn_admin, sql, isSelect=False)
            messagebox.showinfo('提示', '操作成功！\n成功录入线路{0}司机{1}相关信息！\n登录密码为{2}。'.format(
                xianlu, name, password
            ))
            self.destroy()
    
    def UpdateInfo(self):
        w1 = UpdateInfo(self.cnxn, self.job_number, self.position)
    
    def refresh(self):
        sql = "SELECT 职位 FROM 成员信息 WHERE 工号=" + self.job_number + ";"
        self.position = Sql(self.cnxn, sql, isSelect=True)[0][0]
        if self.position == '队长':  # 仍为队长
            self.title("查询车队成员信息")
            sql = "SELECT * FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 姓名='" + self.name + "');"
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                      "入职时间", "车队号", "线路号", "职位"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=0, column=0)
        elif self.position == '路队长':
            self.title("查询路线成员信息")
            sql = "SELECT 信息2.* FROM 成员信息 信息1,成员信息 信息2 WHERE 信息1.工号=" + self.job_number + " AND 信息1.车队号=信息2.车队号 AND 信息1.线路号=信息2.线路号;"
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                      "入职时间", "车队号", "线路号", "职位"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=0, column=0)
        else:
            self.title("查询个人信息")
            sql = "SELECT * FROM 成员信息 WHERE 工号=" + self.job_number + ";"
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                      "入职时间", "车队号", "线路号", "职位"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=0, column=0)
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def cancel2(self):
        self.destroy()


class UpdateInfo(tk.Toplevel):
    def __init__(self, cnxn, job_number, position):
        super().__init__()
        self.cnxn = cnxn
        self.job_number = job_number  # 修改人工号
        self.position = position  # 修改人职位
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("修改信息")
        self.lab1 = tk.Label(self.frame, text="请输入需要修改信息人员的工号:", pady=10)
        self.lab1.pack(side=TOP, padx=5)
        self.ent1 = tk.Entry(self.frame)
        self.ent1.pack(side=TOP, padx=5)
        self.lab2 = tk.Label(self.frame, text="请选择要修改的列:", pady=10)
        self.lab2.pack(side=TOP, padx=5)
        self.value = StringVar()
        values = ['年龄', '车队号', '线路号', '职位']
        self.value.set('年龄')
        self.combobox = ttk.Combobox(
            master=self.frame,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=5,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            # font=('', 20),  # 字体
            textvariable=self.value,  # 通过StringVar设置可改变的值
            values=values,  # 设置下拉框的选项
        )
        
        self.combobox.pack(side=TOP, padx=5)
        self.lab2 = tk.Label(self.frame, text="请输入修改后的新值:", pady=10)
        self.lab2.pack(side=TOP, padx=5)
        self.ent2 = tk.Entry(self.frame)
        self.ent2.pack(side=TOP, padx=5)
        self.lab2 = tk.Label(self.frame, text="请注意！不要输入引号！正确输入示例：L01", pady=10)
        self.lab2.pack(side=TOP, padx=5)
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.pack(padx=5)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.pack(padx=5)
        
        self.geometry('500x400')
    
    def confirm(self):
        # 使用var.get()来获得目前选项内容
        self.col = self.value.get()  # 需要修改哪一列
        self.update_job_number = self.ent1.get()  # 需要修改信息的人员工号
        self.update_value = self.ent2.get()  # 新值
        if self.update_job_number == '' or self.update_value == '':
            messagebox.showinfo('提示', '操作失败！\n请检查是否填写了所有项并选择了更改列！')
            self.destroy()
        
        # data: 有权限修改的工号集合
        if self.position == '队长':
            sql = "SELECT 工号 FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.job_number + ");"
            data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        elif self.position == '路队长':
            sql = "SELECT 信息1.工号 FROM 成员信息 信息1,成员信息 信息2 WHERE 信息1.工号=" + self.job_number + " AND 信息1.车队号=信息2.车队号 AND 信息1.线路号=信息2.线路号;"
            data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        else:
            data = [self.job_number]
        flag = False
        for item in data:
            if self.update_job_number in item:
                flag = True
                break
        if not flag:
            messagebox.showinfo('提示', '操作失败！\n工号不存在或者超出权限！')
            self.destroy()
        elif self.col == '年龄':
            sql = "UPDATE 成员信息 SET 年龄=" + self.update_value + " WHERE 工号=" + self.update_job_number + ";"
            try:
                Sql(self.cnxn, sql, isSelect=False)
                messagebox.showinfo('提示', '操作成功！')
            except pyodbc.IntegrityError:
                messagebox.showinfo('提示', '操作失败！\n年龄需在18至50之间！')
        elif self.col == '线路号':
            sql = "SELECT 线路号 FROM 线路信息 WHERE 车队号 IN (SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ");"
            inLine = False
            for line in Sql(self.cnxn, sql, isSelect=True):
                if self.update_value in line[0]:
                    inLine = True
                    break
            if not inLine:
                messagebox.showinfo('提示', '操作失败！\n线路号修改只能在同一车队下完成！\n跨车队线路号修改请先修改车队号。')
            else:
                sql = "SELECT 职位 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                position = Sql(self.cnxn, sql, isSelect=True)[0][0]
                if position == '队长':
                    # 更改的人员职位为队长，则变更到新的线路后职位将变为司机，同时提示原车队缺少队长。
                    sql = "SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                    original_motorcade = Sql(self.cnxn, sql, isSelect=True)[0][0]  # 原车队号
                    sql = "UPDATE 成员信息 SET 线路号='" + self.update_value + "',职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                    Sql(self.cnxn, sql, isSelect=False)
                    messagebox.showinfo('提示', '操作成功！\n请注意，变更后职位为司机且原车队{:s}缺少一名队长！'.format(original_motorcade))
                elif position == '司机':
                    sql = "SELECT 线路号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                    original_line = Sql(self.cnxn, sql, isSelect=True)[0][0]  # 原线路号
                    if self.update_value == original_line:
                        messagebox.showinfo('提示', '新线路号与原线路号相同！\n线路号不变！')
                    else:
                        sql = "UPDATE 成员信息 SET 线路号='" + self.update_value + "' WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn, sql, isSelect=False)
                        messagebox.showinfo('提示', '操作成功！')
                else:
                    # 更改的人员职位为路队长，则变更到新的线路后职位将变为司机，同时提示原线路缺少路队长。
                    sql = "SELECT 线路号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                    original_line = Sql(self.cnxn, sql, isSelect=True)[0][0]  # 原线路号
                    if self.update_value == original_line:
                        messagebox.showinfo('提示', '新线路号与原线路号相同！\n线路号不变！')
                    else:
                        sql = "UPDATE 成员信息 SET 线路号='" + self.update_value + "',职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn, sql, isSelect=False)
                        
                        messagebox.showinfo('提示', '操作成功！\n请注意，变更后职位为司机且原线路{:s}缺少一名路队长！'.format(original_line))
        elif self.col == '职位':
            sql = "SELECT 职位 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
            position = Sql(self.cnxn, sql, isSelect=True)[0][0]
            if position == '司机':  # 更改人员现职位为司机，改为路队长、队长：需先判断是否存在路队长或队长
                sql = "SELECT * FROM 成员信息 信息1 WHERE EXISTS (SELECT * FROM 成员信息 信息2 WHERE 信息1.工号=" + self.update_job_number + " AND 信息1.车队号=信息2.车队号 AND 信息2.职位 = N'队长');"
                have_duizhang = True if Sql(self.cnxn, sql, isSelect=True) else False  # 更改人员所在车队是否有队长
                sql = "SELECT 工号 FROM 成员信息 信息1 WHERE EXISTS (SELECT * FROM 成员信息 信息2 WHERE 信息1.工号=" + self.update_job_number + " AND 信息1.线路号=信息2.线路号 AND 信息2.职位 = '路队长');"
                have_luduizhang = True if Sql(self.cnxn, sql, isSelect=True) else False  # 更改人员所在线路是否有路队长
                if self.update_value == '队长':  # 司机改为队长
                    if have_duizhang:
                        messagebox.showinfo('提示', '操作失败！\n目标车队已存在队长！')
                    else:
                        sql = "UPDATE 成员信息 SET 职位=N'队长',线路号=NULL WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn, sql, isSelect=False)
                        messagebox.showinfo('提示', '操作成功！')
                elif self.update_value == '路队长':  # 司机改为路队长
                    if have_luduizhang:
                        messagebox.showinfo('提示', '操作失败！\n目标线路已存在路队长！')
                    else:
                        sql = "UPDATE 成员信息 SET 职位=N'路队长' WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn, sql, isSelect=False)
                        messagebox.showinfo('提示', '操作成功！')
                else:
                    messagebox.showinfo('提示', '操作失败！\n请重新输入！')
            elif position == '路队长':  # 更改人员现职位为路队长，改为司机：可以；改成队长需先判断有无队长
                sql = "SELECT * FROM 成员信息 信息1 WHERE EXISTS (SELECT * FROM 成员信息 信息2 WHERE 信息1.工号=" + self.update_job_number + " AND 信息1.车队号=信息2.车队号 AND 信息2.职位 = N'队长');"
                have_duizhang = True if Sql(self.cnxn, sql, isSelect=True) else False  # 更改人员所在车队是否有队长
                if self.update_value == '司机':  # 路队长改为司机
                    sql = "UPDATE 成员信息 SET 职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                    Sql(self.cnxn, sql, isSelect=False)
                    messagebox.showinfo('提示', '操作成功！')
                elif self.update_value == '队长':  # 路队长改为队长
                    if have_duizhang:
                        messagebox.showinfo('提示', '操作失败！\n目标车队已存在队长！')
                    else:
                        sql = "UPDATE 成员信息 SET 职位=N'队长' WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn, sql, isSelect=False)
                        messagebox.showinfo('提示', '操作成功！')
                else:
                    messagebox.showinfo('提示', '操作失败！\n请重新输入！')
            else:  # 更改人员现职位为队长，无法更改职位，需先指定线路号
                messagebox.showinfo('提示', '操作失败！\n队长请先指定线路号！')
        else:  # 修改车队号
            if self.position == '路队长' or self.position == '司机':
                messagebox.showinfo('提示', '操作失败！\n超出权限！')
            else:  # 仅有队长能修改车队成员车队号
                sql = "SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                original_motorcade = Sql(self.cnxn, sql, isSelect=True)[0][0]  # 原车队号
                if self.update_value == original_motorcade:
                    messagebox.showinfo('提示', '原车队号与新车队号相同！')
                else:
                    sql = "UPDATE 成员信息 SET 车队号='" + self.update_value + "', 线路号=NULL, 职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                    Sql(self.cnxn, sql, isSelect=False)
                    messagebox.showinfo('提示',
                                        '操作成功！\n车队号由{0}改为{1}，职位变为司机！'.format(original_motorcade, self.update_value))
        self.destroy()
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()


class CheckLineInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        队长查看车队下线路信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("查询车队辖下路线信息")
        sql = "SELECT 线路号 FROM 线路信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号='" + self.job_number + "');"
        data = Sql(self.cnxn, sql, isSelect=True)
        self.table = PrettyTable(["线路号"])
        self.table.add_rows(data)
        self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
        self.lab1.grid(row=0, column=0)
        self.bo1 = tk.Button(self.frame, text="删除信息", command=self.DeleteLineInfo)
        self.bo1.grid(row=1, column=0)
        self.bo1 = tk.Button(self.frame, text="录入信息", command=self.InsertLineInfo)
        self.bo1.grid(row=1, column=1)
        self.exit = tk.Button(self.frame, text="确认", command=self.cancel1)
        self.exit.grid(row=1, column=3)
        self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
        self.bo2.grid(row=1, column=2)
        self.geometry('350x200')
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def cancel1(self):
        self.destroy()
    
    def InsertLineInfo(self):
        w1 = InsertLineInfo(self.job_number, self.name, self.position, self.cnxn)
    
    def DeleteLineInfo(self):
        w1 = DeleteLineInfo(self.job_number, self.cnxn)
    
    def refresh(self):
        self.title("查询车队辖下路线信息")
        sql = "SELECT 线路号 FROM 线路信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号='" + self.job_number + "');"
        data = Sql(self.cnxn, sql, isSelect=True)
        self.table = PrettyTable(["线路号"])
        self.table.add_rows(data)
        self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
        self.lab1.grid(row=0, column=0)
        self.bo1 = tk.Button(self.frame, text="删除信息", command=self.DeleteLineInfo)
        self.bo1.grid(row=1, column=0)
        self.bo1 = tk.Button(self.frame, text="录入信息", command=self.InsertLineInfo)
        self.bo1.grid(row=1, column=1)
        self.exit = tk.Button(self.frame, text="确认", command=self.cancel1)
        self.exit.grid(row=1, column=3)
        self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
        self.bo2.grid(row=1, column=2)
        self.geometry('350x200')


class InsertLineInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        队长录入车队下线路信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("录入车队下线路信息")
        self.lab1 = Label(self.frame, text="线路号:", pady=10)
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(self.frame)
        self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)
        
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.grid(row=1, column=0)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.grid(row=1, column=1)
        
        self.geometry('200x100')
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def confirm(self):
        xianlu = self.ent1.get()
        if xianlu == '' or xianlu[0] != 'L':
            messagebox.showinfo('提示', '操作失败！\n请检查线路号是否输入正确！')
            self.destroy()
        else:
            sql = "SELECT 线路号 FROM 线路信息; "
            inLine = False
            for line in Sql(self.cnxn, sql, isSelect=True):
                if xianlu == line[0]:
                    inLine = True
                    break
            
            if inLine:
                messagebox.showinfo('提示', '操作失败！\n线路号已存在！')
                self.destroy()
            else:
                sql = "SELECT 车队号 FROM 成员信息 WHERE 工号={0}".format(self.job_number)
                chedui = Sql(self.cnxn, sql, isSelect=True)[0][0]
                sql = "INSERT INTO 线路信息 VALUES ('{0}','{1}');".format(xianlu, chedui)
                Sql(self.cnxn, sql, isSelect=False)
                messagebox.showinfo('提示', '操作成功！\n成功向车队{0}下添加线路{1}！'.format(chedui, xianlu))
                self.destroy()


class DeleteLineInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 cnxn
                 ):
        """
        队长删除车队下线路信息
        :param job_number: 工号
        """
        super().__init__()
        self.job_number = job_number
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("删除车队下线路信息")
        self.lab1 = Label(self.frame, text="线路号:", pady=10)
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(self.frame)
        self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)
        
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.grid(row=11, column=0)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.grid(row=11, column=1)
        
        self.geometry('200x100')
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def confirm(self):
        xianlu = self.ent1.get()
        sql = "SELECT 线路号 FROM 线路信息; "
        inLine = False
        for line in Sql(self.cnxn, sql, isSelect=True):
            if xianlu == line[0]:
                inLine = True
                break
        
        if not inLine:
            messagebox.showinfo('提示', '操作失败！\n线路号不存在！')
            self.destroy()
        else:
            sql = "SELECT * FROM 成员信息 WHERE 线路号='{0}'".format(xianlu)
            if Sql(self.cnxn, sql, isSelect=True):
                messagebox.showinfo('提示', '操作失败！\n该线路上尚有成员！')
                self.destroy()
            else:
                sql = "DELETE FROM 线路信息 WHERE 线路号='{0}'".format(xianlu)
                Sql(self.cnxn, sql, isSelect=False)
                messagebox.showinfo('提示', '操作成功！\n成功删除线路{0}！'.format(xianlu))
                self.destroy()


class CheckBusInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        查看线路下公交信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        if self.position == '路队长' or self.position == '司机':
            # 路队长可以查看本线路下的公交信息
            self.title("查询线路辖下公交信息")
            sql = "SELECT 线路公交表.* FROM 线路公交表 WHERE 线路公交表.线路号 = (SELECT 线路号 FROM 成员信息 WHERE 工号={0});".format(
                self.job_number)
        else:
            # 队长可以查看车队所有线路下的公交信息
            self.title("查询车队辖下公交信息")
            sql = "SELECT DISTINCT 线路公交表.* FROM 线路公交表, 成员信息 WHERE 线路公交表.线路号=成员信息.线路号 AND 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号={0});".format(
                self.job_number)
        data = Sql(self.cnxn, sql, isSelect=True)
        self.table = PrettyTable(["车牌号", "线路号", "座位号", "品牌", "车龄"])
        self.table.add_rows(data)
        self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
        self.lab1.grid(row=0, column=0)
        self.bo1 = tk.Button(self.frame, text="删除信息", command=self.DeleteBusInfo)
        self.bo1.grid(row=1, column=0)
        self.bo1 = tk.Button(self.frame, text="录入信息", command=self.InsertBusInfo)
        self.bo1.grid(row=1, column=1)
        self.exit = tk.Button(self.frame, text="确认", command=self.cancel1)
        self.exit.grid(row=1, column=3)
        self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
        self.bo2.grid(row=1, column=2)
        self.geometry('400x200')
    
    def refresh(self):
        if self.position == '路队长' or self.position == '司机':
            # 路队长可以查看本线路下的公交信息
            self.title("查询线路辖下公交信息")
            sql = "SELECT 线路公交表.* FROM 线路公交表 WHERE 线路公交表.线路号 = (SELECT 线路号 FROM 成员信息 WHERE 工号={0});".format(
                self.job_number)
        else:
            # 队长可以查看车队所有线路下的公交信息
            self.title("查询车队辖下公交信息")
            sql = "SELECT DISTINCT 线路公交表.* FROM 线路公交表, 成员信息 WHERE 线路公交表.线路号=成员信息.线路号 AND 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号={0});".format(
                self.job_number)
        data = Sql(self.cnxn, sql, isSelect=True)
        self.table = PrettyTable(["车牌号", "线路号", "座位号", "品牌", "车龄"])
        self.table.add_rows(data)
        self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
        self.lab1.grid(row=0, column=0)
        self.bo1 = tk.Button(self.frame, text="删除信息", command=self.DeleteBusInfo)
        self.bo1.grid(row=1, column=0)
        self.bo1 = tk.Button(self.frame, text="录入信息", command=self.InsertBusInfo)
        self.bo1.grid(row=1, column=1)
        self.exit = tk.Button(self.frame, text="确认", command=self.cancel1)
        self.exit.grid(row=1, column=3)
        self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
        self.bo2.grid(row=1, column=2)
        self.geometry('400x200')
    
    def cancel1(self):
        self.destroy()
    
    def InsertBusInfo(self):
        w1 = InsertBusInfo(self.job_number, self.name, self.position, self.cnxn)
    
    def DeleteBusInfo(self):
        w1 = DeleteBusInfo(self.job_number, self.name, self.position, self.cnxn)


class InsertBusInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        录入公交信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("录入公交信息")
        self.lab1 = Label(self.frame, text="车牌号:", pady=10)
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(self.frame)
        self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)
        
        self.lab2 = Label(self.frame, text="线路号:", pady=10)
        self.lab2.grid(row=1, column=0, sticky=W)
        self.ent2 = Entry(self.frame)
        self.ent2.grid(row=1, column=1, columnspan=2, sticky=W)
        
        self.lab3 = Label(self.frame, text="座位数:", pady=10)
        self.lab3.grid(row=2, column=0, sticky=W)
        self.ent3 = Entry(self.frame)
        self.ent3.grid(row=2, column=1, columnspan=2, sticky=W)
        
        self.lab4 = Label(self.frame, text="品牌:", pady=10)
        self.lab4.grid(row=3, column=0, sticky=W)
        self.ent4 = Entry(self.frame)
        self.ent4.grid(row=3, column=1, columnspan=2, sticky=W)
        
        self.lab5 = Label(self.frame, text="车龄:", pady=10)
        self.lab5.grid(row=4, column=0, sticky=W)
        self.ent5 = Entry(self.frame)
        self.ent5.grid(row=4, column=1, columnspan=2, sticky=W)
        
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.grid(row=11, column=0)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.grid(row=11, column=1)
        
        self.geometry('300x250')
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def confirm(self):
        chepai = self.ent1.get()
        xianlu = self.ent2.get()
        zuowei = self.ent3.get()
        pingpai = self.ent4.get()
        cheling = self.ent5.get()
        
        if not chepai:
            messagebox.showinfo('提示', '操作失败！\n车牌不能为空！')
            self.destroy()
            return
        else:
            sql = "SELECT 车牌号 FROM 线路公交表"
            all_chepai = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
            if chepai in all_chepai:
                messagebox.showinfo('提示', '操作失败！\n车牌号已存在！')
                self.destroy()
                return
        
        if not xianlu:
            messagebox.showinfo('提示', '操作失败！\n线路号不能为空！')
            self.destroy()
            return
        else:
            if self.position == '路队长' or self.position == '司机':
                sql = "SELECT 线路号 FROM 成员信息 WHERE 工号={0};".format(self.job_number)
            else:
                sql = "SELECT DISTINCT 线路号 FROM 线路成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号={0});".format(
                    self.job_number)
            all_xianlu = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
            if xianlu not in all_xianlu:
                messagebox.showinfo('提示', '操作失败！\n线路号不存在或超出权限！')
                self.destroy()
                return
        
        if not zuowei:
            messagebox.showinfo('提示', '操作失败！\n座位数不能为空！')
            self.destroy()
            return
        else:
            try:
                zuowei = int(zuowei)
            except ValueError:
                messagebox.showinfo('提示', '操作失败！\n请检查座位数是否输入正确！')
                self.destroy()
                return
            if zuowei < 0:
                messagebox.showinfo('提示', '操作失败！\n座位数不能为负数！')
                self.destroy()
                return
        
        if not pingpai:
            messagebox.showinfo('提示', '操作失败！\n品牌不能为空！')
            self.destroy()
            return
        
        if not cheling:
            messagebox.showinfo('提示', '操作失败！\n车龄不能为空！')
            self.destroy()
            return
        else:
            try:
                cheling = int(cheling)
            except ValueError:
                messagebox.showinfo('提示', '操作失败！\n请检查车龄是否输入正确！')
                self.destroy()
                return
            if cheling < 0 or cheling > 8:
                messagebox.showinfo('提示', '操作失败！\n车龄需在0到8之间！')
                self.destroy()
                return
        
        sql = "INSERT INTO 线路公交表 VALUES ('{0}', '{1}', {2}, '{3}', {4});".format(chepai, xianlu, zuowei, pingpai,
                                                                                 cheling)
        Sql(self.cnxn, sql, isSelect=False)
        messagebox.showinfo('提示', '操作成功！\n成功在线路{0}下添加车牌号为{1}的公交信息！'.format(xianlu, chepai))
        self.destroy()
        return


class DeleteBusInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        删除公交信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("删除公交信息")
        self.lab1 = Label(self.frame, text="车牌号:", pady=10)
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(self.frame)
        self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)

        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.grid(row=11, column=0)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.grid(row=11, column=1)

        self.geometry('200x100')
        
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def confirm(self):
        chepai = self.ent1.get()
        if self.position == '路队长' or self.position == '司机':
            sql = "SELECT 车牌号 FROM 线路公交表 WHERE 线路号 IN (SELECT 线路号 FROM 成员信息 WHERE 工号={0});".format(self.job_number)
        else:
            sql = "SELECT 车牌号 FROM 线路公交表 WHERE 线路号 IN (SELECT DISTINCT 线路号 FROM 线路成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号={0}));".format(self.job_number)
        all_chepai = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        if chepai not in all_chepai:
            messagebox.showinfo('提示', '操作失败！\n车牌号不存在或超出权限！')
            self.destroy()
            return
        else:
            sql = "DELETE FROM 线路公交表 WHERE 车牌号='{0}';".format(chepai)
            Sql(self.cnxn, sql, isSelect=False)
            messagebox.showinfo('提示', '操作成功！\n成功删除车牌号为{0}的公交信息！'.format(chepai))
            self.destroy()
            return
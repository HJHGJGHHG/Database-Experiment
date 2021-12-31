import tkinter as tk
from Sql import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from prettytable import PrettyTable


class AdminUpdatePassword(tk.Toplevel):
    def __init__(self,
                 admin_user_name: str,
                 original_password,
                 cnxn_admin,
                 ):
        """
        :param admin_user_name: 管理员用户名
        """
        super().__init__()
        self.admin_user_name = admin_user_name
        self.original_password = original_password
        self.cnxn_admin = cnxn_admin
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("修改管理员密码")
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
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def confirm(self):
        password = self.ent1.get()
        if password == self.original_password:
            messagebox.showinfo('提示', '操作失败\n新密码与原密码相同！')
            self.destroy()
        else:
            sql = 'ALTER LOGIN sa ' + ' WITH PASSWORD=' + "'" + password + "'" + ';'
            Sql(self.cnxn_admin, sql, isSelect=False)
            messagebox.showinfo('提示', '修改成功！\n 新密码为：' + password)
            self.destroy()


class AdminCheckUserInfo(tk.Toplevel):
    def __init__(self, cnxn_admin):
        super(AdminCheckUserInfo, self).__init__()
        self.cnxn_admin = cnxn_admin
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("查询成员信息")
        sql = "SELECT * FROM 成员信息;"
        data = Sql(self.cnxn_admin, sql, isSelect=True)
        self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                  "入职时间", "车队号", "线路号", "职位"])
        self.table.add_rows(data)
        self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
        self.lab1.grid(row=0, column=0)
        self.bo1 = tk.Button(self.frame, text="修改信息", command=self.AdminUpdateInfo)
        self.bo1.grid(row=1, column=0)
        self.exit = tk.Button(self.frame, text="确认", command=self.cancel2)
        self.exit.grid(row=1, column=2)
        self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
        self.bo2.grid(row=1, column=1)
        self.geometry('500x300')
    
    def AdminUpdateInfo(self):
        w1 = AdminUpdateInfo(self.cnxn_admin)
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def cancel2(self):
        self.destroy()
    
    def refresh(self):
        sql = "SELECT * FROM 成员信息;"
        data = Sql(self.cnxn_admin, sql, isSelect=True)
        self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                  "入职时间", "车队号", "线路号", "职位"])
        self.table.add_rows(data)
        self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
        self.lab1.grid(row=0, column=0)


class AdminUpdateInfo(tk.Toplevel):
    def __init__(self, cnxn_admin):
        super(AdminUpdateInfo, self).__init__()
        self.cnxn_admin = cnxn_admin
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
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def confirm(self):
        # 使用var.get()来获得目前选项内容
        self.col = self.value.get()  # 需要修改哪一列
        self.update_job_number = self.ent1.get()  # 需要修改信息的人员工号
        self.update_value = self.ent2.get()  # 新值
        if self.update_job_number == '' or self.update_value == '':
            messagebox.showinfo('提示', '操作失败！\n请检查是否填写了所有项并选择了更改列！')
            self.destroy()
        
        if self.col == '年龄':
            sql = "UPDATE 成员信息 SET 年龄=" + self.update_value + " WHERE 工号=" + self.update_job_number + ";"
            try:
                Sql(self.cnxn_admin, sql, isSelect=False)
                messagebox.showinfo('提示', '操作成功！')
            except pyodbc.IntegrityError:
                messagebox.showinfo('提示', '操作失败！\n年龄需在18至50之间！')
        elif self.col == '线路号':
            sql = "SELECT 线路号 FROM 线路信息 WHERE 车队号 IN (SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ");"
            inLine = False
            for line in Sql(self.cnxn_admin, sql, isSelect=True):
                if self.update_value in line[0]:
                    inLine = True
                    break
            if not inLine:
                messagebox.showinfo('提示', '操作失败！\n线路号修改只能在同一车队下完成！\n跨车队线路号修改请先修改车队号。')
            else:
                sql = "SELECT 职位 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                position = Sql(self.cnxn_admin, sql, isSelect=True)[0][0]
                if position == '队长':
                    # 更改的人员职位为队长，则变更到新的线路后职位将变为司机，同时提示原车队缺少队长。
                    sql = "SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                    original_motorcade = Sql(self.cnxn_admin, sql, isSelect=True)[0][0]  # 原车队号
                    sql = "UPDATE 成员信息 SET 线路号='" + self.update_value + "',职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                    Sql(self.cnxn_admin, sql, isSelect=False)
                    messagebox.showinfo('提示', '操作成功！\n请注意，变更后职位为司机且原车队{:s}缺少一名队长！'.format(original_motorcade))
                elif position == '司机':
                    sql = "SELECT 线路号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                    original_line = Sql(self.cnxn_admin, sql, isSelect=True)[0][0]  # 原线路号
                    if self.update_value == original_line:
                        messagebox.showinfo('提示', '新线路号与原线路号相同！\n线路号不变！')
                    else:
                        sql = "UPDATE 成员信息 SET 线路号='" + self.update_value + "' WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn_admin, sql, isSelect=False)
                        messagebox.showinfo('提示', '操作成功！')
                else:
                    # 更改的人员职位为路队长，则变更到新的线路后职位将变为司机，同时提示原线路缺少路队长。
                    sql = "SELECT 线路号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                    original_line = Sql(self.cnxn_admin, sql, isSelect=True)[0][0]  # 原线路号
                    if self.update_value == original_line:
                        messagebox.showinfo('提示', '新线路号与原线路号相同！\n线路号不变！')
                    else:
                        sql = "UPDATE 成员信息 SET 线路号='" + self.update_value + "',职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn_admin, sql, isSelect=False)
                        
                        messagebox.showinfo('提示', '操作成功！\n请注意，变更后职位为司机且原线路{:s}缺少一名路队长！'.format(original_line))
        elif self.col == '车队号':
            sql = "SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
            original_motorcade = Sql(self.cnxn_admin, sql, isSelect=True)[0][0]  # 原车队号
            if self.update_value == original_motorcade:
                messagebox.showinfo('提示', '原车队号与新车队号相同！')
            else:
                sql = "UPDATE 成员信息 SET 车队号='" + self.update_value + "', 线路号=NULL, 职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                Sql(self.cnxn_admin, sql, isSelect=False)
                messagebox.showinfo('提示',
                                    '操作成功！\n车队号由{0}改为{1}，职位变为司机！'.format(original_motorcade, self.update_value))
        else:
            # 管理员修改职位
            sql = "SELECT 职位 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
            position = Sql(self.cnxn_admin, sql, isSelect=True)[0][0]
            if position == '司机':  # 更改人员现职位为司机，改为路队长、队长：需先判断是否存在路队长或队长
                sql = "SELECT * FROM 成员信息 信息1 WHERE EXISTS (SELECT * FROM 成员信息 信息2 WHERE 信息1.工号=" + self.update_job_number + " AND 信息1.车队号=信息2.车队号 AND 信息2.职位 = N'队长');"
                have_duizhang = True if Sql(self.cnxn_admin, sql, isSelect=True) else False  # 更改人员所在车队是否有队长
                sql = "SELECT 工号 FROM 成员信息 信息1 WHERE EXISTS (SELECT * FROM 成员信息 信息2 WHERE 信息1.工号=" + self.update_job_number + " AND 信息1.线路号=信息2.线路号 AND 信息2.职位 = '路队长');"
                have_luduizhang = True if Sql(self.cnxn_admin, sql, isSelect=True) else False  # 更改人员所在线路是否有路队长
                if self.update_value == '队长':  # 司机改为队长
                    if have_duizhang:
                        messagebox.showinfo('提示', '操作失败！\n目标车队已存在队长！')
                    else:
                        sql = "UPDATE 成员信息 SET 职位=N'队长',线路号=NULL WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn_admin, sql, isSelect=False)
                        messagebox.showinfo('提示', '操作成功！')
                elif self.update_value == '路队长':  # 司机改为路队长
                    if have_luduizhang:
                        messagebox.showinfo('提示', '操作失败！\n目标线路已存在路队长！')
                    else:
                        sql = "UPDATE 成员信息 SET 职位=N'路队长' WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn_admin, sql, isSelect=False)
                        messagebox.showinfo('提示', '操作成功！')
                else:
                    messagebox.showinfo('提示', '操作失败！\n请重新输入！')
            elif position == '路队长':  # 更改人员现职位为路队长，改为司机：可以；改成队长需先判断有无队长
                sql = "SELECT * FROM 成员信息 信息1 WHERE EXISTS (SELECT * FROM 成员信息 信息2 WHERE 信息1.工号=" + self.update_job_number + " AND 信息1.车队号=信息2.车队号 AND 信息2.职位 = N'队长');"
                have_duizhang = True if Sql(self.cnxn_admin, sql, isSelect=True) else False  # 更改人员所在车队是否有队长
                if self.update_value == '司机':  # 路队长改为司机
                    sql = "UPDATE 成员信息 SET 职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                    Sql(self.cnxn_admin, sql, isSelect=False)
                    messagebox.showinfo('提示', '操作成功！')
                elif self.update_value == '队长':  # 路队长改为队长
                    if have_duizhang:
                        messagebox.showinfo('提示', '操作失败！\n目标车队已存在队长！')
                    else:
                        sql = "UPDATE 成员信息 SET 职位=N'队长' WHERE 工号=" + self.update_job_number + ";"
                        Sql(self.cnxn_admin, sql, isSelect=False)
                        messagebox.showinfo('提示', '操作成功！')
                else:
                    messagebox.showinfo('提示', '操作失败！\n请重新输入！')
            else:  # 更改人员现职位为队长，无法更改职位，需先指定线路号
                messagebox.showinfo('提示', '操作失败！\n队长请先指定线路号！')

        self.destroy()

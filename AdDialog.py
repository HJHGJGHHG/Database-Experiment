import tkinter as tk


class AdDialog(tk.Toplevel):
    def __init__(self,
                 job_number,
                 password,
                 name,
                 position,
                 function):
        """
        :param job_number: 工号
        :param position: 职位
        :param function: 功能
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.function = function
        self.name = name
        self.password = password
        frame = tk.Frame(self)
        frame.pack()
        self.title("信息更改")

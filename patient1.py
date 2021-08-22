# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 11:11:38 2021

@author: Cheng
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:58:24 2021

@author: 417-02
"""
from tkinter import messagebox
import pickle
import tkutils as tku
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import ai2
import os
from datetime import datetime
class patient:
    def __init__(self, parent):
        self.window1 = tk.Toplevel()
        self.initializeUI()
        self.body()
        self.window1.grab_set()
	# 绘制窗体组件
    def initializeUI(self):
        #self.window.iconbitmap("./resource/icon/hunter.ico")
        self.window1.title('心电智能诊断平台登录')
        background_color="#9999FF"
        self.window1.configure(bg=background_color)
        #self.window.overrideredirect(True)
        

        ft = tkFont.Font(family='微软雅黑', size=20, weight=tkFont.BOLD)
        tk.Label(self.window1, text="医生登录助手",font=ft, fg="black",bg=background_color).place(x=100,y=50)
        self.file_path = R"E:\cpsc2019cai\example\infor1.txt"
        self.user_list = [] #用户存储读取文件中所有的元素
        self.misspasswd_counter = 0 #记录password错误的次数
        self.input_user = "" #记录当前用户
        self.input_password = "" #记录当前用户密码
        self.current_login_list = [] #存储登录的账号和密码

        #自动执行文件中文件的加载
        self.load_localfile_info()        
        #photo = tk.PhotoImage(file="images\\2.gif")
        #label = tk.Label(image=photo)
        #label.image =photo
        #label.place(x=0,y=90)	
    def body(self):    
        #self.img = ImageTk.PhotoImage(file="images\\2.gif")
        #canvas = tk.Canvas(self.window, width=720, height=420)
        #canvas.create_image(300, 200, image=self.img)
        #canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        entryBackGroundColor="#F3F3F4"
        background_color="#9999FF"
        userNameFont = tkFont.Font(family='Fixdsys', size=12)
        tk.Label(self.window1, text='请输入用户名:',font=userNameFont, bg=background_color).place(x=20, y=150)
        userName = tk.StringVar()
        tk.Entry(self.window1, highlightthickness=1,bg=entryBackGroundColor,textvariable =userName).place(x=20, y=180,width=320, height=30)
        passWordFont = tkFont.Font(family='Fixdsys', size=12)
        passWord = tk.StringVar() #
        tk.Label(self.window1, text='请输入密码:',font=passWordFont, bg=background_color).place(x=20, y=220)
        tk.Entry(self.window1, highlightthickness=1, bg=entryBackGroundColor,textvariable =passWord, show='*').place(x=20, y=250,width=320, height=30)
#        remeberMeFont=tkFont.Font(family='Fixdsys', size=12)
#        tk.Checkbutton(self.window1, text="记住我",fg="#0081FF",variable="0",font=remeberMeFont, bg=background_color).place(x=20, y=300)
        tk.Button(self.window1, text='立即登录', font=('Fixdsys', 14, 'bold'), width=29,fg='white',bg="#0081FF",command=lambda :self.login1(userName,passWord)).place(x=20, y=330)

        regester_info=tkFont.Font(family='Fixdsys', size=10)
#        tk.Label(self.window1, text='还没有账号？', font=regester_info, bg=background_color).place(x=102,y=375)
#        tk.Button(self.window1, text='立即注册', font=regester_info, bg=background_color,fg="#FFA500",command=lambda :self.usr_sign_up()).place(x=185,y=375)
        #zhu.place(x=185,y=375)        
        w = 370
        h = 480
        sw = self.window1.winfo_screenwidth()
        # 得到屏幕宽度
        sh = self.window1.winfo_screenheight()
        # 得到屏幕高度
        # 窗口宽高为100
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.window1.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window1.mainloop()
        pass

    def load_localfile_info(self):
        """
        加载本地文件:
            通过readline()方法一次读取一行的方式进行读取(避免日后文件过大一次性读取的弊端)
        :return:
        """
        if not os.path.exists(self.file_path):
            messagebox.showinfo("系统提示","文件不存在.请确认后重新加载!!")
        else:
            try:
                with open(self.file_path,mode = "r") as fd:
                    current_list = fd.readline() #一次读一行
                    while current_list: #表示直到current_list中所有元素被读完，循环结束
                        temp_list = current_list.split(",")     #按照逗号把每个list中的元素分割出来
                        self.user_list.append(temp_list)    #把分割后的每个元素重新添加到user_list列表中
                        current_list = fd.readline()    #因为我们一次只读一行。读完后如果不加这一句那么循环会一直只读第一行。

            except:
                messagebox.showinfo("系统信息","文件读取出现异常.请联系管理员！！")

    def write_file(self):
        """
        写入文件":1.分2次写入第一次先清空原文件，第2次再逐一写入
                 2. 写入的是用户登录后反应的最新的状态信息
        :return:
        """
        try:
            #[1] 先清空原文件（不放心可以先备份原文件再执行代码,不然数据会丢失）
            with open(self.file_path,mode="w") as fd:
                fd.write("") #不写任何东西代表清空

            #[2] 再逐一把user_list中的数据写入到文件."a"代表追加写入
            with open(self.file_path,mode = "a") as fd:
                for item in self.user_list:
                    fd.write(",".join(item)) #通过.join()方法指定写入时按照什么进行分割写入文件。这里指定的是按照逗号分割写入
        except:
            messagebox.showinfo("系统信息","写入数据失败.")
                
    def login(self,userName,passWord):
        errMessage=""
        if len(userName.get())==0:
            errMessage=errMessage+"用户名不能为空！\r"
        if len(passWord.get())==0:
            errMessage=errMessage+"密码不能为空！"
        if errMessage!="":
            messagebox.showinfo('提示', errMessage)
        print(passWord.get())
        pass
    def get_login_time(self):
        """
        实现用户登录后自动加载登录时间功能
            #通过import datetime这个模块中datetime.today()方法来实现.当然也可以通过其他方法实现比如时间元祖等
        :return:
        """
        today = datetime.today()
        return ("%04d/%02d/%02d %02d:%02d:%02d" % (
        today.year, today.month, today.day, today.hour, today.minute, today.second))
    def login1(self,userName,passWord):
        """
        用户身份验证功能的实现
            1. 获取到文件中的用户名，密码,状态(是否被锁定)
            2. 判断用户是否被锁定及是否是规定用户以外的非法用户登录(如果是拒绝登录)
            3. 用户正确判断密码是否匹配，密码不匹配3次被锁定并写入到文件
        :return:
        """
        # 获取输入的用户名及密码
        self.input_user = userName.get()
        self.input_password = passWord.get()
        #showinfo("提示信息","用户名：" + input_user + "\n" + "密码：" + input_password)

        #实现身份验证
        for index in range(len(self.user_list)): #这里的user_list 为之前从文件中读取重新存入list列表中的数据
            #先判断用户名是否存在
            if self.input_user.strip().lower() == str(self.user_list[index][0]).strip().lower():
                #如果用户名存在,再判断用户名是否被锁定。1为锁定,0为active.
                if "1" in str(self.user_list[index][2]):
                    messagebox.showinfo("系统提示", "该用户被锁定.请联系管理员解锁后再登录。")
                    break
                else:
                    #如果用户存在并且是active的状态再判断密码是否正确
                    if self.input_password != str(self.user_list[index][1]):
                        self.misspasswd_counter +=1 #初始值设置为0.如果上述条件不成立则循环加1次
                        if self.misspasswd_counter >=3: #设置密码错误次数最大不能超过3次
                            messagebox.showinfo("系统提示","密码输入错误3次账号被锁定！")

                            #改变锁定账户的状态(如果错误3次则改变文件中账户的状态把第3个元素变为1代表用户被锁定)
                            self.user_list[index][2] = "1\n" #这里需要加一个空格

                            #写入文件
                            self.write_file()  #调用下列write_file()方法
                        else:
                            messagebox.showinfo("系统提示", "密码错误，请重新输入")

                        break

                    else:
                        self.misspasswd_counter = 0 #如果输入的password正确那么这里的错误次数还是为0
                        self.current_login_list = self.user_list[index]
                        #用户密码输入都正确则加载主窗体()
                        tk.messagebox.showinfo(title='welcome',message='欢迎您：' + self.input_user)
                        self.window1.destroy()
                #Window(self.window)
                        ai2.Window2(self.window1,self.input_user,self.get_login_time(),self.current_login_list)                       
                        break
            #这句话的意思是：循环到最后如果没有找到相同的用户名则用户判定为不存在！！！(这句话为重点,也是因为这句话才循环时用索引)
            if index == len(self.user_list)-1:
                messagebox.showinfo("系统提示","输入的用户名不存在！")
    def usr_log_in(self,userName,passWord):
        # 输入框获取用户名密码
        usr_name = userName.get()
        usr_pwd = passWord.get()
        # 从本地字典获取用户信息，如果没有则新建本地数据库
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
        # 判断用户名和密码是否匹配
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tk.messagebox.showinfo(title='welcome',message='欢迎您：' + usr_name)
                self.window1.destroy()
                #Window(self.window)
                ai2.Window2(self.window1,usr_name,self.get_login_time())                
                #self.window.destroy()
            else:
                tk.messagebox.showerror(message='密码错误')
        # 用户名密码不能为空
        elif usr_name == '' or usr_pwd == '':
            tk.messagebox.showerror(message='用户名或密码为空')
        # 不在数据库中弹出是否注册的框
        else:
            is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
            if is_signup:
                self.usr_sign_up()
        
    
    # 注册函数
    def usr_sign_up(self):
        # 确认注册时的相应函数
        def signtowcg():
            # 获取输入框内的内容
            nn = new_name.get()
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
    
            # 本地加载已有用户信息,如果没有则已有用户信息为空
            try:
                with open('usr_info.pickle', 'rb') as usr_file:
                    exist_usr_info = pickle.load(usr_file)
            except FileNotFoundError:
                exist_usr_info = {}
    
                # 检查用户名存在、密码为空、密码前后不一致
            if nn in exist_usr_info:
                tk.messagebox.showerror('错误', '用户名已存在')
            elif np == '' or nn == '':
                tk.messagebox.showerror('错误', '用户名或密码为空')
            elif np != npf:
                tk.messagebox.showerror('错误', '密码前后不一致')
            # 注册信息没有问题则将用户名密码写入数据库
            else:
                exist_usr_info[nn] = np
                with open('usr_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo('欢迎', '注册成功')
                # 注册成功关闭注册框
                window_sign_up.destroy()
        
        
        # 新建注册界面
        #ft = tkFont.Font(family='Fixdsys', size=16, weight=tkFont.BOLD)
        window_sign_up = tk.Toplevel(self.window1)
        window_sign_up.geometry('350x200')
        tku.center_window(window_sign_up)
        window_sign_up.title('注册')
        # 用户名变量及标签、输入框
        new_name = tk.StringVar()
        tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
        tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
        # 密码变量及标签、输入框
        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
        tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
        # 重复密码变量及标签、输入框
        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
        tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
        # 确认注册按钮及位置
        bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',
                                       command=signtowcg)
        bt_confirm_sign_up.place(x=150, y=130)
        
    # 退出的函数
    def usr_sign_quit(self):
        self.window1.destroy()
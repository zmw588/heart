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
from datetime import datetime
class Window1:
    def __init__(self, parent):
        self.window1 = tk.Toplevel()
        self.initializeUI()
        self.body()
        self.window1.grab_set()        
#        self.window1.grab_set()
	# 绘制窗体组件
    def initializeUI(self):
        #self.window.iconbitmap("./resource/icon/hunter.ico")
        self.window1.title('心电智能诊断平台登录')
        background_color="#CCFFFF"
        self.window1.configure(bg=background_color)
        #self.window.overrideredirect(True)
        

        ft = tkFont.Font(family='微软雅黑', size=20, weight=tkFont.BOLD)
        tk.Label(self.window1, text="登录助手",font=ft, fg="black",bg=background_color).place(x=130,y=50)
        
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
        background_color="#CCFFFF"
        userNameFont = tkFont.Font(family='Fixdsys', size=12)
        tk.Label(self.window1, text='请输入用户名:',font=userNameFont, bg=background_color).place(x=20, y=150)
        userName = tk.StringVar()
        tk.Entry(self.window1, highlightthickness=1,bg=entryBackGroundColor,textvariable =userName).place(x=20, y=180,width=320, height=30)
        passWordFont = tkFont.Font(family='Fixdsys', size=12)
        passWord = tk.StringVar() #
        tk.Label(self.window1, text='请输入密码:',font=passWordFont, bg=background_color).place(x=20, y=220)
        tk.Entry(self.window1, highlightthickness=1, bg=entryBackGroundColor,textvariable =passWord, show='*').place(x=20, y=250,width=320, height=30)
        remeberMeFont=tkFont.Font(family='Fixdsys', size=12)
        tk.Checkbutton(self.window1, text="记住我",fg="#0081FF",variable="0",font=remeberMeFont, bg=background_color).place(x=20, y=300)
        tk.Button(self.window1, text='立即登录', font=('Fixdsys', 14, 'bold'), width=29,fg='white',bg="#0081FF",command=lambda :self.usr_log_in(userName,passWord)).place(x=20, y=330)

        regester_info=tkFont.Font(family='Fixdsys', size=10)
        tk.Label(self.window1, text='还没有账号？', font=regester_info, bg=background_color).place(x=102,y=375)
        tk.Button(self.window1, text='立即注册', font=regester_info, bg=background_color,fg="#FFA500",command=lambda :self.usr_sign_up()).place(x=185,y=375)
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
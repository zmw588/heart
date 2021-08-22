# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:17:38 2021

@author: 417-02
"""


from tkinter import messagebox
import pickle
import tkutils as tku
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
#import login2 as log 
import turtle
def center_window(win, width=None, height=None):
	""" 将窗口屏幕居中 """
	screenwidth = win.winfo_screenwidth()
	screenheight = win.winfo_screenheight()
	if width is None:
		width, height = get_window_size(win)[:2]
	size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/3)
	win.geometry(size)


def get_window_size(win, update=True):
	""" 获得窗体的尺寸 """
	if update:
		win.update()
	return win.winfo_width(), win.winfo_height(), win.winfo_x(), win.winfo_y()


def tkimg_resized(img, w_box, h_box, keep_ratio=True):
	"""对图片进行按比例缩放处理"""
	w, h = img.size

	if keep_ratio:
		if w > h:
			width = w_box
			height = int(h_box * (1.0 * h / w))

		if h >= w:
			height = h_box
			width = int(w_box * (1.0 * w / h))
	else:
		width = w_box
		height = h_box

	img1 = img.resize((width, height), Image.ANTIALIAS)
	tkimg = ImageTk.PhotoImage(img1)
	return tkimg


def image_label(frame, img, width, height, keep_ratio=True):
	"""输入图片信息，及尺寸，返回界面组件"""
	if isinstance(img, str):
		_img = Image.open(img)
	else:
		_img = img
	lbl_image = tk.Label(frame, width=width, height=height)

	tk_img = tkimg_resized(_img, width, height, keep_ratio)
	lbl_image.image = tk_img
	lbl_image.config(image=tk_img)
	return lbl_image


def _font(fname="微软雅黑", size=12, bold=tkFont.NORMAL):
	"""设置字体"""
	ft = tkFont.Font(family=fname, size=size, weight=bold)
	return ft


def _ft(size=12, bold=False):
	"""极简字体设置函数"""
	if bold:
		return _font(size=size, bold=tkFont.BOLD)
	else:
		return _font(size=size, bold=tkFont.NORMAL)


def h_seperator(parent, height=2):  # height 单位为像素值
	"""水平分割线, 水平填充 """
	tk.Frame(parent, height=height, bg="whitesmoke").pack(fill=tk.X)


def v_seperator(parent, width, bg="whitesmoke"):  # width 单位为像素值
	"""垂直分割线 , fill=tk.Y, 但如何定位不确定，直接返回对象，由容器决定 """
	frame = tk.Frame(parent, width=width, bg=bg)
	return frame

class Window1:
    def __init__(self):
        self.window = tk.Tk()
        self.initializeUI()
        self.body()
	# 绘制窗体组件
    def initializeUI(self):
        #self.window.iconbitmap("./resource/icon/hunter.ico")
        self.window.title('心电智能诊断平台登录')
        background_color="#CCFFFF"
        self.window.configure(bg=background_color)
        #self.window.overrideredirect(True)
        

        ft = tkFont.Font(family='微软雅黑', size=20, weight=tkFont.BOLD)
        tk.Label(self.window, text="登录助手",font=ft, fg="black",bg=background_color).place(x=130,y=50)
        
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
        tk.Label(self.window, text='请输入用户名:',font=userNameFont, bg=background_color).place(x=20, y=150)
        userName = tk.StringVar()
        tk.Entry(self.window, highlightthickness=1,bg=entryBackGroundColor,textvariable =userName).place(x=20, y=180,width=320, height=30)
        passWordFont = tkFont.Font(family='Fixdsys', size=12)
        passWord = tk.StringVar() #
        tk.Label(self.window, text='请输入密码:',font=passWordFont, bg=background_color).place(x=20, y=220)
        tk.Entry(self.window, highlightthickness=1, bg=entryBackGroundColor,textvariable =passWord, show='*').place(x=20, y=250,width=320, height=30)
        remeberMeFont=tkFont.Font(family='Fixdsys', size=12)
        tk.Checkbutton(self.window, text="记住我",fg="#0081FF",variable="0",font=remeberMeFont, bg=background_color).place(x=20, y=300)
        tk.Button(self.window, text='立即登录', font=('Fixdsys', 14, 'bold'), width=29,fg='white',bg="#0081FF",command=lambda :self.usr_log_in(userName,passWord)).place(x=20, y=330)

        regester_info=tkFont.Font(family='Fixdsys', size=10)
        tk.Label(self.window, text='还没有账号？', font=regester_info, bg=background_color).place(x=102,y=375)
        tk.Button(self.window, text='立即注册', font=regester_info, bg=background_color,fg="#FFA500",command=lambda :self.usr_sign_up()).place(x=185,y=375)
        #zhu.place(x=185,y=375)        
        w = 370
        h = 480
        sw = self.window.winfo_screenwidth()
        # 得到屏幕宽度
        sh = self.window.winfo_screenheight()
        # 得到屏幕高度
        # 窗口宽高为100
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.mainloop()
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
                self.window.destroy()
                Window(self.window)
                
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
        window_sign_up = tk.Toplevel(self.window)
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
        self.window.destroy()
    

class Window():
	def __init__(self, parent):
		self.root = tk.Toplevel()
		self.parent = parent
		self.root.geometry("%dx%d" % (1200, 800))  # 窗体尺寸
		center_window(self.root)                   # 将窗体移动到屏幕中央
		self.root.title("诊断系统")                 # 窗体标题
		self.root.iconbitmap("images\\Money.ico")  # 窗体图标
		self.root.grab_set()
		self.body()      # 绘制窗体组件

	# 绘制窗体组件
	def body(self):
		self.title(self.root).pack(fill=tk.X)

		self.main(self.root).pack(expand=tk.YES, fill=tk.BOTH)

		self.bottom(self.root).pack(fill=tk.X)

	def title(self, parent):
		""" 标题栏 """

		def label(frame, text, size, bold=False):
			return tk.Label(frame, text=text, bg="black", fg="white", height=2, font=_ft(size, bold))

		frame = tk.Frame(parent, bg="black")

		label(frame, "人工智能三级诊断平台", 16, True).pack(side=tk.LEFT, padx=10)
		#label(frame, "一级诊断", 12).pack(side=tk.LEFT, padx=100)
		#label(frame, "二级诊断", 12).pack(side=tk.LEFT, padx=0)
		#label(frame, "三级诊断", 12).pack(side=tk.LEFT, padx=100)
		label(frame, "", 12).pack(side=tk.RIGHT, padx=20)
		label(frame, "欢迎您", 12).pack(side=tk.RIGHT, padx=20)
		#ttk.Button(frame, text="登录用户", width=12,  command=self.showlog).pack(side=tk.RIGHT, padx=20, pady=5)
		image_label(frame, "images\\user.png", 40, 40, False).pack(side=tk.RIGHT)

		return frame
	#def showlog(self):
	#	log.LoginView(self.root)
		#return frame
        
	def bottom(self, parent):
		""" 窗体最下面留空白 """

		frame = tk.Frame(parent, height=10, bg="whitesmoke")
		frame.propagate(True)
		return frame

	def main(self, parent):
		""" 窗体主体 """

		frame = tk.Frame(parent, bg="whitesmoke")

		self.main_top(frame).pack(fill=tk.X, padx=30, pady=15)
		self.main_left(frame).pack(side=tk.LEFT, fill=tk.Y, padx=30)
		v_seperator(frame, 30).pack(side=tk.RIGHT, fill=tk.Y)
		self.main_right(frame).pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

		return frame

	def main_top(self, parent):
		def label(frame, text, size=12):
			return tk.Label(frame, bg="white", fg="gray", text=text, font=_ft(size))

		frame = tk.Frame(parent, bg="white", height=150)

		image_label(frame, "images\\img_title.png", width=240, height=120, keep_ratio=False) \
			.pack(side=tk.LEFT, padx=10, pady=10)

		self.main_top_middle(frame).pack(side=tk.LEFT)

		label(frame, "收起^").pack(side=tk.RIGHT, padx=10)

		frame.propagate(False)
		return frame

	def main_top_middle(self, parent):
		str1 = "心律失常智能诊断模型，可以识别患者的异常心电，并根据需要，辅助医生进行初级和深度诊断。"
		str2 = "一般情况下只需要十秒钟即可完成辅助诊断。"

		def label(frame, text):
			return tk.Label(frame, bg="white", fg="gray", text=text, font=_ft(12))

		frame = tk.Frame(parent, bg="white")

		self.main_top_middle_top(frame).pack(anchor=tk.NW)

		label(frame, str1).pack(anchor=tk.W, padx=10, pady=2)
		label(frame, str2).pack(anchor=tk.W, padx=10)

		return frame

	def main_top_middle_top(self, parent):
		def label(frame, text, size=12, bold=True, fg="blue"):
			return tk.Label(frame, text=text, bg="white", fg=fg, font=_ft(size, bold))

		frame = tk.Frame(parent, bg="white")

		label(frame, "智能诊断", 20, True, "black").pack(side=tk.LEFT, padx=10)
		label(frame, "操作文档").pack(side=tk.LEFT, padx=10)
		label(frame, "教学视频").pack(side=tk.LEFT, padx=10)
		label(frame, "常见问题").pack(side=tk.LEFT, padx=10)

		return frame

	def main_left(self, parent):
		def label(frame, text, size=10, bold=False, bg="white"):
			return tk.Label(frame, text=text, bg=bg, font=_ft(size, bold))

		frame = tk.Frame(parent, width=180, bg="white")
		label(frame, "诊断中心", 12, True).pack(anchor=tk.W, padx=20, pady=10)
		#label(frame, "一级诊断").pack(anchor=tk.W, padx=40, pady=5)
        
		f2 = tk.Frame(frame, bg="whitesmoke")
		v_seperator(f2, width=5, bg="blue").pack(side=tk.LEFT, fill=tk.Y)
		label(f2, "一级诊断", bg="whitesmoke").pack(side=tk.LEFT, anchor=tk.W, padx=40, pady=5)
		f2.pack(fill=tk.X)
        
		f1 = tk.Frame(frame, bg="whitesmoke")
		v_seperator(f1, width=5, bg="blue").pack(side=tk.LEFT, fill=tk.Y)
		label(f1, "二级诊断", bg="whitesmoke").pack(side=tk.LEFT, anchor=tk.W, padx=35, pady=5)
		f1.pack(fill=tk.X)

		label(frame, "三级诊断").pack(anchor=tk.W, padx=40, pady=5)
		#label(frame, "校验模型").pack(anchor=tk.W, padx=40, pady=5)
		#label(frame, "发布模型").pack(anchor=tk.W, padx=40, pady=5)

		h_seperator(frame, 10)

		label(frame, "数据中心", 12, True).pack(anchor=tk.W, padx=20, pady=10)
		label(frame, "病人数据管理").pack(anchor=tk.W, padx=40, pady=5)
		label(frame, "添加病人数据").pack(anchor=tk.W, padx=40, pady=5)

		frame.propagate(False)
		return frame

	def main_right(self, parent):
		def label(frame, text, size=10, bold=False, fg="black"):
			return tk.Label(frame, text=text, bg="white", fg=fg, font=_ft(size, bold))

		def space(n):
			s = " "
			r = ""
			for i in range(n):
				r += s
			return r
        
		def zhenduan(self,frame, text, size=10, bold=False, fg="black"):
			print('**')
            
		frame = tk.Frame(parent, width=200, bg="white")
        
		def onResize(event):
		    """Prints the scrollbar's position on window resize."""
		    print(str(myScrollbar.get()))
		
		myFrame = frame
		mySecondaryFrame = frame
		myCanvas = tk.Canvas(myFrame)
		myScrollbar = tk.Scrollbar(myFrame, orient='vertical', command=myCanvas.yview)

		myCanvas.config(yscrollcommand=myScrollbar.set)

		#for i in range(0,100):
		 #   print(i)
		 #   button = tk.Button(mySecondaryFrame, text=i)
		 #   button.pack(fill='y',expand=True)
		 #   myCanvas.configure(scrollregion=(0, 0, 0, 400))

		myFrame.pack(fill='both',expand=True)
		myScrollbar.pack(side="right",fill='y')
		myCanvas.pack(side='right', fill='both', expand=True)

		button_window = myCanvas.create_window(0, 0, anchor='nw', window=mySecondaryFrame)

		myCanvas.bind('<Configure>', onResize)

		tk.mainloop()
		#111
		label(frame, "一级诊断", 12, True).pack(anchor=tk.W, padx=20, pady=5)

		h_seperator(frame)

		f1 = tk.Frame(frame, bg="white")
		label(f1, space(8) + "诊断性质:").pack(side=tk.LEFT, pady=5)
		label(f1, "识别病人异常心律").pack(side=tk.LEFT, padx=20)
		f1.pack(fill=tk.X)

		f2 = tk.Frame(frame, bg="white")
		label(f2, space(5) + "*", fg="red").pack(side=tk.LEFT, pady=5)
		label(f2, "输入病人姓名:").pack(side=tk.LEFT)
		tk.Entry(f2, bg="white", font=_ft(10), width=25).pack(side=tk.LEFT, padx=20)
		#tk.Button(f2, text="下一步", width=12, command=zhenduan).pack(side=tk.LEFT, padx=5, pady=5)
		f2.pack(fill=tk.X)

		'''
        f3 = tk.Frame(frame, bg="white")
		label(f3, space(5) + "*", fg="red").pack(side=tk.LEFT, pady=5)
		label(f3, "联系方式:").pack(side=tk.LEFT)
		tk.Entry(f3, bg="white", font=_ft(10), width=25).pack(side=tk.LEFT, padx=20)
		f3.pack(fill=tk.X)
        '''
		ttk.Button(frame, text="下一步", width=12, command=zhenduan).pack(anchor=tk.W, padx=172, pady=5)
        
		f4 = tk.Frame(frame, bg="white")
		#label(f4, space(5) + "*", fg="red").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		label(f4, space(8) +"一级诊断:").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		tk.Text(f4, bg="white", font=_ft(10), height=10, width=70).pack(side=tk.LEFT, padx=20, pady=5)
		f4.pack(fill=tk.X)
        
		f5 = tk.Frame(frame, bg="white")
		#label(f4, space(5) + "*", fg="red").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		label(f5, space(8) +"二级诊断:").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		tk.Text(f5, bg="white", font=_ft(10), height=10, width=70).pack(side=tk.LEFT, padx=20, pady=5)
		f5.pack(fill=tk.X)

		f6 = tk.Frame(frame, bg="white")
		#label(f4, space(5) + "*", fg="red").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		label(f6, space(8) +"三级诊断:").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		tk.Text(f6, bg="white", font=_ft(10), height=10, width=70).pack(side=tk.LEFT, padx=20, pady=5)
		f6.pack(fill=tk.X)
		#tk.Button(canvas, text="基本信息", bg="cadetblue", command=self.show_single, font=ft2, height=2, fg="white", width=15)\
		#	.pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)
		#tk.Button(canvas, text="患者系统", bg="cadetblue", command=self.show_multi, font=ft2, height=2, fg="white", width=15)\
		#	.pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)
		return frame
if __name__ == "__main__":
	app = Window
	app.root.mainloop()
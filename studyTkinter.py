import tkinter as tk
from tkinter import ttk

root = tk.Tk()  # 定义
root.geometry('960x540')  # 一种定义窗口长宽的方式（长x宽）
root.title('Test program')  # 窗口标题

# 后面程序要用的各函数
def clickPrint1():
    print('Hello, you clicked button 1.')
def clickPrint2():
    print('Hello, you clicked button 2.')
def entryPrint():
    print('Entry get: ' + entry.get())
choice1 = tk.StringVar
def choicePrint():
    print(choice1.get())

# 定义框架
centerFrame = tk.Frame(root, height=2)
centerFrame.pack()
leftFrame = tk.Frame(root, height=2)
leftFrame.pack(side=tk.LEFT)
rightFrame = tk.Frame(root, height=2)
rightFrame.pack(side=tk.RIGHT)

# 定义标签（文本输出）
centerLabel = tk.Label(centerFrame, text='Hello,world!', font=('Microsoft YaHei UI', 18),
                       justify=tk.CENTER)
centerLabel.pack()
leftLabel = tk.Label(leftFrame, text='Left', font=('Microsoft YaHei Light', 16),
                     justify=tk.CENTER)
leftLabel.pack()
leftLabel = tk.Label(rightFrame, text='Right', font=('Microsoft YaHei Light', 16),
                     justify=tk.CENTER)
leftLabel.pack()

# 定义按钮
leftButton = tk.Button(leftFrame, bg='#eeeeee', fg='#00aaaa',
                       activebackground='#aaaaaa', activeforeground='#006666',
                       text='Click me!', command=clickPrint1,
                       font=('Microsoft YaHei UI light', 14, 'underline'),
                       padx=20, pady=5)
leftButton.pack()
rightButton = tk.Button(rightFrame, bg='#eeeeee', fg='#aa00aa',
                        activebackground='#aaaaaa', activeforeground='#660066',
                        text='Click me!', command=clickPrint2,
                        font=('Microsoft YaHei light', 14, 'underline'),
                        padx=20, pady=5)
rightButton.pack()

# 定义输入入口
entry = tk.Entry(centerFrame, bg='#eeeeee', fg='#ff0000', font=('Microsoft YaHei light', 14),
                 highlightcolor='#ff2222', selectforeground='#ee2222', show='#',
                 width=35, exportselection=0, justify='center', relief=tk.SUNKEN,
                 )
entry.pack()
printEntry = tk.Button(centerFrame, bg='#eeeeee', fg='#ff0000',
                       activebackground='#aaaaaa', activeforeground='#ee2222',
                       text='Show entry', command=entryPrint,
                       font=('Microsoft YaHei light', 14), padx=5)  # 按钮输出输入内容
printEntry.pack()

# 单选按钮
# 各单选按钮组件使用同一个记录变量时就能实现控制单选。
# 可以设置按钮对选项进行处理，也可以像此处设置command在被选中时进行操作。
# # 程序有报错
radioButton1 = tk.Radiobutton(leftFrame, bg='#eeeeee', fg='#f000f0', font=('Microsoft YaHei UI Light', 14),
                              activebackground='#aaaaaa', activeforeground='#d000d0', highlightcolor='#da00da',
                              text='1', variable=choice1, value='1', command=choicePrint)
radioButton1.pack()
radioButton2 = tk.Radiobutton(leftFrame, bg='#eeeeee', fg='#f000f0', font=('Microsoft YaHei UI Light', 14),
                              activebackground='#aaaaaa', activeforeground='#d000d0', highlightcolor='#da00da',
                              text='2', variable=choice1, value='2', command=choicePrint)
radioButton2.pack()

root.mainloop()  # 触发 GUI

#用 Python Tkinter 搭建 GUI
入门版
##一、搭建窗口
```Python
import tkinter as tk

root = tk.Tk()
# Tk类的实例化，创建根窗口（即顶级窗口、程序主窗口）。下文用此处变量名root代表这个实例类。
root.geometry("240x135")
# root.geometry("宽x高") ：定义窗口大小，中间时小写字母x
root.title("Test")  # root.title("标题") ：定义窗口标题

root.mainloop()  # 触发GUI
```

##二、基本小组件
Tkinter 界面是由不同的小组件组成的。\
小部件按照一定的层次与次序排列，我们称这次序为`小部件层次结构`。子级组件创建时要传入它的父级（框架或根窗口）。\
定义小部件是可以传入参数以改变其外观和行为，称为`配置选项`。\
将小部件放入窗口的行为称作`几何管理`。
###1.四个常用组件
####1.1 按钮
按钮是Tkinter的一种交互组件。\
句法：变量 = tkinter.Button(父级, **配置选项)\
例如：button = tkinter.Button(root, text="hello", padx=5, pady=5)\
 \
一般情况下，按钮被点击后会有操作。\
事先定义函数，再在配置选项中加入“commamd”传入函数，可使按钮被点击时运行函数。\
观察下面代码：
```python
import tkinter as tk

# 在这里定义函数时习惯
def butp():
    # 这函数设置传入参数无用
    print("Hello")

root = tk.Tk()
root.geometry("240x135")
root.title("Test")

button = tk.Button(root, text="hello", padx=5, pady=5, 
                   command=butp)
#                          | 不要带括号，否则程序在按钮被点击时不执行，反而在一开始就执行了。
button.pack()

root.mainloop()
```
**常用的按钮组件配置选项：**\
    *font*：字符串或元组，字符串需为"字体名 参数 参数……"，元组需为("字体名", "参数", "参数"……)。\
    如"等线 14"或("等线", "14", "underline")\
    *text*：字符串，按钮显示的文本。\
	*height*：整型，按钮高度。\
    *width*：整型，按钮宽度。\
    *justify*：字体对齐方式。有靠左（tkinter.LEFT)、靠右（tkinter.RIGHT）和居中（tkinter.CENTER）。\
	*padx*：整型，文字左右填充宽度。\
    *pady*：整型，文字上下填充宽度。
####1.2 标签
标签组件用于在屏幕上输出简单的文本行。它有个特别用途时插入图像（这里暂时不介绍）。\
句法：变量 = tkinter.Label(父级, **配置选项)\
例如：label = tkinter.Label(root, text="Hello", font="等线")\
**常用的标签组件配置选项：**
    *text*：字符串，标签文本。若要换行课用"\n"。\
    *height*：整型，标签高度。\
    *width*：整型，标签宽度。\
    *font*：字符串或元组，字符串需为"字体名 参数 参数……"，元组需为("字体名", "参数", "参数"……)。\
    如"等线 14"或("等线", "14", "underline")\
	*justify*：字体对齐方式。有靠左（tkinter.LEFT)、靠右（tkinter.RIGHT）和居中（tkinter.CENTER）。\
	*padx*：整型，文字左右填充宽度。\
    *pady*：整型，文字上下填充宽度。

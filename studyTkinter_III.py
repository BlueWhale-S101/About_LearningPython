import tkinter as tk

root = tk.Tk()
root.title("III")
root.geometry("500x300")

tF = tk.Frame(root, justify=tk.TOP(), bg='#eeeeee')
tF.pack()
rF = tk.Frame(root, justify=tk.RIGHT(), bg='#ff0000')
rF.pack()

lb1 = tk.Frame(tF, text="left")
lb1.pack()
lb2 = tk.Frame(tF, text="right")
lb2.pack()

root.mainloop()

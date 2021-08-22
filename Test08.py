import tkinter as tk

def set_message():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()
window.title('Desktop Application')
window.minsize(width=500, height=600)

title_label = tk.Label(master=window, text='กรุณาระบุข้อความ')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='OK', command=set_message)
ok_button.pack()

window.mainloop()






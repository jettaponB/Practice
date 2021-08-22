import tkinter as tk

def show_output():
    number = int(input_number.get())

    output = ''
    for i in range(1, 13):
        output += str(number) + ' * ' + str(i) + ' = ' + str(number * i) + '\n'
        output_label.configure(text=output)


window = tk.Tk()
window.title('โปรแกรมคำนวนสูตรคูณ')
window.minsize(width=500, height=400)

title_label = tk.Label(master=window, text='กรุณาระบุแม่สูตรคูณ')
title_label.pack()

input_number = tk.Entry(master=window)
input_number.pack()

cal_button = tk.Button(master=window, text='คำนวน', command=show_output)
cal_button.pack()

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()
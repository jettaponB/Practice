import tkinter as tk

def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='ผิด')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + ' * ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)


window = tk.Tk()
window.title('JustDoIT')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack(pady=20)

number_input = tk.Entry(master=window, width=15)
number_input.pack()

ok_button = tk.Button(
    master=window, text='คือ', command=show_output,
    width=6, height=1
)
ok_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)


window.mainloop()
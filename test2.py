import tkinter as tk


def change_color(event):
    event.widget.config(bg='green')
    entry.insert('end', event.widget['text'])


def change_back(event):
    event.widget.config(bg='ghost white')


root = tk.Tk()
num_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

entry = tk.Entry(root, width=50)
entry.grid(row=0, column=0)

pad_frame = tk.Frame(root)
pad_frame.grid(row=1, column=0)
# Is a label but works like a button due to bind.
# This method should fit your needs.
for index, sub_list in enumerate(num_pad):
    for sub_index, sub_value in enumerate(sub_list):
        lbl = tk.Label(pad_frame, text=sub_value, bg="ghost white", activebackground="LightSteelBlue2",
                       height=2, width=3)
        lbl.grid(row=index, column=sub_index, padx=2, pady=2)
        lbl.bind("<Button-1>", change_color)
        lbl.bind("<ButtonRelease-1>", change_back)
        lbl.bind("<Leave>", change_back)
root.mainloop()
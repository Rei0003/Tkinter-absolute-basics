import tkinter as tk
from tkinter import ttk

def button_func():
  print("A button was pressed")

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(window, text = "This is a test")
label.pack()

# tk.text
text = tk.Text(window)
text.pack()

# ttk entry
entry = ttk.Entry(window)
entry.pack()

# ttk label 2
label2 = ttk.Label( window, text = "my label")
label2.pack()
#ttk button
button = ttk.Button(window, text = 'A button', command = button_func)
button.pack()
button2 = ttk.Button(window, text = 'Hello', command = lambda:print("hello"))
button2.pack()
# run
window.mainloop()
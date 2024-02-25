import tkinter as tk
from tkinter import filedialog

def readFile(filePath: str = None):
    return open(filePath).read()

def openFile():
    file_path = filedialog.askopenfilename()
    if file_path:
        content = readFile(file_path)
        text.delete('1.0', tk.END)  # Clear previous content
        text.insert(tk.END, content)
        text.tag_configure("color_tag", foreground="green")
        text.tag_add("color_tag", "1.0", "9999999999999999999999999999999999999999999999999999999999999999999999999999.0")
        

root = tk.Tk()
root.configure(bg="black")
root.title("File Reader")

text = tk.Text(root, bg="black")

text.pack()

open_button = tk.Button(root, text="Open File",command=openFile)
open_button.pack()

root.mainloop()

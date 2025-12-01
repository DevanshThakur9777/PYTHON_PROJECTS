import tkinter as tk  # Tkinter module ko tk name se import kar rahe hain
from tkinter import filedialog, messagebox  # File dialog & message boxes import


# New file function
def new_File():
    text.delete(1.0, tk.END)  # Textbox ka pura text delete karega


# Open file function
def open_file():
    file_path = filedialog.askopenfilename(      # File manager open hoga
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]      
    )

    if file_path:  # Agar user ne koi file choose ki ho
        with open(file_path, 'r') as file:        # File read mode me open karenge
            text.delete(1.0, tk.END)              # Purana text delete
            text.insert(tk.END, file.read())      # Naya text insert


# Save file function
def save_file():
    file_Path = filedialog.asksaveasfilename(     # Save dialog open hota hai
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_Path:  # Agar user ne file path diya ho
        with open(file_Path, "w") as file:        # File write mode me open hoti hai
            file.write(text.get(1.0, tk.END))     # Textbox ka text file me save
            messagebox.showinfo("Info", "File Saved Successfully!")  # Popup message


# Main window create
root = tk.Tk()
root.title("Simple Text Editor")  # Window title
root.geometry("800x600")          # Window size


# Menu bar create
menu = tk.Menu(root)
root.config(menu=menu)


# File menu create
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_File)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# Text area create
text = tk.Text(
    root,
    wrap=tk.WORD,          # Word wrap
    font=("Helvetica", 12),
    fg="blue"
)
text.pack(expand=tk.YES, fill=tk.BOTH)  # Fill full window


# Start GUI loop
root.mainloop()



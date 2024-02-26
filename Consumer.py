import tkinter as tk
from tkinter import filedialog, messagebox
import csv

def update_display():
    global display_label
    text = entry.get()
    entry.delete(0, tk.END)  # Clear the entry after getting the text
    display_label.config(text=display_label.cget("text") + "\n" + text)  # Append new text to existing display text

def save_as_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            data = display_label.cget("text").split("\n")
            for line in data:
                if line:  # Ensure non-empty lines are written
                    values = line.split(",")
                    writer.writerow([f'"{value.strip()}"' for value in values])
        
        # Clear both screens
        entry.delete(0, tk.END)
        display_label.config(text="")
        
        # Close main window with confirmation popup
        if messagebox.askyesno("Close Confirmation", "Do you want to close the application?"):
            root.destroy()

root = tk.Tk()
root.title("Text Display App")
root.geometry("500x500")

entry = tk.Entry(root, font=("Helvetica", 16))
entry.grid(row=0, column=0, sticky="nsew")

entry.bind("<Return>", lambda event: update_display())

display_window = tk.Toplevel(root)
display_window.geometry("500x500")
display_label = tk.Label(display_window, text="", font=("Helvetica", 16))
display_label.pack(fill=tk.BOTH, expand=True)

save_button = tk.Button(root, text="Save as CSV", command=save_as_csv)
save_button.grid(row=1, column=0, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()

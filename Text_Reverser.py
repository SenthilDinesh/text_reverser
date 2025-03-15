import tkinter as tk
from tkinter import messagebox, filedialog

def reverse_text(text, mode):
    return text[::-1] if mode == 1 else ' '.join(text.split()[::-1])

def save_to_file(content):
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        messagebox.showinfo("Success", "Text saved successfully!")

def process_choice():
    text = entry.get().strip()
    if not text:
        return messagebox.showwarning("Warning", "Enter valid text!")
    result = reverse_text(text, var.get())
    result_label.config(text=f"Result: {result}")
    save_button.config(state=tk.NORMAL, command=lambda: save_to_file(result))

root = tk.Tk()
root.title("Text Reverser")
root.geometry("400x250")

tk.Label(root, text="Enter text:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

var = tk.IntVar()
tk.Radiobutton(root, text="Reverse Characters", variable=var, value=1).pack()
tk.Radiobutton(root, text="Reverse Words", variable=var, value=2).pack()

tk.Button(root, text="Process", command=process_choice).pack(pady=10)
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=5)

save_button = tk.Button(root, text="Save to File", state=tk.DISABLED)
save_button.pack(pady=5)

root.mainloop()

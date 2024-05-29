import tkinter as tk
from ttkbootstrap import Style
from tkinter import filedialog, messagebox
import mergePDFs
import rotatePDFs

def merge_pdfs():
    pdf_files = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
    if pdf_files:
        selected_pages_list = []
        for pdf_file in pdf_files:
            selected_pages = mergePDFs.select_pages(pdf_file, window)
            if selected_pages:
                selected_pages_list.append(selected_pages)
            else:
                messagebox.showwarning("Warning", "No pages selected. Skipping this PDF.")
        if selected_pages_list:
            mergePDFs.merge_pdfs(pdf_files, selected_pages_list)

def rotate_left():
    rotatePDFs.rotate_left(window)

def rotate_right():
    rotatePDFs.rotate_right(window)

# Create the main window
style = Style(theme="superhero")
window = style.master
window.title("PDF Tools")
window.geometry("600x400")

# Add a header or logo
header_frame = tk.Frame(window, bg="#2c3e50", height=80)
header_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
header_label = tk.Label(header_frame, text="PDF Tools", font=("Arial", 24, "bold"), fg="white", bg="#2c3e50")
header_label.pack(pady=20)

# Create a frame for the buttons
button_frame = tk.Frame(window, bg="#34495e")
button_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

# Create a button to launch PDF merging
merge_icon = tk.PhotoImage(file="merge.png")
merge_button = tk.Button(button_frame, image=merge_icon, text="Merge PDFs", compound=tk.TOP,
                         command=merge_pdfs, font=("Arial", 14), bg="#3498db", fg="white", padx=20, pady=10)
merge_button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Create buttons for rotating left and right
rotate_left_icon = tk.PhotoImage(file="rotate-left.png")
rotate_left_button = tk.Button(button_frame, image=rotate_left_icon, text="Rotate Left", compound=tk.TOP,
                               command=rotate_left, font=("Arial", 14), bg="#3498db", fg="white", padx=20, pady=10)
rotate_left_button.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

rotate_right_icon = tk.PhotoImage(file="rotate-right.png")
rotate_right_button = tk.Button(button_frame, image=rotate_right_icon, text="Rotate Right", compound=tk.TOP,
                                command=rotate_right, font=("Arial", 14), bg="#3498db", fg="white", padx=20, pady=10)
rotate_right_button.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

# Configure the columns and rows to expand and fill the available space
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

# Run the main event loop
window.mainloop()
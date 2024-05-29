import os
import pypdf
import tkinter as tk
from ttkbootstrap import Style
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
from PIL import ImageTk

def rotate_pdf(file_path, selected_pages, rotation_angle):
    try:
        with open(file_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            writer = pypdf.PdfWriter()
            for i, page in enumerate(reader.pages):
                if i in selected_pages:
                    writer.add_page(page.rotate(rotation_angle))
                else:
                    writer.add_page(page)
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_path:
                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)
                messagebox.showinfo("Success", "PDF rotated successfully!")
            else:
                messagebox.showwarning("Warning", "No output file selected. PDF rotation canceled.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def select_pages(file_path, rotation_angle, main_window):
    pages = convert_from_path(file_path)
    selected_pages = []

    def on_select():
        nonlocal selected_pages
        selected_pages = [i for i, var in enumerate(page_vars) if var.get()]
        selection_window.destroy()

    style = Style(theme="superhero")
    selection_window = tk.Toplevel(main_window)
    selection_window.title(f"Select Pages - {os.path.basename(file_path)}")
    selection_window.geometry("800x600")

    # Create a frame for the thumbnail grid
    thumbnail_frame = tk.Frame(selection_window, bg="#34495e")
    thumbnail_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Create a canvas and scrollbar for scrolling the thumbnail grid
    canvas = tk.Canvas(thumbnail_frame, bg="#34495e")
    scrollbar = tk.Scrollbar(thumbnail_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#34495e")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create checkboxes for each page thumbnail
    page_vars = []
    for i, page in enumerate(pages):
        page_image = ImageTk.PhotoImage(page.resize((150, 200), resample=3))
        page_var = tk.BooleanVar()
        page_vars.append(page_var)
        checkbutton = tk.Checkbutton(scrollable_frame, image=page_image, variable=page_var,
                                     bg="#34495e", activebackground="#34495e")
        checkbutton.image = page_image
        checkbutton.grid(row=i // 4, column=i % 4, padx=10, pady=10)

    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Create a button to confirm the selection
    select_button = tk.Button(selection_window, text="Rotate Selected Pages", command=on_select,
                              font=("Arial", 14), bg="#3498db", fg="white", padx=20, pady=10)
    select_button.grid(row=1, column=0, pady=20)

    # Configure the grid to expand and fill the available space
    selection_window.columnconfigure(0, weight=1)
    selection_window.rowconfigure(0, weight=1)
    thumbnail_frame.columnconfigure(0, weight=1)
    thumbnail_frame.rowconfigure(0, weight=1)

    main_window.wait_window(selection_window)

    if selected_pages:
        rotate_pdf(file_path, selected_pages, rotation_angle)
    else:
        messagebox.showwarning("Warning", "No pages selected. PDF rotation canceled.")

def rotate_left(main_window):
    file_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        select_pages(file_path, -90, main_window)

def rotate_right(main_window):
    file_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        select_pages(file_path, 90, main_window)
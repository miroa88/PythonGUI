import tkinter as tk
from tkinter import filedialog
import pandas as pd

from readExcel import readExcelFile
from grouping import startGrouping
from writeExcel import *
import re
import pandas as pd
data = None
message = ""

def load_excel_file():
    global data
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        log_box.insert(tk.END, f"Excel file selected: {file_path}\n")
        data = readExcelFile("data.xlsx")

def start_processing():
    global data, message
    if data:
        log_box.insert(tk.END, "Starting processing...\n")
        message = startGrouping(data)
        log_box.insert(tk.END, message)
        log_box.insert(tk.END, "Processing completed.\n")

def export_to_excel():
    global message
    if message:
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
                
            convert_to_excel(message, file_path)

            log_box.insert(tk.END, f"Message exported to: {file_path}\n")
        else:
            log_box.insert(tk.END, "Export canceled.\n")

# Create the main window
window = tk.Tk()
window.title("Excel File Processing")

# Create the load file button
load_button = tk.Button(window, text="Load Excel File", command=load_excel_file)
load_button.pack(pady=10)

# Create the start button
start_button = tk.Button(window, text="Start Processing", command=start_processing)
start_button.pack(pady=10)

# Create the export button
export_button = tk.Button(window, text="Export to Excel", command=export_to_excel)
export_button.pack(pady=10)

# Create the log box frame
log_frame = tk.Frame(window)
log_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the vertical scrollbar
v_scrollbar = tk.Scrollbar(log_frame, orient=tk.VERTICAL)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the horizontal scrollbar
h_scrollbar = tk.Scrollbar(log_frame, orient=tk.HORIZONTAL)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Create the log box
log_box = tk.Text(log_frame, height=20, width=80, wrap=tk.NONE, yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
log_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure the scrollbars to scroll the log box
v_scrollbar.config(command=log_box.yview)
h_scrollbar.config(command=log_box.xview)

# Start the main loop
window.mainloop()
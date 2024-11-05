import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import backend
from datetime import datetime

def get_selected_row(event):
    try:
        global selected_tuple
        index = record_display.selection()[0]
        selected_tuple = record_display.item(index, 'values')
        
        # Set entries for selected record's data
        t1.delete(0, END)
        t1.insert(END, selected_tuple[1])
        t2.delete(0, END)
        t2.insert(END, selected_tuple[2])
        t3.delete(0, END)
        t3.insert(END, selected_tuple[3])
        t4.delete(0, END)
        t4.insert(END, selected_tuple[4])
        t5.delete(0, END)
        t5.insert(END, selected_tuple[5])
        t6.delete(0, END)
        t6.insert(END, selected_tuple[6])
        t7.delete(0, END)
        t7.insert(END, selected_tuple[7])
        t8.delete(0, END)
        t8.insert(END, selected_tuple[8])
        t9.delete(0, END)
        t9.insert(END, selected_tuple[9])
        t10.delete(0, END)
        t10.insert(END, selected_tuple[10])
    except IndexError:
        pass

def view_command():
    # Clear the current display and populate it with all records from the database
    for row in record_display.get_children():
        record_display.delete(row)
    for row in backend.view():
        record_display.insert("", "end", values=row)

def search_command():
    # Clear current display and populate it with search results
    for row in record_display.get_children():
        record_display.delete(row)
    for row in backend.search(title_text.get(), author_text.get(), publisher_text.get(), collection_text.get(), pages_text.get(), translator_text.get(), edition_text.get(), first_edition_text.get(), print_year_text.get(), isbn_text.get()):
        record_display.insert("", "end", values=row)

def add_command():
    # Insert new record into the database
    backend.insert(title_text.get(), author_text.get(), publisher_text.get(), collection_text.get(),
                   pages_text.get(), translator_text.get(), edition_text.get(), first_edition_text.get(), print_year_text.get(), isbn_text.get())
    view_command() # Refresh the display

def update_command():
    # Update the selected record in the database
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), publisher_text.get(), collection_text.get(), pages_text.get(), translator_text.get(), edition_text.get(), first_edition_text.get(),print_year_text.get(), isbn_text.get())
    view_command() # Refresh the display

def delete_command():
    # Delete the selected record from the database
    backend.delete(selected_tuple[0])
    view_command() # Refresh the display

def close_command():
    # Close the main window
    window.destroy()

def clear_fields():
    # Clear all entry fields
    for entry in entries:
        entry.delete(0, END)

def export_to_excel():
    # Obtain data from the database
    data = backend.view()
    columns = ["ID", "Title", "Author", "Publisher", "Collection", "Pages", "Translator", "Edition", "First Edition", "Print Year", "ISBN"]
    
    # Create a DataFrame with the data
    df = pd.DataFrame(data, columns=columns)
    
    # Get the current date and time for the filename
    now = datetime.now().strftime("%Y%m%d_%H%M")
    
    # Generate the filename with the date and time
    file_name = f"books_export_{now}.xlsx"
    
    # Export to an Excel file
    df.to_excel(file_name, index=False)
    print(f"Database exported to {file_name}")

# Main window setup
window = Tk()
window.title("Library")

# Labels and Entry fields for book information
labels = ["Title", "Author", "Publisher", "Collection", "Pages", "Translator", "Edition", "First Edition", "Print Year", "ISBN"]
text_vars = [StringVar() for _ in labels]
entries = []

for i, label_text in enumerate(labels):
    Label(window, text=label_text).grid(row=i//2, column=(i % 2) * 2)
    entry = Entry(window, textvariable=text_vars[i])
    entry.grid(row=i//2, column=(i % 2) * 2 + 1)
    entries.append(entry)

# Unpacking text variables for direct use
title_text, author_text, publisher_text, collection_text, pages_text, translator_text, edition_text, first_edition_text, print_year_text, isbn_text = text_vars
t1, t2, t3, t4, t5, t6, t7, t8, t9, t10 = entries  # Optional aliasing for specific fields if needed

# Treeview to display records in a tabular format
record_display = ttk.Treeview(window, columns=("ID", *labels), show="headings")
record_display.grid(row=5, column=0, rowspan=6, columnspan=4, pady=10)

# Define column headings and widths
record_display.heading("ID", text="ID")
for label in labels:
    record_display.heading(label, text=label)

for col in record_display["columns"]:
    record_display.column(col, width=100)

# Bind selection event to populate entry fields
record_display.bind('<<TreeviewSelect>>', get_selected_row)

# Action buttons
buttons_frame = tk.Frame(window)
buttons_frame.grid(row=6, column=4, padx=10, pady=10)

# Create action buttons with appropriate commands
tk.Button(buttons_frame, text="View All", width=12, command=view_command).grid(row=0, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Search", width=12, command=search_command).grid(row=1, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Add Entry", width=12, command=add_command).grid(row=2, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Update", width=12, command=update_command).grid(row=3, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Delete Selection", width=12, command=delete_command).grid(row=4, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Clear", width=12, command=clear_fields).grid(row=5, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Export to Excel", width=12, command=export_to_excel).grid(row=6, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Close", width=12, command=close_command).grid(row=7, column=0, padx=5, pady=5)


# Start the main loop
window.mainloop()
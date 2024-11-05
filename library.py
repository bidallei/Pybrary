from tkinter import *
import backend

# Function to populate text fields based on selected item in the listbox
def get_selected_row(event):
    try: 
        global selected_tuple
        # Get the selected item from the listbox
        index = record_display.curselection()[0]
        selected_tuple = record_display.get(index)
        
        # Insert the selected data into each text field
        t1.delete(0, END)
        t1.insert(END, selected_tuple[1])
        t2.delete(0, END)
        t2.insert(END, selected_tuple[2])
        t3.delete(0, END)
        t3.insert(END, selected_tuple[3])
        t4.delete(0, END)
        t4.insert(END, selected_tuple[4])
    except IndexError:
        pass

# Function to display all records in the listbox
def view_command():
    record_display.delete(0, END)
    for row in backend.view():
        record_display.insert(END, row)

# Function to search for a record based on the text fields
def search_command():
    record_display.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        record_display.insert(END, row)

# Function to add a new record using the values in the text fields
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

# Function to update the selected record with the new values in the text fields
def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

# Function to delete the selected record
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

# Function to close the main window
def close_command():
    window.destroy()

# Function to clear all text fields without other actions
def clear_fields():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)

# Main window setup
window = Tk()
window.title("Book Store")

# Labels and Entry fields for book information
Label(window, text="Title").grid(row=0, column=0)
title_text = StringVar()
t1 = Entry(window, textvariable=title_text)
t1.grid(row=0, column=1)

Label(window, text="Author").grid(row=0, column=2)
author_text = StringVar()
t2 = Entry(window, textvariable=author_text)
t2.grid(row=0, column=3)

Label(window, text="Year").grid(row=1, column=0)
year_text = StringVar()
t3 = Entry(window, textvariable=year_text)
t3.grid(row=1, column=1)

Label(window, text="ISBN").grid(row=1, column=2)
isbn_text = StringVar()
t4 = Entry(window, textvariable=isbn_text)
t4.grid(row=1, column=3)

# Listbox to display records and scrollbar
record_display = Listbox(window, height=6, width=50)
record_display.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

record_display.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=record_display.yview)

# Bind selection in listbox to get_selected_row function
record_display.bind('<<ListboxSelect>>', get_selected_row)

# Action buttons
Button(window, text="View All", width=12, command=view_command).grid(row=2, column=3)
Button(window, text="Search Entry", width=12, command=search_command).grid(row=3, column=3)
Button(window, text="Add Entry", width=12, command=add_command).grid(row=4, column=3)
Button(window, text="Update", width=12, command=update_command).grid(row=5, column=3)
Button(window, text="Delete", width=12, command=delete_command).grid(row=6, column=3)
Button(window, text="Clear", width=12, command=clear_fields).grid(row=7, column=3)  # New Clear button
Button(window, text="Close", width=12, command=close_command).grid(row=8, column=3)

# Start the main loop
window.mainloop()

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
    for row in record_display.get_children():
        record_display.delete(row)
    for row in backend.view():
        record_display.insert("", "end", values=row)

def search_command():
    for row in record_display.get_children():
        record_display.delete(row)
    for row in backend.search(title_text.get(), author_text.get(), publisher_text.get(), collection_text.get(),
                              pages_text.get(), translator_text.get(), edition_text.get(), first_edition_text.get(), 
                              print_year_text.get(), isbn_text.get()):
        record_display.insert("", "end", values=row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), publisher_text.get(), collection_text.get(),
                   pages_text.get(), translator_text.get(), edition_text.get(), first_edition_text.get(),
                   print_year_text.get(), isbn_text.get())
    view_command()

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), publisher_text.get(), collection_text.get(),
                   pages_text.get(), translator_text.get(), edition_text.get(), first_edition_text.get(),
                   print_year_text.get(), isbn_text.get())
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def close_command():
    window.destroy()

def clear_fields():
    for entry in entries:
        entry.delete(0, END)

def export_to_excel():
    # Obtener datos de la base de datos
    data = backend.view()
    columns = ["ID", "Title", "Author", "Publisher", "Collection", "Pages", "Translator", "Edition", "First Edition", "Print Year", "ISBN"]
    
    # Crear un DataFrame con los datos
    df = pd.DataFrame(data, columns=columns)
    
    # Obtener la fecha y hora actuales
    now = datetime.now().strftime("%Y%m%d_%H%M")
    
    # Generar el nombre del archivo con la fecha y hora
    file_name = f"books_export_{now}.xlsx"
    
    # Exportar a un archivo Excel
    df.to_excel(file_name, index=False)
    print(f"Database exported to {file_name}")

# Main window setup
window = Tk()
window.title("Biblioteca")

# Labels and Entry fields for book information
labels = ["Título", "Autor", "Editor", "Colección", "Páginas", "Traductor", "Edición", "Primera Edición", "Año de impresión", "ISBN"]
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

tk.Button(buttons_frame, text="Ver todo", width=12, command=view_command).grid(row=0, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Buscar", width=12, command=search_command).grid(row=1, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Agregar entrada", width=12, command=add_command).grid(row=2, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Actualizar", width=12, command=update_command).grid(row=3, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Borrar selección", width=12, command=delete_command).grid(row=4, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Limpiar", width=12, command=clear_fields).grid(row=5, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Guardar en Excel", width=12, command=export_to_excel).grid(row=6, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Cerrar", width=12, command=close_command).grid(row=7, column=0, padx=5, pady=5)

# Start the main loop
window.mainloop()
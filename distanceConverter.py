import tkinter as tk
from tkinter import ttk

def convert(event=None):
    from_unit = from_cbox.get()
    to_unit = to_cbox.get()

    try:
        unit_float = float(distance.get())
    except ValueError:
        result_label.config(text='Invalid characters')

    if from_unit == to_unit:
        result_label.config(text=f'{unit_float} {to_unit}')
        return

    preconversion = {
        'Kilometers': lambda x: x * 1000,
        'Miles': lambda x: x * 1609.344,
        'Feet': lambda x: x * 0.3048,
        'Yards': lambda x: x * 0.9144,
    }
    if from_unit != 'Meters':
        unit_float = preconversion[from_unit](unit_float)
        from_unit = 'Meters'
    
    conversions = {
        'Kilometers': lambda x: x * 0.001,
        'Miles': lambda x: x * 0.0006213712,
        'Feet': lambda x: x * 3.28084,
        'Yards': lambda x: x * 1.093613
    }
    result = conversions[to_unit](unit_float)
    result_label.config(text=f'{result:.2f} {to_unit}')

root = tk.Tk()
root.title('Distance Converter')
root.geometry('390x130')
root.resizable(False, False)
style = ttk.Style(root)

from_units = ['Meters', 'Kilometers', 'Miles', 'Feet', 'Yards']
to_units = ['Miles', 'Feet', 'Yards', 'Meters', 'Kilometers']


top_frame = ttk.Frame(root)
top_frame.grid(row=0, column=0)

style.configure(
    'label.TLabel',
    font=('Arial Black', 14, 'bold')
)

from_label = ttk.Label(top_frame, text='From:', style='label.TLabel')
from_label.grid(row=0, column=0)

from_cbox = ttk.Combobox(top_frame, values=from_units)
from_cbox.grid(row=0, column=1)
from_cbox.set('Meters')

to_label = ttk.Label(top_frame, text='To:', style='label.TLabel')
to_label.grid(row=0, column=2)

to_cbox = ttk.Combobox(top_frame, values=to_units)
to_cbox.grid(row=0, column=3)
to_cbox.set('Miles')


mid_frame = ttk.Frame(root)
mid_frame.grid(row=1, column=0)

distance = tk.StringVar()
entrybox = ttk.Entry(mid_frame, textvariable=distance)
entrybox.grid(row=0, column=0)
entrybox.bind('<Return>', convert)

button = ttk.Button(mid_frame, text='Convert', command=convert)
button.grid(row=0, column=1)

bottom_frame = ttk.Frame(root)
bottom_frame.grid(row=2, column=0)

style.configure(
    'result.TLabel',
    font=('monospace', 16, 'bold'),
    foreground='green'
)

result_label = ttk.Label(bottom_frame, text='', style='result.TLabel')
result_label.grid(row=0, column=0)

entrybox.focus()
root.mainloop()
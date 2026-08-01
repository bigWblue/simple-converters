import tkinter as tk
from tkinter import ttk

def switch():
    from_combo = input_cb.get()
    to_combo = output_cb.get()
    input_cb.set(to_combo)
    output_cb.set(from_combo)

def convert(event=None):
    entryboxStr = entrybox.get()
    from_combo = input_cb.get()
    to_combo = output_cb.get()

    if len(entryboxStr) > 15:
        result_label.config(text='Too long.')
        return
    elif len(entryboxStr) == 0:
        return

    conversions = {
        ('Celsius', 'Fahrenheit'): lambda x: x * 1.8 + 32,
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) / 1.8,
        ('Fahrenheit', 'Kelvin'): lambda x: (x + 459.67) * 5/9,
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x * 1.8) - 459.67
    }
    
    try:
        degrees = float(entryboxStr)
    except ValueError:
        result_label.config(text='Invalid temperature.')
        return

    if from_combo == to_combo:
        result_label.config(text=f'{degrees}º')
        return
    result = conversions[from_combo, to_combo](degrees)
    result_label.config(text=f'{result:.2f}º')

root = tk.Tk()
root.title('Temperature Converter')
root.geometry('385x115')
root.resizable(False, False)

input_temps = ['Celsius', 'Fahrenheit', 'Kelvin']
output_temps = ['Fahrenheit', 'Kelvin', 'Celsius']

style = ttk.Style(root)

# Top frame
top_frame = ttk.Frame(root)
top_frame.grid(row=0, column=0)

style.configure(
    'cbox.TCombobox',
    padding=8
)
input_cb = ttk.Combobox(top_frame, values=input_temps, style='cbox.TCombobox')
input_cb.set('Celsius')
input_cb.grid(row=0, column=0, padx=3, pady=3)

style.configure(
    'switch.TButton',
    width=4,
    font=('Arial', 16, 'bold'),
    background='red',
    foreground='red'
)
switch_btn = ttk.Button(top_frame, text='↔', style='switch.TButton', command=switch)
switch_btn.grid(row=0, column=1, padx=3, pady=3)

output_cb = ttk.Combobox(top_frame, values=output_temps, style='cbox.TCombobox')
output_cb.set('Fahrenheit')
output_cb.grid(row=0, column=2, padx=3, pady=3)

# Mid frame
mid_frame = ttk.Frame(root)
mid_frame.grid(row=1, column=0)

style.configure(
    'entry.TEntry',
    padding=4,
    font=('Consolas', 16)
)
temp = tk.StringVar()
entrybox = ttk.Entry(mid_frame, style='entry.TEntry', textvariable=temp)
entrybox.grid(row=0, column=0, padx=3)

style.configure(
    'convert.TButton',
    padding=4,
    background='green',
    foreground='green'
)
convert_btn = ttk.Button(mid_frame, text='Convert', style='convert.TButton', command=convert)
convert_btn.grid(row=0, column=1)

# Bottom frame
bottom_frame = ttk.Frame(root)
bottom_frame.grid(row=2, column=0)

style.configure(
    'result.TLabel',
    font=('Helvetica', 20, 'bold')
)
result_label = ttk.Label(bottom_frame, text='', style='result.TLabel')
result_label.grid(row=0, column=0)

entrybox.focus()
entrybox.bind('<Return>', convert)

root.mainloop()
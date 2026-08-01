import tkinter as tk
from tkinter import ttk

def roman_validator(numeral, roman_nums):
    is_valid = True
    max_count = {
        '1': ['IV', 'V', 'IX', 'XL', 'L', 'XC', 'CD', 'D', 'CM'],
        '3': ['I', 'X', 'C', 'M']
    }
    for num in (max_count['1'] + max_count['3']):
        counter = numeral.count(num)
        if num in max_count['1'] and counter > 1:
            is_valid = False
        elif num in max_count['3'] and counter > 3:
            is_valid = False
        if not is_valid:
            break
    
    return is_valid

def roman_translate(numeral):
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_validator(numeral, roman_nums):
        return 'Invalid'
    total = 0
    next_char = ''
    if numeral in roman_nums:
        return roman_nums[numeral]
    for char in numeral[::-1]:
        if not char in roman_nums.keys():
            return 'Invalid'
        if next_char == '':
            total += roman_nums[char]
            next_char = char
            continue
        if roman_nums[char] < roman_nums[next_char]:
            total -= roman_nums[char]
            next_char = char
        elif roman_nums[char] >= roman_nums[next_char]:
            total += roman_nums[char]
            next_char = char
    if 0 < total <= 3999:
        return total
    else:
        return 'Invalid'

def roman_maker(digit):
    result = ''
    roman_nums = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    countdown = int(digit)
    if countdown < 1 or countdown > 3999:
        return 'Invalid'
    
    for key in roman_nums:
        val = roman_nums[key]
        while val <= countdown:
            countdown -= val
            result += key
        if countdown == 0:
            break
    
    return result

def result_getter(event=None):
    result = ''
    curr_title = title_label.cget('text')
    user_input = entrybox.get()
    if not user_input:
        return
    if user_input.isdigit():
        title_label.config(text='Number to Roman')
        result = roman_maker(user_input)
    else:
        title_label.config(text='Roman to Number')
        result = roman_translate(user_input)

    result_label.config(text=f'{result}')

root = tk.Tk()
root.title('XV')
root.geometry('190x100')
root.resizable(False, False)

style = ttk.Style(root)

style.configure(
    'title.TLabel',
    font=('Consolas', 16, 'bold')
)
title_label = ttk.Label(root, text='Roman to Number', style='title.TLabel')
title_label.grid(row=0, column=0, columnspan=2)

user_input = tk.StringVar()
entrybox = ttk.Entry(root, textvariable=user_input)
entrybox.grid(row=1, column=0)
entrybox.bind('<Return>', result_getter)

convert_btn = tk.Button(root, text='convert', command=result_getter)
convert_btn.grid(row=1, column=1)

style.configure(
    'result.TLabel',
    font=('monospace', 20, 'bold')
)
result_label = ttk.Label(root, text='', style='result.TLabel')
result_label.grid(row=2, column=0, columnspan=2)

entrybox.focus()

root.mainloop()
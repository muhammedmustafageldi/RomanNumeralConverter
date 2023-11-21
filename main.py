from tkinter import *
from tkinter import messagebox

root = Tk()
FONT = ('poppins', 25, 'bold')


def window_settings():
    bg1 = '#f87a17'
    bg2 = '#fd580a'
    root.title('Roma Numeral Converter')
    root.config(bg=bg1)
    root.iconbitmap('convert.ico')

    label_title = Label(root, text='Converter', font=FONT, bg=bg1)
    label_title.pack(padx=25, pady=20)

    roma_label = Label(root, text=' Please enter the number of roma you want to convert ', bg=bg1)
    roma_label.pack(padx=20)

    entry = Entry(root, bg=bg2, fg='white')
    entry.pack(padx=25, pady=10)
    entry.focus()

    button = Button(root, text='Convert', bg=bg2,
                    command=lambda: get_input_user(entry=entry, result_label=result_label))
    button.pack(padx=10, pady=10)

    divider = Canvas(root, height=1, bg=bg2)
    divider.pack(fill='x')

    result_label = Label(root, text=f'Result: ', font=FONT, bg=bg1)
    result_label.pack(padx=10, pady=10)


def get_input_user(entry, result_label):
    user_input = entry.get()

    validate = validator(user_input)

    if validate:
        # keep going transaction
        result = convert_to_int(user_input)
        result_label.config(text=f'Result: {result}')

    else:
        # Error
        messagebox.showerror(title='Error!', message='Invalid Value!')


def validator(user_input):
    roma_chars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    validate = True
    value_quantity = 1
    current_char = user_input[0]

    for char in user_input[1:]:

        if char not in roma_chars:
            validate = False
            break
        else:
            if char == current_char:
                value_quantity += 1
            else:
                current_char = char
                value_quantity = 1

        if value_quantity > 3:
            validate = False
            break

    return validate


def convert_to_int(user_input):
    roma_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    previous_value = 0

    for value in user_input[::-1]:

        numeric_value = roma_dict[value]

        if numeric_value >= previous_value:
            total += numeric_value
        else:
            total -= numeric_value

        previous_value = numeric_value

    return total


window_settings()

root.mainloop()

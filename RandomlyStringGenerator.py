# -*- coding: utf-8 -*-
# @Time    : 4/25/2019 10:20 AM
# @Author  : Yemor
# @Email   : albert971@qq.com
# @File    : RandomlyStringGeneration.py
# @Software: PyCharm

import random
from tkinter import *


# 生成随机字符串
def random_string(str_len=18, alpha=True, digit=True, punct=True, lower=True, upper=True):  # {
    base_str = ""
    lower_str = "abcdefghijklmnopqrstuvwxyz"
    upper_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit_str = "0123456789"
    punct_str = "!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~"
    if alpha:  # {
        if lower:
            base_str += lower_str
        if upper:
            base_str += upper_str
    # }
    if digit:  # {
        base_str += digit_str
    # }
    if punct:  # {
        base_str += punct_str
    # }
    while True:
        lower_num = 0
        upper_num = 0
        digit_num = 0
        punct_num = 0
        rand_str = ""
        while str_len > 0:
            tmp = random.sample(base_str, 1)
            tmp = tmp[0]
            rand_str += tmp
            if tmp.islower():
                lower_num += 1
            elif tmp.isupper():
                upper_num += 1
            elif tmp.isdigit():
                digit_num += 1
            else:
                punct_num += 1
            str_len -= 1
        if lower_num != 0 or (lower is False):
            if upper_num != 0 or (upper is False):
                if digit_num != 0 or (digit is False):
                    if punct_num != 0 or (punct is False):
                        break
    return rand_str


# }


def len_check_change():  # {
    if len_check_state.get():
        len_input_entry.config(state=NORMAL)
    else:
        len_input_entry.config(state=DISABLED)


# }

def alpha_check_change():  # {
    if alpha_check_state.get():
        upper_check_entry.config(state=NORMAL)
        lower_check_entry.config(state=NORMAL)
    else:
        upper_check_entry.config(state=DISABLED)
        lower_check_entry.config(state=DISABLED)


# }

def generate_tap():  # {
    len_state = True if len_check_state.get() == 1 else False
    alpha_state = True if alpha_check_state.get() == 1 else False
    upper_state = True if upper_check_state.get() == 1 else False
    lower_state = True if lower_check_state.get() == 1 else False
    punct_state = True if punct_check_state.get() == 1 else False
    digit_state = True if digit_check_state.get() == 1 else False
    if not upper_state and not lower_state and not punct_state and not digit_state:
        ret = "please select at lease one type of character"
    elif len_state:
        getstr = len_input_text.get()
        if len(getstr) > 0:
            strtoint = int(len_input_text.get())
            ret = random_string(str_len=strtoint, alpha=alpha_state, upper=upper_state, lower=lower_state,
                                punct=punct_state, digit=digit_state)
        else:
            ret = "please input you need length"
    else:
        ret = random_string(alpha=alpha_state, upper=upper_state, lower=lower_state, punct=punct_state,
                            digit=digit_state)
    hint_string_var.set(ret)
    text_entry.config(state=NORMAL)


# }

def exit_tap():  # {
    root_windows.destroy()


# }

root_windows = Tk()

root_windows.title("RandomlyStringGeneration")
root_windows.geometry("300x200")
text_area = Frame(root_windows)
check_area = Frame(root_windows)
button_area = Frame(root_windows)

hint_string_var = StringVar()
hint_string_var.set("have not init yet")

text_entry = Entry(text_area, state=DISABLED, justify=CENTER, textvariable=hint_string_var)
text_message = Message(text_area)

len_check_state = IntVar()
alpha_check_state = IntVar()
upper_check_state = IntVar()
lower_check_state = IntVar()
punct_check_state = IntVar()
digit_check_state = IntVar()
len_input_text = StringVar()

len_check_label = Label(check_area, text="setlen")
len_check_label.grid(row=0, column=0, sticky=W)
len_check_entry = Checkbutton(check_area, justify=CENTER, variable=len_check_state, command=len_check_change)
len_check_entry.grid(row=0, column=1, sticky=W)

len_input_label = Label(check_area, text="length")
len_input_label.grid(row=0, column=3, sticky=W)
len_input_entry = Entry(check_area, justify=CENTER, textvariable=len_input_text, state=DISABLED)
len_input_entry.grid(row=0, column=4, sticky=W)

alpha_check_label = Label(check_area, text="alpha")
alpha_check_label.grid(row=1, column=0, sticky=W)
alpha_check_entry = Checkbutton(check_area, justify=CENTER, variable=alpha_check_state, command=alpha_check_change)
alpha_check_entry.grid(row=1, column=1, sticky=W)

upper_check_label = Label(check_area, text="upper")
upper_check_label.grid(row=2, column=0, sticky=W)
upper_check_entry = Checkbutton(check_area, justify=CENTER, variable=upper_check_state, state=DISABLED)
upper_check_entry.grid(row=2, column=1, sticky=W)

lower_check_label = Label(check_area, text="lower")
lower_check_label.grid(row=2, column=3, sticky=W)
lower_check_entry = Checkbutton(check_area, justify=CENTER, variable=lower_check_state, state=DISABLED)
lower_check_entry.grid(row=2, column=4, sticky=W)

punct_check_label = Label(check_area, text="punct")
punct_check_label.grid(row=3, column=0, sticky=W)
punct_check_entry = Checkbutton(check_area, justify=CENTER, variable=punct_check_state)
punct_check_entry.grid(row=3, column=1, sticky=W)

digit_check_label = Label(check_area, text="numric")
digit_check_label.grid(row=3, column=3, sticky=W)
digit_check_entry = Checkbutton(check_area, justify=CENTER, variable=digit_check_state)
digit_check_entry.grid(row=3, column=4, sticky=W)

check_area.columnconfigure(0, weight=1)
check_area.columnconfigure(1, weight=1)
check_area.columnconfigure(2, weight=1)
check_area.columnconfigure(3, weight=1)
check_area.columnconfigure(4, weight=1)

generate_button = Button(button_area, text="Generate", command=generate_tap)
exit_button = Button(button_area, text="Exit", command=exit_tap)

text_area.pack(fill=X)
text_entry.pack(fill=X)

check_area.pack()

button_area.pack()
generate_button.grid(row=0, column=0, padx=10, pady=10, sticky=E + W)
exit_button.grid(row=0, column=1, padx=10, pady=10, sticky=E + W)
button_area.columnconfigure(0, weight=1)
button_area.columnconfigure(1, weight=1)

# 进入消息循环
root_windows.mainloop()

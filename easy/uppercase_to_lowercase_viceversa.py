"""
Lowercase to Uppercase and Vice Versa
Given a string S consisting of only English alphabets, write a program to convert each lowercase alphabet
in it to its uppercase form and each uppercase alphabet in it to its lowercase form.
"""

def convert(data):

    out_string = ""
    for char in data:
        if char.islower():
            out_string += char.upper()
        else:
            out_string += char.lower()

    return out_string

print(convert("helLO WORld"))

# letter = '''Dear <\\NAME\\>\n\tYou are selected!\n\t<\\DATE\\>'''
letter = '''Dear <!NAME!>
    You are selected!

    <!DATE!>'''

name = input("enter the name\n")
date = input("enter the date\n")
letter = letter.replace("<!NAME!>", name)
letter = letter.replace("<!DATE!>", date)
print(letter)
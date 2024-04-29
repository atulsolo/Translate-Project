from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from googletrans import Translator

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

def translate():
    language_1 = t1.get("1.0", "end-1c")
    cl = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the box')
    else:
        t2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(language_1, dest=cl)
        t2.insert('end', output.text)

def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

root = tk.Tk()
root.title('Language Translator')
root.configure(bg="#F0F0F0")  # Setting background color to light gray

# Get the window dimensions
window_width = 1280
window_height = 720

# Auto detect language ComboBox
a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('Verdana', 10, 'bold'))
auto_detect['values'] = ('Auto Detect',)
auto_detect.place(x=30, y=70)
auto_detect.current(0)

# Language selection ComboBox
l = tk.StringVar()
choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('Verdana', 10, 'bold'))
choose_langauge['values'] = (
    'Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian',
    'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch',
    'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German',
    'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic',
    'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda',
    'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy',
    'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar', 'Nepali', 'Norwegian', 'Odia',
    'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian',
    'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili',
    'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur',
    'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
choose_langauge.place(x=290, y=70)
choose_langauge.current(0)

# Input and output text boxes
t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

# Translate and Clear buttons with a black background and white text
translate_button = ttk.Button(root, text="Translate", command=translate, width=12, style='Black.TButton')
translate_button.place(x=150, y=280)

clear_button = ttk.Button(root, text="Clear", command=clear, width=12, style='Black.TButton')
clear_button.place(x=280, y=280)

# Styling for buttons
button_style = ttk.Style()
button_style.configure('Black.TButton', font=('Verdana', 10, 'bold'), background='black', foreground='black')

# Center the window
center_window(root, window_width, window_height)

root.mainloop()

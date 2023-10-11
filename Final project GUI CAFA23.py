"""
Final project GUI 
Chad Allen 10/8/23
language translator GUI program
"""
from tkinter import *
from googletrans import Translator
from textblob import TextBlob
from tkinter import ttk, messagebox
translator = Translator()


# text boxes
root = Tk()
root.title('Language translator')
root.geometry("880x300")

def translate_it():
    # delete previous translations
    translated_text.delete(1.0, END)
    try:
        # Get languages from dictionary keys
        # Get from language key
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
        
        
        # Get to language key
        for key, value in languages.items():
            if (value == translated_combo.get()): 
                to_language_key = key
         
        # turn original text into textblob
        words = TextBlob.TextBlob(original_text.get(1.0, END))
        
        # translate text
        words = words.translate(from_lang=from_language_key , to=to_language_key)
        
        # output translated text
        translated_text.insert(1.0, words)
        
    except Exception as e:
        messagebox.showerror("Translator", e)
        
        
        
def clear():
    #clear text boxes
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# get language list from google translate
#languages = googletrans.LANGUAGES
#print('languages')
languages=Translator.LANGUAGES 

language_list = list(languages.values())
print(language_list)

# text boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate", font=("Helvetica",24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

# combo boxes 
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

# clear button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()
import tkinter as tk
from tkinter import ttk

# Define dictionaries with 20 words in Latin, French, Spanish, German, and Greek
dictionary = {
    "apple": {"Latin": "malum", "French": "pomme", "Spanish": "manzana", "German": "Apfel", "Greek": "μήλο"},
    "book": {"Latin": "liber", "French": "livre", "Spanish": "libro", "German": "Buch", "Greek": "βιβλίο"},
    "car": {"Latin": "carrus", "French": "voiture", "Spanish": "coche", "German": "Auto", "Greek": "αυτοκίνητο"},
    "dog": {"Latin": "canis", "French": "chien", "Spanish": "perro", "German": "Hund", "Greek": "σκύλος"},
    "house": {"Latin": "domus", "French": "maison", "Spanish": "casa", "German": "Haus", "Greek": "σπίτι"},
    "love": {"Latin": "amor", "French": "amour", "Spanish": "amor", "German": "Liebe", "Greek": "αγάπη"},
    "school": {"Latin": "schola", "French": "école", "Spanish": "escuela", "German": "Schule", "Greek": "σχολείο"},
    "friend": {"Latin": "amicus", "French": "ami", "Spanish": "amigo", "German": "Freund", "Greek": "φίλος"},
    "water": {"Latin": "aqua", "French": "eau", "Spanish": "agua", "German": "Wasser", "Greek": "νερό"},
    "food": {"Latin": "cibus", "French": "nourriture", "Spanish": "comida", "German": "Essen", "Greek": "τροφή"},
    "sun": {"Latin": "sol", "French": "soleil", "Spanish": "sol", "German": "Sonne", "Greek": "ήλιος"},
    "moon": {"Latin": "luna", "French": "lune", "Spanish": "luna", "German": "Mond", "Greek": "φεγγάρι"},
    "tree": {"Latin": "arbor", "French": "arbre", "Spanish": "árbol", "German": "Baum", "Greek": "δέντρο"},
    "family": {"Latin": "familia", "French": "famille", "Spanish": "familia", "German": "Familie", "Greek": "οικογένεια"},
    "music": {"Latin": "musica", "French": "musique", "Spanish": "música", "German": "Musik", "Greek": "μουσική"},
    "work": {"Latin": "labor", "French": "travail", "Spanish": "trabajo", "German": "Arbeit", "Greek": "εργασία"},
    "money": {"Latin": "pecunia", "French": "argent", "Spanish": "dinero", "German": "Geld", "Greek": "χρήματα"},
    "happiness": {"Latin": "felicitas", "French": "bonheur", "Spanish": "felicidad", "German": "Glück", "Greek": "ευτυχία"},
    "peace": {"Latin": "pax", "French": "paix", "Spanish": "paz", "German": "Frieden", "Greek": "ειρήνη"},
    "beauty": {"Latin": "pulchritudo", "French": "beauté", "Spanish": "belleza", "German": "Schönheit", "Greek": "ομορφιά"}
}

# Function to display translations
def show_translation():
    selected_word = word_var.get()
    if selected_word in dictionary:
        translations = dictionary[selected_word]

    else:
        result.set("Word not found!")

# Create the main application window
root = tk.Tk()
root.title("Multilingual Dictionary")

# UI Elements
tk.Label(root, text="Select a word:").grid(row=0, column=0, padx=10, pady=10)

word_var = tk.StringVar()
word_dropdown = ttk.Combobox(root, textvariable=word_var)
word_dropdown['values'] = list(dictionary.keys())  # Load word choices
word_dropdown.grid(row=0, column=1, padx=10, pady=10)

btn_translate = tk.Button(root, text="Translate", command=show_translation)
btn_translate.grid(row=1, column=0, columnspan=2, pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, justify="left", font=("Arial", 12)).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI application
root.mainloop()

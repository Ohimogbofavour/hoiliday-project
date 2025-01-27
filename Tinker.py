import tkinter
from tkinter import messagebox


# Define the dictionaries
hausa_dict = {
    "sannu": "hello",
    "na gode": "thank you",
    "ina kwana": "how are you?",
    "lafiya lau": "fine",
    "barkada sallama": "goodbye",
    "karanta":"read",
    "gida":"home",
    "wasa":"play",
    "shiru":"quiet",
    "kudi":"momey",
    "babba":"big",
    "yau":"today",
    "dare":"night",
    "maraba":"you are welcome",
    "ture":"flower",
    "wawa":"fool",
    "manta":"forget",
    "front":"gaba",
    "fowl":"kaza",
    "fly":"kuda",
    "foot":"kafa"
    
}

igala_dict = {
    "adu": "people",
    "ote": "house",
    "k'ondo": "good",
    "ode": "thank you",
    "ade": "come",
    "pioola":"law",
    "chaaka":"farm",
    "duu":"tool",
    "hair":"oji",
    "nose":"imo",
    "ana":"in-law",
    "agbari":"skull",
    "okoto":"brain",
    "eju":"eye",
    "leg":"ere",
    "nine":"ela",
    "je":"eat",
    "okuta":"stone",
    "efa":"six",
    "adua":"poor",
    "eie":"gift",
    "ekwutee":"plenty",
    "okoo":"pig"

}

efik_dict = {
    "owo": "people",
    "ufok": "house",
    "nno": "good",
    "afiak": "thank you",
    "kama": "come",
    "kot":"call",
    "atwa":"palmwine",
    "sak":"laugh",
    "uruk":"rope",
    "utim":"times",
    "mbi":"ambush",
    "awa":"blueness",
    "utin":"sun",
    "utib":"creek",
    "mbo":"seedling",
    "kap":"carve",
    "ada":"barren woman",
    "adan":"jaundice",
    "akaj":"forest",
    "afan":"a kind of fish"
}
igbo_dict = {
    "ndi": "people",
    "ụlọ": "house",
    "kedu": "how",
    "nọọ": "good",
    "daalụ": "thank you",
    "akwa":"cry",
    "ochi":"laugh",
    "aja":"sacrfice",
    "nti":"ear",
    "anya":"eye",
    "ntutu isi":"hair",
    "isi":"head",
    "imi":"nose",
    "afa onu":"moustache",
    "ala aka":"arm",
    "aka":"hand",
    "mpisi aka":"finger",
    "ukwu":"leg",
    "ikpere":"knee",
    "obu ukwu":"foot"
}
# Create the main window
window = Tk()
window.title("Nigerian Language Dictionary")

# Create a label for the language selection
language_label = Label(window, text="Select Language:")
language_label.pack()

# Create a dropdown menu for language selection
selected_language = StringVar(window)
selected_language.set("Hausa")  # Default language
language_menu = OptionMenu(window, selected_language, "Hausa", "Yoruba", "Igbo", "Igala", "Efik")
language_menu.pack()

# Create a label for the word input
word_label = Label(window, text="Enter Word:")
word_label.pack()

# Create an entry field for word input
word_entry = Entry(window)
word_entry.pack()

# Create a button to search for the word
search_button = Button(window, text="Search", command=lambda: search_word())
search_button.pack()

# Create a label to display the meaning
meaning_label = Label(window, text="")
meaning_label.pack()

# Function to search for the word
def search_word():
    word = word_entry.get()
    language = selected_language.get()

    if language == "Hausa":
        meaning = hausa_dict.get(word, "Word not found")
    elif language == "Yoruba":
        meaning = yoruba_dict.get(word, "Word not found")
    elif language == "Igbo":
        meaning = igbo_dict.get(word, "Word not found")
    elif language == "Igala":
        meaning = igala_dict.get(word, "Word not found")
    elif language == "Efik":
        meaning = efik_dict.get(word, "Word not found")
    else:
        meaning = "Invalid language selected"

    meaning_label.config(text=f"Meaning: {meaning}")

# Run the GUI
window.mainloop()

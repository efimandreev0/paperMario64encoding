from tkinter import *
from tkinter import ttk


def copy():
    label.clipboard_clear()
    label.clipboard_append(label["text"])
    
def show_message():
    enc = "utf-8"

    BRACKET_READ = False
    LETTERS = {"F7 ":" ","01 ": "!", "02 ": '"',"03 ": "#","04 ": "$","05 ": "%"
,"06 ": "&","07 ": "'","08 ": "(","09 ": ")","0A ": "*","0B ": "+","0C ": ","
,"0D ": "-","0E ": ".","0F ": "/","10 ": "0","11 ": "1","12 ": "2","13 ": "3"
,"14 ": "4","15 ": "5","16 ": "6","17 ": "7","18 ": "8","19 ": "9","1A ":  ":"
,"1B ": ";","1C ": "<","1D ": "=","1E ": ">","1F ": "?","20 ": "@","21 ": "A"
,"22 ": "B","23 ": "C","24 ": "D","25 ": "E","26 ": "F","27 ": "G","28 ": "H"
,"29 ": "I","2A ": "J","2B ": "K","2C ": "L","2D ": "M","2E ": "N","2F ": "O"
,"30 ": "P","31 ": "Q","32 ": "R","33 ": "S","34 ": "T","35 ": "U","36 ": "V"
,"37 ": "W","38 ": "X","39 ": "Y","3A ": "Z","3B ": "[","3C ": "¥","3D ": "]","3E ": "^"
,"3F ": "_","40 ": "`","41 ": "a","42 ": "b","43 ": "c","44 ": "d","45 ": "e","46 ": "f"
,"47 ": "g","48 ": "h","49 ": "i","4A ": "j","4B ": "k","4C ": "l","4D ": "m","4E ": "n"
,"4F ": "o","50 ": "p","51 ": "q","52 ": "r","53 ": "s","54 ": "t","55 ": "u","56 ": "v"
,"57 ": "w","58 ": "x","59 ": "y","5A ": "z","5B ": "{","5C ": "|","5D ": "}","5E ": "~"
,"5F ": "°","60 ": "À","61 ": "Á","62 ": "Â","63 ": "Ä","64 ": "Ç","65 ": "È","66 ": "É"
,"67 ": "Ê","68 ": "Ë","69 ": "Ì","6A ": "Í","6B ": "Î","6C ": "Ï","6D ": "Ñ","6E ": "Ò"
,"6F ": "Ó","70 ": "Ô","71 ": "Ö","72 ": "Ù","73 ": "Ú","74 ": "Û","75 ": "Ü","76 ": "ß"
,"77 ": "à","78 ": "á","79 ": "â","7A ": "ä","7B ": "ç","7C ": "è","7D ": "é","7E ": "ê"
,"7F ": "ë","80 ": "ì","81 ": "í","82 ": "î","83 ": "ï","84 ": "ñ","85 ": "ò","86 ": "ó"
,"87 ": "ô","88 ": "ö","89 ": "ù","8A ": "ú","8B ": "û","8C ": "ü","8D ": "¡","8E ": "¿"
,"8F ": "ª","A2 ": "“","A3 ": "”","A4 ": "‘","A5 ": "å"}
    LETTERS_REV = {k: v for v, k in LETTERS.items()}
    text = entry.get("1.0",END)
    text_code = ''
    for symbol in text:
        if symbol in LETTERS_REV:
            text_code += LETTERS_REV[symbol]
        else:
            text_code += symbol
    label["text"] = text_code
 
root = Tk()
root.title("METANIT.COM")
root.geometry("430x350")
 
entry=Text(root, width=50, height=10)
entry.pack()

btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Copy", command=copy)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=90, pady=0)
  
root.mainloop()
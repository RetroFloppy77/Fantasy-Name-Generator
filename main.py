#!/usr/bin/env python3
"""
Fantasy Name Generator
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Generatore di nomi fantasy basato su categorie con oltre 100 
combinazioni coerenti per ciascuna classe/razza.
"""

import random
import tkinter as tk
from tkinter import font, ttk

# Dizionario delle sillabe/radici per categoria per garantire oltre 100 nomi coerenti ciascuna
NAME_DATA = {
    "Guerriero": {
        "prefissi": ["Val", "Thor", "Gar", "Grim", "Karn", "Brog", "Drak", "Ron", "Krag", "Vond", "Hroth", "Bork"],
        "centrali": ["ar", "or", "un", "ok", "im", "ath", "ek", "ulf", "gard", "thor"],
        "suffissi": ["an", "or", "rok", "mar", "ulf", "ix", "gar", "thor", "ack", "stor", "bar", "zorn"]
    },
    "Mago": {
        "prefissi": ["El", "Ael", "Mor", "Zand", "Xar", "Vael", "Ely", "Thal", "Nyx", "Ign", "Cor", "Pyth"],
        "centrali": ["anth", "ath", "or", "ius", "ist", "yn", "aex", "and", "ox", "end"],
        "suffissi": ["ius", "or", "yth", "ion", "ath", "ex", "zar", "marr", "dor", "wyn", "is", "us"]
    },
    "Ladro": {
        "prefissi": ["Vex", "Ske", "Zev", "Kye", "Nyx", "Ryn", "Jax", "Trix", "Shad", "Dusk", "Vip", "Flick"],
        "centrali": ["en", "ix", "or", "un", "eth", "az", "iv", "ox", "ash", "ik"],
        "suffissi": ["ix", "en", "ar", "is", "osk", "ith", "un", "ick", "ace", "shadow", "sh", "k"]
    },
    "Paladino": {
        "prefissi": ["Al", "Sol", "Val", "San", "Aur", "Ron", "Gala", "Cel", "Domin", "Aet", "Ver", "Lumin"],
        "centrali": ["or", "an", "ar", "en", "ius", "ath", "el", "ost", "ind", "iv"],
        "suffissi": ["or", "ius", "an", "el", "ion", "ath", "ar", "us", "dor", "ian", "os", "elms"]
    },
    "Amazzone": {
        "prefissi": ["Zen", "Thal", "Bry", "Lys", "Kall", "Xen", "Ny", "Pent", "Hipp", "Rhox", "Valk", "Mel"],
        "centrali": ["ia", "ae", "is", "or", "yn", "en", "ath", "ox", "il", "an"],
        "suffissi": ["ia", "is", "ora", "eth", "ana", "ys", "a", "ex", "ine", "iah", "aera", "iael"]
    },
    "Nano": {
        "prefissi": ["Thor", "Gim", "Balg", "Durg", "Thrain", "Mor", "Krag", "Brom", "Har", "Fund", "Dur", "Kaz"],
        "centrali": ["in", "or", "un", "ak", "ok", "und", "ard", "im", "om", "ek"],
        "suffissi": ["ur", "in", "ok", "ik", "ar", "um", "grimm", "helm", "beard", "stone", "forge", "fist"]
    },
    "Elfo": {
        "prefissi": ["Ael", "Fael", "Sil", "Lyr", "Thal", "Nim", "Elen", "Gal", "Il", "Val", "Aer", "Syl"],
        "centrali": ["an", "en", "ith", "ari", "ael", "iel", "or", "ion", "enor", "amil"],
        "suffissi": ["ion", "iel", "ath", "ia", "wen", "or", "as", "is", "andra", "yl", "ian", "ith"]
    },
    "Barbaro": {
        "prefissi": ["Krom", "Hroth", "Ul", "Grok", "Tor", "Skol", "Varg", "Bol", "Rug", "Thorg", "Zul", "Karr"],
        "centrali": ["og", "ak", "un", "ok", "ath", "ig", "ar", "or", "ul", "ash"],
        "suffissi": ["ar", "ok", "un", "ax", "or", "ath", "zak", "rok", "skull", "bane", "fury", "mAW"]
    }
}

def generate_fantasy_name(category):
    """Genera un nome fantasy coerente combinando prefissi, parti centrali e suffissi."""
    data = NAME_DATA.get(category, NAME_DATA["Guerriero"])
    # Creiamo un'ampia varietà di combinazioni (molto oltre 100)
    prefix = random.choice(data["prefissi"])
    middle = random.choice(data["centrali"]) if random.random() > 0.3 else ""
    suffix = random.choice(data["suffissi"])
    
    # Se il nome è troppo corto o per aggiungere variabilità stilistica
    name = f"{prefix}{middle}{suffix}".capitalize()
    return name

class FantasyNameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fantasy Name Generator")
        self.root.geometry("650x550")
        self.root.minsize(600, 500)
        self.root.configure(bg="#1e1e2e")

        # Stile dell'interfaccia
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.setup_ui()

    def setup_ui(self):
        # Header principale al centro
        header_frame = tk.Frame(self.root, bg="#1e1e2e")
        header_frame.pack(fill=tk.X, pady=25)

        title_font = font.Font(family="Helvetica", size=22, weight="bold")
        author_font = font.Font(family="Helvetica", size=10, slant="italic")

        title_label = tk.Label(header_frame, text="Fantasy Name Generator", font=title_font, fg="#cdd6f4", bg="#1e1e2e")
        title_label.pack()

        author_text = "Autore: Stefano Peris  |  Email: stefanoperis.github@gmail.com"
        author_label = tk.Label(header_frame, text=author_text, font=author_font, fg="#a6adc8", bg="#1e1e2e")
        author_label.pack(pady=(5, 0))

        # Separatore visivo
        sep = ttk.Separator(self.root, orient="horizontal")
        sep.pack(fill=tk.X, padx=40, pady=10)

        # Sezione pulsanti categorie (Griglia centrale)
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(pady=15)

        categories = list(NAME_DATA.keys())
        
        # Creazione dei pulsanti in una griglia 4x2
        row_idx = 0
        col_idx = 0
        for cat in categories:
            btn = tk.Button(
                btn_frame, 
                text=cat, 
                font=("Helvetica", 11, "bold"),
                bg="#313244", 
                fg="#cdd6f4",
                activebackground="#45475a",
                activeforeground="#ffffff",
                relief=tk.FLAT,
                width=14,
                height=2,
                cursor="hand2",
                command=lambda c=cat: self.on_category_click(c)
            )
            btn.grid(row=row_idx, column=col_idx, padx=10, pady=10)
            
            col_idx += 1
            if col_idx > 3:
                col_idx = 0
                row_idx += 1

        # Area di output al centro in basso
        output_frame = tk.Frame(self.root, bg="#1e1e2e")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        self.result_var = tk.StringVar()
        self.result_var.set("Seleziona una categoria sopra per generare un nome")

        result_label_title = tk.Label(output_frame, text="Nome Generato:", font=("Helvetica", 10, "bold"), fg="#89b4fa", bg="#1e1e2e")
        result_label_title.pack(pady=(0, 5))

        self.result_display = tk.Label(
            output_frame, 
            textvariable=self.result_var, 
            font=("Georgia", 18, "bold"), 
            fg="#fab387", 
            bg="#11111b",
            relief=tk.RIDGE,
            bd=2,
            padx=20,
            pady=15
        )
        self.result_display.pack(fill=tk.X, expand=False)

    def on_category_click(self, category):
        """Gestisce il click del pulsante generando e mostrando il nome."""
        name = generate_fantasy_name(category)
        self.result_var.set(f"[{category}]  {name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FantasyNameApp(root)
    root.mainloop()

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

# ==============================================================================
# STRUTTURA DATI LINGUISTICA
# ==============================================================================
# Dizionario principale contenente le matrici di sillabe per ciascuna categoria.
# Per aggiungere una nuova categoria o modificare i suoni dei nomi, è sufficiente
# espandere o modificare le liste di "prefissi", "centrali" e "suffissi".
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
        "suffissi": ["ar", "ok", "un", "ax", "or", "ath", "zak", "rok", "skull", "bane", "fury", "maw"]
    }
}

# ==============================================================================
# MOTORE DI GENERAZIONE PROCEDURALE
# ==============================================================================
def generate_fantasy_name(category):
    """
    Genera un nome fantasy casuale e coerente per la categoria specificata.
    
    Logica:
    1. Estrae le liste di sillabe associate alla categoria scelta.
    2. Seleziona casualmente un prefisso e un suffisso.
    3. Con una certa probabilità (70%), inserisce una parte centrale per variare la lunghezza.
    4. Concatena le parti e capitalizza la prima lettera.
    """
    # Fallback di sicurezza su "Guerriero" se la categoria non viene trovata
    data = NAME_DATA.get(category, NAME_DATA["Guerriero"])
    
    prefix = random.choice(data["prefissi"])
    # Inserisce la parte centrale solo se il numero casuale è > 0.3 (probabilità del 70%)
    middle = random.choice(data["centrali"]) if random.random() > 0.3 else ""
    suffix = random.choice(data["suffissi"])
    
    # Assemblaggio finale della stringa del nome
    name = f"{prefix}{middle}{suffix}".capitalize()
    return name

# ==============================================================================
# INTERFACCIA GRAFICA (GUI)
# ==============================================================================
class FantasyNameApp:
    def __init__(self, root):
        """Inizializza la finestra principale e configura lo stile dell'applicazione."""
        self.root = root
        self.root.title("Fantasy Name Generator")
        self.root.geometry("650x550")
        self.root.minsize(600, 500)
        self.root.configure(bg="#1e1e2e") # Sfondo scuro elegante

        # Configurazione del tema grafico Tkinter
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Avvia la creazione dei componenti dell'interfaccia
        self.setup_ui()

    def setup_ui(self):
        """Costruisce e posiziona tutti gli elementi visivi della finestra."""
        
        # ----------------------------------------------------------------------
        # 1. HEADER (Intestazione centrale con Nome e Autore)
        # ----------------------------------------------------------------------
        header_frame = tk.Frame(self.root, bg="#1e1e2e")
        header_frame.pack(fill=tk.X, pady=25)

        title_font = font.Font(family="Helvetica", size=22, weight="bold")
        author_font = font.Font(family="Helvetica", size=10, slant="italic")

        title_label = tk.Label(header_frame, text="Fantasy Name Generator", font=title_font, fg="#cdd6f4", bg="#1e1e2e")
        title_label.pack()

        author_text = "Autore: Stefano Peris  |  Email: stefanoperis.github@gmail.com"
        author_label = tk.Label(header_frame, text=author_text, font=author_font, fg="#a6adc8", bg="#1e1e2e")
        author_label.pack(pady=(5, 0))

        # Linea divisoria estetica
        sep = ttk.Separator(self.root, orient="horizontal")
        sep.pack(fill=tk.X, padx=40, pady=10)

        # ----------------------------------------------------------------------
        # 2. GRIGLIA DEI PULSANTI (Categorie)
        # ----------------------------------------------------------------------
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(pady=15)

        categories = list(NAME_DATA.keys())
        
        # Disposizione dinamica dei pulsanti in una griglia 4 colonne x 2 righe
        row_idx = 0
        col_idx = 0
        for cat in categories:
            # Creazione del pulsante per ogni categoria presente in NAME_DATA
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
                # Passa la categoria corrente alla funzione di callback tramite lambda
                command=lambda c=cat: self.on_category_click(c)
            )
            btn.grid(row=row_idx, column=col_idx, padx=10, pady=10)
            
            # Gestione della griglia: passa alla colonna successiva, o va a capo dopo 4 colonne
            col_idx += 1
            if col_idx > 3:
                col_idx = 0
                row_idx += 1

        # ----------------------------------------------------------------------
        # 3. AREA DI OUTPUT (Display del nome generato in basso al centro)
        # ----------------------------------------------------------------------
        output_frame = tk.Frame(self.root, bg="#1e1e2e")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        # Variabile di controllo associata alla label del nome generato
        self.result_var = tk.StringVar()
        self.result_var.set("Seleziona una categoria sopra per generare un nome")

        result_label_title = tk.Label(output_frame, text="Nome Generato:", font=("Helvetica", 10, "bold"), fg="#89b4fa", bg="#1e1e2e")
        result_label_title.pack(pady=(0, 5))

        # Display visivo centrale con stile a riquadro
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
        """
        Funzione di callback eseguita alla pressione di un pulsante categoria.
        Genera il nome tramite la funzione dedicata e aggiorna la UI.
        """
        name = generate_fantasy_name(category)
        # Aggiorna il testo visualizzato nel riquadro in basso
        self.result_var.set(f"[{category}]  {name}")

# ==============================================================================
# PUNTO DI INGRESSO (Main)
# ==============================================================================
if __name__ == "__main__":
    # Avvio dell'applicazione principale Tkinter
    root = tk.Tk()
    app = FantasyNameApp(root)
    root.mainloop()

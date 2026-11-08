# Fantasy Name Generator 🗡️✨

Un generatore di nomi fantasy leggero, modulare e interattivo scritto in **Python 3.12**, progettato per creare nomi unici, evocativi e perfettamente coerenti con diverse classi e razze fantasy (Guerrieri, Maghi, Ladri, Paladini, Amazzoni, Nani, Elfi e Barbari). 

---

## 👨‍💻 Autore e Contatti

* **Autore:** Stefano Peris
* **Email:** [stefanoperis.github@gmail.com](mailto:stefanoperis.github@gmail.com)
* **Versione:** 1.0
* **Linguaggio:** Python 3.12+

---

## 🚀 Caratteristiche Principali

* **Generazione Procedurale Avanzata:** Sfrutta dizionari linguistici strutturati con prefissi, parti centrali e suffissi foneticamente affini per ciascuna categoria, garantendo **oltre 100 combinazioni uniche e coerenti** per ogni razza/classe.
* **Interfaccia Grafica Moderna (GUI):** Sviluppata interamente con `tkinter` (libreria standard Python, zero dipendenze esterne da installare), caratterizzata da un layout pulito, centrato e rifinito con una palette di colori scura ed elegante.
* **Categorie Supportate:**
  * 🛡️ **Guerriero** (Nomi forti, decisi e marziali)
  * 🔮 **Mago** (Suoni arcani, mistici ed esoterici)
  * 🗡️ **Ladro** (Accenti agili, furtivi e taglienti)
  * ⚔️ **Paladino** (Denominazioni nobili, sacre e solenni)
  * 🏹 **Amazzone** (Nomi fieri, dinamici e battaglieri)
  * ⛏️ **Nano** (Radici profonde, robuste e tradizionali)
  * 🍃 **Elfo** (Accenti melodici, aggraziati ed eterei)
  * 🪓 **Barbaro** (Termini grezzi, potenti e selvaggi)

---

## 💻 Requisiti di Sistema

* **Python:** Versione **3.12** o superiore (compatibile anche con versioni 3.x precedenti).
* **Librerie:** Nessuna dipendenza esterna richiesta (`tkinter` è incluso di default nella libreria standard di Python).

---

## 📦 Struttura del Codice

Il programma è organizzato in modo pulito e modulare:
1. **Dati Linguistici (`NAME_DATA`):** Matrici di sillabe suddivise per archetipo.
2. **Motore di Generazione (`generate_fantasy_name`):** Funzione randomica che assembla in modo armonico i componenti del nome.
3. **Interfaccia Grafica (`FantasyNameApp`):** Gestisce la disposizione dei componenti visivi, la griglia dei pulsanti e l'aggiornamento dinamico del display centrale.

---

## 🛠️ Istruzioni per l'Avvio

1. Salva il codice sorgente del programma in un file denominato `fantasy_generator.py`.
2. Apri il terminale o il prompt dei comandi nella cartella in cui hai salvato il file.
3. Esegui lo script digitando:

```bash
python3 fantasy_generator.py

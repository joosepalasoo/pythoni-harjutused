#joosep alasoo
#tkinter KT
#20.02.2024
"""
1. TOPP SIKRET ehk Salatoimikute haldamise sĆ¼steem

EesmĆ¤rk: loo Pythoni ja Tkinteri abil rakendus, mis simuleerib "salatoimikute haldamise sĆ¼steemi". Rakendus peab vĆµimaldama kasutajal hallata eriti ohtlike isikute andmeid, sealhulgas inimese nime, isikukoodi, sĆ¼nniaega, sugu, pikemat infot/teksti ning pilti.

Funktsionaalsus:
* Andmete kuvamine: Rakendus kuvab olemasolevaid andmeid loetelus, kus kasutaja saab Ć¼ksikute kirjete peal klikkides vaadata tĆ¤psemat teavet.
* Andmete lisamine: Kasutaja saab lisada uusi isikuid andmebaasi, sisestades vajalikud andmed lĆ¤bi liidese.
* Andmete muutmine: Kasutaja saab olemasolevaid andmeid muuta, valides loetelust konkreetse kirje ja tehes vajalikud tĆ¤iendused vĆµi parandused.
* Andmete kustutamine: Kasutaja saab eemaldada kirjeid andmebaasist.
* Andmete hoiustamine: Andmeid hoitakse CSV, TXT vĆµi muus sobilikus failiformaadis, mis vĆµimaldab lihtsat andmete lisamist, muutmist ja kustutamist.

NĆµuded:
* Rakendus peab olema kasutajasĆµbralik ja intuitiivne.
* Andmete salvestamiseks ja lugemiseks tuleb kasutada failisĆ¼steemi (CSV, TXT vms).
* Rakendus peab vĆµimaldama piltide lisamist ja kuvamist koos isikute andmetega.
* Kasutajaliides peab olema loodud Tkinteri abil.
* Failid peavad olema kĆ¤ttesaadavad Githubis
"""

import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import base64
import io
from PIL import Image, ImageTk

class SecretAgentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("TOPP SIKRET - Salatoimikute haldamise süsteem")
        self.entries = {}
        self.current_index = None

        self.listbox = tk.Listbox(root)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        frame = tk.Frame(root)
        frame.pack(side=tk.RIGHT, padx=10)

        labels = ['Nimi', 'Isikukood', 'Sünniaeg', 'Sugu', 'Info']
        for label_text in labels:
            label = tk.Label(frame, text=label_text)
            label.grid(sticky='w')
            entry = tk.Entry(frame)
            entry.grid(sticky='we')
            self.entries[label_text.lower()] = entry

        self.image_label = tk.Label(root)
        self.image_label.pack()

        button_frame = tk.Frame(root)
        button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        add_button = tk.Button(button_frame, text="Lisa uus agent", command=self.add_person)
        add_button.grid(row=0, column=0, padx=5, pady=5)
        update_button = tk.Button(button_frame, text="Uuenda agenti", command=self.update_person)
        update_button.grid(row=1, column=0, padx=5, pady=5)
        delete_button = tk.Button(button_frame, text="Kustuta agent", command=self.delete_person)
        delete_button.grid(row=2, column=0, padx=5, pady=5)
        add_image_button = tk.Button(button_frame, text="Lisa pilt", command=self.add_image)
        add_image_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.search_var = tk.StringVar()  # Variable to track changes in search entry
        self.search_var.trace("w", self.search_person)  # Trace changes in search entry
        search_entry = tk.Entry(button_frame, textvariable=self.search_var)
        search_entry.grid(row=4, column=0, padx=5, pady=5)
        search_entry.insert(0, "Otsi...")

        self.load_data()

    def on_select(self, event):
        if self.listbox.curselection():
            index = int(self.listbox.curselection()[0])
            person = self.data[index]
            self.current_index = index  # Update current index
            self.show_person_info(person)
            if 'image' in person:
                self.show_image(person['image'])
            else:
                self.image_label.config(image='')
        else:
            self.current_index = None

    def add_person(self):
        person = {}
        for key, entry in self.entries.items():
            person[key] = entry.get()
            entry.delete(0, tk.END)
        self.data.append(person)
        self.save_data()
        self.load_data()

    def update_person(self):
        if self.current_index is not None:
            person = self.data[self.current_index]
            for key, entry in self.entries.items():
                person[key] = entry.get()
                entry.delete(0, tk.END)
            self.save_data()
            self.load_data()
        else:
            messagebox.showerror("Viga", "Palun valige agent enne uuendamist.")

    def delete_person(self):
        if self.current_index is not None:
            confirm = messagebox.askyesno("Kinnita kustutamine", "Kas olete kindel, et soovite selle agendi kustutada?")
            if confirm:
                del self.data[self.current_index]
                self.save_data()
                self.load_data()
        else:
            messagebox.showerror("Viga", "Palun valige agent enne kustutamist.")

    def add_image(self):
        if self.current_index is not None:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
            if file_path:
                with open(file_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                    self.data[self.current_index]['image'] = encoded_string
                    self.save_data()
                    self.show_image(encoded_string)
        else:
            messagebox.showerror("Viga", "Palun valige agent enne pildi lisamist.")

    def search_person(self, *args):
        search_query = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        if search_query and search_query != "otsi...":
            found = False
            for person in self.data:
                if search_query in person['nimi'].lower():
                    self.data.insert(0, self.data.pop(self.data.index(person)))  # Move found person to first position
                    self.show_person_info(person)
                    self.listbox.insert(0, person['nimi'])
                    self.listbox.itemconfig(0, foreground='black')  # Reset the text color
                    found = True
            if not found:
                self.clear_person_info()
        else:
            for person in self.data:
                self.listbox.insert(tk.END, person['nimi'])

    def load_data(self):
        try:
            with open('salatoimikud.csv', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
        except FileNotFoundError:
            self.data = []
        self.search_person()  # Load data into listbox when starting
        self.current_index = None  # Reset current index

    def save_data(self):
        with open('salatoimikud.csv', 'w', newline='', encoding='utf-8') as file:
            fieldnames = self.data[0].keys() if self.data else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def show_image(self, image_data):
        if image_data:
            decoded_image = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(decoded_image))
            photo_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo_image)
            self.image_label.image = photo_image
        else:
            self.image_label.config(image='')

    def show_person_info(self, person):
        for key, value in person.items():
            if key != 'image':
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, value)

    def clear_person_info(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = SecretAgentSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()

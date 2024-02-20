import csv
import tkinter as tk
from tkinter import filedialog, messagebox

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

        add_button = tk.Button(button_frame, text="Lisa", command=self.add_person)
        add_button.grid(row=0, column=0, padx=5, pady=5)
        update_button = tk.Button(button_frame, text="Uuenda", command=self.update_person)
        update_button.grid(row=1, column=0, padx=5, pady=5)
        delete_button = tk.Button(button_frame, text="Kustuta", command=self.delete_person)
        delete_button.grid(row=2, column=0, padx=5, pady=5)
        add_image_button = tk.Button(button_frame, text="Lisa Pilt", command=self.add_image)
        add_image_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.search_var = tk.StringVar()  # Variable to track changes in search entry
        self.search_var.trace("w", self.search_person_realtime)  # Trace changes in search entry
        search_entry = tk.Entry(button_frame, textvariable=self.search_var)
        search_entry.grid(row=4, column=0, padx=5, pady=5)

        self.load_data()

    def on_select(self, event):
        if self.listbox.curselection():
            index = int(self.listbox.curselection()[0])
            person = self.data[index]
            self.current_index = index
            for key, value in person.items():
                if key != 'image':
                    self.entries[key].delete(0, tk.END)
                    self.entries[key].insert(0, value)
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

    def delete_person(self):
        if self.current_index is not None:
            del self.data[self.current_index]
            self.save_data()
            self.load_data()

    def add_image(self):
        if self.current_index is not None:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
            if file_path:
                self.data[self.current_index]['image'] = file_path
                self.save_data()
                self.show_image(file_path)

    def search_person_realtime(self, *args):
        search_query = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        found_person = None
        for index, person in enumerate(self.data):
            if search_query in person['nimi'].lower():
                self.listbox.insert(tk.END, person['nimi'])
                self.listbox.itemconfig(index, foreground='blue')  # Highlight the search results
                found_person = person
        if found_person:
            for key, entry in self.entries.items():
                entry.delete(0, tk.END)
                entry.insert(0, found_person.get(key, ''))
        else:
            print("Isikut ei leitud.")

    def load_data(self):
        try:
            with open('salatoimikud.csv', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
        except FileNotFoundError:
            self.data = []
        self.listbox.delete(0, tk.END)
        for person in self.data:
            self.listbox.insert(tk.END, person['nimi'])

    def save_data(self):
        with open('salatoimikud.csv', 'w', newline='', encoding='utf-8') as file:
            fieldnames = self.data[0].keys() if self.data else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def show_image(self, image_path):
        image = tk.PhotoImage(file=image_path)
        self.image_label.config(image=image)
        self.image_label.image = image

def main():
    root = tk.Tk()
    app = SecretAgentSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()

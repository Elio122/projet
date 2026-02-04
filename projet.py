import tkinter as tk

films = [
    {"Titre": "Inception", "Genre": ["Action", "Science Fiction"]},
    {"Titre": "Titanic", "Genre": ["Romance", "Drama"]},
    {"Titre": "Avengers", "Genre": ["Action", "Science Fiction"]},
    {"Titre": "The Godfather", "Genre": ["Crime", "Drama"]},
    {"Titre": "La La Land", "Genre": ["Musical", "Romance"]},
    {"Titre": "Interstellar", "Genre": ["Science Fiction", "Drama"]},
    {"Titre": "The Notebook", "Genre": ["Romance", "Drama"]},
    {"Titre": "Gladiator", "Genre": ["Action", "Drama"]},
    {"Titre": "Amélie", "Genre": ["Romance", "Comedy"]},
    {"Titre": "The Dark Knight", "Genre": ["Action", "Crime"]},
    {"Titre": "Pulp Fiction", "Genre": ["Crime", "Drama"]},
    {"Titre": "Whiplash", "Genre": ["Musical", "Drama"]},
    {"Titre": "grande bataille d'algerie", "Genre": ["Pour les vrais DZ"]},
]


options = ["Action", "Romance", "Crime", "Musical", "Science Fiction", "Drama", "Comedy","pour les NEUILLE","Pour les vrais DZ"]


root = tk.Tk()
root.title("🎬 Recommandateur de Films 🎬")
root.geometry("800x600")
root.configure(bg="#414153")


var_dict = {}

tk.Label(root, text="Sélectionne tes genres préférés :", bg="#414153", fg="white", font=("Helvetica", 16, "bold")).pack(pady=10)

max_length = max(len(opt) for opt in options)


for opt in options:
    var = tk.IntVar()
    chk = tk.Checkbutton(root, text=opt, variable=var, width=max_length+2, anchor="w",
                         bg="#414153", fg="white", selectcolor="#ffcc00", font=("Helvetica", 12))
    chk.pack(padx=30, pady=5)
    var_dict[opt] = var

result_label = tk.Label(root, text="", bg="white", fg="black", width=80, height=15, anchor="nw", justify="left")
result_label.pack(pady=20)

def close_app():
    root.destroy()

def valider():
    choisis = [g for g, var in var_dict.items() if var.get() == 1]
    if not choisis:
        result_label.config(text="Sélectionne au moins un genre, chp sah fait un effort STP",font=("Arial", 20))
        return
    
    films_selectionnes = [f for f in films if any(g in choisis for g in f["Genre"])]
    
    if not films_selectionnes:
        root.bell()
        result_label.config(text="Aucun film trouvé NEUILLE FREEUUURRR !",font=("Arial", 50))
        root.after(2000, close_app)
        return
    
    
    textes = "\n".join(f"{f['Titre']} ({', '.join(f['Genre'])})" for f in films_selectionnes)
    result_label.config(text=textes)


mon_bouton = tk.Button(
    root,
    text="Valider",
    command=valider,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 14, "bold"),
    padx=25, pady=5
)


mon_bouton.pack(pady=10)


root.mainloop()
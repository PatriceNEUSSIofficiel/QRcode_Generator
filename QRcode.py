import qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def generer_qrcode():
    texte = texte_entree.get()

    if texte:
        nom_fichier = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG", "*.png"), ("Tous les fichiers", "*.*")])
        if nom_fichier:
            img = qrcode.make(texte)
            img.save(nom_fichier)
            messagebox.showinfo("QR Code généré", "Le QR Code a été généré avec succès.")
        else:
            messagebox.showwarning("Aucun fichier sélectionné", "Veuillez sélectionner un fichier.")
    else:
        messagebox.showwarning("Texte manquant", "Veuillez entrer un texte.")

def afficher_aide():
    messagebox.showinfo("Aide", "Entrez le texte que vous souhaitez encoder en QR Code, puis cliquez sur le bouton 'Générer QR Code'.\n\n"
                                "Un dialogue vous demandera de choisir l'emplacement et le nom du fichier de sortie.\n\n"
                                "Le QR Code sera généré et enregistré sous forme d'image PNG.")

fenetre = tk.Tk()
fenetre.title("Générateur de QR Code")
fenetre.geometry("300x200")

etiquette_texte = tk.Label(fenetre, text="Entrez le texte", font=("Arial", 35, "bold"))
etiquette_texte.pack(pady=20)

texte_entree = tk.Entry(fenetre, font=("Arial", 40))
texte_entree.pack(padx=10, pady=0)

bouton_generer = tk.Button(fenetre, text="Générer QR Code", font=("Arial", 12, "bold"), command=generer_qrcode)
bouton_generer.pack(pady=10)

bouton_aide = tk.Button(fenetre, text=" Aide ?", font=("Arial", 12, "bold"), command=afficher_aide)
bouton_aide.pack(padx=10, pady=10)

fenetre.mainloop()
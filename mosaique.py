# Import de l'outil image
from PIL import Image

# définir l'image avec la photo choisie et sa taille
image = Image.open("photo.jpg")
largeur, hauteur = image.size

# choix du nombre de blocs et couleurs
blocs = 40
couleurs = 15

# filtrage des valeurs non conformes
if blocs < 1 or blocs > largeur:
    print("Valeur non conforme (extrêmes), blocs doit être entre 1 et", largeur)
    exit()
if couleurs < 2 or couleurs > 256:
    print("Fenêtre de couleurs non conforme, elle doit être entre 2 et 256")
    exit()

# format miniature pour isoler les pixels
petite_largeur = blocs
petite_hauteur = round(hauteur * blocs / largeur)

# réduction de la taille et des couleurs, puis réagrandissement
petite = image.resize((petite_largeur, petite_hauteur), Image.Resampling.BOX)
petite = petite.quantize(colors=couleurs)
mosaique = petite.resize((largeur, hauteur), Image.Resampling.NEAREST)

# enregistrement de la mosaïque et affichage du résultat
mosaique.save("mosaique.png")
print("Mosaïque enregistrée :", petite_largeur, "x", petite_hauteur, "blocs et", couleurs, "couleurs")
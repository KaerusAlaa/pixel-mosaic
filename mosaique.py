# 1. Importer l'outil d'images

from PIL import Image

# 2. Ouvrir photo.jpg et récupérer largeur et hauteur

image = Image.open("photo.jpg")
largeur, hauteur = image.size

# 3. Choisir le nombre de blocs et calculer la hauteur en blocs

blocs = 40
petite_largeur = blocs
petite_hauteur = round(hauteur * blocs / largeur)

# 4. Réduire en faisant la moyenne, puis réagrandir sans lisser

petite = image.resize((petite_largeur, petite_hauteur), Image.Resampling.BOX)
mosaique = petite.resize((largeur, hauteur), Image.Resampling.NEAREST)

# 5. Enregistrer et afficher un message

mosaique.save("mosaique.png")
print("Mosaïque enregistrée :", petite_largeur, "x", petite_hauteur, "blocs")
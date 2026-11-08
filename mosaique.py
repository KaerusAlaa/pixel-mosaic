from PIL import Image

image = Image.open("photo.jpg")
largeur, hauteur = image.size

blocs = 40
couleurs = 15
if blocs <1 or blocs > largeur:
    print("valeur non conforme (extrêmes), blocs doit être entre 1 et", largeur)
    exit()
if couleurs<2 or couleurs>256 :
    print("Range de couleurs non conforme, elle doit être entre 2 et 256")
    exit()

petite_largeur = blocs
petite_hauteur = round(hauteur * blocs / largeur)

petite = image.resize((petite_largeur, petite_hauteur), Image.Resampling.BOX)
petite = petite.quantize(colors=couleurs)
mosaique = petite.resize((largeur, hauteur), Image.Resampling.NEAREST)

mosaique.save("mosaique.png")
print("Mosaïque enregistrée :", petite_largeur, "x", petite_hauteur, "blocs et", couleurs, "couleurs")
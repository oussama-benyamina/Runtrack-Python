# Programme affichant tous les nombres de 0 à 100 sauf 26, 37, 88
for nombre in range(101):
    if nombre not in [26, 37, 88]:
        print(nombre)
            
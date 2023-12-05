def deleted_doublons(liste):
    sans_doublons = []

    for element in liste:
        if element not in sans_doublons:
            sans_doublons.append(element)

    return sans_doublons

# Liste réalisé :
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Appeler la fonction pour supprimer les doublons
liste_sans_doublons = deleted_doublons(ma_liste)

# Afficher le résultat
print("Résultat sans doublons :", liste_sans_doublons)

l = ['pomme', 'cerise', 'orange', 'Melon']

def main(liste: list) -> list:
    liste[2] = 'Mangue'
    return liste

print(main(l))
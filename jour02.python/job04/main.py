def mutliplication(x: int) -> None:
    print(f"Table de multiplication de {x}: ")
    for j in range(1, 11):
        print(f"{x} X {j} = {x*j}")
    print()

rep = int(input("Entrez un entier supérieur à zéro (x): "))
for k in range(1, rep + 1):
    mutliplication(k)
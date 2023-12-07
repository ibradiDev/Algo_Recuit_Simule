from fonctions import *


if __name__ == "__main__":
    s = solution_initiale()
    T = 10000000  # Température
    alpha = 0.95  # Taux de refroidissement
    nbre_iteration = 0

    print(f"\nTempérature initiale: T = {T}")
    print(f"     Solution initiale: s = {s}  ==>  Conflits = {conflits(s)}")

    while True:
        nbre_iteration += 1
        s1 = voisinage(s, 1)  # Voisin à s
        print(f"\t  Solution voisine s' = {s1}  ==>  Conflits = {conflits(s1)}")

        if conflits(s1) < conflits(s):
            s = s1
        else:  # Principe de Métropolis
            r = random.uniform(0, 1)
            if r < proba_metropolis(T, s, s1):
                s = s1
            T *= alpha

        if conflits(s) == 0:
            print(
                "\n******************************************************************************"
            )
            print(
                f"\t     Solution optimale trouvée:  s = {s}  ==>  Conflits = {conflits(s)}"
            )
            print(f"\t        Température du système:  {T}")
            print(f"\tNombre d'itérations effectuées:  {nbre_iteration}")
            print(
                "******************************************************************************\n"
            )
            break

        print(f"\n    Tempétature actuelle: T = {T}")
        print(f"Solution optimale actuelle: s = {s}  ==>  Conflits = {conflits(s)}")

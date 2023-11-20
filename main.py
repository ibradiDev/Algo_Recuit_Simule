from fonctions import *


if __name__ == "__main__":
    s = solution_initiale()
    T = 1000000000  # Température

    print(f"\nTempérature initiale T = {T}")
    print(f"Solution initiale s = {s}  ==>  Conflits = {conflits(s)}")

    while T >= 1:
        s1 = voisinage(s, 1)  # Voisin à s
        print(f"\t  Solution voisine s' = {s1}  ==>  Conflits = {conflits(s1)}")

        if conflits(s1) < conflits(s):
            s = s1
        else:  # Vérification Métropolis
            r = random.randint(0, 1)
            if r < proba_metropolis(T, s, s1):
                s = s1
                T -= 1

        if conflits(s) == 0:
            print(
                "\n******************************************************************************"
            )
            print(f"\tSolution optimale trouvée: s = {s}  ==>  {conflits(s)}")
            print(
                "******************************************************************************\n"
            )
            break

        print(f"\nTempétature actuelle: T = {s}")
        print(f"Solution optimale actuelle: s = {s}  ==>  Conflits = {conflits(s)}")

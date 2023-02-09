class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, adresa, rodne_cislo, telefon, pojistena_vec):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.adresa = adresa
        self.rodne_cislo = rodne_cislo
        self.telefon = telefon
        self.pojistena_vec = pojistena_vec

    def __str__(self):
        return f"Jméno: {self.jmeno}\nPříjmení: {self.prijmeni}\nVěk: {self.vek}\nAdresa: {self.adresa}\nRodné číslo: {self.rodne_cislo}\nTelefon: {self.telefon}\nPojištěná věc Item: {self.pojistena_vec}"


pojistenci = []

def pridej_pojisteneho():
    jmeno = input("Zadejte jméno: ")
    prijmeni = input("Zadejte příjmení: ")
    vek = input("Zadejte věk: ")
    adresa = input("Zadejte adresu: ")
    rodne_cislo = input("Zadejte rodne číslo: ")
    telefon = input("Zadejte telefon: ")
    pojistena_vec = input("Zadejte pojištěnou věc: ")

    pojisteny = Pojisteny(jmeno, prijmeni, vek, adresa, rodne_cislo, telefon, pojistena_vec)
    pojistenci.append(pojisteny)
    print("Záznám o novém pojištění byl přidán.")

def vypis_vsechny_pojistene():
    for i, pojisteny in enumerate(pojistenci):
        print(f"{i+1}. {pojisteny}")

def vyhledej_pojisteneho():
    vyhledej_prijmeni = input("Zadej příjmení pro vyhledání pojištěného: ")
    vyhledej_vysledky = [pojisteny for pojisteny in pojistenci if pojisteny.prijmeni == vyhledej_prijmeni]
    for i, pojisteny in enumerate(vyhledej_vysledky):
        print(f"{i+1}. {pojisteny}")

if __name__ == "__main__":
    while True:
        print("1. Přidej nového pojištěného\n2. Vypsát všechny pojištěné\n3. Vyhledej pojištěného\n4. Ukončit program")
        moznost = input("Zvolte jednu z vyše uvedených možnosti a stiskněte tlačítko Enter: ")

        if moznost == "1":
            pridej_pojisteneho()
        elif moznost == "2":
            vypis_vsechny_pojistene()
        elif moznost == "3":
            vyhledej_pojisteneho()
        elif moznost == "4":
            break
        else:
            print("Chybné zadání. Zkuste znovu.")
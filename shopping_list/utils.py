# utils.py


# Funkcija aprēķina viena produkta kopējo cenu
def calc_line_total(item):
    # Sagaidām, ka item ir vārdnīca ar atslēgām:
    # "qty" (daudzums) un "price" (cena par vienību)

    # Piemērs:
    # item = {"name": "Maize", "qty": 3, "price": 1.20}

    # Daudzums reiz cena par vienību
    # 3 * 1.20 = 3.60
    return item["qty"] * item["price"]


# Funkcija aprēķina visu produktu kopējo summu
def calc_grand_total(items):
    # Izveidojam mainīgo kopējai summai
    total = 0

    # Izejam cauri katram produktam sarakstā
    for item in items:
        # Katram produktam aprēķinām rindas summu
        # un pieskaitām pie kopējās summas
        total += calc_line_total(item)

    # Atgriežam gala summu
    return total


# Funkcija saskaita kopējo vienību skaitu
def count_units(items):
    # Mainīgais kopējam daudzumam
    total_units = 0

    # Izejam cauri visiem produktiem
    for item in items:
        # Saskaitām daudzumus
        # Piemēram:
        # Maize qty=3
        # Piens qty=2
        # Rezultāts = 5
        total_units += item["qty"]

    # Atgriežam kopējo vienību skaitu
    return total_units
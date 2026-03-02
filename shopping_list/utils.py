# utils.py

# Funkcija aprēķina viena produkta kopējo cenu
def calc_line_total(item):
    # Daudzums reiz cena par vienību
    return item["qty"] * item["price"]


# Funkcija aprēķina visu produktu kopējo summu
def calc_grand_total(items):
    total = 0

    # Izejam cauri katram produktam
    for item in items:
        # Pieskaitām katras rindas summu
        total += calc_line_total(item)

    return total


# Funkcija saskaita kopējo vienību skaitu
def count_units(items):
    total_units = 0

    for item in items:
        # Saskaitām daudzumus
        total_units += item["qty"]

    return total_units
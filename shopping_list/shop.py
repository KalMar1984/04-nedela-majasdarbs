# shop.py

# Importējam sys moduli,
# lai varētu izmantot komandrindas argumentus (sys.argv)
import sys

# Importējam funkcijas no storage.py,
# lai varētu ielādēt un saglabāt datus failā
# + jaunās cenu datubāzes funkcijas
from storage import (
    load_list,
    save_list,
    get_price,   # atgriež cenu no prices.json
    set_price    # saglabā/atjaunina cenu prices.json
)

# Importējam palīgfunkcijas no utils.py,
# lai varētu aprēķināt summas un vienību skaitu
from utils import calc_line_total, calc_grand_total, count_units


# ---------------- PRODUKTA PIEVIENOŠANA SARAKSTAM ----------------

def add_item(name, qty):
    # Ielādējam esošo iepirkumu sarakstu no JSON faila
    items = load_list()

    # Mēģinām iegūt cenu no cenu datubāzes (prices.json)
    price = get_price(name)

    # Ja cena jau eksistē datubāzē
    if price is not None:
        print(f"Atrasta cena: {price:.2f} EUR/gab.")

        # Prasām lietotājam, vai pieņemt vai mainīt cenu
        # .lower() nodrošina, ka A un a strādā vienādi
        choice = input("[A]kceptēt / [M]ainīt? > ").lower()

        # Ja lietotājs izvēlas mainīt cenu
        if choice == "m":
            try:
                # Lietotājs ievada jaunu cenu
                new_price = float(input("Jaunā cena: > "))

                # Pārbaudām vai cena ir pozitīva
                if new_price <= 0:
                    print("Cenai jābūt pozitīvai.")
                    return

            except ValueError:
                print("Nederīga cena.")
                return

            # Saglabājam jauno cenu datubāzē
            set_price(name, new_price)

            print(f"✓ Cena atjaunināta: {name} → {new_price:.2f} EUR")

            # Izmantojam jauno cenu tālāk
            price = new_price

    # Ja cena NAV atrodama datubāzē
    else:
        print("Cena nav zināma.")

        try:
            # Prasām lietotājam ievadīt cenu
            price = float(input("Ievadi cenu: > "))

            # Pārbaudām vai cena ir pozitīva
            if price <= 0:
                print("Cenai jābūt pozitīvai.")
                return

        except ValueError:
            print("Nederīga cena.")
            return

        # Saglabājam cenu datubāzē
        set_price(name, price)

        print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")

    # Izveidojam jaunu produktu kā vārdnīcu
    new_item = {
        "name": name,
        "qty": qty,
        "price": price
    }

    # Pievienojam produktu sarakstam
    items.append(new_item)

    # Saglabājam atjaunināto sarakstu
    save_list(items)

    # Aprēķinām rindas kopējo summu
    line_total = calc_line_total(new_item)

    # Izdrukājam apstiprinājuma ziņojumu
    print(
        f"✓ Pievienots: {name} × {qty} "
        f"({price:.2f} EUR/gab.) = {line_total:.2f} EUR"
    )


# ---------------- SARAKSTA ATTĒLOŠANA ----------------

def list_items():
    items = load_list()

    if not items:
        print("Saraksts ir tukšs.")
        return

    print("Iepirkumu saraksts:")

    for index, item in enumerate(items, start=1):
        line_total = calc_line_total(item)

        print(
            f"  {index}. {item['name']} × {item['qty']} — "
            f"{item['price']:.2f} EUR/gab. — {line_total:.2f} EUR"
        )


# ---------------- KOPSUMMAS APRĒĶINS ----------------

def show_total():
    items = load_list()

    grand_total = calc_grand_total(items)
    total_units = count_units(items)

    print(
        f"Kopā: {grand_total:.2f} EUR "
        f"({total_units} vienības, {len(items)} produkti)"
    )


# ---------------- SARAKSTA NOTĪRĪŠANA ----------------

def clear_list():
    save_list([])
    print("✓ Saraksts notīrīts.")


# ---------------- GALVENĀ PROGRAMMAS DAĻA ----------------

def main():

    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add/list/total/clear]")
        return

    command = sys.argv[1]

    # ---------- ADD KOMANDA (3. SOLIS) ----------
    if command == "add":

        # Tagad sagaidām tikai:
        # Nosaukums + Daudzums
        if len(sys.argv) != 4:
            print("Lietošana: python shop.py add Nosaukums Daudzums")
            return

        name = sys.argv[2]

        try:
            qty = int(sys.argv[3])

            if qty <= 0:
                print("Daudzumam jābūt pozitīvam skaitlim.")
                return

        except ValueError:
            print("Daudzumam jābūt veselam skaitlim.")
            return

        # Izsaucam 3. soļa add_item funkciju
        add_item(name, qty)

    elif command == "list":
        list_items()

    elif command == "total":
        show_total()

    elif command == "clear":
        clear_list()

    else:
        print("Nezināma komanda.")


# Šis nosacījums nodrošina,
# ka main() izpildās tikai,
# ja fails tiek palaists tieši
if __name__ == "__main__":
    main()
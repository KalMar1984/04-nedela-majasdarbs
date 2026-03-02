# shop.py

# Importējam sys moduli,
# lai varētu izmantot komandrindas argumentus (sys.argv)
import sys

# Importējam funkcijas no storage.py,
# lai varētu ielādēt un saglabāt datus failā
from storage import load_list, save_list

# Importējam palīgfunkcijas no utils.py,
# lai varētu aprēķināt summas un vienību skaitu
from utils import calc_line_total, calc_grand_total, count_units


# ---------------- PRODUKTA PIEVIENOŠANA ----------------

def add_item(name, qty, price):
    # Ielādējam esošo iepirkumu sarakstu no JSON faila
    items = load_list()

    # Izveidojam jaunu produktu kā vārdnīcu (dictionary)
    # Šeit saglabājam nosaukumu, daudzumu un cenu par vienību
    new_item = {
        "name": name,   # Produkta nosaukums (piemēram, "Maize")
        "qty": qty,     # Daudzums (piemēram, 3 gab.)
        "price": price  # Cena par vienību (piemēram, 1.20 EUR)
    }

    # Pievienojam jauno produktu sarakstam
    items.append(new_item)

    # Saglabājam atjaunināto sarakstu atpakaļ failā
    save_list(items)

    # Aprēķinām šīs rindas kopējo summu (daudzums × cena)
    line_total = calc_line_total(new_item)

    # Izdrukājam apstiprinājuma ziņojumu lietotājam
    print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")


# ---------------- SARAKSTA ATTĒLOŠANA ----------------

def list_items():
    # Ielādējam sarakstu no faila
    items = load_list()

    # Ja saraksts ir tukšs, paziņojam lietotājam
    if not items:
        print("Saraksts ir tukšs.")
        return  # pārtraucam funkciju

    # Izdrukājam virsrakstu
    print("Iepirkumu saraksts:")

    # enumerate ļauj mums iegūt gan indeksu (numuru), gan pašu produktu
    # start=1 nozīmē, ka numerācija sāksies no 1, nevis 0
    for index, item in enumerate(items, start=1):

        # Aprēķinām katra produkta kopējo summu
        line_total = calc_line_total(item)

        # Izdrukājam formatētu informāciju par produktu
        print(
            f"  {index}. {item['name']} × {item['qty']} — "
            f"{item['price']:.2f} EUR/gab. — {line_total:.2f} EUR"
        )


# ---------------- KOPSUMMAS APRĒĶINS ----------------

def show_total():
    # Ielādējam sarakstu
    items = load_list()

    # Aprēķinām visu produktu kopējo summu
    grand_total = calc_grand_total(items)

    # Saskaitām kopējo vienību skaitu
    total_units = count_units(items)

    # Izdrukājam rezultātu:
    # - kopējā summa
    # - kopējais vienību skaits
    # - produktu skaits
    print(
        f"Kopā: {grand_total:.2f} EUR "
        f"({total_units} vienības, {len(items)} produkti)"
    )


# ---------------- SARAKSTA NOTĪRĪŠANA ----------------

def clear_list():
    # Saglabājam tukšu sarakstu failā
    # Tas faktiski izdzēš visus ierakstus
    save_list([])

    # Paziņojam lietotājam
    print("✓ Saraksts notīrīts.")


# ---------------- GALVENĀ PROGRAMMAS DAĻA ----------------

def main():
    # Pārbaudām, vai lietotājs ir ievadījis komandu
    # Ja argumentu skaits ir mazāks par 2,
    # tas nozīmē, ka komanda nav ievadīta
    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add/list/total/clear]")
        return

    # Komanda vienmēr atrodas otrajā argumentā
    # (pirmais ir faila nosaukums)
    command = sys.argv[1]

    # ---------- ADD KOMANDA ----------
    if command == "add":

        # Sagaidām tieši 3 papildu argumentus:
        # Nosaukums, Daudzums, Cena
        if len(sys.argv) != 5:
            print("Lietošana: python shop.py add Nosaukums Daudzums Cena")
            return

        # Produkta nosaukums
        name = sys.argv[2]

        # Mēģinām pārvērst daudzumu uz veselu skaitli
        try:
            qty = int(sys.argv[3])

            # Pārbaudām vai daudzums ir pozitīvs
            if qty <= 0:
                print("Daudzumam jābūt pozitīvam skaitlim.")
                return

        # Ja ievade nav skaitlis, parādām kļūdu
        except ValueError:
            print("Daudzumam jābūt veselam skaitlim.")
            return

        # Mēģinām pārvērst cenu uz decimālskaitli (float)
        try:
            price = float(sys.argv[4])

            # Cena nevar būt negatīva
            if price < 0:
                print("Cena nevar būt negatīva.")
                return

        # Ja cena nav skaitlis
        except ValueError:
            print("Cenai jābūt skaitlim.")
            return

        # Ja viss ir pareizi, pievienojam produktu
        add_item(name, qty, price)

    # ---------- LIST KOMANDA ----------
    elif command == "list":
        list_items()

    # ---------- TOTAL KOMANDA ----------
    elif command == "total":
        show_total()

    # ---------- CLEAR KOMANDA ----------
    elif command == "clear":
        clear_list()

    # Ja komanda nav atpazīta
    else:
        print("Nezināma komanda.")


# Šis nosacījums nodrošina, ka main() izpildās
# tikai tad, ja fails tiek palaists tieši,
# nevis importēts citā Python failā
if __name__ == "__main__":
    main()
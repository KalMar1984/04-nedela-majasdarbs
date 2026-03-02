# Importējam sys moduli, lai varētu izmantot komandrindas argumentus
import sys

# Importējam mūsu pašu funkcijas no storage.py
from storage import load_list, save_list


# Ielādējam esošo sarakstu no faila
items = load_list()


# Pārbaudām, vai lietotājs ir ievadījis komandu
if len(sys.argv) < 2:
    print("Lietošana: python shop.py [add/list/total/clear]")
    sys.exit()


# Komanda atrodas otrajā argumentā
command = sys.argv[1]


# ---------------- ADD ----------------
if command == "add":
    # Pārbaudām vai ievadīts nosaukums un cena
    if len(sys.argv) != 4:
        print("Lietošana: python shop.py add Nosaukums Cena")
        sys.exit()

    # Produkta nosaukums
    name = sys.argv[2]

    # Cena tiek pārveidota uz float tipu
    price = float(sys.argv[3])

    # Izveidojam jaunu produktu kā vārdnīcu
    new_item = {"name": name, "price": price}

    # Pievienojam produktu sarakstam
    items.append(new_item)

    # Saglabājam atjaunoto sarakstu failā
    save_list(items)

    print(f"✓ Pievienots: {name} ({price:.2f} EUR)")


# ---------------- LIST ----------------
elif command == "list":
    # Ja saraksts ir tukšs
    if not items:
        print("Saraksts ir tukšs.")
    else:
        print("Iepirkumu saraksts:")
        # Izdrukājam katru produktu ar numuru
        for index, item in enumerate(items, start=1):
            print(f"  {index}. {item['name']} — {item['price']:.2f} EUR")


# ---------------- TOTAL ----------------
elif command == "total":
    # Aprēķinām visu cenu summu
    total_sum = 0

    for item in items:
        total_sum += item["price"]

    print(f"Kopā: {total_sum:.2f} EUR ({len(items)} produkti)")


# ---------------- CLEAR ----------------
elif command == "clear":
    # Notīrām sarakstu
    items = []

    # Saglabājam tukšu sarakstu failā
    save_list(items)

    print("✓ Saraksts notīrīts.")


# ---------------- UNKNOWN COMMAND ----------------
else:
    print("Nezināma komanda.")
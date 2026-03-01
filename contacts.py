# Importējam moduli darbam ar JSON failiem
import json

# Importējam sys, lai varētu lasīt komandrindas argumentus
import sys

# Importējam os, lai pārbaudītu vai fails eksistē
import os


# Mainīgais, kurā saglabājam faila nosaukumu
CONTACTS_FILE = "contacts.json"


def load_contacts():
    """
    Nolasa kontaktus no JSON faila.
    Ja fails neeksistē, atgriež tukšu sarakstu.
    """

    # Pārbaudām vai fails eksistē
    if not os.path.exists(CONTACTS_FILE):
        return []  # Ja nav, atgriežam tukšu sarakstu

    # Atveram failu lasīšanas režīmā
    # with nodrošina, ka fails automātiski aizveras
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        # json.load pārvērš JSON tekstu Python datu struktūrā
        return json.load(f)


def save_contacts(contacts):
    """
    Saglabā kontaktu sarakstu JSON failā.
    """

    # Atveram failu rakstīšanas režīmā ("w" = write)
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        # json.dump pārvērš Python objektu par JSON tekstu
        json.dump(contacts, f, indent=2, ensure_ascii=False)


def add_contact(name, phone):
    """
    Pievieno jaunu kontaktu.
    """

    # Ielādējam esošos kontaktus
    contacts = load_contacts()

    # Izveidojam jaunu kontaktu kā vārdnīcu (dict)
    new_contact = {
        "name": name,
        "phone": phone
    }

    # Pievienojam kontaktu sarakstam
    contacts.append(new_contact)

    # Saglabājam atjaunināto sarakstu
    save_contacts(contacts)

    print(f"✓ Pievienots: {name} ({phone})")


def list_contacts():
    """
    Izdrukā visus kontaktus.
    """

    contacts = load_contacts()

    if not contacts:
        print("Nav neviena kontakta.")
        return

    print("Kontakti:")

    # enumerate dod gan indeksu, gan vērtību
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} — {contact['phone']}")


def search_contacts(query):
    """
    Meklē kontaktus pēc vārda daļas.
    """

    contacts = load_contacts()

    # Meklējam tos kontaktus, kuru vārdā ir meklētais teksts
    results = [
        contact for contact in contacts
        if query.lower() in contact["name"].lower()
    ]

    if not results:
        print("Nekas netika atrasts.")
        return

    print(f"Atrasti {len(results)} kontakti:")

    for index, contact in enumerate(results, start=1):
        print(f"{index}. {contact['name']} — {contact['phone']}")


# Šis nodrošina, ka kods zemāk izpildās tikai,
# ja fails tiek palaists tieši (nevis importēts)
if __name__ == "__main__":

    # sys.argv ir saraksts ar komandrindas argumentiem
    # Piemēram:
    # python contacts.py add Anna 123
    # sys.argv = ["contacts.py", "add", "Anna", "123"]

    if len(sys.argv) < 2:
        print("Lieto: add | list | search")
        sys.exit()

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print("Lieto: add 'Vārds' 'Telefons'")
        else:
            add_contact(sys.argv[2], sys.argv[3])

    elif command == "list":
        list_contacts()

    elif command == "search":
        if len(sys.argv) != 3:
            print("Lieto: search 'teksts'")
        else:
            search_contacts(sys.argv[2])

    else:
        print("Nezināma komanda.")
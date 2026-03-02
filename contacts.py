# Importējam moduli darbam ar JSON failiem
import json

# Importējam sys, lai varētu lasīt komandrindas argumentus
import sys

# Importējam os, lai pārbaudītu vai fails eksistē
import os


# Mainīgais, kurā saglabājam faila nosaukumu (visi kontakti tiks saglabāti failā "contacts.json") faila nosaukuma definēšana
CONTACTS_FILE = "contacts.json"

# Funkcija, kas nolasa kontaktus no JSON faila (funkvija=darbība, ko var atkārtoti izmantot)
def load_contacts():
    """
    Nolasa kontaktus no JSON faila.
    Ja fails neeksistē, atgriež tukšu sarakstu.
    """

    # Pārbaudām vai fails eksistē
    if not os.path.exists(CONTACTS_FILE):
        return []  # Ja nav, atgriežam tukšu sarakstu (tukšs saraksts=nav kontaktu)

    # Atveram failu lasīšanas režīmā
    # with nodrošina, ka fails automātiski aizveras
    # "r" = read nozīmē lasīt failu (citi režīmi "w"-write, "a"-append, "x"-create)
    # encoding="utf-8" nodrošina, ka faila teksts ir UTF-8 lai atbalstītu latviešu burtus ar garumzīmēm. 
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        # json.load pārvērš JSON tekstu Python datu struktūrā
        # rerturn= atdod atpakaļ rezultātu no funkcijas. Atdod vērtību tam, kas fnkciju zsauca. 
        # f = atvērts fails (mainīgais var rakstīt arī as fails) - nosaukums, nosauc šo failu par f            with open(CONTACTS_FILE, "r", encoding="utf-8") as kontaktu_fails:
        return json.load(f)


def save_contacts(contacts):
    """
    Saglabā kontaktu sarakstu JSON failā.
    """

    # Atveram failu rakstīšanas režīmā ("w" = write)
    # ja fails neeksistē, tiks izveidots jauns
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        # json.dump pārvērš Python objektu par JSON tekstu
        # dump- pārvērš Python objektu par JSON tekstu un ierakst to failā (load-lasa no faila)
        # f = atvērts fails
        # contacts = atdod atpakaļ rezultātu no funkcijas, glabājas python dati
        # ident=2 - cik atstarpes lietot sakistam noformējumam. (ja ident=2, nebūtu - teksts būtu vienā rindā) 
        # ensure_ascii=False - nodrošina, ka latviešu burtus neizmanto ascii kodu. Lauj saglabāt latviešu burtus pareizi
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
    # f nozīmē ka varam ielikt mainīgos sarakstā. (f-string)
    # {}- darbojas tāpēc ka teksts sākas ar f. Figūriekavas nozīmē - ievieto šeit mainīgo (name, phone) 
    # ({phone}) = parastas iekavas, teksts izdrukāsies iekavās (1234567)
    save_contacts(contacts)

    print(f"✓ Pievienots: {name} ({phone})")


def list_contacts():
    """
    Izdrukā visus kontaktus.
    """

    # Ielādējam esošos kontaktus
    contacts = load_contacts()

    # Pārbaudām, vai saraksts nav tukšs (ja nav neviena kontakta - izdrukās "Nav neviena kontakta")
    # not - nav vai pretēji (if not contacts: būs true jo saraksts ir tukšs)
    if not contacts:
        print("Nav neviena kontakta.")
        return # Ja nav neviena kontakta, izdruka "Nav neviena kontakta" un pabeidza funkciju tikai tad ja if nosacījums ir patiess

    # atrdas ārpus if bloka - izpildās tikai tad ja nosacījums nebija patiess. Ja saraksts nav tukšs, izdruka "Kontakti:" ja saraksts ir tukšs apstājas pie return
    print("Kontakti:")

    # enumerate dod gan indeksu, gan vērtību
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} — {contact['phone']}")

# Meklā kontaktus
# def - definēdefine = definēt
# search_contacts - meklā kontaktus = funkcijas nosaukums - raksturo ko funkcija dara 
# query - arguments, meklējamais teksts. ()
def search_contacts(query):
    """
    Meklē kontaktus pēc vārda daļas.
    """

    #funkcija nolasa JSON failu (contacts.json) un atgriež sarakstu ar kontaktiem. 
    contacts = load_contacts()

    # Meklējam tos kontaktus, kuru vārdā ir meklētais teksts
    # results= [...] Python saraksts (list)jauns saraksts , kur glabāsim atrastos kontaktus, kuri atbilst meklējumam.  
    # contact for contact in contacts - Šī daļa saucas list comprehension (īss veids, kā veidot sarakstu).
    # for contact in contacts → ej cauri katram kontaktam sarakstā contacts. 
    # contact → mainīgais, kas katrā cikla solī satur vienu kontaktu (viena vārdnīca). 
    # contact pirms for → nozīmē, ka šo kontaktu ievieto jaunajā sarakstā, ja tas iztur nosacījumu.
    results = [
        contact for contact in contacts 
        # contact pirms for → nozīmē, ka šo kontaktu ievieto jaunajā sarakstā, ja tas iztur nosacījumu.
        # query.lower() → meklējamais teksts ar mazajiem burtiem 
        # contact["name"].lower() → kontakta vārds ar mazajiem burtiem 
        # in → pārbauda, vai query ir daļa no vārda
        if query.lower() in contact["name"].lower()
    ]

    # Pārbaudām, vai saraksts nav tukšs 
    # results = saraksts ar atrastajiem kontaktiem (tajā ir tikai tie, kas atbilst meklējumam).
    # if not results: pārbauda vai results ir tukš saraksts, Tukšs saraksts [] tiek uzskatīts par False, bet not False = True. Ja nekas netika atrasts → nosacījums ir patiess → kods zem if izpildās. Izdrukā nekas netika atrsts.
    # ja nekas netika atrasts return beidz funkciju uzreiz (izdruka "Nekas netika atrasts.")
    if not results:
        print("Nekas netika atrasts.")
        return

    # "Atrasti ... kontakti:" teksts starp pēdiņām = tas, ko redzēs lietotājs. "Atrasti ... kontakti:"
    # {len(results)} - len(results) = funkcija, kas skaita elementus sarakstā results. Figūriekavas {} = Python ievieto mainīgā vērtību tekstā.
    print(f"Atrasti {len(results)} kontakti:")

    # Šis ir cikls, kas iet cauri visiem rezultātiem (results) un pievieno skaitītāju (index).
    # for = cikls, kas atkārto darbību vairākas reizes. Katru reizi ņem vienu kontaktu no saraksta results.
    # index → kārtas numurs (1, 2, 3…)
    # contact → pats kontakts (vārdnīca ar "name" un "phone")
    # enumerate() = funkcija, kas piešķir katram elementam numuru ciklā.
    # results = saraksts ar atrastajiem kontaktiem 
    # start=1 = skaitīšana sākas no 1 (nevis no 0, kā Python pēc noklusējuma)
    for index, contact in enumerate(results, start=1):

        # Izvada katru kontaktu skaistā formā 
        # f"..." = F-string = ļauj ievietot mainīgos tekstā, izmantojot {}"
        # {index} = Ievieto kārtas numuru no enumerate().
        # contact["name"] = ievieto kontaktu vārdu no vārdnīcas.
        # contact["phone"] = ievieto kontaktu telefona numuru no vārdnīcas.
        # Punkts . = vizuāli norāda numuru pirms vārda 
        # Garā domuzīme — = skaists atdalījums starp vārdu un telefonu
        print(f"{index}. {contact['name']} — {contact['phone']}")


# Šis nodrošina, ka kods zemāk izpildās tikai,
# ja fails tiek palaists tieši (nevis importēts)
#  __name__ ir īpašs Python mainīgais, kas automātiski pastāv katrā failā. Python iedod tam vērtību atkarībā no tā, kā fails tiek izmantots. Ja fails tiek palaists tieši (piemēram: python contacts.py) → __name__ = "__main__" fails tiek importēts citā failā (piemēram: import contacts) → __name__ = "contacts"  # faila nosaukums
# “Ja šis fails tiek palaists tieši, tad izpildi zemāk esošo kodu” Tātad viss, kas atkāpēs zem šīs rindas, izpildīsies tikai tad, kad fails tiek palaists tieši, nevis importēts.
# Kāpēc tas ir vajadzīgs? Ja tu importē contacts.py citā Python failā, tu nevēlies, lai viss kods automātiski izpildītos. Tu tikai gribi izmantot funkcijas (add_contact, list_contacts, search_contacts) if __name__ == "__main__": nodrošina, ka komandas izpildās tikai tiešā palaišanas gadījumā
if __name__ == "__main__":

    
    # sys.argv ir saraksts ar komandrindas argumentiem
    # len() = funkcija, kas skaita elementu skaitu sarakstā. len() = funkcija, kas skaita elementu skaitu sarakstā.
    # len(sys.argv) < 2 nozīmē: “Ja argumentu skaits ir mazāks par 2…” Tātad: ja lietotājs nav norādījis komandu, piemēram add vai list, nosacījums būs True.
    # print("Lieto: add | list | search") add | list | search = atļautās komandas
    # sys.exit() = beidz programmu tūlīt, jo bez komandas nav jēgas turpināt. Alternatīvi: programma varētu mest kļūdu vai iziet ar citu ziņojumu. Šeit vienkārši apstājam programmu, jo nav argumentu.
    if len(sys.argv) < 2:
        print("Lieto: add | list | search")
        sys.exit()

    # command = mainīgais, kurā mēs saglabājam lietotāja ievadīto komandu. Piemēram: "add", "list" vai "search"
    # = sys.argv[1] tiks saglabāts command.
    # sys.argv = saraksts ar komandrindas argumentiem, ko lietotājs ievadīja, palaižot programmu.
    # [1] = pirmā komanda, ko lietotājs ievadījis pēc faila nosaukuma. Paņem otro vārdu (pirmo pēc faila nosaukuma) Jo Python indeksēšana sākas no 0:
    command = sys.argv[1]

    # command → mainīgais, kurā saglabāta lietotāja komanda (sys.argv[1]) == "add" → pārbauda, vai komanda ir precīzi "add ātad: “ja lietotājs grib pievienot kontaktu, tad izpildi šo kodu”. 
    # len(sys.argv) → skaita, cik argumentu lietotājs ievadījis komandā.
    # != 4 → nozīmē nav tieši 4 argumenti
    # Kāpēc 4?
        # "contacts.py" → fails (argv[0])
        # "add" → komanda (argv[1])
        # "Vārds" → vārds (argv[2])
        # "Telefons" → Telefons (argv[3])
        # Ja argumentu nav tieši 4 → lietotājs neievadīja pareizi, jāparāda instrukcija.
    if command == "add":
        if len(sys.argv) != 4:
            print("Lieto: add 'Vārds' 'Telefons'")  # Izdrukā pareizo lietošanas veidu, lai lietotājs saprastu, kā komandu izmantot.
        else:                                        # else → ja argumentu ir tieši 4, tad izpildi šo kodu
            add_contact( sys.argv[2], sys.argv[3])   # Izsauc funkciju add_contact ar diviem argumentiem: sys.argv[2] → vārds ("Anna") sys.argv[3] → telefons ("123") Funkcija pievieno kontaktu sarakstam un saglabā failā.

    # elif = “else if”, t.i., “cits gadījums, ja…”. Tas tiek pārbaudīts tikai tad, ja iepriekšējais if nosacījums bija False. Šeit: ja command nav "add", pārbauda: vai tas ir "list"?
    # command → mainīgais, kurā saglabāta lietotāja komanda (sys.argv[1])Izsauc funkciju . == "list" → pārbauda, vai komanda ir precīzi "list" “Ja lietotājs grib uzskaitīt visus kontaktus, tad izpildi šo kodu.”
    # list_contacts() → funkcijas izsaukums, ko mēs definējām iepriekš. Funkcija nolasa kontaktus no faila un izdrukā tos ekrānā. Nav argumentu, jo viss nepieciešamais tiek iegūts iekš funkcijas.
    elif command == "list":     
        list_contacts()         

    # Nosaka ko darīt, ja lietotājs ievada komandu search vai kādu nezināmu komandu.
    # elif = “cits gadījums, ja…”
    # command = lietotāja ievadītā komanda (piemēram, "add", "list" vai "search") 
    # == "search" → pārbauda, vai komanda ir tieši "search"
    # len(sys.argv) = skaita, cik argumenti tika ievadīti komandrindā
    # != 3 → pārbauda, vai argumentu skaits nav 3
    # Kāpēc 3?
        # "contacts.py" → fails (argv[0])
        # "search" → komanda (argv[1])
        # "teksts" → teksts (argv[2])
        # Ja argumentu nav tieši 3 → lietotājs neievadīja pareizi, jāparāda instrukcija.
    # Ja lietotājs ievada komandu search, tad pārbauda, vai lietotājs ievadīs 3 argumentus.
    
    elif command == "search":
        if len(sys.argv) != 3:
            # Izdrukā pareizo lietošanas veidu, lai lietotājs zinātu, kā pareizi rakstīt komandu.
            print("Lieto: search 'teksts'") 
            # Ja argumentu ir tieši 3, izpilda kodu zem else. Tas nozīmē: “komanda ir pareizi ievadīta, turpinām ar meklēšanu”.
        else:
            # Izsauc funkciju search_contacts ar argumentiem: sys.argv[2] = meklējamais teksts ko lietotājs ievadīja. Funkcija meklē kontaktus pēc vārda daļas un izdrukā atrastos kontaktus.
            search_contacts(sys.argv[2])

    # Tas ir pēdējais gadījums, ja komanda nav "add", "list" vai "search". 
    else:
        # Ja lietotājs ievada nezināmu komandu, tad izdrukā, "Nezināma komanda." 
        # Lietotājam parāda, ka jāizmanto tikai atļautās komandas (add, list, search).
        print("Nezināma komanda.")
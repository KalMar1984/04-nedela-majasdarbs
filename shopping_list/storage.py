# Importējam json moduli, lai varētu saglabāt un nolasīt datus JSON formātā
import json

# Importējam os moduli, lai pārbaudītu vai fails eksistē
import os


# ---------------- IEPIRKUMU SARAKSTS ----------------

# Funkcija, kas nolasa sarakstu no shopping.json
def load_list():
    # Pārbaudām, vai fails eksistē
    if not os.path.exists("shopping.json"):
        # Ja fails neeksistē, atgriežam tukšu sarakstu
        return []

    # Atveram failu lasīšanas režīmā ("r")
    with open("shopping.json", "r", encoding="utf-8") as file:
        # Nolasām datus no faila un pārvēršam par Python sarakstu
        data = json.load(file)

    # Atgriežam nolasītos datus
    return data


# Funkcija, kas saglabā sarakstu shopping.json failā
def save_list(items):
    # Atveram failu rakstīšanas režīmā ("w")
    # Ja fails neeksistē, tas tiks izveidots automātiski
    with open("shopping.json", "w", encoding="utf-8") as file:
        # Saglabājam sarakstu JSON formātā
        # indent=2 padara failu vizuāli sakārtotu
        json.dump(items, file, indent=2)


# ---------------- 3. SOLIS – CENU DATUBĀZE ----------------

# Funkcija, kas nolasa cenu datubāzi no prices.json
def load_prices():
    # Pārbaudām, vai cenu fails eksistē
    if not os.path.exists("prices.json"):
        # Ja neeksistē, atgriežam tukšu vārdnīcu
        # {} nozīmē – nav nevienas saglabātas cenas
        return {}

    # Atveram cenu failu lasīšanas režīmā
    with open("prices.json", "r", encoding="utf-8") as file:
        # Nolasām JSON un pārvēršam par Python vārdnīcu
        data = json.load(file)

    # Atgriežam cenu vārdnīcu
    return data


# Funkcija, kas saglabā cenu datubāzi prices.json
def save_prices(prices):
    # Atveram failu rakstīšanas režīmā
    with open("prices.json", "w", encoding="utf-8") as file:
        # Saglabājam vārdnīcu JSON formātā
        json.dump(prices, file, indent=2)


# Funkcija, kas atgriež konkrēta produkta cenu
def get_price(name):
    # Ielādējam visas cenas
    prices = load_prices()

    # Meklējam cenu pēc produkta nosaukuma
    # Ja produkts nav atrasts, atgriezīs None
    return prices.get(name)


# Funkcija, kas saglabā vai atjaunina produkta cenu
def set_price(name, price):
    # Ielādējam esošās cenas
    prices = load_prices()

    # Iestatām vai atjaunojam cenu konkrētam produktam
    prices[name] = price

    # Saglabājam atjaunināto cenu datubāzi atpakaļ failā
    save_prices(prices)
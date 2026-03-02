# Importējam json moduli, lai varētu saglabāt un nolasīt datus JSON formātā
import json

# Importējam os moduli, lai pārbaudītu vai fails eksistē
import os


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
import json

file_name = input("Ievadi datnes nosaukumu ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Tādas datnes nav.")
except json.JSONDecodeError:
    print("Datnes formāts nav derīgs.")

# Izvada uz ekrāna kopējo grāmatu skaitu.
skaits = len(data)
print(f"1) Kopējais grāmatu skaits: {skaits}")

#Prasa lietotājam ievadīt autoru vārdu, un tad izvada uz ekrāna visu šī autora grāmatu nosaukumus un izdošanas gadus.

autora_vards = input("2) Ievadiet autora vārdu: ")

wow = [book for book in data if book["autors"] == autora_vards]

if wow:
    print(f"Autora sarakstītās grāmatas: ")
    for book in wow:
        print(f"Grāmatas nosaukums: {book['nosaukums']}, Izdošanas gads: {book['izdošanas_gads']}")
else:
    print(f"Autora '{autora_vards}' vārds nav atrasts datnes vārdnīcā.")


#Izvada uz ekrāna visu žanru sarakstu un to grāmatu skaitu katrā žanrā.

skaits = {}
for book in data:
    žanri = book['žanrs']
    skaits[žanri] = skaits.get(žanri, 0) + 1

for žanri, sk in skaits.items():
    print(f"Datnes vārdnīcā eksistē {sk} grāmatas ar žanru '{žanri}'")
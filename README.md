# Weather Python

Jednostavan Python program koji dohvata podatke o vremenu iz različitih gradova.

## Šta sam naučio/naučila

- Kako koristiti **requests** biblioteku za slanje HTTP zahtjeva
- Kako raditi sa **JSON** podacima
- Kako koristiti **for petlje** za iteraciju kroz listu
- Kako koristiti **f-stringove** za formatiranje ispisa
- Kako pristupati **ugniježđenim podacima** u JSON-u

## Kako radi

1. Program ima listu gradova
2. Za svaki grad šalje zahtjev ka `wttr.in` API-ju
3. Dohvata trenutno vrijeme i prognozu za 3 dana
4. Ispisuje podatke na konzolu

## Kako pokrenuti

```bash
# Instaliraj requests ako ga nemaš
pip install requests

# Pokreni program
python weather.py
```

## Primjer izlaza

```
=== Boynton Beach ===
Trenutno: 82 °F - Partly cloudy - UV: 7 , Osijecaj u clzijevih stupnjeva 28 °C

Prognoza:
2024-01-15 - Max: 84 °F - Min: 68 °F - UV: 5
2024-01-16 - Max: 80 °F - Min: 65 °F - UV: 4
```

## Gradovi koje sam dodao/dodala

- Boynton Beach
- San Francisco
- Napa County
- Kastav

Možeš dodati svoje gradove u listu `gradovi`.

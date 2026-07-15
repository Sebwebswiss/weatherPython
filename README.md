# Weather Python

Jednostavan Python program koji dohvata podatke o vremenu iz različitih gradova.

## API koji koristim

**Open-Meteo** - potpuno besplatan API koji ne zahtijeva API ključ.

Prednosti:
- Ne treba registracija ni API ključ
- Tačni podaci sa 30+ meteoroloških modela
- Podaci na °C (Celsius)
- Besplatan za nekomercijalnu upotrebu

## Šta sam naučio/naučila

- Kako koristiti **requests** biblioteku za slanje HTTP zahtjeva
- Kako raditi sa **JSON** podacima
- Kako koristiti **for petlje** za iteraciju kroz listu
- Kako koristiti **f-stringove** za formatiranje ispisa
- Kako pristupati **ugniježđenim podacima** u JSON-u
- Kako koristiti **funkcije** za organizaciju koda

## Kako radi

1. Program ima listu gradova sa koordinatima
2. Za svaki grad šalje zahtjev ka Open-Meteo API-ju
3. Dohvata trenutno vrijeme i prognozu za 3 dana
4. Ispisuje podatke na konzolu na hrvatskom jeziku

## Kako pokrenuti

```bash
# Instaliraj requests ako ga nemaš
pip install requests

# Pokreni program
python weather.py
```

## Primjer izlaza

```
=== Kastav ===
Trenutno: 21.7°C
Osjećaj: 22.0°C
Vlažnost: 69%
UV Index: 0.0
Vrijeme: Oblačno

Prognoza:
2026-07-15 - Pljuskovi - Max: 31.9°C | Min: 20.7°C | UV: 7.25
2026-07-16 - Pljuskovi - Max: 31.6°C | Min: 22.0°C | UV: 6.3
```

## Gradovi koje sam dodao/dodala

- Boynton Beach (Florida, USA)
- San Francisco (California, USA)
- Napa County (California, USA)
- Kastav (Hrvatska)

Možeš dodati svoje gradove u listu `gradovi` - samo trebaš znati latitude i longitude.

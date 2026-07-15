# Weather Python

Jednostavan Python program koji dohvata podatke o vremenu iz različitih gradova.

## API koji koristim

**7Timer** - potpuno besplatan API koji ne zahtijeva nikakav API ključ.

Prednosti:
- Ne treba registracija ni API ključ
- Potpuno besplatan za nekomercijalnu upotrebu
- Postoji od 2012. godine
- Podaci su u °C
- Prognoza za svaka 3 sata

## Šta sam naučio/naučila

- Kako koristiti **requests** biblioteku za slanje HTTP zahtjeva
- Kako raditi sa **JSON** podacima
- Kako koristiti **for petlje** za iteraciju kroz listu
- Kako koristiti **f-stringove** za formatiranje ispisa
- Kako pristupati **ugniježđenim podacima** u JSON-u
- Kako koristiti **funkcije** za organizaciju koda

## Kako radi

1. Program ima listu gradova sa koordinatima
2. Za svaki grad šalje zahtjev ka 7Timer API-ju
3. Dohvata trenutno vrijeme i prognozu za 24 sata
4. Ispisuje podatke na konzolu na hrvatskom jeziku

## Kako pokrenuti

```bash
# Instaliraj requests ako ga nemaš
pip install requests

# Pokreni program
python3 weather.py
```

## Primjer izlaza

```
=== Kastav ===
Vrijeme: Oblačno (noć)
Temperatura: 18°C
Vjetar: 1 m/s (NE)

Prognoza (svaka 3 sata):
  +3h: Oblačno (noć) | 18°C | Vjetar: 1 m/s
  +6h: Oblačno (noć) | 17°C | Vjetar: 2 m/s
  +9h: Oblačno (noć) | 16°C | Vjetar: 2 m/s
  +12h: Oblačno (dan) | 22°C | Vjetar: 2 m/s
```

## Gradovi koje sam dodao/dodala

- Boynton Beach (Florida, USA)
- San Francisco (California, USA)
- Napa County (California, USA)
- Kastav (Hrvatska)

Možeš dodati svoje gradove u listu `gradovi` - samo trebaš znati latitude i longitude.

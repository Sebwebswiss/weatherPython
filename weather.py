import requests


def opisi_vrijeme(kod):
    """Pretvara weather code od 7Timer u čitljiv opis na hrvatskom"""
    opisi = {
        "clearday": "Vedro (dan)",
        "clearnight": "Vedro (noć)",
        "pcloudyday": "Djelomično oblačno (dan)",
        "pcloudynight": "Djelomično oblačno (noć)",
        "mcloudyday": "Oblačno (dan)",
        "mcloudynight": "Oblačno (noć)",
        "cloudy": "Oblačno",
        "cloudynight": "Oblačno (noć)",
        "humidday": "Vlažno (dan)",
        "humidnight": "Vlažno (noć)",
        "lightrainday": "Slaba kiša (dan)",
        "lightrainnight": "Slaba kiša (noć)",
        "oshowerday": "Slabi pljuskovi (dan)",
        "oshowernight": "Slabi pljuskovi (noć)",
        "ishowerday": "Pljuskovi (dan)",
        "ishowernight": "Pljuskovi (noć)",
        "rainday": "Kiša (dan)",
        "rainnight": "Kiša (noć)",
        "lightsnowday": "Slab snijeg (dan)",
        "lightsnownight": "Slab snijeg (noć)",
        "snowday": "Snijeg (dan)",
        "snownight": "Snijeg (noć)",
        "rainsnowday": "Kiša sa snijegom (dan)",
        "rainsnownight": "Kiša sa snijegom (noć)",
        "tsday": "Grmljavina (dan)",
        "tsnight": "Grmljavina (noć)",
        "humid": "Vlažno",
        "lightrain": "Slaba kiša",
        "lightsnow": "Slab snijeg",
        "rainsnow": "Kiša sa snijegom",
        "rain": "Kiša",
        "snow": "Snijeg",
        "ts": "Grmljavina",
    }
    return opisi.get(kod, kod)


# Gradovi sa koordinatima (latitude, longitude)
gradovi = [
    {"ime": "Boynton Beach", "lat": 26.5253, "lon": -80.0664},
    {"ime": "San Francisco", "lat": 37.7749, "lon": -122.4194},
    {"ime": "Napa County", "lat": 38.2975, "lon": -122.2869},
    {"ime": "Kastav", "lat": 45.3753, "lon": 14.3428},
]

for grad in gradovi:
    # 7Timer za vrijeme i prognozu
    url_7timer = "https://www.7timer.info/bin/api.pl"
    params_7timer = {
        "lon": grad["lon"],
        "lat": grad["lat"],
        "product": "civil",
        "output": "json"
    }
    odgovor_7timer = requests.get(url_7timer, params=params_7timer)
    podaci_7timer = odgovor_7timer.json()
    
    # Open-Meteo samo za vlažnost zraka
    url_meteo = "https://api.open-meteo.com/v1/forecast"
    params_meteo = {
        "latitude": grad["lat"],
        "longitude": grad["lon"],
        "current": "relative_humidity_2m",
        "timezone": "auto"
    }
    odgovor_meteo = requests.get(url_meteo, params=params_meteo)
    podaci_meteo = odgovor_meteo.json()
    vlaznost = podaci_meteo["current"]["relative_humidity_2m"]
    
    print(f"\n=== {grad['ime']} ===")
    
    # Trenutno vrijeme (prvi sat)
    trenutno = podaci_7timer["dataseries"][0]
    print(f"Vrijeme: {opisi_vrijeme(trenutno['weather'])}")
    print(f"Temperatura: {trenutno['temp2m']}°C")
    print(f"Vlažnost zraka: {vlaznost}%")
    print(f"Vjetar: {trenutno['wind10m']['speed']} m/s ({trenutno['wind10m']['direction']})")
    
    # Prognoza za sljedećih 24 sata (svaka 3 sata)
    print("\nPrognoza (svaka 3 sata):")
    for i in range(min(8, len(podaci_7timer["dataseries"]))):
        podatak = podaci_7timer["dataseries"][i]
        sat = podatak["timepoint"]
        temp = podatak["temp2m"]
        weather = opisi_vrijeme(podatak["weather"])
        vjetar = podatak["wind10m"]["speed"]
        print(f"  +{sat}h: {weather} | {temp}°C | Vjetar: {vjetar} m/s")

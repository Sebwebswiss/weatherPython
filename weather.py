import requests


def opisi_vrijeme(kod):
    """Pretvara weather code u čitljiv opis na hrvatskom"""
    opisi = {
        0: "Vedro",
        1: "Uglavnom vedro",
        2: "Djelomično oblačno",
        3: "Oblačno",
        45: "Magla",
        48: "Poledica",
        51: "Slaba kiša",
        53: "Umjerena kiša",
        55: "Jaka kiša",
        61: "Slaba kiša",
        63: "Umjerena kiša",
        65: "Jaka kiša",
        71: "Snijeg",
        73: "Umjeren snijeg",
        75: "Jak snijeg",
        80: "Pljuskovi",
        81: "Umjereni pljuskovi",
        82: "Obilni pljuskovi",
        95: "Oluja",
        96: "Oluja sa tučom",
        99: "Jaka oluja sa tučom",
    }
    return opisi.get(kod, f"Kod: {kod}")


# Gradovi sa koordinatima (latitude, longitude)
gradovi = [
    {"ime": "Boynton Beach", "lat": 26.5253, "lon": -80.0664},
    {"ime": "San Francisco", "lat": 37.7749, "lon": -122.4194},
    {"ime": "Napa County", "lat": 38.2975, "lon": -122.2869},
    {"ime": "Kastav", "lat": 45.3753, "lon": 14.3428},
]

for grad in gradovi:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": grad["lat"],
        "longitude": grad["lon"],
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,uv_index",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code,uv_index_max",
        "timezone": "auto",
        "forecast_days": 3
    }
    
    odgovor = requests.get(url, params=params)
    podaci = odgovor.json()
    
    print(f"\n=== {grad['ime']} ===")
    
    trenutno = podaci["current"]
    print(f"Trenutno: {trenutno['temperature_2m']}°C")
    print(f"Osjećaj: {trenutno['apparent_temperature']}°C")
    print(f"Vlažnost: {trenutno['relative_humidity_2m']}°%")
    print(f"UV Index: {trenutno['uv_index']}")
    print(f"Vrijeme: {opisi_vrijeme(trenutno['weather_code'])}")
    
    print("\nPrognoza:")
    for i in range(len(podaci["daily"]["time"])):
        datum = podaci["daily"]["time"][i]
        max_temp = podaci["daily"]["temperature_2m_max"][i]
        min_temp = podaci["daily"]["temperature_2m_min"][i]
        uv = podaci["daily"]["uv_index_max"][i]
        weather = opisi_vrijeme(podaci["daily"]["weather_code"][i])
        print(f"{datum} - {weather} - Max: {max_temp}°C | Min: {min_temp}°C | UV: {uv}")

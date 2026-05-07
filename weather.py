import requests

gradovi = ["Boynton+Beach", "San+Francisco", "Napa+County", "Kastav"]

for grad in gradovi:
    odgovor = requests.get(f"https://wttr.in/{grad}?format=j1")
    podaci = odgovor.json()
    
    print(f"\n=== {grad.replace('+', ' ')} ===")
    
    trenutno = podaci["current_condition"][0]
    print("Trenutno:", trenutno["temp_F"], "°F -", trenutno["weatherDesc"][0]["value"], "- UV:", trenutno["uvIndex"], ", Osijecaj u clzijevih stupnjeva",trenutno["FeelsLikeC"], "°C")
    
    print("\nPrognoza:")
    for dan in podaci["weather"]:
        print(dan["date"], 
              "- Max:", dan["maxtempF"], "°F",
              "- Min:", dan["mintempF"], "°F",
              "- UV:", dan["uvIndex"])

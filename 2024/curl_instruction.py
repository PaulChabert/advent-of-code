import requests

def download_input_file(day, session_token, output_file):
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookies = {'session': session_token}
    
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        with open(output_file, 'w') as f:
            f.write(response.text)
        print(f"Fichier du jour {day} téléchargé avec succès dans '{output_file}'.")
    else:
        print(f"Échec du téléchargement : code {response.status_code}")

# Exemple d’utilisation
session_token = "53616c7465645f5fae85bdbfb4ba753a83306ab5a783c629001d93d112b4443e08d5da7e690feabbf039762a1f9692037c05144f97273910ca44bd7f9a32a014"
day = int(input('day?'))
download_input_file(day=day, session_token=session_token, output_file="input_" + str(day) + ".txt")


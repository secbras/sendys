# Códigos ANSI para cores
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

import requests

print(f"{GREEN}\n███████╗███████╗███╗   ██╗██████╗ ██╗   ██╗███████╗{RESET}")
print(f"{GREEN}██╔════╝██╔════╝████╗  ██║██╔══██╗╚██╗ ██╔╝██╔════╝{RESET}")
print(f"{GREEN}███████╗█████╗  ██╔██╗ ██║██║  ██║ ╚████╔╝ ███████╗{RESET}")
print(f"{GREEN}╚════██║██╔══╝  ██║╚██╗██║██║  ██║  ╚██╔╝  ╚════██║{RESET}")
print(f"{GREEN}███████║███████╗██║ ╚████║██████╔╝   ██║   ███████║{RESET}")
print(f"{GREEN}╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝    ╚═╝   ╚══════╝{RESET}")
print(f"{YELLOW}Desenvolvido pela SecBras Research            {BLUE}v1.0{RESET}")

target = input("\nDigite o IP ou o site (com ou sem http/https): ")

if not target.startswith("http"):
    target = "http://" + target

try:
    # Realizar várias requisições HTTP para detectar WAFs
    responses = [
        requests.get(target),
        requests.post(target, data={'test': 'test'}),
        requests.head(target)
    ]
    
    print(f"{GREEN}Conexão bem-sucedida com {target}{RESET}")

    for response in responses:
        headers = response.headers

        print("\nCabeçalhos:")
        for key, value in headers.items():
            print(f"{key}: {GREEN}{value}{RESET}")

except requests.exceptions.RequestException as e:
    print(f"{RED}Erro ao conectar-se ao alvo: {e}{RESET}")
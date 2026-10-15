import random

def tecnologias ():
    tecnologias =  ["nmap", "wireshark", "john the ripper", "hydra", "ollama", "burp suite", "metasploit"]
    return random.choice(tecnologias)

def grupos ():
    grupos = ["grupo 1", "grupo 2", "grupo 3", "grupo 4", "grupo 5", "grupo 6", "grupo 7"]
    return random.choice(grupos)

for i in range(7):
    tecnologia = tecnologias()
    grupo = grupos()
    print(f"Grupo: {grupo} - Tecnologia: {tecnologia}")
#  Generador Aleatorio de Grupos y Tecnologías

## Descripción

Este proyecto es un sencillo programa desarrollado en Python que asigna aleatoriamente una tecnología a un grupo de trabajo.

El programa dispone de una lista de siete tecnologías relacionadas con la informática y la ciberseguridad, y una lista de siete grupos. En cada ejecución, selecciona aleatoriamente un grupo y una tecnología, mostrando el resultado por pantalla.

## Tecnologías utilizadas

El programa utiliza **Python 3** y el módulo `random`, que permite realizar selecciones aleatorias.

### Herramientas disponibles

- Nmap
- Wireshark
- John the Ripper
- Hydra
- Ollama
- Burp Suite
- Metasploit

## Requisitos

- Tener instalado Python 3.
- No es necesario instalar dependencias adicionales, ya que `random` forma parte de la biblioteca estándar de Python.

## Instalación y ejecución

1. Clona el repositorio:

       git clone https://github.com/xM4rks/theme_giveaway

2. Accede al directorio del proyecto:

        cd theme_giveaway

3. Ejecuta el programa:

       python3 main.py


## Funcionamiento

El programa está dividido en tres partes:

1. **Función `tecnologias()`:** selecciona aleatoriamente una tecnología de la lista disponible.
2. **Función `grupos()`:** selecciona aleatoriamente un grupo de trabajo.
3. **Bucle `for`:** repite el proceso siete veces y muestra el grupo y la tecnología seleccionados en cada iteración.

## Ejemplo de salida

```text
Grupo: grupo 3 - Tecnologia: nmap
Grupo: grupo 1 - Tecnologia: wireshark
Grupo: grupo 5 - Tecnologia: metasploit
Grupo: grupo 2 - Tecnologia: ollama
Grupo: grupo 7 - Tecnologia: hydra
Grupo: grupo 4 - Tecnologia: burp suite
Grupo: grupo 6 - Tecnologia: john the ripper
```

*Nota: los resultados son aleatorios y pueden variar en cada ejecución. Un mismo grupo o tecnología puede aparecer varias veces.*

## Estructura del proyecto

    nombre-del-proyecto/
    ├── main.py
    └── README.md

- `main.py`: contiene el código fuente del programa.
- `README.md`: documenta el proyecto y explica cómo ejecutarlo.

##  Objetivo

Facilitar la asignación aleatoria de tecnologías a grupos para organizar actividades, prácticas o ejercicios relacionados con la informática y la ciberseguridad.

## Consideraciones

Las selecciones se realizan de forma independiente. Por tanto, el programa no garantiza que cada grupo o tecnología aparezca exactamente una vez. Si se necesita una asignación única, será necesario modificar la lógica del programa.

## Autor
Powered by xM4rks

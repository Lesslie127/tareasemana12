#Crear una matriz 3D que represente los datos de temperaturas diarias
#Primera dimension: Ciudades (3 Ciudades)
#Segunda dimension: Semanas (2)
#Tercera dimension: Dias de la semana (7 dias)
temperaturas = [
    [   # Ciudad 1 (Cuenca)
        [   # Semana 1
            {"city": "Cuenca", "day": "Lunes", "temp": 25},
            {"city": "Cuenca", "day": "Martes", "temp": 26},
            {"city": "Cuenca", "day": "Miércoles", "temp": 27},
            {"city": "Cuenca", "day": "Jueves", "temp": 28},
            {"city": "Cuenca", "day": "Viernes", "temp": 29},
            {"city": "Cuenca", "day": "Sábado", "temp": 30},
            {"city": "Cuenca", "day": "Domingo", "temp": 31}
        ],
        [   # Semana 2
            {"city": "Cuenca", "day": "Lunes", "temp": 24},
            {"city": "Cuenca", "day": "Martes", "temp": 25},
            {"city": "Cuenca", "day": "Miércoles", "temp": 26},
            {"city": "Cuenca", "day": "Jueves", "temp": 27},
            {"city": "Cuenca", "day": "Viernes", "temp": 28},
            {"city": "Cuenca", "day": "Sábado", "temp": 29},
            {"city": "Cuenca", "day": "Domingo", "temp": 30}
        ]
    ],
    [   # Ciudad 2 (Guayaquil)
        [   # Semana 1
            {"city": "Guayaquil", "day": "Lunes", "temp": 20},
            {"city": "Guayaquil", "day": "Martes", "temp": 21},
            {"city": "Guayaquil", "day": "Miércoles", "temp": 22},
            {"city": "Guayaquil", "day": "Jueves", "temp": 23},
            {"city": "Guayaquil", "day": "Viernes", "temp": 24},
            {"city": "Guayaquil", "day": "Sábado", "temp": 25},
            {"city": "Guayaquil", "day": "Domingo", "temp": 26}
        ],
        [   # Semana 2
            {"city": "Guayaquil", "day": "Lunes", "temp": 19},
            {"city": "Guayaquil", "day": "Martes", "temp": 20},
            {"city": "Guayaquil", "day": "Miércoles", "temp": 21},
            {"city": "Guayaquil", "day": "Jueves", "temp": 22},
            {"city": "Guayaquil", "day": "Viernes", "temp": 23},
            {"city": "Guayaquil", "day": "Sábado", "temp": 24},
            {"city": "Guayaquil", "day": "Domingo", "temp": 25}
        ]
    ],
    [   # Ciudad 3 (Quito)
        [   # Semana 1
            {"city": "Quito", "day": "Lunes", "temp": 30},
            {"city": "Quito", "day": "Martes", "temp": 31},
            {"city": "Quito", "day": "Miércoles", "temp": 32},
            {"city": "Quito", "day": "Jueves", "temp": 33},
            {"city": "Quito", "day": "Viernes", "temp": 34},
            {"city": "Quito", "day": "Sábado", "temp": 35},
            {"city": "Quito", "day": "Domingo", "temp": 36}
        ],
        [   # Semana 2
            {"city": "Quito", "day": "Lunes", "temp": 29},
            {"city": "Quito", "day": "Martes", "temp": 30},
            {"city": "Quito", "day": "Miércoles", "temp": 31},
            {"city": "Quito", "day": "Jueves", "temp": 32},
            {"city": "Quito", "day": "Viernes", "temp": 33},
            {"city": "Quito", "day": "Sábado", "temp": 34},
            {"city": "Quito", "day": "Domingo", "temp": 35}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        city_name = semana[0]["city"]
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {city_name}, Semana: {promedio:.2f}°C")
    print()

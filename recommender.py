# Datos de bancos (pueden expandirse o cargarse de un archivo)
bancos = [
    {
        "nombre": "Sabadell",
        "producto": {"Muy bueno plus", "Muy bueno", "Bueno", "Regular"},
        "antiguedad_minima": 10,
        "ingresos_minimos": 0,
        "tasa_interes": 2.30,
        "requisitos": "Funcionarios o >10 años antigüedad",
        "financiacion_maxima": 100,
        "convenio": "Si",
    },
    {
        "nombre": "Deutsche Bank",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "Ingresos >50,000€/año",
        "financiacion_maxima": 90,
        "convenio": "Si",
    },
    {
        "nombre": "UCI",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "InDeutsche",
        "convenio": "Si",

    },
     {
        "nombre": "Unicaja",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "InDeutsche",
        "convenio": "Si"
    },# Agrega más bancos...
    {
        "nombre": "Abanca",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "InDeutsche",
        "convenio": "Si"

    },# Agrega m
    {
        "nombre": "KutxaLaboral",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "InDeutsche",
        "convenio": "Si"

    },# Agrega m
       {
        "nombre": "Santander",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "InDeutsche",
        "convenio": "Si"

    },# Agrega más bancos...
    {
        "nombre": "BBVA",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "InDeutsche",
        "convenio": ""
    },# Agrega m
    {
        "nombre": "Pichincha",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "InDeutsche",
        "convenio": "No"
    },# Agrega m
    {
        "nombre": "ING",
        "antiguedad_minima": 2,
        "ingresos_minimos": 50000,
        "tasa_interes": 1.35,
        "requisitos": "InDeutsche",
        "convenio": "No"
    },# Agrega m
]

# Perfil del cliente
perfil_cliente = {
    "antiguedad": 5,  # Años de experiencia laboral
    "ingresos": 40000,  # Ingresos anuales en euros
    "financiacion_necesaria": 90  # Porcentaje de financiación
}

# Lógica de recomendación
def recomendar_bancos(bancos, perfil):
    recomendados = []
    for banco in bancos:
        if (
            perfil["antiguedad"] >= banco["antiguedad_minima"] and
            perfil["ingresos"] >= banco["ingresos_minimos"] and
            perfil["financiacion_necesaria"] <= banco["financiacion_maxima"]
        ):
            recomendados.append(banco)
    return recomendados

# Obtener recomendaciones
recomendaciones = recomendar_bancos(bancos, perfil_cliente)

# Mostrar resultados
if recomendaciones:
    print("Bancos recomendados:")
    for banco in recomendaciones:
        print(f"- {banco['nombre']} (Tasa de interés: {banco['tasa_interes']}%)")
else:
    print("No se encontraron bancos que cumplan con los requisitos.")

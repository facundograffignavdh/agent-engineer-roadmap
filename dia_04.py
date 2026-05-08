tareas = ["revisar email", "escribir reporte", "llamar a cliente"]
print(tareas[0])
print(tareas[-1])
tareas.append("cerrar venta")
print(tareas[-1])
tareas.remove("escribir reporte")
print(len(tareas))
for tarea in tareas:
    print(f"- {tarea}")

contacto = {
    "nombre" : "Ignacio",
    "email" : "ignacioredondo@gmail.com",
    "telefono" : 1278999872
}
print(contacto["nombre"])
contacto["nacionalidad"] = "Costa Rica"
print(contacto)
contacto["telefono"] = 2873838219
print(contacto)
for clave, valor in contacto.items():
    print (clave, valor)
if "trabajo" in contacto:
    print (contacto["trabajo"])
else:
    print("no tiene trabajo")

agentes = [
    {"nombre": "OpenAI", "modelo": "GPT 5.5", "activo": False},
    {"nombre": "Claude", "modelo": "Sonnet 4.6", "activo": True},
    {"nombre": "Gemini", "modelo": "Pro 3", "activo": True}
]
print(agentes[0]["nombre"])
print(agentes[-1]["modelo"])
for agente in agentes:
    print(f"Agente: {agente['nombre']} · Modelo: {agente['modelo']}")
for agente in agentes:
    if agente['activo'] == True:
        print(f"Agente: {agente['nombre']}")

historial = []
historial.append({"rol":"usuario", "mensaje": "hola, necesito ayuda" })
historial.append({"rol":"asistente", "mensaje": "claro, ¿en qué te puedo ayudar?" })
historial.append({"rol":"usuario", "mensaje": "quiero aprender Python" })
print (len(historial))
for historia in historial:
    print(f"{historia['rol']}: {historia['mensaje']}")
for mensaje in historial:
    if mensaje['rol'] == "usuario":
        print(mensaje["mensaje"])
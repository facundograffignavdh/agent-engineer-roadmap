import json
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

# os.path.exists(...) — chequea si el archivo existe. Si no existe y lo intentás abrir, Python tira un error.
# "r" — modo lectura. El opuesto de "w".
# json.load(f) — lee el archivo JSON y lo convierte de vuelta a una lista de Python.
# len(conversation) — devuelve la cantidad de elementos de la lista. Te avisa cuántos mensajes hay en memoria.
# else: conversation = [] — si no existe el archivo, arranca con lista vacía como antes.
if os.path.exists("conversacion.json"):
    with open("conversacion.json", "r", encoding="utf-8") as f:
        conversation = json.load(f)
    print(f"Conversación previa cargada. {len(conversation)} mensajes en memoria.\n")
else:
    conversation = []
system_prompt = "Sos un mentor de programación para principiantes en español. Sos directo y didáctico."

print("Mini-Chatbot. Escribí 'salir' para terminar.\n")

while True:
    user_input = input("Tú: ").strip()
    if user_input.lower() == "salir":
        break
    if not user_input:
        continue
    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=system_prompt,
            messages=conversation[-20:]
        )
        assistant_text = response.content[0].text
        conversation.append({"role": "assistant", "content": assistant_text})
        print(f"Claude: {assistant_text}\n")
    except Exception as e:
        print(f"Error: {e}")

# open(...) — abre o crea el archivo conversacion.json en la carpeta actual.
# "w" — modo escritura. Si el archivo ya existe, lo sobreescribe. Si no existe, lo crea.
# encoding="utf-8" — para que las tildes y la ñ se guarden correctamente.
# as f — le da el nombre f al archivo abierto, para usarlo en la línea siguiente.
# with — se encarga de cerrar el archivo automáticamente cuando termina el bloque. Sin with, tendrías que cerrarlo vos a mano con f.close().
with open("conversacion.json", "w", encoding="utf-8") as f:
    json.dump(conversation, f, ensure_ascii=False, indent=2)
    # json.dump(...) — convierte la lista conversation a formato JSON y la escribe en el archivo.
    # conversation — los datos que querés guardar.
    # f — el archivo donde los escribís.
    # ensure_ascii=False — permite guardar tildes y ñ directamente, sin convertirlas a códigos raros como \u00f3.
    # indent=2 — hace el JSON legible, con indentación de 2 espacios. Sin esto el archivo sería una sola línea imposible de leer.
print("Conversación guardada en conversacion.json")
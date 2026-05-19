from anthropic import Anthropic         ##  trae herramienta de puente
from dotenv import load_dotenv      ## trae función para ocultar API key

load_dotenv()       ## ejecutando función que importe (lee API y carga a la memoria)
client = Anthropic()        ## guardo conexión a la API en variable (API key)

message = client.messages.create(       ## API call
    model="claude-haiku-4-5-20251001",       ## modelo más barato
    max_tokens=1024,     ## límite máx. de respuesta de Claude (token=0.8 palabras)
    messages=[
        {"role": "user",        ## quién habla
         "content": "Explicame en 3 oraciones qué es un AI Agent."      ## texto
         }
    ],
)

print(message.content[0].text)
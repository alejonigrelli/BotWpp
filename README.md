# BurgerBot

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python
- **Framework Web:** Flask
- **Integración de Mensajería:** Twilio API (WhatsApp Business API)
- **Despliegue:** Preparado para servidores en la nube (ej. AlwaysData) o pruebas locales mediante herramientas de túnel (como ngrok).


## 💻 Instalación y Uso Local

Para probar este bot en tu computadora, sigue estos pasos:

### 1. Clonar el repositorio y preparar el entorno
```bash
# Clonar el proyecto
git clone <tu-repositorio-url>
cd "Bot Wpp"

# Crear y activar un entorno virtual (recomendado)
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 2. Instalar dependencias
Asegúrate de tener instalados Flask y la librería de Twilio:
```bash
pip install Flask twilio
```

### 3. Ejecutar la aplicación
Inicia el servidor Flask localmente (por defecto correrá en el puerto 5000):
```bash
python app.py
```

### 4. Exponer el servidor a Internet (Ngrok)
Como Twilio necesita una URL pública a la cual enviar los mensajes (Webhooks), debes usar una herramienta como ngrok o alwaysData:
```bash
ngrok http 5000
```

### 5. Configurar Twilio
1. Ve a la consola de [Twilio](https://console.twilio.com/).
2. Entra a la sección de **WhatsApp Sandbox**.
3. En la configuración de *When a message comes in* (Cuando entra un mensaje), pega la URL pública generada por ngrok añadiendo la ruta del webhook. Debería quedar así:
   `https://<tu-url-de-ngrok>.ngrok-free.app/webhook` (Asegúrate de que el método sea `POST`).
4. ¡Envía un mensaje al número de prueba de Twilio para interactuar con BurgerBot!
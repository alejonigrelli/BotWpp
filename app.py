from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # obtener mensaje recibido
    mensaje_recibido = request.form.get('Body', '').strip().lower()
    
    # obtener nombre
    nombre_usuario = request.form.get('ProfileName', 'amigo/a')
    
    resp = MessagingResponse()
    
    # logica menu
    if mensaje_recibido == '1':
        respuesta_bot = "🍔 *Nuestra Carta* 🍕\n\n- Hamburguesa Completa: $5000\n- Pizza Muzzarella: $4500\n- Porción de Papas Fritas: $2000\n\nSi ya sabés qué pedir, escribí *2* para hacer tu pedido."
        
    elif mensaje_recibido == '2':
        respuesta_bot = "✍️ ¡Excelente! Por favor, escribime en un solo mensaje qué te gustaría pedir y a qué dirección te lo enviamos."
        
    elif mensaje_recibido == '3':
        respuesta_bot = "👨‍💻 ¡Dale! Aguardá un momento en línea que ya te conecto con una persona de nuestro equipo para que te ayude."
        
    else:
        respuesta_bot = f"👋 ¡Holaa {nombre_usuario}! Bienvenido a *BurgerBot* 🍔.\n\nPor favor, elegí una opción respondiendo con el número:\n\n*1* - Pedir la carta / menú 📋\n*2* - Hacer un pedido 🛵\n*3* - Hablar con un humano 🙋‍♂️"

    # enviar respuesta
    resp.message(respuesta_bot)
    return str(resp), 200, {'Content-Type': 'text/xml'}

if __name__ == '__main__':
    # Esto es solo para correrlo local, AlwaysData usa su propio sistema
    app.run(debug=True)

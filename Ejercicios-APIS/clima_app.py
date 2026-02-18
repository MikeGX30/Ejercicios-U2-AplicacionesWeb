from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# IMPORTANTE: Reemplaza con tu API key de OpenWeatherMap
WEATHER_API_KEY = '7cfd58384ccccf67fc6c53428cc98ab2'

@app.route('/')
def index():
    return render_template('clima.html')

@app.route('/api/clima')
def obtener_clima():
    try:
        # 1. Obtener ubicación por IP
        print("🔍 Obteniendo ubicación...")
        ip_response = requests.get('https://ipapi.co/json/')
        ubicacion = ip_response.json()
        
        ciudad = ubicacion.get('city', 'Ciudad desconocida')
        lat = ubicacion.get('latitude')
        lon = ubicacion.get('longitude')
        
        print(f"📍 Ubicación: {ciudad} ({lat}, {lon})")
        
        # 2. Obtener clima de esa ubicación
        weather_url = f'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': lat,
            'lon': lon,
            'appid': WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'es'
        }
        
        print(f"🌤️  Consultando clima con API key: {WEATHER_API_KEY[:8]}...")
        clima_response = requests.get(weather_url, params=params)
        
        # Imprimir código de respuesta
        print(f"📊 Código de respuesta: {clima_response.status_code}")
        
        # Si la API responde con error
        if clima_response.status_code != 200:
            error_data = clima_response.json()
            print(f"❌ Error de API: {error_data}")
            return jsonify({
                'error': f"Error de OpenWeatherMap: {error_data.get('message', 'Error desconocido')}. Verifica tu API key."
            }), 500
        
        clima = clima_response.json()
        print(f"✅ Datos del clima obtenidos correctamente")
        
        resultado = {
            'ciudad': ciudad,
            'pais': ubicacion.get('country_name'),
            'temperatura': clima['main']['temp'],
            'descripcion': clima['weather'][0]['description'],
            'humedad': clima['main']['humidity'],
            'viento': clima['wind']['speed'],
            'icono': clima['weather'][0]['icon']
        }
        
        return jsonify(resultado)
        
    except KeyError as e:
        print(f"❌ Error de clave: {e}")
        return jsonify({'error': f'Datos faltantes en la respuesta: {str(e)}'}), 500
    except Exception as e:
        print(f"❌ Error general: {e}")
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    print("🚀 Iniciando aplicación del clima...")
    print(f"🔑 API Key configurada: {WEATHER_API_KEY[:8]}..." if len(WEATHER_API_KEY) > 8 else "⚠️  API Key no configurada")
    app.run(debug=True)
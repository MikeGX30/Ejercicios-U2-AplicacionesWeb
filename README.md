# 🚀 Ejercicios de APIs con Flask

> Colección de aplicaciones web construidas con **Python + Flask** que consumen distintas APIs públicas y privadas.

---


**Dependencias principales:**

| Paquete | Versión |
|--------|---------|
| Flask | 3.1.2 |
| requests | 2.32.5 |
| Werkzeug | 3.1.5 |
| Jinja2 | 3.1.6 |
| firebase-admin | (solo para chat) |

---

## 📂 Estructura del Proyecto

```
Ejercicios-APIS/
├── chat_app.py          # 💬 Chat en tiempo real con Firebase
├── clima_app.py         # 🌤️  Clima por geolocalización IP
├── divisas_app.py       # 💱 Conversor de divisas
├── github_app.py        # 🐙 Dashboard de GitHub
├── libros_app.py        # 📚 Buscador de libros
├── lugares_app.py       # 📍 Lugares cercanos
├── peliculas_app.py     # 🎬 Buscador de películas y series
├── productos_api.py     # 🛒 API REST con SQLite (CRUD completo)
├── reddit_app.py        # 🤖 Lector de Reddit
├── templates/           # HTMLs de cada ejercicio
├── static/              # CSS, JS e imágenes
├── screenshots/         # Capturas de pantalla
├── productos.db         # Base de datos SQLite (autogenerada)
└── requirements.txt
```

---

## 🌤️ Ejercicio 1 — Clima por IP

**Archivo:** `clima_app.py` &nbsp;|&nbsp; **Puerto:** `5000`

Detecta automáticamente la ubicación del usuario por su IP y muestra el clima actual en tiempo real. Muestra temperatura, humedad, velocidad del viento, descripción del estado del cielo e ícono animado.

![Preview clima](1.png)

### APIs utilizadas
- [`ipapi.co`](https://ipapi.co) — Geolocalización por IP (sin key)
- [`OpenWeatherMap`](https://openweathermap.org/api) — Datos meteorológicos en tiempo real

### ⚙️ Configuración

```python
# clima_app.py — línea 7
WEATHER_API_KEY = 'TU_API_KEY'
# Obtén tu key gratis en: https://home.openweathermap.org/users/sign_up
```

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz web |
| `GET` | `/api/clima` | Clima actual detectado por IP |

### ▶️ Ejecutar

```bash
python clima_app.py
# → http://127.0.0.1:5000
```

---

## 💬 Ejercicio 2 — Chat en Tiempo Real

**Archivo:** `chat_app.py` &nbsp;|&nbsp; **Puerto:** `5000`

Aplicación de chat multiusuario con mensajes persistentes usando Firebase Realtime Database. Soporta avatares emoji, timestamps y lista de usuarios conectados actualmente.

![Preview chat](screenshots/chat.png)

### Servicio utilizado
- [`Firebase Realtime Database`](https://firebase.google.com/) — Backend en tiempo real

### ⚙️ Configuración

1. Crear un proyecto en [Firebase Console](https://console.firebase.google.com/)
2. Ir a **Configuración del proyecto → Cuentas de servicio → Generar nueva clave privada**
3. Guardar el archivo como `firebase-credentials.json` en la raíz del proyecto
4. Actualizar la URL de la base de datos:

```python
# chat_app.py — línea 14
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://TU-PROYECTO.firebaseio.com/'
})
```

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz del chat |
| `GET` | `/api/mensajes` | Últimos 50 mensajes ordenados |
| `POST` | `/api/mensajes` | Enviar un nuevo mensaje |
| `DELETE` | `/api/mensajes/<id>` | Eliminar un mensaje |
| `POST` | `/api/usuarios/online` | Registrar usuario como activo |
| `GET` | `/api/usuarios/online` | Lista de usuarios conectados |

### 📨 Body del mensaje (POST)

```json
{
  "usuario": "nombre_de_usuario",
  "texto": "Hola a todos! 👋",
  "avatar": "🧑‍💻"
}
```

### ▶️ Ejecutar

```bash
python chat_app.py
# → http://127.0.0.1:5000
```

> ⚠️ Asegúrate de tener `firebase-credentials.json` configurado antes de correr la app.

---

## 💱 Ejercicio 3 — Conversor de Divisas

**Archivo:** `divisas_app.py` &nbsp;|&nbsp; **Puerto:** `5000`

Convierte entre 13+ monedas internacionales con tasas de cambio actualizadas en tiempo real. Incluye banderas de países, símbolos de moneda y la fecha de última actualización de las tasas.

![Preview dolar](screenshots/dolar.png)

### API utilizada
- [`ExchangeRate-API v6`](https://www.exchangerate-api.com/) — Tasas de cambio en tiempo real

### ⚙️ Configuración

```python
# divisas_app.py — línea 7
API_KEY = 'TU_API_KEY'
# Obtén tu key gratis en: https://www.exchangerate-api.com/
```

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz web |
| `GET` | `/api/divisas/tasas/<moneda>` | Todas las tasas para una moneda base |
| `GET` | `/api/divisas/convertir?monto=&de=&a=` | Conversión entre dos monedas |
| `GET` | `/api/divisas/monedas` | Catálogo de monedas disponibles |

### Ejemplo de conversión

```
GET /api/divisas/convertir?monto=100&de=USD&a=MXN
```

### Monedas disponibles

| Flag | Código | Moneda |
|------|--------|--------|
| 🇺🇸 | `USD` | Dólar Estadounidense |
| 🇪🇺 | `EUR` | Euro |
| 🇬🇧 | `GBP` | Libra Esterlina |
| 🇯🇵 | `JPY` | Yen Japonés |
| 🇲🇽 | `MXN` | Peso Mexicano |
| 🇨🇦 | `CAD` | Dólar Canadiense |
| 🇦🇺 | `AUD` | Dólar Australiano |
| 🇨🇭 | `CHF` | Franco Suizo |
| 🇨🇳 | `CNY` | Yuan Chino |
| 🇧🇷 | `BRL` | Real Brasileño |
| 🇦🇷 | `ARS` | Peso Argentino |
| 🇨🇴 | `COP` | Peso Colombiano |
| 🇨🇱 | `CLP` | Peso Chileno |

### ▶️ Ejecutar

```bash
python divisas_app.py
# → http://127.0.0.1:5000
```

---

## 📍 Ejercicio 4 — Lugares Cercanos

**Archivo:** `lugares_app.py` &nbsp;|&nbsp; **Puerto:** `5001`

Encuentra lugares de interés cerca de una ubicación dada (lat/lon) con radio configurable. Muestra nombre, dirección, teléfono y horario de atención de cada lugar.

![Preview gasolinera](screenshots/gasolinera.png)

### API utilizada
- [`Overpass API`](https://overpass-api.de/) — Datos de OpenStreetMap, **sin API key requerida**

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz web |
| `GET` | `/api/lugares?lat=&lon=&tipo=&radio=` | Buscar lugares en el radio indicado |

### Tipos de lugares soportados

| Parámetro `tipo=` | Descripción |
|-------------------|-------------|
| `restaurant` | 🍽️ Restaurantes |
| `hospital` | 🏥 Hospitales |
| `cafe` | ☕ Cafeterías |
| `farmacia` | 💊 Farmacias |
| `tienda` | 🛒 Supermercados |
| `gasolinera` | ⛽ Gasolineras |
| `banco` | 🏦 Bancos |
| `hotel` | 🏨 Hoteles |

### Ejemplo de uso

```
GET /api/lugares?lat=20.9667&lon=-89.6236&tipo=farmacia&radio=1500
```

### ▶️ Ejecutar

```bash
python lugares_app.py
# → http://127.0.0.1:5001
```

---

## 🎬 Ejercicio 5 — Películas y Series

**Archivo:** `peliculas_app.py` &nbsp;|&nbsp; **Puerto:** `5000`

Busca películas y series con información completa: trailers de YouTube, reparto, géneros, productoras, películas similares y recomendaciones personalizadas. También muestra la cartelera actual en México.

![Preview goat](screenshots/goat.png)

### API utilizada
- [`The Movie Database (TMDB)`](https://www.themoviedb.org/settings/api) — Base de datos cinematográfica

### ⚙️ Configuración

```python
# peliculas_app.py — línea 8
TMDB_API_KEY = 'TU_API_KEY'
# Obtén tu key gratis en: https://www.themoviedb.org/settings/api
```

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz web |
| `GET` | `/api/peliculas/buscar?q=&page=` | Buscar películas por título |
| `GET` | `/api/peliculas/<id>` | Detalle: trailers, reparto, similares |
| `GET` | `/api/peliculas/populares?page=` | Películas más populares |
| `GET` | `/api/peliculas/cartelera` | En cartelera (región MX) |
| `GET` | `/api/series/buscar?q=` | Buscar series de TV |
| `GET` | `/api/generos/peliculas` | Lista de géneros disponibles |

### ▶️ Ejecutar

```bash
python peliculas_app.py
# → http://127.0.0.1:5000
```

---

## 🐙 Ejercicio 6 — GitHub Dashboard

**Archivo:** `github_app.py` &nbsp;|&nbsp; **Puerto:** `5003`

Visualiza el perfil completo de cualquier usuario de GitHub: repositorios, estadísticas de estrellas y forks, lenguajes más usados y repositorios trending de la semana.

![Preview linus](screenshots/linus.png)

### API utilizada
- [`GitHub REST API v3`](https://docs.github.com/en/rest) — Sin autenticación (60 req/hora)

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz web |
| `GET` | `/api/github/usuario/<username>` | Perfil + repos + lenguajes + estadísticas |
| `GET` | `/api/github/trending` | Top 10 repos con más estrellas esta semana |
| `GET` | `/api/github/buscar/repos?q=&lenguaje=` | Búsqueda de repositorios |

### Datos del perfil devueltos

- Nombre, bio, avatar, ubicación, empresa, Twitter
- Total de repos públicos, seguidores y seguidos
- Total de ⭐ y forks acumulados en todos los repos
- Top 3 lenguajes más utilizados
- Top 5 repositorios más destacados por estrellas

### ▶️ Ejecutar

```bash
python github_app.py
# → http://127.0.0.1:5003
```

> ⚠️ Límite de 60 requests/hora sin autenticación. Para más, agrega un [Personal Access Token](https://github.com/settings/tokens) en los headers de las peticiones.

---

## 📚 Ejercicio 7 — Buscador de Libros

**Archivo:** `libros_app.py` &nbsp;|&nbsp; **Puerto:** `5000`

Busca libros por título, autor o categoría. Muestra portada, descripción, número de páginas, editorial, calificación promedio, precio y enlace de compra cuando está disponible.

![Preview principito](screenshots/principito.png)

### API utilizada
- [`Google Books API`](https://developers.google.com/books) — **Gratuita y sin API key**

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz web |
| `GET` | `/api/libros/buscar?q=&categoria=&max=` | Buscar libros (máx. 40 resultados) |
| `GET` | `/api/libros/<book_id>` | Detalle completo de un libro |
| `GET` | `/api/libros/categorias` | Lista de categorías populares |

### Categorías disponibles

`Fiction` · `Science` · `History` · `Biography` · `Technology` · `Business` · `Self-Help` · `Poetry` · `Mystery` · `Romance` · `Fantasy` · `Science Fiction` · `Programming` · `Education` · `Health` · `Art`

### ▶️ Ejecutar

```bash
python libros_app.py
# → http://127.0.0.1:5000
```

---

## 🛒 Ejercicio 8 — API REST de Productos (CRUD)

**Archivo:** `productos_api.py` &nbsp;|&nbsp; **Puerto:** `5000`

API REST completa con las 4 operaciones CRUD sobre una base de datos SQLite local. Incluye filtrado por categoría, ordenamiento dinámico, estadísticas por categoría e interfaz web para gestión visual.

![Preview productos](screenshots/productos.png)

### Base de datos

- **Motor:** SQLite (`productos.db`) — se crea automáticamente al iniciar
- **Tabla:** `productos` con campos: `id`, `nombre`, `descripcion`, `precio`, `stock`, `categoria`, `fecha_creacion`, `fecha_actualizacion`

**Datos precargados de ejemplo:**

| Producto | Precio | Stock | Categoría |
|---------|--------|-------|-----------|
| Laptop HP | $15,999.99 | 10 | Electrónica |
| Mouse Logitech | $299.99 | 50 | Accesorios |
| Teclado Mecánico | $1,299.99 | 25 | Accesorios |
| Monitor Samsung | $3,499.99 | 15 | Electrónica |
| Webcam | $899.99 | 30 | Accesorios |

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz web |
| `POST` | `/api/productos` | ➕ Crear producto |
| `GET` | `/api/productos` | 📋 Listar todos los productos |
| `GET` | `/api/productos/<id>` | 🔍 Obtener un producto |
| `PUT` | `/api/productos/<id>` | ✏️ Actualizar producto |
| `DELETE` | `/api/productos/<id>` | 🗑️ Eliminar producto |
| `GET` | `/api/productos/stats` | 📊 Estadísticas generales y por categoría |
| `GET` | `/api/categorias` | 🏷️ Categorías únicas registradas |

### Filtros disponibles

```
GET /api/productos?categoria=Electrónica
GET /api/productos?orden=precio&dir=DESC
GET /api/productos?orden=stock&dir=ASC
```

### 📦 Body para crear/actualizar (JSON)

```json
{
  "nombre": "Audífonos Sony WH-1000XM5",
  "descripcion": "Audífonos inalámbricos con cancelación de ruido activa",
  "precio": 2499.99,
  "stock": 20,
  "categoria": "Accesorios"
}
```

### ▶️ Ejecutar

```bash
python productos_api.py
# → http://127.0.0.1:5000
# La base de datos se crea e inicializa automáticamente
```

---

## 🤖 Ejercicio 9 — Lector de Reddit

**Archivo:** `reddit_app.py` &nbsp;|&nbsp; **Puerto:** `5002`

Lee posts de cualquier subreddit filtrando por hot, new o top. Permite búsquedas globales en Reddit con información de puntos, comentarios y fecha de publicación.

![Preview redit](screenshots/redit.png)

### API utilizada
- [`Reddit JSON API`](https://www.reddit.com/dev/api/) — **Pública, sin autenticación**

### 🔗 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Interfaz web |
| `GET` | `/api/reddit/posts?subreddit=&filtro=&limit=` | Posts de un subreddit |
| `GET` | `/api/reddit/buscar?q=&limit=` | Búsqueda global en Reddit |
| `GET` | `/api/reddit/subreddits/populares` | Subreddits sugeridos |

### Parámetros de `posts`

| Parámetro | Valores | Default |
|-----------|---------|---------|
| `subreddit` | cualquier nombre | `python` |
| `filtro` | `hot` / `new` / `top` | `hot` |
| `limit` | 1 – 100 | `10` |

### Subreddits sugeridos incluidos

`python` · `learnprogramming` · `webdev` · `javascript` · `flask` · `technology` · `programming` · `mexico` · `argentina` · `es`

### ▶️ Ejecutar

```bash
python reddit_app.py
# → http://127.0.0.1:5002
```

---

## 🔑 Resumen de API Keys

| Ejercicio | API | Key requerida | Link de registro |
|-----------|-----|:---:|------|
| 🌤️ Clima | OpenWeatherMap | ✅ | [openweathermap.org](https://home.openweathermap.org/users/sign_up) |
| 💬 Chat | Firebase | ✅ | [firebase.google.com](https://console.firebase.google.com/) |
| 💱 Divisas | ExchangeRate-API | ✅ | [exchangerate-api.com](https://www.exchangerate-api.com/) |
| 📍 Lugares | Overpass / OSM | ❌ | [overpass-api.de](https://overpass-api.de/) |
| 🎬 Películas | TMDB | ✅ | [themoviedb.org](https://www.themoviedb.org/settings/api) |
| 🐙 GitHub | GitHub REST API | ❌ | [docs.github.com](https://docs.github.com/en/rest) |
| 📚 Libros | Google Books API | ❌ | [developers.google.com/books](https://developers.google.com/books) |
| 🛒 Productos | SQLite (local) | ❌ | — |
| 🤖 Reddit | Reddit JSON API | ❌ | [reddit.com/dev/api](https://www.reddit.com/dev/api/) |

---

## 🖼️ Capturas de pantalla

Para que las imágenes se muestren correctamente en GitHub, coloca los screenshots en una carpeta `screenshots/` con estos nombres exactos:

```
screenshots/
├── 1.png            # Clima
├── chat.png         # Chat en tiempo real
├── dolar.png        # Conversor de divisas
├── gasolinera.png   # Lugares cercanos
├── goat.png         # Películas y series
├── linus.png        # GitHub dashboard
├── principito.png   # Buscador de libros
├── productos.png    # API REST de productos
└── redit.png        # Lector de Reddit
```

---

<div align="center">
  <sub>Construido con 🐍 Python &nbsp;·&nbsp; 🌶️ Flask &nbsp;·&nbsp; ❤️ y mucho café</sub>
</div>

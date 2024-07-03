# Convertify

Convertify es una aplicación web sencilla que convierte listas de reproducción de Spotify a YouTube Music. Utiliza la API de Spotify y ytmusicapi (una API no oficial para YouTube Music) para realizar la conversión.

<!-- imagen -->
![Imagen_ejemplo](/assets/imagen-readme.jpg)

## Requisitos previos

- Python 3.9 o superior
- [Spotify Developer Account](https://developer.spotify.com/dashboard/login)
- [YouTube Music OAuth](https://ytmusicapi.readthedocs.io/en/latest/setup.html#authentication)

## Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/convertify.git
cd convertify
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar OAuth para YouTube Music

Ejecuta el siguiente comando para registrar oauth.json en el directorio y poder usar la API de YouTube Music:
```bash
ytmusicapi oauth
```

### 5. Crear una aplicación en Spotify Developer

 - Ve a [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) e inicia sesión.
 - Crea una nueva aplicación.
 - Copia el Client ID y Client Secret.
 - Configura el Redirect URI como `http://localhost:8000/callback` en la configuración de la aplicación de Spotify.

### 6. Configurar las variables de entorno

Crea un archivo .env en el directorio raíz del proyecto y agrega las siguientes variables de entorno:
```makefile
SECRET_KEY=tu_secreto_flask
CLIENT_ID_SPOTIFY=tu_client_id_de_spotify
CLIENT_SECRET_SPOTIFY=tu_client_secret_de_spotify
```

## Uso
```bash
flask run
```

La aplicación se ejecutará en http://localhost:8000.

## Funcionalidades
 - Login con Spotify: Inicia sesión con tu cuenta de Spotify para acceder a tus listas de reproducción.
 - Convertir listas de reproducción: Convierte tus listas de reproducción de Spotify a YouTube Music con un solo clic.

## Contribuir
¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o enviar un pull request.


import firebase_admin
from firebase_admin import credentials, storage

# Inicializa la app de Firebase con las credenciales
cred = credentials.Certificate(
    "firebase-credentials.json"
)  # Cambia esto por tu archivo de credenciales
firebase_admin.initialize_app(
    cred,
    {
        "storageBucket": "billabongcopy.appspot.com"  # Cambia esto por tu bucket de Firebase Storage
    },
)


# Función para subir un archivo a Firebase Storage
def upload_to_firebase(file_path, destination_path):
    bucket = storage.bucket()
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    print(f"Archivo {file_path} subido a {destination_path} en Firebase Storage.")


def get_file_url(file_name: str) -> str:
    bucket = storage.bucket()
    blob = bucket.blob(f"uploaded/{file_name}")

    # Generar un enlace de descarga temporal
    download_url = blob.generate_signed_url(expiration=3600)  # Expira en 1 hora
    return download_url


# Ejemplo de uso
file_path = "test.txt"
destination_path = "test/test.txt"
upload_to_firebase(file_path, destination_path)

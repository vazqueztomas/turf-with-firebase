import shutil
from fastapi import APIRouter, File, UploadFile

from ..firebase import get_file_url, upload_to_firebase

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World from pdf"}


@router.post("/upload")
async def upload_file_to_firebase(file: UploadFile = File(...)):
    # Guardar temporalmente el archivo subido
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Subir el archivo a Firebase Storage
    destination_path = (
        f"uploaded/{file.filename}"  # Aquí puedes personalizar la ruta en el bucket
    )
    upload_to_firebase(temp_file_path, destination_path)

    # Devolver una respuesta
    return {"filename": file.filename, "firebase_path": destination_path}


@router.post("/download")
def download_file(file_name: str):
    try:
        # Llama a la función externa para obtener la URL del archivo
        download_url = get_file_url(file_name)
        return {"url": download_url}
    except Exception as e:
        return {"error": str(e)}

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time

# Título de la aplicación
st.title("Aplicacion de deteccion de rostros")

# Inicializar el estado de la cámara
if "stop_camera" not in st.session_state:
    st.session_state["stop_camera"] = False

# Cargar el clasificador de rostros de OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Función para detectar rostros en tiempo real
def detectar_rostros_en_tiempo_real():
    st.subheader("Detectando rostros en tiempo real...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("No se pudo acceder a la cámara.")
        return

    # Botón de detener cámara fuera del bucle
    if st.button("Detener cámara", key="stop_button"):
        st.session_state["stop_camera"] = True

    try:
        frame_placeholder = st.empty()
        while not st.session_state.get("stop_camera", False):
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)
            time.sleep(0.03)

        st.session_state["stop_camera"] = False
    finally:
        cap.release()

def detectar_rostros_subiendo_imagen():
    st.subheader("Detecta rostros subiendo una imagen")
    uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convertir la imagen subida a un objeto PIL
        image = Image.open(uploaded_file)
        img_array = np.array(image)

        # Convertir a escala de grises
        gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

        # Detectar rostros
        # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        faces = face_cascade.detectMultiScale(gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30),
            maxSize=(200,200))

        # Dibujar rectángulos alrededor de los rostros
        for (x, y, w, h) in faces:
            cv2.rectangle(img_array, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mostrar la imagen con los rostros detectados
        st.image(img_array, channels="RGB", caption="Rostros detectados")

# Crear un formulario
st.header("Selecciona una opción:")

option = st.radio(
    "Selecciona una opción",
    ("Detectar rostros en tiempo real", "Detectar rostros subiendo una imagen")
)


if option == "Detectar rostros en tiempo real":
    if st.button("Iniciar cámara"):
        st.session_state["stop_camera"] = False
        detectar_rostros_en_tiempo_real()
elif option == "Detectar rostros subiendo una imagen":
    detectar_rostros_subiendo_imagen()
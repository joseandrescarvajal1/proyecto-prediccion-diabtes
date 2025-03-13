import streamlit as st
import requests
import logging
import json

def load_config():
    with open("config.json", "r") as file:
        config = json.load(file)
    return config["API_URL"]

API_URL = load_config()



def predecir_diabetes(edad, glucosa, presion, grosor_piel,
                     bmi, embarazos, insulina, pedigree):
    """
    Aquí colocarías la lógica de tu modelo.
    Este ejemplo simplemente devuelve un número ficticio.
    """

    logging.basicConfig(level=logging.DEBUG)

    # Llamada a la API

    payload = json.dumps({
        "edad": edad,
        "glucosa": glucosa,
        "grosor_piel": grosor_piel,
        "bmi": bmi,
        "presion_sanguinea": presion,
        "embarazos": embarazos,
        "insulina": insulina,
        "pedigree": pedigree
    })

    headers = {
        'Content-Type': 'application/json'
    }

    logging.debug(f"Enviando payload: {payload}")

    try:
        response = requests.request("GET", API_URL, headers=headers, data=payload)
        logging.debug(f"Respuesta recibida: {response.status_code} - {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            prediction = data.get("prediction", "Error en la respuesta")
            resultado_texto = "Positivo para diabetes" if prediction == 1 else "Negativo para diabetes"

            logging.info(f"Predicción: {prediction}")

            st.session_state.resultado = resultado_texto

            if prediction == 1:
                # st.warning("Positivo para diabetes")
                st.html(f"<div class='alert-msg'>🔴 Alerta: Posible Riesgo de Diabetes</div>")
            else:    
                st.html(f"<div class='no-alert-msg'>🟢 Sin Riesgo Significativo Detectado</div>")


        else:
            st.session_state.resultado = "Error en la respuesta de la API: "
            logging.error(f"Error en la respuesta de la API: {response.text}")
            st.error("Error en la respuesta de la API: " + response.text)

    except Exception as e:
        logging.exception("Error en la conexión con la API")
        st.session_state.resultado = f"Error en la conexión: {str(e)}"


def main():
    # Ajusta la configuración general de la página
    st.set_page_config(page_title="Predicción de Diabetes", layout="centered")

    # Algo de CSS para “simular” un fondo y colores
    st.markdown("""
<style>
/* General Background */
.stApp {
    background: linear-gradient(to right, #eef2f3, #dfe9f3);
    font-family: 'Segoe UI', Roboto, sans-serif;
}

/* Form Card Styling */
div[data-testid="stForm"] {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
    max-width: 800px;
    margin: auto;
    overflow: hidden;
    width: 100%;
}

/* Form Title */
.titulo-formulario {
    background: linear-gradient(to right, #0078D7, #005bb5); /* Blue Gradient */
    color: white;
    text-align: center;
    font-weight: bold;
    font-size: 1.7rem;
    padding: 1rem;
    margin-bottom: 0;
    border-top-left-radius: 12px;
    border-top-right-radius: 12px;
    width: 100%;
}

/* Form Container */
.form-container {
    padding: 2rem;
}

/* Gradient Buttons */
.stForm button {
    background: linear-gradient(to right, #0078D7, #005bb5) !important;
    color: white !important;
    border-radius: 8px !important;
    width: 100%;
    font-weight: bold;
    font-size: 1rem;
    border: none;
    transition: all 0.3s ease-in-out;
    padding: 0.8rem;
}

/* Button Hover Effect */
.stForm button:hover {
    background: linear-gradient(to right, #005bb5, #003f80) !important;
    transform: scale(1.03);
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

/* Input Fields */
.stForm input {
    background: white !important;
    color: black !important;
    border-radius: 6px;
}

/* Labels */
label {
    font-weight: 600 !important;
    color: #333;
}
                
div[data-baseweb="input"] {
    background: transparent !important;
}
div[data-baseweb="input"] > div {
    background: transparent !important;
}

.stElementContainer, div[role="alert"] * {
    color: black !important;
    font-weight: bold !important;
}                
                
p {
    color: black !important;
    font-weight: bold !important;
}
                
.stFormSubmitButton * {
                color: white !important;
}

.alert-msg {
    font-size:26px; padding: 10px; border: 2px solid rgb(241, 33, 147); background-color: #ffecec;
}
                
 .no-alert-msg
{
                font-size:26px; padding: 10px; border: 2px solid rgb(14 222 108); background-color: #e6ffe6;
    
}
</style>


    """, unsafe_allow_html=True)

    # Iniciamos el formulario con título integrado
    with st.form(key='diabetes_form'):
        st.markdown('<div class="titulo-formulario">FORMULARIO PREDICTOR DE DIABETES</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)


        with col1:
            edad = st.number_input("Edad (Años)", min_value=0, max_value=120, value=30)
            glucosa = st.number_input("Glucosa", min_value=0.0, max_value=300.0, value=100.0, step=1.0)
            grosor_piel = st.number_input("Grosor de la piel", min_value=0, max_value=99, value=20)
            bmi = st.number_input("Índice de masa corporal (BMI)", min_value=0.0, max_value=70.0, value=25.0, step=0.1)

        with col2:
            presion = st.number_input("Presión Sanguínea", min_value=0, max_value=200, value=80)
            embarazos = st.number_input("Número de embarazos", min_value=0, max_value=20, value=1)
            insulina = st.number_input("Insulina", min_value=0.0, max_value=900.0, value=30.0, step=0.1)
            pedigree = st.number_input("Diabetes Pedigree", min_value=0.0, max_value=3.0, value=0.5, step=0.1)

        # Botones dentro del formulario
        c1, c2 = st.columns(2)
        with c1:
            submit_button = st.form_submit_button("Calcular")
        with c2:
            clear_button = st.form_submit_button("Reestablecer Valores")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Lógica de los botones
    if clear_button:
        # "Limpiar" recarga la página para resetear los campos
        st.rerun()


    if submit_button:
        predecir_diabetes(
            edad, glucosa, presion, grosor_piel, bmi,
            embarazos, insulina, pedigree
        )
        

if __name__ == '__main__':
    main()

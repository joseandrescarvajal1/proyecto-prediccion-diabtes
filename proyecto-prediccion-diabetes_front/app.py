import streamlit as st

def predecir_diabetes(edad, glucosa, presion, grosor_piel,
                     bmi, embarazos, insulina, pedigree):
    """
    Aquí colocarías la lógica de tu modelo.
    Este ejemplo simplemente devuelve un número ficticio.
    """
    return 0.65  # Valor de ejemplo

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
</style>


    """, unsafe_allow_html=True)

    # Iniciamos el formulario con título integrado
    with st.form(key='diabetes_form'):
        st.markdown('<div class="titulo-formulario">FORMULARIO PREDICTOR DE DIABETES</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            edad = st.number_input("Edad (Años)", min_value=0, max_value=120, value=30)
            glucosa = st.number_input("Glucosa", min_value=0.0, max_value=300.0, value=100.0)
            grosor_piel = st.number_input("Grosor de la piel", min_value=0, max_value=99, value=20)
            bmi = st.number_input("Índice de masa corporal (BMI)", min_value=0.0, max_value=70.0, value=25.0)

        with col2:
            presion = st.number_input("Presión Sanguínea", min_value=0, max_value=200, value=80)
            embarazos = st.number_input("Número de embarazos (Pregnancies)", min_value=0, max_value=20, value=1)
            insulina = st.number_input("Insulina", min_value=0.0, max_value=900.0, value=30.0)
            pedigree = st.number_input("Diabetes Pedigree", min_value=0.0, max_value=3.0, value=0.5)

        # Botones dentro del formulario
        c1, c2 = st.columns(2)
        with c1:
            submit_button = st.form_submit_button("Calcular")
        with c2:
            clear_button = st.form_submit_button("Limpiar Formulario")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Lógica de los botones
    if clear_button:
        # "Limpiar" recarga la página para resetear los campos
        st.experimental_rerun()

    if submit_button:
        probabilidad = predecir_diabetes(
            edad, glucosa, presion, grosor_piel, bmi,
            embarazos, insulina, pedigree
        )
        st.success(f"La probabilidad estimada de diabetes es: {probabilidad * 100:.2f}%")

if __name__ == '__main__':
    main()

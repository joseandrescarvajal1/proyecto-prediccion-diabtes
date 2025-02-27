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
/* Fondo de la app */
.stApp {
    background-color: #F7F7F7;
}

/* Contenedor de la tarjeta del formulario */
div[data-testid="stForm"] {
    background-color: #FFFFFF;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    max-width: 900px; /* Se aumentó el ancho máximo */
    margin: auto;
    overflow: hidden; /* Para mantener los bordes redondeados */
    width: 100%;
}

/* Título integrado en la tarjeta */
.titulo-formulario {
    background-color: #115A9E; /* Azul */
    color: #FFFFFF; /* Texto blanco */
    text-align: center;
    font-family: 'Segoe UI', Roboto, sans-serif;
    font-weight: 600;
    font-size: 1.5rem;
    padding: 1rem;
    margin-bottom: 0;
    border-top-left-radius: 8px; /* Redondea las esquinas superiores */
    border-top-right-radius: 8px;
    width: 100%;
}

/* Contenido del formulario */
.form-container {
    padding: 2rem;
}

/* Botones */
.stForm button {
    background-color: #115A9E !important;
    color: #FFFFFF !important;
    border-radius: 6px !important;
    height: 3em;
    width: 100%;
    font-weight: 600;
    font-size: 1rem;
    border: none;
}

/* Labels en negrita */
label {
    font-weight: 600 !important;
}
</style>
    """, unsafe_allow_html=True)

    # Iniciamos el formulario con título integrado
    with st.form(key='diabetes_form'):
        st.markdown('<div class="titulo-formulario">PREDICTOR DE DIABETES - FORMULARIO</div>', unsafe_allow_html=True)
        
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

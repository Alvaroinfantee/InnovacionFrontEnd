import streamlit as st
import requests

# Function to send data to the API
def enviar_a_api(data):
    url = "https://prod-10.westus.logic.azure.com/workflows/39fa9f0c755b4d10b3fb2ac472ffcbb4/triggers/manual/paths/invoke/innovacion?api-version=2016-06-01"
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            st.success("¡Propuesta enviada correctamente!")
        else:
            st.error(f"Error en la respuesta de la API: {response.status_code}")
    except Exception as e:
        st.error(f"Error al enviar datos: {e}")

# Title of the page
st.title('Formulario del Departamento de Innovación')

# Reminder for the department
st.sidebar.write("Recordatorio: Nuestro deber es responder con un 'cómo' a las propuestas.")

# Form to collect user data
with st.form("formulario_innovacion"):
    que = st.text_input("¿Qué?", help="Describe qué quieres proponer.")
    cuando = st.text_input("¿Cuándo?", help="Indica una fecha o período estimado.")
    por_que = st.text_area("¿Por qué?", help="Explica las razones detrás de esta propuesta.")
    para_que = st.text_area("¿Para qué?", help="Describe el objetivo o la finalidad de la propuesta.")
    
    # Submit button
    submitted = st.form_submit_button("Enviar Propuesta")

    if submitted:
        data = {
            "que": que,
            "cuando": cuando,
            "por_que": por_que,
            "para_que": para_que
        }
        
        # Send data to the API
        enviar_a_api(data)

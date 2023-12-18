import streamlit as st

st.set_page_config(
   page_title="Sistema de Saúde",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

hide_menu_style = """<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

st.title("Saúde")

caixa = st.sidebar.selectbox("Saúde", ["Selecione", "IMC", "ChatBot"])
if caixa == "IMC":
    peso = st.number_input("Insira seu Peso (em quilogramas): ", step=1)
    altura = st.number_input("Insira sua altura (em centímetros): ", step=1)

    action = st.button("Calcular", type="primary")

    if action:
        altura_calculada = altura / 100
        altura_quadrada = altura_calculada * altura_calculada
        calculo = peso / altura_quadrada

        st.write(calculo)

        if calculo <= 18.5:
            st.write("Você está abaixo do peso.")
        elif calculo > 18.5 and calculo <= 24.9:
            st.write("Seu peso está normal")
        elif calculo > 25 and calculo <= 29.9:
            st.write("Sobrepeso.")
        else:
            st.write("Obesidade.")





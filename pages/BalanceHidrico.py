import streamlit as st

st.page_link("MdCalculator.py",icon="🩺")

st.title("🚰Balance hidrico")
st.write("Esta es una calculadora para calcular el balance hidrico; entradas y salidas(Adulto)")

st.divider()
peso = st.number_input("🐷Peso del paciente", value=1)
horas = st.slider("⏱️Horas de balance", 1,24)
st.divider()

st.write("## Ingresos")
col1, col2, col3 = st.columns(3)
with col1:
    ingreso1 = st.number_input("Ingreso 1", value=0)
with col2: 
    ingreso2 = st.number_input("Ingreso 2", value=0)
with col3:
    ingreso3 = st.number_input("Ingreso 3", value=0)

st.write("## Egresos" )
col4, col5, col6 = st.columns(3)
with col4:
    egreso1 = st.number_input("Egreso 1", value=0)
with col5:
    egreso2 = st.number_input("Egreso 2", value=0)
with col6:
    egreso3 = st.number_input("Egreso 3", value=0)

ingresot = (ingreso1 + ingreso2 + ingreso3)
egresot = (egreso1 + egreso2 + egreso3)
prebal = (ingresot - egresot)

st.write("El paciente cuenta con ventilacion mecanica, abdomen abierto o fiebre?")
on = st.toggle("Perdidas extras")

st.divider()

if ingresot >=1:
    st.write("➕El ingreso total es ", ingresot)
else: 
    st.write("🚩Coloca los ingresos")

if egresot >=1:
    st.write("➖El egreso total es ", egresot)
else:
    st.write("🚩Coloca los egresos")
st.divider()
orina = ((egreso1 + egreso2 + egreso3)/peso)/horas
st.write("💦*Uresis*(Coloca solo orina en los egresos)", orina)

st.divider()

if on:
    total = prebal -((peso * 1)*horas)
else:
    total = prebal -((peso * .3)*horas)
    
st.write("⚖️ Balance total ", total)
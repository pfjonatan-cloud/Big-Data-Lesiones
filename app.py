import streamlit as st
import pandas as pd

st.set_page_config(page_title='FC Deportivo Nexus', layout='wide')
st.title('FC Deportivo Nexus')
st.markdown('### Dashboard de Lesiones – Temporada 2024')
st.divider()

df = pd.read_csv('/Users/jonatanemanueltomassantos/Desktop/01_Introduccion/analisis/jugadores.csv')

st.subheader('Historial de lesiones')
st.dataframe(df, use_container_width=True, hide_index=True)

jugadores = ["Todos"] + sorted(df["jugador"].unique().tolist())
jugador_sel = st.selectbox("Filtrar por jugador", jugadores)

if jugador_sel != "Todos":
    df = df[df["jugador"] == jugador_sel]

st.divider()
st.subheader('Lesiones por región corporal')
conteo = df['region'].value_counts()
st.bar_chart(conteo)
st.divider()


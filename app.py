import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

# Carregar os dados
df = pd.read_csv('estacoesbike-tratado.csv')

# Título da aplicação
st.title('Data Storytelling - Estações de Bicicletas')

# Distribuição das estações por bairro
st.header('Distribuição das Estações por Bairro')
bairro_counts = df['bairro'].value_counts()
st.bar_chart(bairro_counts)

# Capacidade total por bairro
st.header('Capacidade Total por Bairro')
bairro_capacity = df.groupby('bairro')['capacidade'].sum()
st.bar_chart(bairro_capacity)

# Mapa das estações
st.header('Mapa das Estações')
mapa = folium.Map(location=[-8.05, -34.87], zoom_start=13)
for _, row in df.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['nome']).add_to(mapa)
folium_static(mapa)

# Conclusão e Insights
st.header('Conclusão e Insights')
st.write('Aqui podemos incluir possíveis soluções e insights baseados na análise dos dados.')

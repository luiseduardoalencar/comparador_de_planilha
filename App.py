import streamlit as st
import pandas as pd

# Função para comparar colunas e identificar inconsistências
def comparar_colunas(df1, coluna1, df2, coluna2):
    # Resetar os índices das colunas e alinhar pelo menor tamanho
    min_length = min(len(df1[coluna1]), len(df2[coluna2]))
    serie1 = df1[coluna1].reset_index(drop=True)[:min_length]
    serie2 = df2[coluna2].reset_index(drop=True)[:min_length]
    
    # Comparar valores das colunas selecionadas
    inconsistentes = serie1 != serie2
    inconsistencias = pd.DataFrame({
        'Linha': inconsistentes[inconsistentes].index,
        coluna1: serie1[inconsistentes],
        coluna2: serie2[inconsistentes]
    })

    if inconsistencias.empty:
        st.success("Os valores das colunas selecionadas são idênticos!")
    else:
        st.error("Há inconsistências nas colunas selecionadas:")
        st.dataframe(inconsistencias)

# Interface do usuário
st.title("Comparação de Colunas de Planilhas")

# Upload dos arquivos
uploaded_file1 = st.file_uploader("Upload da primeira planilha", type=["xlsx", "csv"])
uploaded_file2 = st.file_uploader("Upload da segunda planilha", type=["xlsx", "csv"])

if uploaded_file1 and uploaded_file2:
    # Leitura dos arquivos
    if uploaded_file1.name.endswith('.csv'):
        df1 = pd.read_csv(uploaded_file1)
    else:
        df1 = pd.read_excel(uploaded_file1)

    if uploaded_file2.name.endswith('.csv'):
        df2 = pd.read_csv(uploaded_file2)
    else:
        df2 = pd.read_excel(uploaded_file2)

    # Exibir uma pré-visualização das primeiras linhas das tabelas
    st.subheader("Pré-visualização da Primeira Planilha")
    st.dataframe(df1.head())

    st.subheader("Pré-visualização da Segunda Planilha")
    st.dataframe(df2.head())

    # Seleção de colunas
    coluna1 = st.selectbox("Selecione a coluna da primeira planilha", df1.columns)
    coluna2 = st.selectbox("Selecione a coluna da segunda planilha", df2.columns)

    # Botão para comparar
    if st.button("Comparar Colunas"):
        comparar_colunas(df1, coluna1, df2, coluna2)

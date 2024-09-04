import streamlit as st
import pandas as pd

def ordenar_planilha(df1, df2, id_coluna):
    df1[id_coluna] = df1[id_coluna].astype(str)
    df2[id_coluna] = df2[id_coluna].astype(str)
    df2_ordenada = df2.set_index(id_coluna).reindex(df1[id_coluna]).reset_index()
    return df2_ordenada

def comparar_colunas(df1, df2, coluna1, coluna2, id_coluna):
    df1[coluna1] = df1[coluna1].astype(str).fillna('')
    df2[coluna2] = df2[coluna2].astype(str).fillna('')
    inconsistencias = pd.DataFrame(columns=[id_coluna, 'Valor Planilha 1', 'Valor Planilha 2', 'Status'])

    try:
        for idx, (val1, val2) in enumerate(zip(df1[coluna1], df2[coluna2])):
            if val1 == val2:
                status = "Valores coincidem"
            else:
                status = "Valores não coincidem"
                inconsistencias = pd.concat([
                    inconsistencias, 
                    pd.DataFrame({
                        id_coluna: [df1[id_coluna][idx]],
                        'Valor Planilha 1': [val1],
                        'Valor Planilha 2': [val2],
                        'Status': [status]
                    })
                ], ignore_index=True)

        
        if inconsistencias.empty:
            st.success("Todos os valores das colunas selecionadas coincidem!")
        else:
            st.error("Há inconsistências nos valores das colunas selecionadas:")
            st.dataframe(inconsistencias)

    except Exception as e:
        st.error(f"Ocorreu um erro ao comparar as colunas: {str(e)}")

st.title("Ordenação e Comparação de Planilhas com Base na Referência")

uploaded_file1 = st.file_uploader("Upload da Planilha de Referência (Planilha 1)", type=["xlsx", "csv"])
uploaded_file2 = st.file_uploader("Upload da Planilha a ser Ordenada (Planilha 2)", type=["xlsx", "csv"])

if uploaded_file1 and uploaded_file2:
    if uploaded_file1.name.endswith('.csv'):
        df1 = pd.read_csv(uploaded_file1, dtype=str)
    else:
        df1 = pd.read_excel(uploaded_file1, dtype=str)

    if uploaded_file2.name.endswith('.csv'):
        df2 = pd.read_csv(uploaded_file2, dtype=str)
    else:
        df2 = pd.read_excel(uploaded_file2, dtype=str)

    st.subheader("Planilha de Referência (Planilha 1)")
    st.dataframe(df1.head())

    st.subheader("Planilha a ser Ordenada (Planilha 2)")
    st.dataframe(df2.head())

    id_coluna = st.selectbox("Selecione a coluna de ID para ordenação", df1.columns)

    if st.button("Ordenar"):
        try:
            df2_ordenada = ordenar_planilha(df1, df2, id_coluna)
            st.session_state['df2_ordenada'] = df2_ordenada
            st.success("Planilha 2 ordenada com sucesso!")
        except KeyError:
            st.error("Erro: A coluna de ID selecionada não existe em uma das planilhas.")
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {str(e)}")

if 'df2_ordenada' in st.session_state:
    df2_ordenada = st.session_state['df2_ordenada']
    st.subheader("Planilha 2 Ordenada")
    st.dataframe(df2_ordenada)

    coluna1 = st.selectbox("Selecione a coluna da Planilha 1 para comparação", df1.columns, key='coluna1')
    coluna2 = st.selectbox("Selecione a coluna da Planilha 2 para comparação", df2_ordenada.columns, key='coluna2')

    if st.button("Comparar Colunas"):
        comparar_colunas(df1, df2_ordenada, coluna1, coluna2, id_coluna)

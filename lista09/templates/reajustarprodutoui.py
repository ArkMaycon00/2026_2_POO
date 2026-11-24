import streamlit as st
import time
from service import Service


class ReajustarProdutoUI:
    @staticmethod
    def main():
        st.header("Reajustar Preço de Produtos")
        ReajustarProdutoUI.reajustar()

    @staticmethod
    def reajustar():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            percentual = st.number_input("Informe o percentual de reajuste (%)", value=0.0, format="%.2f")
            if st.button("Reajustar"):
                try:
                    Service.produto_reajustar(float(percentual))
                    st.success("Preços reajustados com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

import streamlit as st
import pandas as pd
import time
from service import Service


class ManterProdutoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterProdutoUI.listar()
        with tab2:
            ManterProdutoUI.inserir()
        with tab3:
            ManterProdutoUI.atualizar()
        with tab4:
            ManterProdutoUI.excluir()

    @staticmethod
    def listar():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            list_dic = []
            for obj in produtos:
                dic = obj.to_json()
                cat = Service.categoria_listar_id(obj.get_id_categoria())
                dic["categoria"] = cat.get_descricao() if cat is not None else ""
                list_dic.append(dic)
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        categorias = Service.categoria_listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada. Cadastre uma categoria antes de inserir produtos.")
            return
        descricao = st.text_input("Informe a descrição")
        preco = st.number_input("Informe o preço", min_value=0.0, format="%.2f")
        estoque = st.number_input("Informe o estoque", min_value=0, step=1)
        categoria = st.selectbox("Informe a categoria", categorias)
        if st.button("Inserir"):
            try:
                Service.produto_inserir(descricao, float(preco), int(estoque), categoria.get_id())
                st.success("Produto inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def atualizar():
        produtos = Service.produto_listar()
        categorias = Service.categoria_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de Produtos", produtos)
            descricao = st.text_input("Nova descrição", op.get_descricao())
            preco = st.number_input("Novo preço", min_value=0.0, value=float(op.get_preco()), format="%.2f")
            estoque = st.number_input("Novo estoque", min_value=0, value=int(op.get_estoque()), step=1)
            index_cat = 0
            for i, c in enumerate(categorias):
                if c.get_id() == op.get_id_categoria():
                    index_cat = i
                    break
            categoria = st.selectbox("Nova categoria", categorias, index=index_cat)
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    id_cat = categoria.get_id() if categoria is not None else op.get_id_categoria()
                    Service.produto_atualizar(id, descricao, float(preco), int(estoque), id_cat)
                    st.success("Produto atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def excluir():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produtos", produtos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.produto_excluir(id)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()

import streamlit as st
from templates.manterclienteui import ManterClienteUI
from templates.mantercategoriaui import ManterCategoriaUI
from templates.manterprodutoui import ManterProdutoUI
from templates.reajustarprodutoui import ReajustarProdutoUI


class IndexUI:
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Cadastro de Clientes",
                "Cadastro de Categorias",
                "Cadastro de Produtos",
                "Reajustar Preço de Produtos",
            ],
        )
        if op == "Cadastro de Clientes":
            ManterClienteUI.main()
        elif op == "Cadastro de Categorias":
            ManterCategoriaUI.main()
        elif op == "Cadastro de Produtos":
            ManterProdutoUI.main()
        elif op == "Reajustar Preço de Produtos":
            ReajustarProdutoUI.main()

    @staticmethod
    def main():
        IndexUI.menu_admin()


if __name__ == "__main__":
    IndexUI.main()

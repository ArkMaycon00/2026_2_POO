from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.categoria import Categoria
from models.categoriadao import CategoriaDAO
from models.produto import Produto
from models.produtodao import ProdutoDAO
from models.venda import Venda
from models.vendadao import VendaDAO
from models.vendaitem import VendaItem
from models.vendaitemdao import VendaItemDAO


class Service:
    # --- CLIENTE ---
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id: int):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_inserir(nome: str, email: str, fone: str):
        obj = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(obj)

    @staticmethod
    def cliente_atualizar(id: int, nome: str, email: str, fone: str):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(obj)

    @staticmethod
    def cliente_excluir(id: int):
        obj = Cliente(id, "x", "x", "x")
        ClienteDAO.excluir(obj)

    # --- CATEGORIA ---
    @staticmethod
    def categoria_listar():
        return CategoriaDAO.listar()

    @staticmethod
    def categoria_listar_id(id: int):
        return CategoriaDAO.listar_id(id)

    @staticmethod
    def categoria_inserir(descricao: str):
        obj = Categoria(0, descricao)
        CategoriaDAO.inserir(obj)

    @staticmethod
    def categoria_atualizar(id: int, descricao: str):
        obj = Categoria(id, descricao)
        CategoriaDAO.atualizar(obj)

    @staticmethod
    def categoria_excluir(id: int):
        obj = Categoria(id, "x")
        CategoriaDAO.excluir(obj)

    # --- PRODUTO ---
    @staticmethod
    def produto_listar():
        return ProdutoDAO.listar()

    @staticmethod
    def produto_listar_id(id: int):
        return ProdutoDAO.listar_id(id)

    @staticmethod
    def produto_inserir(descricao: str, preco: float, estoque: int, id_categoria: int):
        obj = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(obj)

    @staticmethod
    def produto_atualizar(id: int, descricao: str, preco: float, estoque: int, id_categoria: int):
        obj = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO.atualizar(obj)

    @staticmethod
    def produto_excluir(id: int):
        obj = Produto(id, "x", 0.0, 0, 0)
        ProdutoDAO.excluir(obj)

    @staticmethod
    def produto_reajustar(percentual: float):
        for obj in ProdutoDAO.listar():
            novo_preco = obj.get_preco() * (1 + percentual / 100)
            obj.set_preco(round(novo_preco, 2))
            ProdutoDAO.atualizar(obj)

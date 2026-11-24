class VendaItem:
    def __init__(self, id: int, qtd: int, preco: float, id_venda: int, id_produto: int):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_id_venda(id_venda)
        self.set_id_produto(id_produto)

    def set_id(self, id: int):
        self.__id = id

    def set_qtd(self, qtd: int):
        if qtd <= 0:
            raise ValueError("Quantidade inválida")
        self.__qtd = qtd

    def set_preco(self, preco: float):
        if preco < 0:
            raise ValueError("Preço inválido")
        self.__preco = preco

    def set_id_venda(self, id_venda: int):
        self.__id_venda = id_venda

    def set_id_produto(self, id_produto: int):
        self.__id_produto = id_produto

    def get_id(self) -> int:
        return self.__id

    def get_qtd(self) -> int:
        return self.__qtd

    def get_preco(self) -> float:
        return self.__preco

    def get_id_venda(self) -> int:
        return self.__id_venda

    def get_id_produto(self) -> int:
        return self.__id_produto

    def __str__(self):
        return f"{self.__id} - Qtd: {self.__qtd} - Preço: R$ {self.__preco:.2f}"

    def to_json(self):
        return {
            "id": self.__id,
            "qtd": self.__qtd,
            "preco": self.__preco,
            "id_venda": self.__id_venda,
            "id_produto": self.__id_produto
        }

    @staticmethod
    def from_json(dic):
        return VendaItem(dic["id"], dic["qtd"], dic["preco"], dic["id_venda"], dic["id_produto"])

class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int, id_categoria: int):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)

    def set_id(self, id: int):
        self.__id = id

    def set_descricao(self, descricao: str):
        if descricao == "":
            raise ValueError("Descrição inválida")
        self.__descricao = descricao

    def set_preco(self, preco: float):
        if preco < 0:
            raise ValueError("Preço inválido")
        self.__preco = preco

    def set_estoque(self, estoque: int):
        if estoque < 0:
            raise ValueError("Estoque inválido")
        self.__estoque = estoque

    def set_id_categoria(self, id_categoria: int):
        self.__id_categoria = id_categoria

    def get_id(self) -> int:
        return self.__id

    def get_descricao(self) -> str:
        return self.__descricao

    def get_preco(self) -> float:
        return self.__preco

    def get_estoque(self) -> int:
        return self.__estoque

    def get_id_categoria(self) -> int:
        return self.__id_categoria

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__preco:.2f} - Estoque: {self.__estoque}"

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "preco": self.__preco,
            "estoque": self.__estoque,
            "id_categoria": self.__id_categoria
        }

    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["id_categoria"])

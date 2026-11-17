class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_idCategoria(idCategoria)

    def set_id(self, id):
        if not isinstance(id, int) or id < 0:
            raise ValueError("Id deve ser um inteiro positivo")
        self.__id = id

    def set_descricao(self, descricao):
        if not isinstance(descricao, str) or not descricao.strip():
            raise ValueError("Descrição deve ser informada")
        self.__descricao = descricao.strip()

    def set_preco(self, preco):
        if isinstance(preco, bool) or not isinstance(preco, (int, float)) or preco < 0:
            raise ValueError("Preço deve ser um número maior ou igual a zero")
        self.__preco = float(preco)

    def set_estoque(self, estoque):
        if not isinstance(estoque, int) or estoque < 0:
            raise ValueError("Estoque deve ser um inteiro maior ou igual a zero")
        self.__estoque = estoque

    def set_idCategoria(self, idCategoria):
        if not isinstance(idCategoria, int) or idCategoria < 0:
            raise ValueError("Id da categoria inválido")
        self.__idCategoria = idCategoria

    def reajustar(self, percentual):
        if isinstance(percentual, bool) or not isinstance(percentual, (int, float)):
            raise ValueError("Percentual deve ser numérico")
        novo_preco = self.__preco * (1 + percentual / 100)
        if novo_preco < 0:
            raise ValueError("O reajuste não pode deixar o preço negativo")
        self.__preco = round(novo_preco, 2)

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def get_estoque(self): return self.__estoque
    def get_idCategoria(self): return self.__idCategoria

    def to_json(self):
        return {"id": self.__id, "descricao": self.__descricao,
                "preco": self.__preco, "estoque": self.__estoque,
                "idCategoria": self.__idCategoria}

    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"],
                       dic["estoque"], dic["idCategoria"])

    def __str__(self):
        return (f"{self.__id} - {self.__descricao} - R$ {self.__preco:.2f} "
                f"- Estoque: {self.__estoque} - Categoria: {self.__idCategoria}")

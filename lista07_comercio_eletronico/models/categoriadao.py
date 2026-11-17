import json
from pathlib import Path
from models.categoria import Categoria


class CategoriaDAO:
    def __init__(self):
        self.__arquivo = Path(__file__).resolve().parent.parent / "categorias.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        obj.set_id(max((item.get_id() for item in self.__objetos), default=0) + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return list(self.__objetos)

    def listar_id(self, id):
        return next((obj for obj in self.__objetos if obj.get_id() == id), None)

    def atualizar(self, obj):
        atual = self.listar_id(obj.get_id())
        if atual is None:
            return False
        self.__objetos[self.__objetos.index(atual)] = obj
        self.__salvar()
        return True

    def excluir(self, id):
        obj = self.listar_id(id)
        if obj is None:
            return False
        self.__objetos.remove(obj)
        self.__salvar()
        return True

    def __abrir(self):
        try:
            with self.__arquivo.open("r", encoding="utf-8") as arquivo:
                self.__objetos = [Categoria.from_json(item) for item in json.load(arquivo)]
        except FileNotFoundError:
            self.__objetos = []
        except (json.JSONDecodeError, TypeError, KeyError) as erro:
            raise ValueError(f"Arquivo de categorias inválido: {erro}") from erro

    def __salvar(self):
        with self.__arquivo.open("w", encoding="utf-8") as arquivo:
            json.dump([obj.to_json() for obj in self.__objetos],
                      arquivo, ensure_ascii=False, indent=2)

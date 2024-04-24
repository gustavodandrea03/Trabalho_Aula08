from categoria_produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self._tempoDeBateria = tempoDeBateria

    @property
    def tempoDeBateria(self):
        return self._tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, value):
        self._tempoDeBateria = value

    def getInformacoes(self):
        return {
            "modelo": self.modelo,
            "cor": self.cor,
            "preco": self.preco,
            "categoria": self.categoria.nome,
            "tempoDeBateria": self.tempoDeBateria
        }

    def cadastrar(self):
        pass

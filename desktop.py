from categoria_produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, value):
        self._potenciaDaFonte = value

    def getInformacoes(self):
        return {
            "modelo": self.modelo,
            "cor": self.cor,
            "preco": self.preco,
            "categoria": self.categoria.nome,
            "potenciaDaFonte": self.potenciaDaFonte
        }

    def cadastrar(self):
        pass

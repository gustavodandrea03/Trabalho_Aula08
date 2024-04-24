from categoria_produto import Categoria
from desktop import Desktop
from notebook import Notebook

if __name__ == "__main__":
    categoria1 = Categoria(1, print("Eletrônicos"))

    desktop1 = Desktop("Dell", "Preto", 3500, categoria1, "1100 W")
    desktop1.potenciaDaFonte = "600W"

    notebook1 = Notebook("Apple", "Prata", 1900, categoria1, "10 horas")
    notebook1.tempoDeBateria = "10 horas"

    print("Informações do Desktop:")
    print(desktop1.getInformacoes())
    print("\nInformações do Notebook:")
    print(notebook1.getInformacoes())

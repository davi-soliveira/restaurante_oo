from modelos.restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('melancia', 5.0, 'Grande')
prato_pao = Prato('Pao', 2.0, 'Pão de sal')

def main():
    print(bebida_suco)
    print(prato_pao)
    
    



if __name__ == "__main__":
    main()
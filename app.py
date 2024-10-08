from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', -3)
restaurante_praca.receber_avaliacao('Luiza',0 )
restaurante_praca.receber_avaliacao('Mariana', -5)

def main():
    Restaurante.listar_restaurantes()
    



if __name__ == "__main__":
    main()
from modelos.restaurante import Restaurante

restaurante_vegano = Restaurante('Veg', 'Healthy')
restaurante_churasco = Restaurante('Gaúcho', 'Carnes')
restaurante_koreano = Restaurante('Hanguó', 'Asiático')

restaurante_churasco.alternar_estado()
restaurante_churasco.receber_avaliacao('Luana', 2)
restaurante_churasco.receber_avaliacao('Gabi', 9)
restaurante_churasco.receber_avaliacao('Celeste', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
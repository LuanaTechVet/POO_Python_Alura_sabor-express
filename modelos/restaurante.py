from modelos.avaliacao import Avaliacao

# Uma classe é um modelo para criar objetos, para todos os restaurantes terem esses atributos. Entidade
class Restaurante: #Convenção da primeira maiúscula

    restaurantes = [] #Diretamente dentro da classe, mas fora dos métodos. Isso a torna um atributo de classe.

    def __init__(self, nome, categoria): #construtor, regras. Executado imediatamente após uma instância ser criada
        self._nome = nome.title()                 #self é convenção no python | title deixa a primeira maiuscula | _x é convenção avisando que é privado
        self._categoria = categoria       #Atributos de instância, pois cada objeto Restaurante terá seus próprios valores para esses atributos.
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome.ljust(25)} | Categoria: {self._categoria.ljust(2)}'
    
    @classmethod                  #Método da classe pq não precisa de um objeto para ser utilizado
    def listar_restaurantes(cls): #Convenção snake_case

        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')

        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') #O ativo não vai _ pq sempre que for acessar ela usaremos a property

    @property         #Para modificar ou validar a apresentação de um atributo
    def ativo(self):
        return '☑' if self._ativo else '☒'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property #possibilita acessar a média como se fosse um atributo (sem o () chamando diretamente)
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem Avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qntde_notas = len(self._avaliacao)
        media = round((soma_das_notas / qntde_notas) / 2, 1)
        return media
    
#Um objeto é um instância de uma classe
#restaurante_praca = Restaurante('Praça', 'Gourmet')
#restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

#restaurante_pizza.alternar_estado()

# Se printar cru o terminal mostra o "endereço de memória no pc" do objeto
#O dir() é uma função embutida do Python que serve para listar os atributos e métodos de um objeto. 
# É como se fosse um "raio-x" que revela tudo o que um objeto pode fazer e quais informações ele carrega.

#Restaurante.listar_restaurantes()

#print (restaurante_praca)

#vars é uma função que retorna o atributo __dict__ de um objeto, que é um dicionário contendo os atributos do objeto. 
#Ela funciona para instâncias de classes (objetos), mas aceita apenas 1 argumento/objeto por vez
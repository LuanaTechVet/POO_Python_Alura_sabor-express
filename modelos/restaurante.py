# Uma classe é um modelo para criar objetos
# Para todos os restaurantes ter esses atributos. Entidade
class Restaurante:
    nome = '' 
    categoria = ''
    status = False

#Um objeto é um instância de uma classe
restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

#Definido os valores
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'


restaurantes = [restaurante_pizza, restaurante_praca]
print ((restaurantes)) # Se printar cru o terminal mostra o "endereço de memória no pc" do objeto

print ((restaurante_praca.categoria))

print (dir(restaurantes))
#O dir() é uma função embutida do Python que serve para listar os atributos e métodos de um objeto. 
# É como se fosse um "raio-x" que revela tudo o que um objeto pode fazer e quais informações ele carrega.

print (vars(restaurante_praca))
#vars é uma função que retorna o atributo __dict__ de um objeto, que é um dicionário contendo os atributos do objeto. 
#Ela funciona para instâncias de classes (objetos), mas aceita apenas 1 argumento/objeto por vez
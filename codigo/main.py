from bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '17/06/1992', 1500)
    print(f'Teste = {funcionario_teste.idade()}')
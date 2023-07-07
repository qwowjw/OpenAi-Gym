import random

# Função de fitness (objetivo): encontrar o valor máximo da função f(x) = x^2
def fitness(individual):
    individual = int(individual)
    return individual ** 2

# Função de seleção dos pais usando torneio
def selecao(populacao):
    candidatos = random.sample(populacao, 2)
    return max(candidatos, key=fitness)

# Função de crossover (cruzamento)
def crossover(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

# Função de mutação
def mutacao(individual):
    index = random.randint(0, len(individual) - 1)
    novo_valor = random.randint(0, 9)
    individual = list(individual)
    individual[index] = str(novo_valor)
    return ''.join(individual)

# Configurações do algoritmo genético
tamanho_populacao = 20
tamanho_individuo = 10
numero_geracoes = 20

# Geração da população inicial
populacao = [''.join(random.choices('0123', k=tamanho_individuo)) for _ in range(tamanho_populacao)]

# Execução do algoritmo genético
for geracao in range(numero_geracoes):
    print(f'Geração {geracao+1}:')

    # Avaliação da população atual
    valores_fitness = [fitness(individual) for individual in populacao]
    melhor_individuo = max(populacao, key=fitness)
    print(f'  Melhor indivíduo: {melhor_individuo} - Fitness: {fitness(melhor_individuo)}')

    # Nova população gerada pela seleção, crossover e mutação
    nova_populacao = []
    for _ in range(tamanho_populacao):
        pai1 = selecao(populacao)
        pai2 = selecao(populacao)
        filho1, filho2 = crossover(pai1, pai2)
        filho1 = mutacao(filho1) if random.random() < 0.1 else filho1  # Taxa de mutação de 10%
        filho2 = mutacao(filho2) if random.random() < 0.1 else filho2  # Taxa de mutação de 10%
        nova_populacao.extend([filho1, filho2])

    populacao = nova_populacao

# Resultado final
melhor_individuo = max(populacao, key=fitness)
print('\nResultado final:')
print(f'Melhor indivíduo encontrado: {melhor_individuo} - Fitness: {fitness(melhor_individuo)}')

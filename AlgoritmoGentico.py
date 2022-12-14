import random
import time


    
dna = ['A','T','C','G']
model = "CTTCGCAACGGATCGTGAGCAACAGCGTCGCCTTCTTGGTGGAATTCGGTGACCGAAGTAACGATAGATGTTTTCCATCTACTAACCCAAAGCCGTCCGC"
chromosome_size = len(model)
population_size = 500
generations = 500

def weighted_choice(items):
  total_weight = sum((item[1] for item in items))
  element = random.uniform(0, total_weight)
  for item, weight in items:
    if element < weight:
      return item
    element = element - weight
  return item

def random_character():
  return random.choice(dna)

def random_population():
  population = []
  for i in range(population_size):
    chromosome = ""
    for j in range(chromosome_size):
      chromosome += random_character()
    population.append(chromosome)
  return population

def fitness(chromosome):
  fitness = 0
  for i in range(chromosome_size):
    fitness += abs(ord(chromosome[i]) - ord(model[i]))
  return fitness

def mutation(chromosome):
  chromosome_outside = ""
  mutation_chance = 100
  for i in range(chromosome_size):
    if int(random.random() * mutation_chance) == 1:
      chromosome_outside += random_character()
    else:
      chromosome_outside += chromosome[i]
  return chromosome_outside

def crossover(chromosome1, chromosome2):
  position = int(random.random() * chromosome_size)
  return (chromosome1[:position] + chromosome2[position:], chromosome2[:position] + chromosome1[position:])




def generate(population):
    for generation in range(generations):
      #print("Geração %s | População: '%s'" % (generation, population[0]))
      weight_population = []
      if(population[0] == model):
        break
      for individual in population:
        fitness_value = fitness(individual)
        if fitness_value == 0:
          pair = (individual, 1.0)
        else:
          pair = (individual, 1.0 / fitness_value)
        weight_population.append(pair)
      population = []
      for i in range(int(population_size)):
        individual1 = weighted_choice(weight_population)
        individual2 = weighted_choice(weight_population)
        individual1, individual2 = crossover(individual1, individual2)
        population.append(mutation(individual1))
        population.append(mutation(individual2))

    return population




if __name__ == "__main__":

  tempo_inicial = time.time() # em segundos

  population = random_population()
  
  population1 = generate(population)

  fit_string = population[0]
  minimum_fitness = fitness(population1[0])
  for individual in population1:
    fit_individual = fitness(individual)
    if fit_individual <= minimum_fitness:
      fit_string = individual
      minimum_fitness = fit_individual
  print("População Final: %s" % fit_string)
  print("Modelo: " + model)
valor = 0
for i in range(100):
  if model[i] != fit_string[i]:
    valor += 1
print("Diferença: ", valor)
tempo_final = time.time() # em segundos
total = tempo_final - tempo_inicial
print("Sem paralelismo, ", total, " segundos")
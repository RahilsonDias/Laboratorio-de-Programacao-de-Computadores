import random
caracters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
             " "]

random_string = ""
target_string = "METHINKS IT IS LIKE A WEASEL"

# Gera uma string aleatoria
for i in range(28):
    random_string += random.choice(caracters)

# Verifica a pontuacao dessa string
score = 0
for j in range(28):
    if random_string[j] == target_string[j]:
        score += 1

print(f"Gen 0: {random_string} -- score: {score}")

generation = 1
while score < 28:
    # Cria 100 copias com possíveis mutações
    for i in range(100):
        mutated_string = []
        # Performa mutacao nas strings
        for j in range(28):
            mutation_chance = random.random()
            if mutation_chance <= 0.05:
                mutated_string.append(random.choice(caracters))
            else:
                mutated_string.append(random_string[j])

        # Registra a pontuacao das strings
        mutated_score = 0
        for k in range(28):
            if mutated_string[k] == target_string[k]:
                mutated_score += 1

        # Guarda a string com maior pontuacao
        if mutated_score > score:
            random_string = ''.join(mutated_string)
            score = mutated_score

    print(f"Gen {generation}: {random_string} -- score: {score}")
    generation += 1

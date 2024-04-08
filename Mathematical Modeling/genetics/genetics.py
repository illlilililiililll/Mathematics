import matplotlib.pyplot as plt
import random

# Parameters
num_generations_adjusted = 500
initial_population = 100000

# Initial alleles
alleles = ['A', 'a', 'B', 'b']

# Initialize population with AaBb genotype
initial_genotype = 'AaBb'
population = [initial_genotype] * initial_population

def mysorted(s):
    # Separate the string into uppercase and lowercase letters
    uppercase = [char for char in s if char.isupper()]
    lowercase = [char.upper()+char for char in s if char.islower()]

    uppercase += lowercase
    uppercase.sort()
    for i in range(len(uppercase)):
        if uppercase[i][-1].islower():
            uppercase[i] = uppercase[i][-1]
    sorted_string = ''.join(uppercase)
    return sorted_string

def generate_offspring_correctly(parent1, parent2):
    offspring = ''
    # For each allele pair (Aa, Bb), choose one allele from each parent
    for i in range(0, len(parent1), 2):
        offspring += random.choice([parent1[i], parent1[i+1]]) + random.choice([parent2[i], parent2[i+1]])
    return mysorted(offspring)

def mutate_limited(genotype):
    if random.randint(1, 10**7) == 1:
        # Choose an allele pair to mutate and replace
        pair_to_replace = random.randint(0, 1) * 2  # 0 for the first pair, 2 for the second
        new_allele1 = 'C' if 'C' not in genotype else 'D'  # Example of new alleles
        new_allele2 = new_allele1.lower()
        genotype = genotype[:pair_to_replace] + new_allele1 + new_allele2 + genotype[pair_to_replace+2:]
        alleles.extend([new_allele1, new_allele2])
        print('!', end='')
    return genotype

# Run the simulation
population = [initial_genotype] * initial_population
genotype_counts_revised = []
population_sizes_revised = []

for generation in range(num_generations_adjusted):
    new_population = []
    genotype_count = {}
    for _ in range(len(population) // 2):
        parent1, parent2 = random.sample(population, 2)
        num_offspring = random.randint(1, 3)
        for _ in range(num_offspring):
            offspring = generate_offspring_correctly(parent1, parent2)
            offspring = mutate_limited(offspring)
            new_population.append(offspring)
            genotype_count[offspring] = genotype_count.get(offspring, 0) + 1
    population = new_population
    population_sizes_revised.append(len(population))
    genotype_counts_revised.append(genotype_count)
    print(f'Generation #{generation+1}\tpopulation {len(population)}\t({round((generation+1)/num_generations_adjusted*100, 3)}% done)')

# Plotting the revised simulation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Plot population size
ax1.plot(range(num_generations_adjusted), population_sizes_revised, label="Population Size")
ax1.set_title("Population Size Over Generations")
ax1.set_xlabel("Generation")
ax1.set_ylabel("Population Size")
ax1.legend()

# Plot genotype frequencies
# Sort the genotypes for consistent plotting
genotypes = sorted(set().union(*genotype_counts_revised))

# Calculate frequencies, ensuring we don't divide by zero
for genotype in genotypes:
    frequencies = []
    for genotype_count in genotype_counts_revised:
        total_genotypes = sum(genotype_count.values())
        # If there's no population to calculate the frequency from, set frequency to 0
        freq = genotype_count.get(genotype, 0) / total_genotypes if total_genotypes > 0 else 0
        frequencies.append(freq)
    
    # Plot the frequencies for each genotype
    ax2.plot(range(num_generations_adjusted), frequencies, label=genotype)

# Configure the plot
ax2.set_title("Genotype Frequencies Over Generations")
ax2.set_xlabel("Generation")
ax2.set_ylabel("Frequency")
# ax2.legend(loc='upper right')  # Move the legend out of the plot

# Display the plot with a tight layout
plt.tight_layout()
plt.show()
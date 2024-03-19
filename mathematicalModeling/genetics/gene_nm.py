import matplotlib.pyplot as plt
from collections import deque, Counter
import random

# Parameters
num_generations_adjusted = 500
initial_population_size = 10000

# Initialize population with AaBb genotype
initial_genotype = 'AaBb'
population = [initial_genotype] * initial_population_size

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

# Run the simulation
population = [initial_genotype] * initial_population_size
genotype_counts_revised = []
population_sizes_revised = []

for generation in range(num_generations_adjusted):
    new_population = deque()
    for _ in range(len(population) // 2):
        parent1, parent2 = random.sample(population, 2)
        num_offspring = random.randint(0, 4)
        for _ in range(num_offspring):
            offspring = generate_offspring_correctly(parent1, parent2)
            new_population.append(offspring)
    population = new_population
    genotype_count = Counter(new_population)
    population_sizes_revised.append(len(population))
    genotype_counts_revised.append(genotype_count)
    print(f'Generation #{generation+1}\tpopulation {len(population)}')

# Plotting the revised simulation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Plot population size
ax1.plot(range(num_generations_adjusted), population_sizes_revised)
ax1.set_title("Population Size Over Generations")
ax1.set_xlabel("Generation")
ax1.set_ylabel("Population Size")

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
plt.legend(loc='upper right')  # Move the legend out of the plot

# Display the plot with a tight layout
plt.tight_layout()
plt.show()
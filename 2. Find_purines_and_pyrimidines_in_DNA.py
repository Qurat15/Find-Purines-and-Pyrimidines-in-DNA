DNA = 'AGTTAGCTAGGAG'
# Number of Purines(A and G) 
a_count = DNA.count('A')
g_count = DNA.count('G')
purine_content = a_count + g_count
print(purine_content)

# Number of Pyrimidines(C and T)
c_count = DNA.count('C')
t_count = DNA.count('T')
pyrimidine_content = c_count + t_count
print(pyrimidine_content)

# Percentage of Purine
purine_percent = (purine_content/len(DNA)) * 100
print(purine_percent)

# Percentage of Pyrimidine
pyrimidine_percent = (pyrimidine_content/len(DNA)) * 100
print(pyrimidine_percent)
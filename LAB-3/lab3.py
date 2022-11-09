import csv
file = open('data.csv')
data = list(csv.reader(file))[:]
concepts = []
target = []

for i in data:
    concepts.append(i[:-1])
    target.append(i[-1])

specific_h = ['O']*len(concepts[0])
general_h = [['?' for i in range(len(specific_h))] for i in range(len(specific_h))]

for i, instance in enumerate(concepts):
    if target[i] == "Yes":
        for x in range(len(specific_h)):
            if specific_h[x] == 'O':
                specific_h[x] = instance[x]
            elif instance[x] != specific_h[x]:
                specific_h[x] = '?'
                general_h[x][x] = '?'
    if target[i] == "No":
        for x in range(len(specific_h)):
            if instance[x] != specific_h[x]:
                general_h[x][x] = specific_h[x]
            else:
                general_h[x][x] = '?'

indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]


for i in indices:
    general_h.remove(['?', '?', '?', '?', '?', '?'])

print("Final Specific : ", specific_h, sep = '\n')
print("Final General : ", general_h, sep = '\n')

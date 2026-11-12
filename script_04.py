with open('RF00373.fa', 'r') as file:
    lines = file.readlines()

sequences = {}
name = ''

for line in lines:
    line = line.strip()

    if line.startswith('>'):
        name = line[1:].split()[0]
        sequences[name] = ''
    else:
        sequences[name] = sequences[name] + line

with open('gc_report.txt', 'w') as file:
    for name in sequences:
        seq = sequences[name]
        gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
        file.write(name + '\t' + str(round(gc, 1)) + '\n')

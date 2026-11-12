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

print(sequences)


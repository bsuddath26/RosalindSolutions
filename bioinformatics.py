def gc_content(dna):
    gc = dna.count("G") + dna.count("C")
    return (gc / len(dna)) * 100

print(gc_content("ATGCGC"))
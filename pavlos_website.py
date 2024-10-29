dna_sequence={'A':'T','T':'A','G':'C','C':'G'}
sequence=input()
for char in sequence:
    print(dna_sequence[char],end='')
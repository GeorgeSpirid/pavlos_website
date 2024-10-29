dna_sequence={'A':'T','T':'A','G':'C','C':'G'}
rna_sequence={'A':'U','U':'A','G':'C','C':'G'}
choice=int(input("press 1 for DNA or 2 for RNA: "))
if(choice==1):
    sequence=input()
    for char in sequence:
        print(dna_sequence[char],end='')
elif(choice==2):
    sequence=input()
    for char in sequence:
        print(rna_sequence[char],end='')
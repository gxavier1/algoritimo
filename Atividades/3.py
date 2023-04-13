from itertools import permutations
lst = [''.join(p) for p in permutations(input("Digite letras: "))]
print(lst)
  
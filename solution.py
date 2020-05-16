"""
USANDO LA SOLUCION TRADICCIONAL
seq=[]

for a in range(2,101):
    for b in range(2,101):
        if a**b not in seq:
            seq.append(a**b)
print(len(seq))
"""

#ONE LINER SOLUTION USING SET -- ELIMINATE DUPLICATES
print(len(set([a**b for a in range(2,101) for b in range(2,101)])))

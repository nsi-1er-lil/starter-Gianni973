c = 6
P = 4 * c  
A = c ** 2  
b = A > 5

print(f"Périmètre du carré: {P}")
print(f"Aire du carré: {A}")
print(f"L'aire est-elle supérieure à 5 ? {b}")

def perimetre(x):
    return x * 4

print("Périmètre du carré:", perimetre(5))
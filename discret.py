results = []

for p in [False, True]:
    for q in [False, True]:
        for r in [False, True]:

            F = (not p) or (not q) or r
            results.append(F)

if all(results):
    print("Формула тотожно істинна")
elif not any(results):
    print("Формула тотожно хибна")
else:
    print("Формула ні істинна, ні хибна")
S = input()

#print(S)
length = len(S)
suffix = []

for i in range(length):
    suffix.append(S[i:])

#print(suffix)
suffix.sort()
#print(suffix)
for i in suffix:
    print(i)
#sortedSuffix = sorted(suffix, key=lambda x: x[0])
#print(sortedSuffix)
print("=====")
print("\n".join(suffix))
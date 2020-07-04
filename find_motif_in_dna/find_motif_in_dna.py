s1,s2 = open('rosalind_subs.txt').read().split()

for i in range(len(s1)):
    if s1.startswith(s2,i):
        print(i+1, end=" ")

print("\r")
print(" ".join(map(lambda v: str(v), [(i+1) for i in range(len(s1)) if s1.startswith(s2, i)])))

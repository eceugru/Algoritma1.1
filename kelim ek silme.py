S,K=input().split()
K=int(K)
if 1>=K or K>len(S):
    K=int(input())
c=[]
for i in range(len(S)):
     c.append(S[i:])
c.sort()
print(c[K-1])
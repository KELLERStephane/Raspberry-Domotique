def liste_premiers(N):
    L = list(range(2, N + 1))
    i = 0
    while i < len(L):
        p = L[i]
        j = i+1
        while j < len(L):
            if L[j] % p ==0:
                print(L[j])
                del(L[j])
            j = j + 1
            print(L)
        i = i + 1
    return(L)

print(liste_premiers(30))
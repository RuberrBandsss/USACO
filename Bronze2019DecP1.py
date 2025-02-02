with open('gymnastics.in', 'r') as file:
    fl = file.readline().strip().split()
    K = int(fl[0])
    N = int(fl[1])

    r = []
    for _ in range(K):
        l = file.readline().strip().split()
        r.append(list(map(int, l)))


output = 0

if N == 1:
    output = 0

else:
    for i in range (1, N+1):
        for j in range(1, i):
            counter = 0
            for s in r:
                pi = s.index(i)
                pj = s.index(j)

                if pi < pj:
                    counter +=1
            if counter == 0 or counter == K:
                output += 1


with open('gymnastics.out', 'w') as file:
    file.write(str(output) + '\n')

ls = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
for i in range(0, len(ls)):

    for j in range(i + 1, len(ls)):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
            print(ls)
            l = len(ls)

if l % 2 == 0:
    m1 = ls[l // 2]
    m2 = ls[l // 2]
    mid = (m1 + m2) / 2
    print(mid)

else:
    mid = ls[l // 2]
    print(mid)

    total=0
    for a in l:
        total += a
        mean=total/l
        print(mean)

def cannonball(N, S, hay):
    index = S-1
    not_out = True
    k = 1
    count = 0
    dir = 1
    while not_out:
        if hay[index][0] == 1 and k >= hay[index][1]:
            count += 1
            hay[index][1] = index + dir * k + 2
        elif hay[index][0] == 0:
            dir = -dir
            k += hay[index][1]
        index = index + dir * k
        if index < 0 or index > N-1:
            not_out = False
    return count


if __name__ == "__main__":
    N, S = [int(i) for i in input().split(" ")]
    hay = []
    for i in range(N):
        hay.append([int(i) for i in input().split(" ")])
    print(cannonball(N, S, hay))
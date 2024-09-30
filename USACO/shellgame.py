f = open("shell.in", "r")
out_file = open("shell.out", "w")

n = int(f.readline())

counts = [0, 0, 0]
order = [0, 1, 2]

for step in range(n):
    line = f.readline().strip().split()
    a = int(line[0])
    b = int(line[1])
    g = int(line[2])

    #swap a and b
    a -= 1
    b -= 1
    #want to swap order[a], order[b]
    temp = order[a]
    order[a] = order[b]
    order[b] = temp

    counts[order[g-1]] += 1

out_file.write(str(max(counts)))

f.close()
out_file.close()


















#other way: for loop and see if the pebble is under shell1, 2, or 3 and see which one has max pebbles

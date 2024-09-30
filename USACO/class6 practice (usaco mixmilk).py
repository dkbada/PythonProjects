f = open("mixmilk.in", "r")
g = open("mixmilk.out", "w")

#c1, c2, c3, m1, m2, m3

a = []
c = []
m = []
for i in range(3):
    a = f.readline().split()
    c.append(int(a[0]))
    m.append(int(a[1]))

#print(m)
for pour in range(100):
    #pour from bucket pour%3 to (pour+1)%3

    bucket1 = pour%3
    bucket2 = (pour+1)%3

    if m[bucket2] + m[bucket1] > c[bucket2]:
        how_much_can_i_pour = c[bucket2]-m[bucket2]

    else:
        how_much_can_i_pour = m[bucket1]
    
    m[bucket1] -= how_much_can_i_pour
    m[bucket2] += how_much_can_i_pour

    #print(m)
    
#write function needs a string
g.write(str(m[0])+"/n")
g.write(str(m[1])+"/n")
g.write(str(m[2])+"/n")

g.close()
f.close()

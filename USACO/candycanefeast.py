def cow_height_fin(n, m, cow, candy):
  for i in range(m):
    candy_l = [int(j+1) for j in range (candy[i])]
    for k in range(n):
      if cow[k] <= candy[i]:
        if cow[k] in candy_l:
            length = len(candy_l[0:candy_l.index(cow[k]+1)])
            candy_l = candy_l[candy_l.index(cow[k]+1):]
            cow[k] += length
      else:
        length = len(candy_l)
        candy_l = []
        cow[k] += length
  for i in range(len(cow)-1):
    print(cow[i])
  print(cow[len(cow)-1]).replace("\n", "")

  


if __name__ == "__main__":
  num = [int(i) for i in input().split(" ")]
  n = num[0]
  m = num[1]
  cow = [int(i) for i in input().split(" ")]
  candy = [int(i) for i in input().split(" ")] 
  print(cow_height_fin(n, m, cow, candy))

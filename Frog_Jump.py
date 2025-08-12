n = int(input())
l = eval(input())

states = [[0, 1]]  # [position, jumps]
visited = [0] * n

for i in range(n * 10):
    if i >= len(states):
        break
    pos, c = states[i]

    if pos >= n:
        print(c)
        break

    if visited[pos]:
        continue

    visited[pos] = 1
    jump = l[pos]

    if jump == 0:
        continue

    if pos + jump >= n:
        print(c + 1)
        break

    if pos + jump < n and not visited[pos + jump]:
        states.append([pos + jump, c + 1])

    if pos - jump >= 0 and not visited[pos - jump]:
        states.append([pos - jump, c + 1])
else:
    print("-1")

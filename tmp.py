import numpy as np

s = np.fromiter((x * x for x in range(0, 30)), float).reshape(15, 2)
print(s)


def up(s, step):
    for j in range(step, len(s[1]) - step):
        a.append(s[step][j])


def right(s, step):
    for i in range(step + 1, len(s) - step):
        a.append(s[i][len(s[1]) - step - 1])


def down(s, step):
    for j in range(len(s[1]) - 2 - step, step - 1, -1):
        a.append(s[len(s) - 1 - step][j])


def left(s, step):
    for i in range(len(s) - 2 - step, step, -1):
        a.append(s[i][step])


def check():
    global a
    step = 0
    a = []
    while step <= ((len(s[1]) - 2) // 2) and step <= ((len(s) - 2) // 2):
        up(s, step)
        right(s, step)
        down(s, step)
        left(s, step)
        step += 1
    up(s, step)
    for _ in range(1):
        if len(a) >= len(s) * len(s[1]):
            break

        right(s, step)
        if len(a) >= len(s) * len(s[1]):
            break
        down(s, step)
        if len(a) >= len(s) * len(s[1]):
            break
        left(s, step)


check()
print(a)
print(len(a))

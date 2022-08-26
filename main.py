from clock import Clock12

try:
    c1 = Clock12(123)
    c2 = Clock12()
    c2.input()
    c1.output()
    c2.output()

except BaseException as e:
    print(e)

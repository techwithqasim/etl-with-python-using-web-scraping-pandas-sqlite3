a=200
b=250
c=300

for i in range(1,5):
    ans = a*b/c
    a -= 10
    b +=20
    print(a)
    print(b)
    print(ans)


from icecream import ic

a=200
b=250
c=300

for i in range(1,5):
    ans = ic(a*b/c)
    a -= 10
    b +=20
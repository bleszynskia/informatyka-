N = 8

kwota= 1000

rata= kwota/N

konto = 0,00 


for i in range(N):
    konto= konto+rata


print()
print('powinno być =', kwota)
print('stan konta', konto)
'''
n = int(input('Qual nunméro você deseja: '))

while n > 0:
  if(n % 2 == 0):
    print('Par')
  else:
    print('ímpar')
  n -= 1
'''

for i in range(1,4,1):
  n = int(input('Qual nunméro você deseja: '))
  if(n % 2 == 0):
    print('Par')
  else:
    print('ímpar')
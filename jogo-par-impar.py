par_impar = int(input("Digite 0 se Alice é par ou 1 se Bob é par: "))
qtd_dedo_alice = int(input("Digite a quantidade de dedos estendidos de Alice: "))
qtd_dedo_bob = int(input("Digite a quantidade de dedos estendidos de Bob: "))

# atribuindo valores ao par e impar antes da condicional podemos reduzir o número de if's
par = 0
impar = 1

#fazendo a comparação para saber quem jogou par ou impar

if par_impar == 1:
  par = 1
  impar = 0

''' Soma da quantidade de dedos, para depois verificar
se é par  ou impar e imprimir o vencedor'''

if (qtd_dedo_alice + qtd_dedo_bob) % 2 == 0:
  print(par)
else:
  print(impar)

#neste código, imprimir 0 significa que Alice ganhou e imprimir 1 que quem ganhou foi o Bob
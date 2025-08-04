import random
def main():
  numAleatorio = random.randint(1, 485)

  numero = 0
  i = 0
  while numero != numAleatorio:
    numero = int ( input("Digite um numero:"))
    
    if numero > numAleatorio:
      print("O seu numero e maior")
    elif numero < numAleatorio:
      print("O seu numero e menor")
    i += 1

    print("\n")

  print("Voce acertou, com " , i, "tantativas")
  return 0
main()

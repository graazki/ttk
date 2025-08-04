def main():
    numero = int ( input ( "Digite um numero"))
    

    i = 2

    while numero != i and numero != 1:
        if numero % i == 0:
            break
        i += 1

        if numero == i:
           print ("O numero", numero, "e primo")
        elif numero == 1:
            print ("O numero 1 nao e primo")
        else:
           print ("O numero ", numero, "nao primo porque e divisivel por ", i)


    return 0
main()
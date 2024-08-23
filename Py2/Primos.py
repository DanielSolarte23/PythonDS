numero = int(input("Ingrese numero entero para obtener su binario: "))

binario= ""

while(True):
    resultado = numero//2
    residuo = numero % 2
    binario = binario +  str(residuo)
    if(resultado == 1):
        binario = binario + str(resultado)
        break
    numero=resultado
print("Binario resultante: ", binario)

# for i in range(len(binario)-1,-1,-1):
#     print(binario[i], end="")
    
    
#QUE MIRA SAPO


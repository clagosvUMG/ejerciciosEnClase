#Imprimir Números Impares

numero=0
for i in range(1,101):
    if i%2!=0:
        print(i)
        numero=numero+1
print("Numeros Impares de 1 a 100")
print(numero)

#Permitir solo Ingresar S o N
dato=str(input("Ingrese un Valor: "))
if dato =="s":
    print("Tu respuesta es Sí")
elif dato =="N":
    print("Tu respuesta es No")
else:
    print("Dato Erroneo")
print("hola que hace")

x=int(input("introduse un nuemro pai"))
print("{} este es el numero q metiste".format(x))
cont=0
while x>cont :
	print(cont,end="*")
	cont+=1
	pass

c=int(input("introduse un nuemro pai"))
v=int(input("introduce un segundo numero"))
print("{} este es el numero q metiste".format(c))
if c<10:
	print("{} es menor q 10".format(c))
	pass
else:
	print("{} es mayor que 10".format(c))
c=c+v-2
print("esto es el resultado de la suma y las resta de 2 de los dos numero q metiste {}".format(c))
print("esto solo e una puevita")
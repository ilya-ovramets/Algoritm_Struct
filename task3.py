#Визначити довжину степеня числа у бінарному коді;

k  =int(input("k = "));
m = int(input("m = "));

caunt_repit = 2**m+1
result = 0;
i = 0;

while result <= caunt_repit:
	i+=1
	result = i**k



print("Необхідна степінь",i);
print(result);
print(bin(result));
def media (b1, b2, b3, b4):
    return (b1 + b2 + b3 + b4) / 4

print("\033[33m-=" * 10 + " Média Final em História " + "-=" * 10 + "\033[m")
b1 = float(input("\nDigite sua média de história no primeiro bimestre: "))
b2 = float(input("Digite sua média de história no segundo bimestre: "))
b3 = float(input("Digite sua média de história no terceiro bimestre: "))
b4 = float(input("Digite sua média de história no quarto bimestre: "))
print(f"\n\033[34mA média final em história é: {media(b1, b2, b3, b4)}!!!")

if media(b1, b2, b3, b4) >=7:
    print(f"\033[32mParabéns!!! você foi APROVADO em história!!!\033[m")
else:
    print(f"\033[31mInfelizmente :( você foi REPROVADO em  história!!!\033[m")
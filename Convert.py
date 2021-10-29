dollar = int(input()) #ввод доллара
cent = int(input()) #ввод цента
ruble=0
kopeyka = 0
euro = 0
eurocent =0
#создание переменных для рубля копейки евро и евроцента
dollar = dollar + (cent/100) #объединение доллара и цента в одну переменную
euro = dollar * 0.86 # подсчет евро

ruble = dollar *70 #подсчет рублей
eurocent = euro % 1 #подсчет увроцентов через остаток от деления (пример 19,69 евро при делении на 1, остатком дадут 69)
kopeyka  = ruble % 1 #то же самое с рублем
euro = euro - eurocent #подсчет евро - евроценты
ruble = ruble - kopeyka #то же самое с рублем

print("Евро", euro)
print("Евроцент", eurocent*100)
print("Рубль", ruble)
print("Копейка", kopeyka*100)
#вывод

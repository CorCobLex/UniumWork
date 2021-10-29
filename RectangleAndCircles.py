while(True):
    print("Введите длину прямоугольника:")
    lenght=int(input())
    print("Введите ширину прямоугольника:")
    height=int(input())
    print("Введите радиус 1 окружности:")
    radius1=int(input())
    print("Введите радиус 2 окружности:")
    radius2=int(input())

    SRec=height*lenght
    Sokr1 = radius1*radius1*4
    Sokr2 = radius2*radius2*4
    if(Sokr1+Sokr2<SRec):
        print("Окружности поместяться в прямогуольник точно")
    elif(Sokr1+Sokr2==SRec):
        print("Окружности поместяться в прямогуольник и займут его полностью")
    else:
        print("Окружности не поместились :(\n")


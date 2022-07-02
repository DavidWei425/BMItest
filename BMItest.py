#男女BMI判定
sex = str(input('請問你(妳)的性別為(M/F) : '))
height = eval(input('請輸入身高(cm) : \n'))
weight = eval(input('請輸入體重(kg) : \n'))
bmi = round(weight / (height / 100)**2, 1)
print('你的BMI為 : \n ', bmi)
if sex == 'M':
    if bmi>25:
        print('體重過重')
    elif bmi >= 20 and bmi <= 25:
        print('身材適中')
    else :
        print('體重過輕')
elif sex == 'F':
    if bmi > 22:
        print('體重過重')
    elif bmi >= 18 and bmi <= 22:
        print('身材適中')
    else :
        print('體重過輕')
else:
    print('性別輸入錯誤無法判定')
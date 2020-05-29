viruchka = int(input('Vvedite znachenie viruchki - '))
izderjki = int(input('vvedite znachenie izderjek - '))
kolichestvo_sotrudnikov = int(input('vvtdite colichestvo sotrudnicov - '))
pribyl = viruchka - izderjki
if pribyl <= 0:
    print('firma rabotaet s ubitkom')
else:
    print('firma rabotaet s pribylu')
    print('renabelnost - ', viruchka / pribyl)
    print('pribyl na odnogo strudnika - ', pribyl / kolichestvo_sotrudnikov)

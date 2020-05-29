ss = int(input('Vvedite vremya v sekundah - '))
hh = ss // 3600
ss = ss % 3600
mm = ss // 60
ss = ss % 60
print(hh, ':', mm, ':', ss)

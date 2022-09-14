faktorialGenap = {}

def itungFaktorial(num):
    hasil = 1
    for i in range(1,num+1):
        hasil *= i
    return hasil

inputUser1 = int(input('Masukakan range data : '))
for i in range (inputUser1):
    if i % 2 == 0:
        faktorialGenap[i] = itungFaktorial(i)

print(faktorialGenap)

inputUser2 = int(input('Data ditampilkan : '))
for key,value in faktorialGenap.items():
    if value != inputUser2:
        print('Data tidak ditemukan')
        break
    else:
        print('Data ditemukan')
        break
    
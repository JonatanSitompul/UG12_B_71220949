print('Selamat datang di program pembuat piramida berlubang')
b = int(input('masukan angka: '))

ruang = b-1 
for i in range(b):
    print(' '*ruang, end='')
    print('*' if i == 0 else '**' if i != 0 and i != b-1 else '*'*(b*2-1))
    ruang -= 1

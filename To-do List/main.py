import os
os.sytem('cls')



print('+'*40,'Program To Do List','+'*40)

print('\n')

data_aktvitas = []

while True :
    
    print('-----Menu Fitur-----')
    print('1. Tambah Akvtitas')
    print('2. Hapus Aktivtas')
    print('3. Tampilkan Aktvitas')
    print('4. Keluar Program')
    
    try :
        input_user = int(input('Input No : '))
        
    except ValueError :
        print('Input tidak valid. masukan No yang tertera')
        
    if input_user == 1:
        
        os.sytem('cls')
        
        input_aktivtas = input('Input kegiatan : ')
        input_jam = input('Jam (contoh : 8 pagi) : ')
        
        data_aktvitas.append((input_aktivtas,input_jam))
        print('Aktivitas berhasil ditambahkan')
        
        
        
        
                


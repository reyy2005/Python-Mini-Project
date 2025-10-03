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
        
    elif input_user ==2 :
        
        if not data_aktvitas :
            continue
        
        print('-----DAFTAR AKTIVITAS-----')
        
        for i,(aktivitas,jam) in enumerate(data_aktvitas) :
            print(f'{i+1}. Aktivitas : {aktivitas}\nJam : {jam}')
            
        try :
            
            nomor_remove = int(input('Input no aktivitas yang akan dihapus :  '))
            
            if 1 <= nomer_remove <= len(data_aktvitas) :
                
                del data_aktvitas[nomor_remove-1]
                print('Aktivitas berhasil dihapus.')
                
            else : 
                
                print('Aktvitas tidak valid.')
                
        except ValueError :
            
            print('Input tidak valid. gunakan angka yang tertera.')
            
        
        
                


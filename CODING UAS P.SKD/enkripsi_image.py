# -- coding: utf-8 --
"""
Created on Wed Dec  14 21:09 2022

@author: REVIKE
"""


try:
    #memasukkan nama gambar yang akan di enkripsi 
    path = input(r'Enter path of Image : ')
    #memasukkan kunci gambar enkripsi
    key = int(input('Enter Key for encryption of Image : '))
    
    #kemudian file yang di enkripsi akan ditampilkan 
    print('The path of file : ', path)
    print('Key for encryption : ', key) 
    
    fin = open(path, 'rb')
     
    image = fin.read()
    fin.close()
     
    image = bytearray(image)
 
    for index, values in enumerate(image):
        image[index] = values ^ key
 
    fin = open(path, 'wb')
     
     #ketika gambar berhasil di enrkripsi akan ada tulisan encryption done
    fin.write(image)
    fin.close()
    print('Encryption Done...')
  
    #apabila kunci yang dimasukkan salah akan muncul error caught
except Exception:
    print('Error caught : ', Exception._name_)
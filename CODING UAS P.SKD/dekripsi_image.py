# -*- coding: utf-8 -*-
"""
Created on Wed Dec  14 21:09 2022

@author: REVIKE
"""


# try block to handle the exception
try:
    #memasukkan gambar dan kunci yang akan di deskripsi 
    path = input(r'Enter path of Image : ')
     
    key = int(input('Enter Key for encryption of Image : '))
        
    print('The path of file : ', path)
    print('Note : Encryption key and Decryption key must be same.')
    print('Key for Decryption : ', key)
     
    fin = open(path, 'rb')
     
    image = fin.read()
    fin.close()
        
    image = bytearray(image)
 
    for index, values in enumerate(image):
        image[index] = values ^ key
     
    fin = open(path, 'wb')
     
    #apabila deskripsi berhasil nanti akan muncul tulisan descryption done
    fin.write(image)
    fin.close()
    print('Decryption Done...')
 
    #ketika kunci ataupun nama file yang dimasukkan salah maka akan muncul tulisan error caught
except Exception:
    print('Error caught : ', Exception.__name__)
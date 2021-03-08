# Dedi Yanto_71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# Struktur Kontrol Perulangan


'''Adik tomoe yang bernama Gojo, kesulitan untuk memahami materi FPB(faktor 
persekutuan terbesar) disekolahnya, sehingga gojo meminta tomoe untuk 
membuatkan sebuah program yang dapat menampilkan FPB dari tiga bilangan 
bulat positif yang berbeda. Untuk itu Tomoe meminta bantuan anda untuk 
membuat sebuah program yang dapat menampilkan FPB dari 3 bilangan bulat 
positif yang berbeda. '''

'''Tomoe mengilustrasikan program tersebut sebagai berikut:
Jika Gojo menginputkan 12,24,32 maka program harus dapat menampilkan FPB dari 
3 bilangan tersebut, yaitu 4, serta menampilkan faktor dari masing-masing 
bilangan agar Tomoe dapat mengecek apakah programnya benar dan dapat dipakai 
oleh adiknya Gojo.'''

'''
Input:
inputan 1 = 12
inputan 2 = 24
inputan 3 = 32 

Proses:
faktor 1 = 1,5
faktor 2 = 1,2,5,10
faktor 3 = 1, 7


Output:3
Faktor 1 = 1,2,3,4,6,12
Faktor 2 = 1, 2, 3, 4, 6, 8, 12, 24
Faktor 3 = 1, 2, 4, 8, 16, 32

Dan FPBnya 4.


'''
#Source Code

def faktor(angka,lisfaktor):
    lisfaktor = []
    for i in range(1,angka+1):
        if angka%i == 0:
            lisfaktor.append(i)
        else:
            continue
    return(lisfaktor)
faktor1 = int(input("Masukkan angka ke-1: "))
faktor2 = int(input("Masukkan angka ke-2: "))
faktor3 = int(input("Masukkan angka ke-3: "))
fpb = []
fpb2 = []

lis_fakt1 = faktor(faktor1,[])
lis_fakt2 = faktor(faktor2,[])
lis_fakt3 = faktor(faktor3,[])

for i in lis_fakt1:
    for k in lis_fakt2:
        if i == k:
            fpb.append(k)
        else:
            continue
for i in fpb:
    for k in lis_fakt3:
        if i == k:
            fpb2.append(k)
        else:
            continue
print("\nFaktor dari",faktor1,"adalah,",lis_fakt1)
print("Faktor dari",faktor2,"adalah,",lis_fakt2)
print("Faktor dari",faktor3,"adalah,",lis_fakt3)
print("\nFaktor persekutuan tersebasar dari ketiga bilangannya adalah",max(fpb2),"\n")
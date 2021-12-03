counter = 0
berhenti = "stop"
Nama = [] #Ex:Abel
Kursi = [] #Ex:2
cek = 0

while berhenti.upper!="STOP":
    nama = str(input("Masukkan nama : "))
    if nama=="STOP":
        berhenti = "STOP"
        break
    else:
        n = int(input("Masukkan nomor kursi {} : ".format(nama)))
        
        if(len(Kursi)==0):
            Nama.insert(counter,nama)
            Kursi.insert(counter,n)
            counter = counter + 1
        else:
            for i in range(len(Kursi)):
                if(Kursi[i] == n):
                    cek = 0
                    break
                else:
                    cek = 1
            
            if(cek==1):
                Nama.insert(counter,nama)
                Kursi.insert(counter,n)
                counter = counter + 1
            else:
                print("Mohon maaf kursi tersebut telah terisi!")

print()
print("List kursi yang telah terisi: ")

for i in range (counter):
    print("Kursi nomor " + str(Kursi[i]) + " telah diisi oleh " + str(Nama[i]))

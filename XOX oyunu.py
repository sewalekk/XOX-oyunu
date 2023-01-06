oyunTahtası=[" " for x in range(10)]

def ekranaGöster():
    print(" "+oyunTahtası[1]+" "+"|"+" "+oyunTahtası[2]+" "+"|"" "+oyunTahtası[3])
    print("----------")
    print(" "+oyunTahtası[4]+" "+"|"+" "+oyunTahtası[5]+" "+"|"" "+oyunTahtası[6])
    print("----------")
    print(" "+oyunTahtası[7]+" "+"|"+" "+oyunTahtası[8]+" "+"|"" "+oyunTahtası[9])

def harfkoy(harf,konum):
    oyunTahtası[konum]=harf

def alanBosmu(konum):
    return oyunTahtası[konum]==" "

def tahtadolu():
    if oyunTahtası.count(" ")>1:
        return False
    else:
        return True

def kazanan(oyunTahtası,harf):
    return (oyunTahtası[1]==harf and oyunTahtası[2]==harf and oyunTahtası[3]==harf) or (oyunTahtası[4]==harf and oyunTahtası[5]==harf and oyunTahtası[6]==harf) or (oyunTahtası[7]==harf and oyunTahtası[8]==harf and oyunTahtası[9]==harf) or (oyunTahtası[1]==harf and oyunTahtası[4]==harf and oyunTahtası[7]==harf) or (oyunTahtası[2]==harf and oyunTahtası[5]==harf and oyunTahtası[7]==harf) or (oyunTahtası[3]==harf and oyunTahtası[6]==harf and oyunTahtası[9]==harf) or (oyunTahtası[1]==harf and oyunTahtası[5]==harf and oyunTahtası[9]==harf) or (oyunTahtası[3]==harf and oyunTahtası[5]==harf and oyunTahtası[7]==harf)

def oyuncuHareketi():
    konum=int(input("1-9 arasında bir konum giriniz: "))
    if alanBosmu(konum):
        harfkoy("X",konum)
        if kazanan(oyunTahtası,"X"):
            ekranaGöster()
            print("Tebrikler Kazandınız!")
            exit()
        ekranaGöster()
    else:
        print("Girdiğiniz konum dolu. Tekrar seçiniz")
        oyuncuHareketi()

def bilgisayarHareket():
    import random
    müsait_konumlar=[konum for konum, harf in enumerate(oyunTahtası) if harf==" " and konum !=0]

    hareket=0

    for harf in ["0","X"]:
        for i in müsait_konumlar:
            kopya_Tahta=oyunTahtası[:]
            kopya_Tahta[konum]=harf
            if kazanan(kopya_Tahta, harf):
                hareket=i
                return hareket
            
    köşeler=[]

    for i in müsait_konumlar:
        if i in [1,3,7,9]:
            köşeler.append(i)

    if len(köşeler)>0:
        hareket=random.choice(köşeler)
        return hareket

    if 5 in müsait_konumlar:
        hareket=5
        return hareket

    içerisi = []
    
    for i in müsait_konumlar:
        if i in [2,4,6,8]:
            içerisi.append(i)

    if len(içerisi)>0:
        hareket=random.choice(içerisi)
        return hareket

def Oyun():
    print("XOX Oyununa Hoşgeldin")
    ekranaGöster()

    while not tahtadolu():
        oyuncuHareketi()
        if tahtadolu():
            print("Oyun bitti kazanan yok")
            exit()
        
        print("----------------------------------")

        bilgisayar_hareket=bilgisayarHareket()
        harfkoy("0",bilgisayar_hareket)
        if kazanan(oyunTahtası,"0"):
            ekranaGöster()
            print("Bilgisayar Kazandı")
            exit()
        ekranaGöster()
        if tahtadolu():
            print("Oyun bitti kazanan yok")
            exit()
        
        print("----------------------------------")


Oyun()

while not kazanan("X"):
    konum=int(input("1-9 arasında bir konum giriniz: "))
    harfkoy("X",konum)
    ekranaGöster()

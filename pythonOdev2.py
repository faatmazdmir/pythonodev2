"""
Ödev-1:Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır.
Kullanıcının geliri;
1.10000 ve altındaysa maaşından %5 kesinti olur.
2.25000 ve altındaysa maaşından %10 kesinti olur.
3.45000 ve altındaysa maaşından %25 kesinti olur.
4.Diğer koşullarda %30 kesinti olur.
Bu durumlara göre kullanıcının yeni maaşı yazdırılır.

Ödev-2:Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir.
Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır,
altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır.(Sadece koşul kullanılması yeterli.)

Ödev-3:Bir önceki örnek geliştirilir.
Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda.
Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır.
Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.
Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder

Ödev-4:Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar.
Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter.
Tercihe göre kalan hak bilgisi verilir.
"""

# Ödev-1 #
maas = float(input("Maaş bilginizi giriniz: "))

if maas <= 10000:
    new_maas = maas - (maas*5)/100
elif maas <= 25000:
    new_maas = maas - (maas*10)/100
elif maas <= 45000:
    new_maas = maas - (maas*25)/100
else:
    new_maas = maas - (maas*30)/100

print("Vergi uygulanmış maaşınız: " , new_maas)
print("**********")

# Ödev-2 #
kullanici_adi = input("Kullanıcı adınızı giriniz: ")
sifre = input("Şifrenizi giriniz: ")

if len(sifre) >= 6:
    print("Hesabınız başarıyla oluşturuldu. ")
else:
    print("Şifreniz en az 6 haneli olmalıdır! ")
print("**********")

# Ödev-3 #
while True:
    sifre = input("Şifrenizi giriniz: ")

    if 5 <= len(sifre) <= 10:
       print("Hesabınız oluşturuldu. ")
       break
    else:
       print("Lütfen şifreniz 5 haneden az ve 10 haneden fazla olmasın! ")
print("**********")

# Ödev-4 #
isim = input("İsminizi giriniz: ")
sifree = "123456"
hak = 3

while hak > 0:
    girilen_sifre = input("Şifrenizi giriniz: ")

    if girilen_sifre == sifree:
        print("Giriş yapıldı. ")
        break
    else:
        hak -= 1
        print("Şifre yanlış. ")
        if hak > 0:
            print("Kalan hakkınız: ", hak)
        else:
            print("Üç kez yanlış giriş yaptınız.Program sonlandırılıyor. ")
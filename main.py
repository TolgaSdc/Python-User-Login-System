import json

def kullanicilari_yukle():
    try:
        dosya = open("kullanicilar.json", "r", encoding="utf-8")
        data = json.load(dosya)
        dosya.close()
        return data
    except FileNotFoundError:
        return {}
    
kullanicilar = kullanicilari_yukle()

def kullanicilari_kaydet(kullanicilar):
    dosya = open("kullanicilar.json", "w", encoding="utf-8")
    json.dump(kullanicilar, dosya, ensure_ascii=False, indent=4)
    dosya.close()

def menu():
    print("""**********HOŞGELDİNİZ************
    1. Kayıt Ol
    2. Giriş
    3. Çıkış
*********************************
    """)

def kayit_ekrani():
     k_adi = input("Kullanıcı Adı: ")
     k_sifre = input("Şifrenizi Giriniz: ")
     if k_adi in kullanicilar:
          print("Böyle bir kullanıcı zaten var.")
     else:
          kullanicilar[k_adi] = {"sifre": k_sifre}
          kullanicilari_kaydet(kullanicilar)

def giris_ekrani():
     k_adi = input("Kullanıcı Adı: ")
     k_sifre = input("Şifrenizi Giriniz: ")
     
     if k_adi in kullanicilar and kullanicilar[k_adi]["sifre"] == k_sifre:
          print("giriş başarılı")
          print("Hoş Geldin {}".format(k_adi))
     else:
          print("Kullanıcı Adı veya Şifreniz hatalı. Giriş Yapılamadı...")

while True:
    menu()

    try: 
         secim = int(input("Seçim Yapınız"))
    except ValueError:
         print("Lütfen Sayı Giriniz")
         continue
    if secim == 0:
         print(kullanicilar)

    if secim == 1:
         kayit_ekrani()
    
    elif secim == 2: 
         giris_ekrani()
    elif secim == 3:
         print("Çıkış Yapılıyor...")
         break
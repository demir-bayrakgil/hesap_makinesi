print('hesap makinesine hoş geldiniz 😊')
islem=input('istediğiniz işlemi numaralayınız toplama=1,çıkarma=2,çarpma=3,bölme=2')
birincisayi=int(input('ilk sayıyı lütfen giriniz'))
ikincisayi=int(input('ikinci sayıyı lütfen giriniz'))

if islem=="1":
 print(birincisayi+ikincisayi)
elif islem=="2":
 print(birincisayi-ikincisayi)
elif islem=="3":
 print(birincisayi*ikincisayi)
elif islem=="4":
 print(birincisayi/ikincisayi)
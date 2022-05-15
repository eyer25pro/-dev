x=input("bulunduğunuz tarihi gün ay yıl olarak harf şeklinde giriniz türkçe karakkter kullnamayınız!!!")
x=x"g"
l =[]
y=[]

while  1< 2 :
    z=input("ailenin giderleri q ya basarsan dögü biter")
    x.append(z)
    if z=="q":
        break
while  1< 2 :
    z=input("ailenin gelirleri q ya basarsan dögü biter")
    y.append(z)
    if z=="q":
        break
a = input("gelirler için girdiğiniz tarihin sonuna g ekleyin giderler için normal tarihi yazın ")
if a==x:
    print(x)
elif a==y:
    print(x)

#Algorithmi sem prentar út n stök af breyttri Fibonacci röð
n = int(input("Enter the length of the sequence: ")) 
#Fyrstu þrjú stökin eru gefin
a1 = 1
a2 = 2
a3 = 3
#Ef n er 1,2 eða 3 er röðin gefin
if n==1:
    print(a1)
elif n==2:
    print(a1,a2)
elif n==3:
    print(a1,a2,a3)
else: #Ef n>3 notar algorithma for lykkju
    print(a1,a2,a3)
    for i in range(4,n+1): #For lykkjan er fyrir stak nr. 4 og uppí n
        a4=a1+a2+a3 #Fyrir fjórða stak leggur algorithminn saman 3 stökin á undan
        print(a4)
        a1=a2 #Hliðrar síðustu 3 stök um einn
        a2=a3
        a3=a4
import random


f = open("tarihler.txt", "a")

haftanin_günleri = ("Mon ", 
                    "Tue ",
                    "Wed ",
                    "Thu ",
                    "Fri ",
                    "Sat ",
                    "Sun "
                    )
sayi = []
for l in range(100):
    for i in range(80):
        sayi.append(random.randrange(0, 23)) 
        
    
    say = 0
    hafta = 0
    degiş = 1
    for i in range(80):
        
        if(i == 10 *degiş):
            say = say + 1
            degiş = degiş + 1
            print("---------",str(say))
            if(say == 7):
                break
             
        f.write(haftanin_günleri[say]+str(sayi[i])+"\n")
            

f.close()































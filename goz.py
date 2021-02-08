import numpy as np
import cv2
import time
import datetime
import winsound

yuz_algila = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
göz = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

kapalı_göz = False
göz_kapali = 0
vd_cap = cv2.VideoCapture(0)
ret,img = vd_cap.read()
f = open("tarihler.txt", "a")

while(ret):
    time.sleep(0.1) # saniyenin 10 da birinde kontrol işlemi yapar
    ret,img = vd_cap.read()
    gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gri = cv2.bilateralFilter(gri,5,1,1)
    yüzler = yuz_algila.detectMultiScale(gri, 1.3, 5,minSize=(200,200))
    cv2.putText(img,"cikis icin c ya basiniz",(40,450),cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255),2)
    if(len(yüzler)>0):
        for (x,y,w,h) in yüzler:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            yüz_degeri = gri[y:y+h,x:x+w]
            gözler = göz.detectMultiScale(yüz_degeri,1.3,5,minSize=(50,50))
            if(len(gözler)>=2):
                    print("---------Gozler algılandi-------------")            
            else:                 
                cv2.putText(img, "gozler algilanamadi", (90,50), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),2)
                print("gözler kapali")
                göz_kapali = göz_kapali + 1
                if(göz_kapali == 30):
                    print("----------Veri Tabanına İşlendi----------")
                    tarama_hızı = 2500 
                    tarama_süresi = 1000 
                    winsound.Beep(tarama_hızı, tarama_süresi)                            
                    tarih	  = datetime.datetime.now().strftime("%A"); 
                    saat = datetime.datetime.now().strftime("%H");
                    f.write(str(tarih)[0:3]+ " " +str(saat) + "\n")
                    print ("Tarih : " ,tarih);
                    print ("Tarih Saat :" ,saat);
                    göz_kapali = 0
                    
    else:
        cv2.putText(img,"yuz algilanamadi",(110,50),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),2)

    cv2.imshow('Goz Algila',img)
    cikma = cv2.waitKey(1)
    if(cikma==ord('c')):
        break

f.close()
vd_cap.release()
cv2.destroyAllWindows()
#THE CONTENT OF THE "DOSYA.TXT":
"""
Hatice Günday,70,90,20
Mustafa Akyürek,90,80,60
Ramazan Topaloğlu,60,30,50
Elif Akşit,80,40,80
Mehmet Düşenkalkar,70,20,40
Hatice Dağdaş,90,90,80
Merve Tütüncü,40,30,30
Hatice Pekkan,50,70,60
Merve Alyanak,70,60,30
Meryem Aşıkoğlu,20,80,70
Süleyman Uluhan,40,10,100
Esra Ekici,10,10,30
Emine Kumcuoğlu,90,30,80
Süleyman Kumcuoğlu,50,10,60
Şerife Kumcuoğlu,40,70,70
Sude Tekand,90,50,90
Elif Nebioğlu,10,10,60
Sude Berberoğlu,10,100,50
Yasemin Durmaz,40,70,10
Fadime Akyürek,50,20,100
Fatma Akşit,60,40,90
Emre Sözeri,50,50,20
Yasemin Kurutluoğlu,40,50,40
Fatma Akman,80,20,30
Hacer Korol,80,50,90
Recep Altınbaş,40,70,80
Murat Numanoğlu,70,100,100
Fatih Fahri,40,10,10
Halil Sarıoğlu,30,70,60
Merve Arıcan,30,30,70
İsmail Kaplangı,60,50,10
Emir Egeli,80,20,80
Havva Erbulak,30,10,80
Hacer Okumuş,70,100,70
Salih Ağaoğlu,10,10,40
Zeliha Ağaoğlu,100,80,30
Abdullah Solmaz,60,40,50
Fatih Elmastaşoğlu,20,20,60
Hacer Karaer,90,90,60
Sude Kumcuoğlu,60,20,30
Abdullah Kuzucu,100,40,40
Hanife Söyler,100,20,80
Sude Orbay,60,30,40
Sultan Uluç,90,90,30
Hanife Beşok,80,100,50
Hülya Karadaş,80,100,10
Fatma Tuğluk,60,20,50
Halil Güçlü,100,80,30
Recep Eronat,60,100,20
Büşra Koyuncu,60,70,70
Hüseyin Kunt,50,80,10
Halil Numanoğlu,70,60,40
Hülya Gürmen,80,100,30
Ömer Kulaksızoğlu,40,40,60
Zeliha Demirel,70,40,100
Mustafa Aşıkoğlu,60,70,90
Süleyman Orbay,90,80,60
İbrahim Erez,50,60,40
Süleyman Koçyiğit,100,10,60
Salih Orbay,60,10,30
Şerife Süleymanoğlu,80,30,100
Murat Adal,10,90,100
Osman Aybar,50,20,100
Sude Balcı,60,10,40
Zeynep Koyuncu,50,90,50
İbrahim Pekkan,20,10,60
Fatih Erdoğan,30,60,30
Abdullah Ekşioğlu,40,60,10
Osman Adan,30,90,50
Ramazan Paksüt,90,20,20
Halil Gökgöz,80,10,20
Emre Kurutluoğlu,70,80,100
Mahmut Akışık,40,80,20
Yusuf Hamzaoğlu,100,40,90
Ali Akan,90,90,80
Zeliha Beşerler,100,80,20
Ali Oraloğlu,20,20,90
Hanife Poçan,100,50,10
Ayşe Kurutluoğlu,50,10,80
Fatih Akman,100,10,60
Mehmet Babacan,70,60,60
"""

passedList = []
failedList = []

def Average(lines):
    listToList = i.split(",")
    
    name = listToList[0]
    exam1 = int(listToList[1])
    exam2 = int(listToList[2])
    exam3 = int(listToList[3])
    
    SumAverage = exam1 * 0.3 + exam2 * 0.3 + exam3 * 0.4
    
    if SumAverage >= 90:
        grade = "AA"
    
    elif SumAverage >= 85:
        grade = "BA"
        
    elif SumAverage >= 80:
        grade = "BB"
    
    elif SumAverage >= 75:
        grade = "CB"
    
    elif SumAverage >= 70:
        grade = "CC"
    
    elif SumAverage >= 65:
        grade = "DC"
    
    elif SumAverage >= 60:
        grade = "DD"
    
    elif SumAverage >= 55:
        grade = "FD"
        
    else:
        grade = "FF"
      
    if grade != ("FF" and "FD"):
        passedList.append(name + "\n") 
    
    else:
        failedList.append(name + "\n") 
        
    return name + " : " + grade + "\n"
    
    

with open("dosya.txt","r") as file:
    listAverage = [] 
    for i in file:
        listAverage.append(Average(i))
        
with open("grade.txt","w") as file2:
    for i in listAverage:
        file2.write(i)
        
        
with open("passed.txt","w") as file3:
    for i in passedList:
        file3.write(i)
        
with open("failed.txt","w") as file4:
    for i in failedList:
        file4.write(i)
        

import time
import math
import random
import keyboard
from PIL import ImageGrab, Image


import Setting
from datetime import datetime
import pyautogui

class FortresSender(Setting.AllSettingFile):
    def __init__(self, automatickykoupitbonus, osetreniZima, kone_pirka, vzdalenost_na_kterou_to_jezdi):
        self.vzdalenost_na_kterou_to_jezdi = vzdalenost_na_kterou_to_jezdi
        self.kone_pirka = kone_pirka
        self.WinterFix = osetreniZima
        self.automaticky_koupuit_bonus = automatickykoupitbonus
        super().__init__()

    def Run(self):
        #SEM <-


        #vytvoreni logickeho pole
        with open('fort.txt', 'r') as file:
            radky = file.readlines()
            self.polePevnosti = [radka.strip() for radka in radky]

        #smazat prosle zaznamy
        while True:
            if not self.polePevnosti:
                break

            Kingdom, Cords, Time = self.polePevnosti[0].split(';')
            cas_zaznamu = datetime.strptime(Time, "%y-%m-%d %H:%M:%S")

            aktualni_cas = datetime.now()

            if cas_zaznamu < aktualni_cas:
                print(f"Smazán záznam: {self.polePevnosti[0]}")
                self.polePevnosti.pop(0)
            else:
                break

        while self.RunBool:

            # Zadané časy
            start_time = datetime.strptime("11:00:30", "%H:%M:%S").time()
            end_time = datetime.strptime("11:01:00", "%H:%M:%S").time()

            # Aktuální čas
            current_time = datetime.now().time()

            if ((start_time <= current_time <= end_time) and self.automaticky_koupuit_bonus):
                pyautogui.click(1750,100)
                time.sleep(0.3)
                pyautogui.click(1210,720)
                time.sleep(0.3)
                pyautogui.click(1133,676)
                time.sleep(0.3)
                pyautogui.click(1140,680)
                time.sleep(0.3)
                pyautogui.click(1336,261)



            pyautogui.click(980,700)
            pyautogui.click(950,730)
            self.CloseWindow()

            Kingdom, Cords, Time = self.polePevnosti[0].split(';')
            aktualni_cas = datetime.now()
            formatovany_cas = aktualni_cas.strftime('%y-%m-%d %H:%M:%S')

            cas1_objekt = datetime.strptime(formatovany_cas, "%y-%m-%d %H:%M:%S")
            cas2_objekt = datetime.strptime(Time, "%y-%m-%d %H:%M:%S")

            time.sleep(1)

            if (self.ReturnDistance(Kingdom,Cords) > self.vzdalenost_na_kterou_to_jezdi):
                self.polePevnosti.pop(0)

            if (cas1_objekt > cas2_objekt):


                #poslat
                pyautogui.press('tab')
                pyautogui.typewrite(Cords.split(':')[0])
                pyautogui.press('tab')
                pyautogui.typewrite(Cords.split(':')[1])
                pyautogui.press('Enter')
                time.sleep(1)
                #poslat utok
                self.SendAtk(self.kone_pirka)
                #pop prvniho zaznamu
                self.polePevnosti.pop(0)
                self.WinterCounter += 1
                time.sleep(0.5)
                pyautogui.click(1100,650)
                time.sleep(0.5)
                pyautogui.click(1570,171)

            else:
                print(Time)
                print(formatovany_cas)
                print("Čekání na: "+str(Cords)+" "+Time+". Vzdálenost: "+str(self.ReturnDistance(Kingdom, Cords)))


            if(self.WinterFix):
                if(self.WinterCounter == 30):
                    print("Pauza na zime.")
                    time.sleep(960) #16 minut nez se vrati velitele
                    self.WinterCounter = 0
                    with open('fort.txt', 'r') as file:
                        radky = file.readlines()
                        self.polePevnosti = [radka.strip() for radka in radky]

                    # smazat prosle zaznamy
                    while True:
                        if not self.polePevnosti:
                            break

                        Kingdom, Cords, Time = self.polePevnosti[0].split(';')
                        cas_zaznamu = datetime.strptime(Time, "%y-%m-%d %H:%M:%S")

                        aktualni_cas = datetime.now()

                        if cas_zaznamu < aktualni_cas:
                            print(f"Smazán záznam: {self.polePevnosti[0]}")
                            self.polePevnosti.pop(0)
                        else:
                            break
    def ReturnDistance(self, kingdom, Cords):
        if(kingdom == 'ZIM'):
            return round(math.sqrt((int(Cords.split(':')[0]) - self.WinterX)**2 + (int(Cords.split(':')[1]) - self.WinterX)**2))
        elif(kingdom == 'PSK'):
            return round(math.sqrt((int(Cords.split(':')[0]) - self.SandX)**2 + (int(Cords.split(':')[1]) - self.SandY)**2))
        else:
            return round(math.sqrt((int(Cords.split(':')[0]) - self.FireX)**2 + (int(Cords.split(':')[1]) - self.FireY)**2))

class FortresSenderMultitasking(Setting.AllSettingFile):
    def __init__(self, automatickykoupitbonus, osetreniZima, kone_pirka, vzdalenost_na_kterou_to_jezdi):
        self.vzdalenost_na_kterou_to_jezdi = vzdalenost_na_kterou_to_jezdi
        self.kone_pirka = kone_pirka
        self.WinterFix = osetreniZima
        self.automaticky_koupuit_bonus = automatickykoupitbonus
        super().__init__()

    def Run(self):
        #vytvoreni logickeho pole
        with open('fort.txt', 'r') as file:
            radky = file.readlines()
            self.polePevnosti = [radka.strip() for radka in radky]

        #seradi to pole pevnosti
        self.SortArrayByTime()

        #smazat prosle zaznamy
        while True:
            if not self.polePevnosti:
                break

            Kingdom, Cords, Time = self.polePevnosti[0].split(';')
            cas_zaznamu = datetime.strptime(Time, "%y-%m-%d %H:%M:%S")

            aktualni_cas = datetime.now()

            if cas_zaznamu < aktualni_cas:
                print(f"Smazán záznam: {self.polePevnosti[0]}")
                self.polePevnosti.pop(0)
            else:
                break

        lastWorld = "OHN"

        while self.RunBool:
            # Zadané časy
            start_time = datetime.strptime("11:00:30", "%H:%M:%S").time()
            end_time = datetime.strptime("11:02:30", "%H:%M:%S").time()

            # Aktuální čas
            current_time = datetime.now().time()

            if ((start_time <= current_time <= end_time) and self.automaticky_koupuit_bonus):
                pyautogui.click(self.RngClickOffset(1750,5),self.RngClickOffset(100,5))
                time.sleep(0.3)
                pyautogui.click(self.RngClickOffset(1210,5),self.RngClickOffset(720,5))
                time.sleep(0.3)
                pyautogui.click(self.RngClickOffset(1133,5),self.RngClickOffset(676,5))
                time.sleep(0.3)
                pyautogui.click(self.RngClickOffset(1140,5),self.RngClickOffset(680,5))
                time.sleep(0.3)
                pyautogui.click(self.RngClickOffset(1336,5),self.RngClickOffset(261,5))




            Kingdom, Cords, Time = self.polePevnosti[0].split(';')

            if (self.ReturnDistance(Kingdom,Cords) > self.vzdalenost_na_kterou_to_jezdi):
                self.polePevnosti.pop(0)
                continue

            #-----------PREKLIKAVANI SVETU------------------
            if(Kingdom != lastWorld):
                #prekliknout svet
                if(Kingdom == "OHN"):
                    pyautogui.click(self.RngClickOffset(1850,5),self.RngClickOffset(1011,2))
                    time.sleep(0.3)
                    #pyautogui.click(1840,910) bez vody
                    pyautogui.click(self.RngClickOffset(1840,5),self.RngClickOffset(910,2))
                if (Kingdom == "PSK"):
                    pyautogui.click(self.RngClickOffset(1850,5), self.RngClickOffset(1011,2))
                    time.sleep(0.3)
                    pyautogui.click(self.RngClickOffset(1850,5), self.RngClickOffset(930,2))
                #zmenit last World
                lastWorld = Kingdom
            #----------KONEC PREKLIKAVANI SVETU-----------------

            aktualni_cas = datetime.now()
            formatovany_cas = aktualni_cas.strftime('%y-%m-%d %H:%M:%S')

            cas1_objekt = datetime.strptime(formatovany_cas, "%y-%m-%d %H:%M:%S")
            cas2_objekt = datetime.strptime(Time, "%y-%m-%d %H:%M:%S")

            time.sleep(self.RngDelaygenerator())

            # odkliknout
            self.CloseWindow()

            pyautogui.click(self.RngClickOffset(980, 3), self.RngClickOffset(700, 3))
            pyautogui.click(self.RngClickOffset(950, 3), self.RngClickOffset(730, 3))

            if (cas1_objekt > cas2_objekt):


                #poslat
                pyautogui.press('tab')
                pyautogui.typewrite(Cords.split(':')[0])
                pyautogui.press('tab')
                pyautogui.typewrite(Cords.split(':')[1])
                pyautogui.press('Enter')
                time.sleep(self.RngDelaygenerator())
                #poslat utok
                self.SendAtk(self.kone_pirka, Kingdom)
                #pop prvniho zaznamu
                self.polePevnosti.pop(0)
                self.WinterCounter += 1
                time.sleep(self.RngDelaygenerator())
                pyautogui.click(self.RngClickOffset(1100,5),self.RngClickOffset(650,5))
                time.sleep(self.RngDelaygenerator())
                pyautogui.click(self.RngClickOffset(1570,5),self.RngClickOffset(171,5))

            else:
                print(Time)
                print(formatovany_cas)
                print("Čekání na: "+str(Kingdom)+" "+str(Cords)+" "+Time+". Vzdálenost: "+str(self.ReturnDistance(Kingdom, Cords)))


            if(self.WinterFix):
                if(self.WinterCounter == 30):
                    print("Pauza na zime.")
                    time.sleep(300) #500 sekund nez se vrati velitele
                    self.WinterCounter = 0
                    with open('fort.txt', 'r') as file:
                        radky = file.readlines()
                        self.polePevnosti = [radka.strip() for radka in radky]

                    # smazat prosle zaznamy
                    while True:
                        if not self.polePevnosti:
                            break

                        Kingdom, Cords, Time = self.polePevnosti[0].split(';')
                        cas_zaznamu = datetime.strptime(Time, "%y-%m-%d %H:%M:%S")

                        aktualni_cas = datetime.now()

                        if cas_zaznamu < aktualni_cas:
                            print(f"Smazán záznam: {self.polePevnosti[0]}")
                            self.polePevnosti.pop(0)
                        else:
                            break
    def ReturnDistance(self, kingdom, Cords):
        if(kingdom == 'ZIM'):
            return round(math.sqrt((int(Cords.split(':')[0]) - self.WinterX)**2 + (int(Cords.split(':')[1]) - self.WinterX)**2))
        elif(kingdom == 'PSK'):
            return round(math.sqrt((int(Cords.split(':')[0]) - self.SandX)**2 + (int(Cords.split(':')[1]) - self.SandY)**2))
        else:
            return round(math.sqrt((int(Cords.split(':')[0]) - self.FireX)**2 + (int(Cords.split(':')[1]) - self.FireY)**2))

    def SortArrayByTime(self):
        serazene_zaznamy = sorted(self.polePevnosti, key=lambda x: datetime.strptime(x.split(";")[-1], "%y-%m-%d %H:%M:%S"))
        self.polePevnosti = serazene_zaznamy

class BeriSender(Setting.AllSettingFile):
    def __init__(self, kone_pirka):
        super().__init__()
        self.kone_pirka = kone_pirka

    def Run(self):
        while True:
            self.CloseWindow()
            #odkliknout odmenu
            pyautogui.click(self.RngClickOffset(960,5) ,self.RngClickOffset(681,5))

            time.sleep(7)
            #vyhledat tabor
            pyautogui.press('tab')
            pyautogui.typewrite(str(self.CampArray[self.BeriCounter][0]))
            pyautogui.press('tab')
            pyautogui.typewrite(str(self.CampArray[self.BeriCounter][1]))
            pyautogui.press('Enter')
            time.sleep(1)
            #utocna cast

            '''
            if(self.BeriCounter ==0):
                pyautogui.moveTo(950-5,553-5)
                time.sleep(0.3)
                pyautogui.moveTo(950+5,553+5)
                time.sleep(0.3)
                pyautogui.moveTo(950,553)
                pyautogui.click(950,553)
            '''


            self.SendAtk(self.kone_pirka, beri=True)
            #counter managing
            if(self.BeriCounter == len(self.CampArray) - 1):
                self.BeriCounter = 0
            else:
                self.BeriCounter += 1

class BeriOnContinentSender(Setting.AllSettingFile):
    def __init__(self, kone_pirka):
        super().__init__()
        self.kone_pirka = kone_pirka
        self.pocetUtoku = 0

    def Run(self):
        while True:
            # odkliknout odmenu
            pyautogui.click(969, 678)
            time.sleep(0.2)

            #vyhledat vez
            pyautogui.click(1670,1057)

            self.SendAtk(self.kone_pirka, beri=True)
            #self.SendAtkVlajkySpeslBeri(self.kone_pirka, beri=True)
            print("Utok beri poslan. Counter: "+str(self.pocetUtoku)+"/10")
            self.pocetUtoku += 1
            if(self.pocetUtoku == 16):
                #doplnit vojcle
                pyautogui.click(220,1042)
                time.sleep(0.5)
                pyautogui.click(820, 726)
                time.sleep(0.5)
                pyautogui.click(750, 666)
                time.sleep(0.5)
                pyautogui.click(1026, 550)
                time.sleep(0.5)
                pyautogui.click(1080, 612)
                time.sleep(0.5)
                pyautogui.click(1200, 766)
                time.sleep(0.5)
                pyautogui.click(870, 757)
                time.sleep(0.5)
                pyautogui.click(1111, 550)
                time.sleep(0.5)
                pyautogui.click(1331, 259)
                time.sleep(0.5)
                pyautogui.click(1232, 271)
                time.sleep(0.5)
                pyautogui.click(1327, 263)
                self.pocetUtoku = 0
                time.sleep(0.5)



class SendingNomads(Setting.AllSettingFile):
    def __init__(self, kone_pirka):
        super().__init__()
        self.kone_pirka = kone_pirka

    def Run(self):
        while True:
            self.CloseWindow()

            #vyhledat
            pyautogui.press('tab')
            pyautogui.typewrite('824')
            pyautogui.press('tab')
            pyautogui.typewrite('917')
            pyautogui.press('Enter')

            time_skip = 0.5

            #skip casu
            time.sleep(time_skip)
            pyautogui.click(1050,566)
            time.sleep(time_skip)
            pyautogui.click(1150,500)
            time.sleep(time_skip)
            pyautogui.click(1111,551)
            time.sleep(time_skip)
            pyautogui.click(1050,665)
            time.sleep(time_skip)
            pyautogui.click(1400,800)
            time.sleep(time_skip)
            pyautogui.click(1500,911)
            time.sleep(time_skip)
            pyautogui.click(1200,500)
            time.sleep(time_skip)
            pyautogui.click(1100,750)

            time.sleep(5)







class KingTowerSender(Setting.AllSettingFile):
    def __init__(self, kone_pirka):
        super().__init__()
        self.kone_pirka = kone_pirka

    def Run(self):
        while True:
            self.CloseWindow()

            #vyhledat
            pyautogui.press('tab')
            pyautogui.typewrite(str(self.TowerArray[self.TowerCounter][0]))
            pyautogui.press('tab')
            pyautogui.typewrite(str(self.TowerArray[self.TowerCounter][1]))
            pyautogui.press('Enter')
            time.sleep(1)
            #poslat utok
            self.SendAtk(self.kone_pirka)
            #vypis
            print(str(self.TowerCounter + 1) + " z " + str(len(self.TowerArray)))

            #counter managing
            if(self.TowerCounter == len(self.TowerArray) - 1):
                return
            self.TowerCounter += 1

class SendAtkPVPByName:
    def Run(self):
        poleJmen =[
            'Fanousek2',
            'pietrs',
            'potkanremy',
            'cobraxis',
            'Roby',
            'rajko',
            'petr31',
            'Parom',
            'pool1',
            'Bury',
            'lok25',
            'marty881',
            'jiri17',
            'Druid',
            'FewJucker',
            'Viperrs',
            'Roy',
            'PeMa',
            'kira99',
            'milan7506',
            'Andulinka',
            'bezi1',
            'TATAR4',
            'J0ker',
            'breberka4',
            'jerpa1',
            'ogloj',
            'Alpaka1',
            'verca05',
            'LigaJana',
            'julinkajohy',
            'nayterin',
            'henry73',
            'karel189',
            'GoldPlayer9',
            'darulinka',
            'Bejlijen',
            'Jirkakout',
            'Trinitka',
            'Louly',
            'kralikovec',
            'm50',
            'wert1234',
            'tomka74',
            'Sasuke556',
            'Petrofis',
            'zdenek88',
            'jarda3217',
            'Nepet',
            'Sorcerer',
            'bouchor',
            'JIMTOUR',
            'alfonso99',
            'Iva4V',
            'Benjjaminn',
            'Ashawa',
            'Berta70',
            'jakub98',
            'koln1',
            'NewSpojenec',
            'radek1119',
            'davhanak',
            'zetnek',
            'Ericsonka',
            'krefox',
            'bobrstein',
            'sam_cz',
            'bryb',
            'BlackCobra',
            'krtek59',
            'Karamello',
            'MrSh4dow',
            'lamos',
            'sardonyx',
            'FastJakub3',
            'david32',
            'Tepechriav',
            'dag1111',
            'boomslang',
            'movsi',
            'Fuego62',
            'hroznyplayr',
            'vlasta503',
            'Viagra',
            'Robert37Gamer',
            'Spc2',
            'nanomen2000',
            '79jan',
            'mnch',
            'lionym',
            'abike',
            'eddyzol',
            'Ferdin',
            'KralKarelIV',
            'Percival',
            'VlastaPlayer1',
            'man66',
            'rozka777',
            'Jitka10',
            'jan588',
            'VENDELIN5',
            'crazydrake',
            'guliver48',
            'machy68',
            'amagorka',
            'hvezda1',
            'Wanheda',
            'marago',
            'm77',
            'rafe',
            'luho',
            'karji',
            'batul',
            'max08',
            'Ginerva',
            'petronela',
            'glintofhope',
            'labtec11',
            'Luci83',
            'anelata',
            'Turop',
            'nevrlyota',
            'Biff',
            'Bivoj4',
            'eda63',
            'drahomiraplayer',
            'Fido7',
            'stalian',
            'teri001',
            'hellboy82',
            'voktas',
            'johni',
            'radko66',
            'foxius',
            'Smolda',
            'petrex62',
            'Setti',
            'TARA11',
            'Rista3',
            'OldCesta',
            'vlastuna',
            'Mafitos',
            'ReneRenco',
            'pavsovt',
            'radator',
            'rsochorec',
            'Pedro5',
            'lojzan1',
            'koppel1337',
            'Hagana',
            'Pemap',
            'Mondeo',
            'kadgal',
            'Ikoja',
            'ladenka44',
            'Martas74',
            'Korin',
            'fabi66',
            'Heavy666',
            'Ittieh',
            'jirka65',
            'HonzaGamer2',
            'jurak2',
            'kodl',
            'marky1978',
            'Bublina2',
            'brezinav',
            'macin30',
            'janna12',
            'barbuch',
            'jaavaa',
            'BertS',
            'Lukyno202',
            'Milos12',
            'skajpet',
            'pety',
            'Ronaldo9',
            'Michal33',
            'Alpaka',
            '8966burian',
            'kazatelna',
            'kamila789',
            'olin25',
            'Henry76',
            'witch',
            'had3',
            'Libor62',
            'Merunak',
            'fikus1',
            'josrys',
            'NewPablos',
            'kotyny02',
            'LukyboyX',
            'Tesak79',
            'koudy9',
            'pepis1960',
            'Stanislav62',
            'SuperHouse2',
            'ValentinoR46',
            'koczka',
            'adamus1',
            'miondator',
            'jarin09',
            'Lexus',
            'sentys',
            'Tararinga',
            'kdekdo',
            'cvok5',
            'mirva',
            'merus111',
            'emiliokoem00',
            'Pavelchiel',
            'asticka',
            'Lavas',
            'igor5',

            'barnaby231',
            'vladce',
            'milinek01',
            'vidle',
            'ilka',
            'simča04',
            'mata5',
            'StewKrew2',
            'Gustawson',
            'martinkantor',
            'Kunětice_2',
            'Phoebe08',
            'Červajz',
            'hss',
            'hepy131',
            'mekbomba',
            'PTÁK21',
            'Matysek37',
            'Arthorius',
            'karlosk',
            'pra',
            'honza5806',
            'cuckazk',
            'renata14',
            'Špuntkvaně',
            'Andreios',
            'hfklmn',
            'fanda28',
            'ladabetaax',
            'Elenor',
            'Bobr158',
            'terkl',
            'RiannoN',
            'ddolynka',
            'jirka04',
            'olowain',
            'Brno',
            'mansig',
            'Fírarak2',
            'milanmmm',
            'amigo10',
            'Bolito',
            'xenie1',
            'Catleonka',
            'milam1',
            'tonda33',
            'Ondiiicekk',
            'Poselbozi',
            'nelljana',
            'Hasič1',
            'apurk',
            'janinkacze',
            'smatej07',
            'LiliBax',
            'santus64',
            'haluza',
            'Flandry',
            'Luculus',
            'smidl2',
            'Cecilos80',
            'zraka',
            'Bibi2008',
            'Laxo',
            'Vincek',
            'Sid',
            'Dáša51',
            'zrovnaja',
            'crowenus',
        ]
        for x in poleJmen:
            pyautogui.click(960, 675)
            time.sleep(0.1)

            pyautogui.click(1060,12)
            time.sleep(0.1)
            pyautogui.click(1060,12)
            pyautogui.typewrite(x)
            pyautogui.press('Enter')
            time.sleep(1)
            pyautogui.click(1020,611)
            time.sleep(1)
            pyautogui.click(1050,666)
            time.sleep(1)
            pyautogui.click(1400,800)
            time.sleep(1)
            pyautogui.click(1350,700)
            time.sleep(1)

            pyautogui.click(1500, 900)
            time.sleep(1)

            pyautogui.click(1140,733)
            time.sleep(1)
            pyautogui.click(1175,500)
            time.sleep(1)
            pyautogui.click(1100,750)
            time.sleep(1)
import easyocr
import os
from datetime import datetime, timedelta
class FireScan(Setting.AllSettingFile):
    def __init__(self):
        super().__init__()
    def Run(self):
        self.outputPole = []

        self.seznamZacatecnichPevnosti = [
            [399,516],
            [419,536],
            [399,555],
            [419,575],
            [399,594],
            [419,614],
            [399,633],
            [419,653],
            [399,672],
            [419,692],
            [399,711],
            [419,731],
            [399,750],
            [419,770],
            [399,789],
            [419,809],
            [399,828],
            [419,848],
            [399,867],
            [419,887],
            [399,906],
            [419,926],
            [399,945],
            [419,965],
            [399,984],
            [419,1004],
            [399,1023],
            [419,1043],
            [399,1062]
        ]

        s = 0

        for x in range(len(self.seznamZacatecnichPevnosti)):
            start_x = self.seznamZacatecnichPevnosti[x][0]
            start_y = self.seznamZacatecnichPevnosti[x][1]

            for x in range(0, 16):
                pyautogui.press('tab')
                pyautogui.typewrite(str(start_x))
                pyautogui.press('tab')
                pyautogui.typewrite(str(start_y))
                pyautogui.press('Enter')

                time.sleep(0.2)
                pyautogui.click(985,554)
                time.sleep(0.2)
                pyautogui.moveTo(990,559)
                time.sleep(0.2)
                pyautogui.click(985,554)
                time.sleep(0.2)
                pyautogui.moveTo(1053,564)
                #tady udelat screen a analyzovat
                time.sleep(0.2)

                pyautogui.hotkey('leftalt','printscreen')
                time.sleep(0.2)

                # Načtěte obrázek ze schránky
                screenshot = ImageGrab.grabclipboard()
                time.sleep(0.2)

                x = 930 + 1920
                y = 504
                width = 240
                height = 23

                try:
                    if isinstance(screenshot, Image.Image):
                        self.CloseWindow()
                        if os.path.exists('vyrez.png'):
                            # Pokud existuje, smažte ho
                            os.remove('vyrez.png')
                        # Ořízněte snímek podle zadaných souřadnic a rozměrů
                        cropped_image = screenshot.crop((x, y, x + width, y + height))
                        cropped_image.save('vyrez.png')
                        reader = easyocr.Reader(['en'])  # inicializace s podporovanými jazyky
                        result = reader.readtext('vyrez.png')

                        casDoObnovy = ""

                        for detection in result:
                            casDoObnovy = detection[1][18:]

                        if(len(casDoObnovy) < 7):
                            casDoObnovy = "00:"+casDoObnovy

                        casDoObnovy = casDoObnovy[:2] + ':' + casDoObnovy[3:5] + ':' + casDoObnovy[6:]

                        # Aktuální datum a čas
                        now = datetime.now()

                        # Časový řetězec, který chcete přičíst
                        time_str = casDoObnovy

                        # Rozdělení časového řetězce na hodiny, minuty a sekundy
                        hours, minutes, seconds = map(int, time_str.split(':'))

                        # Vytvoření timedelta objektu pro přičtení času
                        delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)

                        # Přičtení času k aktuálnímu datumu a času
                        result = now + delta

                        # Formátování výsledného času dle specifikace (24-6-24 16:18:22)
                        formatted_result = result.strftime("%y-%m-%d %H:%M:%S")

                        ooputos = "OHN;"+str(start_x)+":"+str(start_y)+";"+formatted_result
                        print(ooputos)
                        self.outputPole.append(ooputos)

                        #self.outputPole.append()


                except:
                    print("chybička")

                s += 1
                print(str(s) + "/464")

                start_x += 39 #offset vezi horizontalne
        # Cesta k souboru, který chcete otevřít a přepsat
        file_path = "fireScan.txt"

        # Otevření souboru pro zápis (režim "w" vymaže obsah souboru, pokud existuje, nebo vytvoří nový)
        with open(file_path, "w", encoding="utf-8") as file:
            # Zápis každého řádku z pole do souboru
            file.writelines(line + "\n" for line in self.outputPole)



class SandScan(Setting.AllSettingFile):
    def __init__(self):
        super().__init__()
    def Run(self):
        self.outputPole = []

        self.seznamZacatecnichPevnosti = [
            [302,497],
            [321,516],
            [302,536],
            [321,555],
            [302,575],
            [321,594],
            [302,614],
            [321,633],
            [341,653],
            [321,672],
            [341,692],
            [321,711],
            [341,731],
            [321,750],
            [341,770],
            [321,789],
            [341,809],
            [321,828],
            [341,848],
            [321,867],
            [341,887],
            [321,906],
            [341,926],
            [321,945],
            [341,965],
            [321,984],
            [341,1004],
            [321,1023],
            [302,1043],
            [243,1062],
            [224,1082],
            [204,1101],
        ]

        s = 0

        for x in range(len(self.seznamZacatecnichPevnosti)):
            start_x = self.seznamZacatecnichPevnosti[x][0]
            start_y = self.seznamZacatecnichPevnosti[x][1]

            for x in range(0, 16):
                pyautogui.press('tab')
                pyautogui.typewrite(str(start_x))
                pyautogui.press('tab')
                pyautogui.typewrite(str(start_y))
                pyautogui.press('Enter')

                time.sleep(0.2)
                pyautogui.click(985,554)
                time.sleep(0.2)
                pyautogui.moveTo(990,559)
                time.sleep(0.2)
                pyautogui.click(985,554)
                time.sleep(0.2)
                pyautogui.moveTo(1053,564)
                #tady udelat screen a analyzovat
                time.sleep(0.2)

                pyautogui.hotkey('leftalt','printscreen')
                time.sleep(0.2)

                # Načtěte obrázek ze schránky
                screenshot = ImageGrab.grabclipboard()
                time.sleep(0.2)

                x = 930 + 1920
                y = 499
                width = 240
                height = 23

                try:
                    if isinstance(screenshot, Image.Image):
                        self.CloseWindow()
                        if os.path.exists('vyrez.png'):
                            # Pokud existuje, smažte ho
                            os.remove('vyrez.png')
                        # Ořízněte snímek podle zadaných souřadnic a rozměrů
                        cropped_image = screenshot.crop((x, y, x + width, y + height))
                        cropped_image.save('vyrez.png')
                        reader = easyocr.Reader(['en'])  # inicializace s podporovanými jazyky
                        result = reader.readtext('vyrez.png')

                        casDoObnovy = ""

                        for detection in result:
                            casDoObnovy = detection[1][18:]

                        if(len(casDoObnovy) < 7):
                            casDoObnovy = "00:"+casDoObnovy

                        casDoObnovy = casDoObnovy[:2] + ':' + casDoObnovy[3:5] + ':' + casDoObnovy[6:]

                        # Aktuální datum a čas
                        now = datetime.now()

                        # Časový řetězec, který chcete přičíst
                        time_str = casDoObnovy

                        # Rozdělení časového řetězce na hodiny, minuty a sekundy
                        hours, minutes, seconds = map(int, time_str.split(':'))

                        # Vytvoření timedelta objektu pro přičtení času
                        delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)

                        # Přičtení času k aktuálnímu datumu a času
                        result = now + delta

                        # Formátování výsledného času dle specifikace (24-6-24 16:18:22)
                        formatted_result = result.strftime("%y-%m-%d %H:%M:%S")

                        ooputos = "PSK;"+str(start_x)+":"+str(start_y)+";"+formatted_result
                        print(ooputos)
                        self.outputPole.append(ooputos)

                        #self.outputPole.append()


                except:
                    print("chybička")

                s += 1
                print(str(s) + "/512")

                start_x += 39 #offset vezi horizontalne
        # Cesta k souboru, který chcete otevřít a přepsat
        file_path = "sandScan.txt"

        # Otevření souboru pro zápis (režim "w" vymaže obsah souboru, pokud existuje, nebo vytvoří nový)
        with open(file_path, "w", encoding="utf-8") as file:
            # Zápis každého řádku z pole do souboru
            file.writelines(line + "\n" for line in self.outputPole)


class buyGoldOstrovy:
    def Run(self):
        while True:
            pyautogui.click(1200,651)
            time.sleep(0.2)
            pyautogui.click(822,545)
            time.sleep(0.2)
            pyautogui.click(1071,634)



class SendingHoriCapitals():
    def Run(self):
        self.seznamAli = [

            "Inder_DE1",
            "BLACK INSANES_FR1",
            "Hierro y Fuego_ES1",
            "AF: Riders_US1",
            "seigneur76_FR1",
            "-POSEIDON-_DE1",
            "L.D.O  -  CARTA_FR1",
            "the crazy wolf_FR1",
            "First Guard_DE1",
            "Arsenal_US1",
            "Waldeck_DE1",
            "Rebels Knights_DE1",
            "Highlandership_US1",
            "The Syndicate_LIVE",
            "K   3_PL1",
            "Ordre du TEMPLE_INT3",
            "DarkMoon_US1",
            "The Dark Union_GB1",
            "- Templer -_DE1",
            "Flames predator_CZ1",
            "Mystery R6_DE1",
            "The Forest_US1",
            "Corda Draconum_GB1",
            "Labyrinth_US1",
            "Almas Vagando_CN1",
            "Rebels Senior_DE1",
            "U N N I_IT1",
            "The Round Table_NL1",
            "Alpha Omega_US1",
            "Family Business_SKN1",
            "Javoroví rytíři_CZ1",
            "Mercenaires_FR1",
            "THE MISC_US1",
            "Scunnered_GB1",
            "Mystery Wolves_DE1",
            "Wolverines_US1",
            "ZU-Handwerker_DE1",
            "Rochade SE_DE1",
            "Initium-Novum_DE1",
            "BL WodanS_DE1",
            "BRAVEHEART-_ES1",
            "suzoo_DE1",
            "Polaris_INT1",
            "RebelsGuardians_DE1",
            "graue Panther_DE1",
            "-AMI-_FR1",
            "CAVE CANEM I_DE1",
            "REBELS. BUG_BR1",
            "FULL TILT_US1",
            "The Roundtable_LIVE",
            "The Iron Empire_US1",
            "Milunka Savić_INT1",
            "Templar Circle_INT3",
            "The Lion Hearts_DE1",
            "~ TWO TOWER ~_IT1",
            "n  e  X  u  s_US1",
            "BATTLEHORN_US1",
            "VALKIRIAS NORTE_ES2",
            "Big Fighter_HU2",
            "DIE INAKTIVEN_DE1",
            "Falken_DE1",
            "Rochade Jedis_DE1",
            "Armageddon_HU2",
            "VÁNDOROK_HU2",
            "ARGOS_PL1",
            "CUNAdeGUERREROS_HIS1",
            "MROCZNY DEMON._PL1",
            "LEGENDS Gambit_DE1",
            "SrbijaKarađorđe_INT1",
            "3 Brothers_CZ1",
            "SUOMI_RO1",
            "Rochade_DE1",
            "UNITED FRONT_US1",
            "confusion_NL1",
            "Fallout_LIVE",
            "Mai Tai_FR1",
            "Prosperity_GB1",
            "RS  Anubis_DE1",
            "Rebels Matrix_DE1",
            "Top Gear_DE1",
            "new age_ES1",
            "Black Souls_AU1",
            "V.I.P._GR1",
            "Legends Tigers_DE1",
            "BF ~ Black MOON_DE1",
            "Devils Academy_INT1",
            "Ludzie Lodu_PL1",
            "ALUCARD_FR1",
            "TheUnNamed_US1",
            "BLUE DRAGON_FR1",
            "JAPAN_DE1",
            "Dark of Shade_PL1",
            "WBA Ex-Yu_INT2",
            "HD-Löwenbund_DE1",
            "Non Plus ultra_HU2",
            "WALKIRIA  XXL_PL1",
            "ROB~Sachsen_DE1",
            "De Musketieren_NL1",
            "COH and Wolves_NL1",
            "SPQR W.Merlins_DE1",
            "DRAGON-KNIGHTS_PL1",
            "L Olympe_FR1",
            "Feuerphönix_DE1",
            "Burgenland_DE1",
            "veni vidi vici_DE1",
            "BL Hörnchen_DE1",
            "Unbreakables_INT1",
            "PRIME-CITADEL_BR1",
            "Gaule-Croisés_FR1",
            "F_R_E_M_E_N_I_PL1",
            "SPQRAkkonFlügel_DE1",
            "Magyar Habtest_HU2",
            "Bankai_CZ1",
            "Razem Wygramy_PL1",
            "PATRIOTAS_PT1",
            "BF Vestas_DE1",
            "Jaster_DE1",
            "Berserk Espada_FR1",
            ".:MAOS:._PT1",
            "LA FIRST ONE_FR1",
            "One Way Ticket_RU1",
            "snacks_DE1",
            "Biergarten_DE1",
            "-The Gods-_RO1",
            "--- BSS ---_DE1",
            "ZU-DarkLegion I_DE1",
            "The membership_NL1",
            "KINGDOM_HIS1",
            "Phoenix_INT1",
            "Finland United_SKN1",
            "LA CITADELLE_FR1",
            "VLASTENCI_CZ1",
            "Tyrus_DE1",
            "K R A T O S_HIS1",
            "Phönix Requiem_DE1",
            "HD-Magic First_DE1",
            "~ShadowKnight~8_DE1",
            "The Gladiators_NL1",
            "HD-Magic First_DE1",
            "BL INFERNO_DE1",
            "Warriors_HU2",
            "Zlatí rytíři_CZ1",
            "Piastowie ..._PL1",
            "DRAKKAR_PL1",
            "Беркут!_RU1",
            "ZU-CASA II_DE1",
            "LOYALTY FIRST_LIVE",
            "LegendBerserker_DE1",
            "SPQRAkkonFlügel_DE1",
            "U Dvou hradů_CZ1",
            "SMETS1er_FR1",
            "Mystery VII THB_DE1",
            "ALLIANCE DXKM_GR1",
            ".:ALBAYRAK:._TR1",
            "Grand Alliance_TR1",
            "GP~TheDragons_DE1",
            "Ravens Samurai_DE1#1",
            "ÉBREDÉS_HU2",
            "~Gate Of Hell~_FR1",
            "AKTIVE Löwen_DE1",
            "Poseidon_JP1",
            "Corvinus_HU2",
            "White Eagles_NL1",
            "Fast~Furious_RO1",
            "Legion XIII_NL1",
            "GLADIATORS_SK1",
            "HISTORIANS_ES2"
        ]
        self.index = 0

        for x in range(len(self.seznamAli)):
            time.sleep(2)
            pyautogui.click(1550,1000)
            time.sleep(2)
            pyautogui.click(600,360)
            time.sleep(2)
            pyautogui.click(1030,737)
            time.sleep(2)
            pyautogui.press('tab')
            time.sleep(2)
            pyautogui.typewrite(self.seznamAli[x])
            time.sleep(2)
            pyautogui.press('Enter')
            time.sleep(2)
            pyautogui.click(880,523)
            time.sleep(2)
            pyautogui.click(700, 543)
            time.sleep(2)
            pyautogui.click(930, 423)
            time.sleep(2)
            pyautogui.click(790, 620)
            time.sleep(5)

            #pyautogui.click(964,537)
            #time.sleep(1)

            pyautogui.click(1050, 565)
            time.sleep(2)

            pyautogui.click(1050, 666)
            time.sleep(3)

            pyautogui.click(1400, 800)
            time.sleep(2)

            pyautogui.click(1400, 910)
            time.sleep(2)

            pyautogui.click(950, 671)
            time.sleep(2)

            pyautogui.click(1170, 500)
            time.sleep(2)

            pyautogui.click(1200,326)
            time.sleep(2)

            pyautogui.press('tab')
            time.sleep(2)

            pyautogui.typewrite('0')
            time.sleep(2)

            pyautogui.press('tab')
            time.sleep(2)

            pyautogui.typewrite('30')
            time.sleep(2)

            pyautogui.click(1100, 777)
            time.sleep(2)


            #pyautogui.click(1170, 500)
            #time.sleep(1)

            pyautogui.click(1090, 755)
            time.sleep(2)

            pyautogui.click(950, 677)
            time.sleep(2)

            pyautogui.click(1264, 281)
            time.sleep(2)


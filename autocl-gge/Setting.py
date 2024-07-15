import pyautogui
import time
import random

class AllSettingFile():
    def __init__(self):
        self.polePevnosti = []

        self.RunBool = True

        self.Resolution = [1920,1080]
        self.AktBtnX = 1050
        self.AktBtnY = 564

        # potvrdit utok
        self.ConfirmAtkX = 1060
        self.ConfirmAtkY = 662

        # naplnit vlnu
        self.FillWaveX = 1400
        self.FillWaveY = 800

        # tlacitko utok
        self.BtnAtkX = 1500
        self.BtnAtkY = 900

        # vybrat pírka
        self.SetPirkaX = 1200
        self.SetPirkaY = 500

        #vybrat kone goldy
        self.SetGoldyX = 750
        self.SetGoldyY = 550

        # potvrdit utok
        self.ConfirmX = 1100
        self.ConfirmY = 750

        #souradnice hradu zima
        self.WinterX = 770
        self.WinterY = 551

        #souradnice hradu pisek
        self.SandX = 607
        self.SandY = 825

        #souradnice hradu ohen
        self.FireX = 759
        self.FireY = 836

        self.WinterFix = False
        self.WinterCounter = 0

        #beri
        '''
                     #modry
            [819,912],
            [823,912],
            [821,916],
            [821,918],
            [823,920]
          
           # cerveny
            [1207, 569],
            [1206, 573],
            [1207, 574],
            [1210, 575],
            [1209, 578]
                  
                  vsechny
                  
                    '''
        self.CampArray = [

            [819, 912],
            [823, 912],
            [817, 914],
            [821, 916],
            [821, 918],
            [823, 920],
            [822, 921],


            [829, 919],
            [826, 924],
            [828, 924]


        ]
        self.BeriCounter = 0

        #kralovsky veze
        self.TowerArray = [
            [733,422],
            [318,422],
            [735,1006],
            [526,772],
            [630,1058],
            [734,540],
            [317,657],
            [1047,1060],
            [631,357 ],
            [735,773],
            [213,241],
            [317,1006],
            [631,473],
            [213,709],
            [630,824],
            [422,826],
            [318,188],
            [943,187],
            [735,189],
            [527,188],
            [1150,305],
            [1150,538],
            [1151,421 ],
            [1151,889 ],
            [1151,1123],
            [421,122],
            [214,124],
            [630,122],
            [837,123],
            [1047,124],
            [110,773],
            [111,890],
            [109,1008],
            [109,657],
            [111,421],
            [111,539],
            [109,305],
            [111,188],
            [837,1177],
            [630,1176],
            [1047,1177],
            [214,1176],
            [422,1176],
            [319,71],
            [111,70],
            [943,71],
            [1150,71],
            [1150,1240],
            [734,1242],
            [526,1240],
            [109,1242],
            [317,1240],
            [942,1241]
        ]
        self.TowerCounter = 0

    def CloseWindow(self):
        try:

            confidence_threshold = 0.6
            #obr 1
            center = pyautogui.locateCenterOnScreen("cross_1.png", confidence=confidence_threshold)

            if center is not None:
                pyautogui.click(center[0], center[1])
            else:
                print("Obrazek nebyl nalezen.")

            #obr 2
            center = pyautogui.locateCenterOnScreen("cross_2.png", confidence=confidence_threshold)

            if center is not None:
                pyautogui.click(center[0], center[1])
            else:
                print("Obrazek nebyl nalezen.")

            # obr 3
            center = pyautogui.locateCenterOnScreen("cross_3.png", confidence=confidence_threshold)

            if center is not None:
                pyautogui.click(center[0], center[1])
            else:
                print("Obrazek nebyl nalezen.")

            #obr 4
            center = pyautogui.locateCenterOnScreen("cross_4.png", confidence=confidence_threshold)

            if center is not None:
                pyautogui.click(center[0], center[1])
            else:
                print("Obrazek nebyl nalezen.")

            #obr 5
            center = pyautogui.locateCenterOnScreen("cross_5.png", confidence=confidence_threshold)

            if center is not None:
                pyautogui.click(center[0], center[1])
            else:
                print("Obrazek nebyl nalezen.")


        except:
            pass

    def RngDelaygenerator(self):
        return round(random.uniform(0.5, 1.5), 5)

    def SendAtkVlajkySpeslBeri(self, kone_pirka, world = None, beri = False):
        time.sleep(self.RngDelaygenerator())

        # pyautogui.click(1050,480) #offset beri vez nahore
        pyautogui.click(self.AktBtnX, self.AktBtnY)  # TOTO JE TO PRAVE NA PEVNOSTI A VSE

        # potvrdit utok
        time.sleep(0.5)
        pyautogui.click(self.ConfirmAtkX, self.ConfirmAtkY)
        time.sleep(1.5)
        #-------------------------
        pyautogui.click(345, 533)
        time.sleep(0.5)
        pyautogui.click(1400,757)
        time.sleep(0.5)
        pyautogui.click(1400,460)
        time.sleep(0.5)
        pyautogui.click(1400, 800)
        time.sleep(0.5)
        pyautogui.click(345, 533)

        time.sleep(0.5)
        pyautogui.click(345, 533)
        time.sleep(0.5)
        pyautogui.click(345, 582)
        time.sleep(0.5)
        pyautogui.click(1400, 757)
        time.sleep(0.5)
        pyautogui.click(1400, 610)
        time.sleep(0.5)
        pyautogui.click(1400, 800)
        time.sleep(0.5)

        pyautogui.click(345, 533)
        time.sleep(0.5)
        pyautogui.click(345, 533)
        time.sleep(0.5)

        # naplnit vlnu
        #time.sleep(0.5)
        #pyautogui.click(self.FillWaveX, self.FillWaveY)
        # tlacitko utok
        time.sleep(0.5)
        pyautogui.click(self.BtnAtkX, self.BtnAtkY)
        # vybrat pírka
        time.sleep(0.5)
        if kone_pirka:
            pyautogui.click(self.SetPirkaX, self.SetPirkaY)
        else:
            pyautogui.click(self.SetGoldyX, self.SetGoldyY)
        # potvrdit utok
        time.sleep(self.RngDelaygenerator())
        pyautogui.click(self.ConfirmX, self.ConfirmY)

        #odkliknout misujici vojcle
        pyautogui.click(1090, 658)
        time.sleep(0.5)
        pyautogui.click(1558, 171)
        time.sleep(0.5)
    def SendAtk(self, kone_pirka, world = None, beri = False):

        if(not beri):
            time.sleep(self.RngDelaygenerator())
            pyautogui.moveTo(self.Resolution[0] / 2 + self.RngClickOffset(10, 4), self.Resolution[1] / 2 + self.RngClickOffset(10, 4))
            time.sleep(0.3)
            pyautogui.moveTo(self.RngClickOffset(self.Resolution[0] / 2, 6), self.RngClickOffset(self.Resolution[1] / 2, 6))
            time.sleep(0.3)
            pyautogui.click(self.RngClickOffset(self.Resolution[0] / 2, 6), self.RngClickOffset(self.Resolution[1] / 2, 6))
        time.sleep(self.RngDelaygenerator())

        #pyautogui.click(self.RngClickOffset(1050, 5),self.RngClickOffset(488, 5)) #offset beri vez nahore
        pyautogui.click(self.RngClickOffset(self.AktBtnX, 5), self.RngClickOffset(self.AktBtnY, 5)) # TOTO JE TO PRAVE NA PEVNOSTI A VSE

        # potvrdit utok
        time.sleep(self.RngDelaygenerator())
        pyautogui.click(self.RngClickOffset(self.ConfirmAtkX, 5), self.RngClickOffset(self.ConfirmAtkY,5))
        time.sleep(self.RngDelaygenerator())
        time.sleep(self.RngDelaygenerator())
        #vybrat predvolbu
        if(world == "PSK"):
            pyautogui.click(self.RngClickOffset(1350, 5),self.RngClickOffset(760, 3))
            time.sleep(self.RngDelaygenerator())
            pyautogui.click(self.RngClickOffset(1366, 5),self.RngClickOffset(725, 3))
        elif(world == "OHN"):
            pyautogui.click(self.RngClickOffset(1350, 5),self.RngClickOffset(760, 3))
            time.sleep(self.RngDelaygenerator())
            pyautogui.click(self.RngClickOffset(1370, 5),self.RngClickOffset(700, 3))

        # naplnit vlnu
        time.sleep(self.RngDelaygenerator())
        pyautogui.click(self.RngClickOffset(self.FillWaveX,5), self.RngClickOffset(self.FillWaveY,5))
        # tlacitko utok
        time.sleep(self.RngDelaygenerator())
        pyautogui.click(self.RngClickOffset(self.BtnAtkX,5), self.RngClickOffset(self.BtnAtkY,5))

        if(beri):
            time.sleep(0.2)
            pyautogui.click(self.RngClickOffset(1100,5), self.RngClickOffset(668,5))
            time.sleep(0.2)
            pyautogui.click(self.RngClickOffset(1568,5), self.RngClickOffset(171,5))
            time.sleep(0.2)


        # vybrat pírka
        time.sleep(self.RngDelaygenerator())
        if kone_pirka:
            pyautogui.click(self.RngClickOffset(self.SetPirkaX,5), self.RngClickOffset(self.SetPirkaY,5))
        else:
            pyautogui.click(self.RngClickOffset(self.SetGoldyX,5), self.RngClickOffset(self.SetGoldyY,5))
        # potvrdit utok
        time.sleep(self.RngDelaygenerator())
        pyautogui.click(self.RngClickOffset(self.ConfirmX,5), self.RngClickOffset(self.ConfirmY,5))

    def RngClickOffset(self, originalCord, offset):
        return originalCord + round(random.uniform(-offset, offset), 0)





import Sender
import Setting
import time
import pyautogui

from PIL import Image
import pytesseract
image_path = 'C:\\Users\\senpa\\Desktop\\xxx.png'
import boto3

import easyocr

time.sleep(5)

automaticky_koupit_bonus = True
osetreni_jezdeni_zima = True #True jedine na zime jinak pičovina
kone_pirka = True #pokud je false tak to je za goldy
vzdalenost_na_kterou_to_jezdi = 450

#sd = Sender.FireScan()
#sd = Sender.SandScan()

#sd = Sender.FortresSender(automaticky_koupit_bonus, osetreni_jezdeni_zima, kone_pirka, vzdalenost_na_kterou_to_jezdi)
#sd = Sender.BeriOnContinentSender(kone_pirka)
#sd = Sender.KingTowerSender(kone_pirka)
#sd = Sender.BeriSender(kone_pirka)
#sd = Sender.FortresSenderMultitasking(automaticky_koupit_bonus, osetreni_jezdeni_zima, kone_pirka, vzdalenost_na_kterou_to_jezdi)
#sd = Sender.SendingNomads(kone_pirka)
sd = Sender.SendAtkPVPByName()
#sd = Sender.buyGoldOstrovy()
#sd = Sender.SendingHoriCapitals()

sd.Run()

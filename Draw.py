import pyautogui as Pawan_Robo_Program
import time as Samay_in_Seconds


Samay_in_Seconds.sleep(5)
Pawan_Robo_Program.click()

Lambai = 500
Bindu = Pawan_Robo_Program.position()

while Lambai > 0:
	if Lambai > 0 and Lambai < 100:
		Pawan_Robo_Program.moveTo(831, 63)
		Pawan_Robo_Program.click()
		Pawan_Robo_Program.moveTo(Bindu)
	if Lambai > 100 and Lambai < 200:
		Pawan_Robo_Program.moveTo(854, 63)
		Pawan_Robo_Program.click()
		Pawan_Robo_Program.moveTo(Bindu)
	if Lambai > 200 and Lambai < 300: 
		Pawan_Robo_Program.moveTo(893, 63)
		Pawan_Robo_Program.click()
		Pawan_Robo_Program.moveTo(Bindu)
	if Lambai > 300 and Lambai < 400:
		Pawan_Robo_Program.moveTo(943, 63)
		Pawan_Robo_Program.click()
		Pawan_Robo_Program.moveTo(Bindu)
	if Lambai > 400 and Lambai < 501:
		Pawan_Robo_Program.moveTo(959, 63)
		Pawan_Robo_Program.click()
		Pawan_Robo_Program.moveTo(Bindu)
	Pawan_Robo_Program.dragRel(Lambai, 0, duration=0.2)
	Lambai = Lambai - 5
	Pawan_Robo_Program.dragRel(0, Lambai, duration=0.2)
	Pawan_Robo_Program.dragRel(-Lambai, 0, duration=0.2)
	Lambai = Lambai - 5
	Pawan_Robo_Program.dragRel(0, -Lambai, duration=0.2)
	Bindu = Pawan_Robo_Program.position()
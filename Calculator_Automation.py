#We import the required packages Pyautogui and time
import pyautogui as Pawan_Robo_Program
import time as Samay_in_Seconds

#Here we give ourselves three seconds to open calculator app
Samay_in_Seconds.sleep(3)

#Here we use the 'locateCenterOnScreen'  function to detect the calculator buttons and 'Click' dfunction to click the buttons
Pawan_Robo_Program.click((Pawan_Robo_Program.locateCenterOnScreen('Number_4.png')))
Samay_in_Seconds.sleep(1)
Pawan_Robo_Program.click((Pawan_Robo_Program.locateCenterOnScreen('Number_Multiply.png')))
Samay_in_Seconds.sleep(1)
Pawan_Robo_Program.click((Pawan_Robo_Program.locateCenterOnScreen('Number_9.png')))
Samay_in_Seconds.sleep(1)
Pawan_Robo_Program.press('enter')

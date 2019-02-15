import pyautogui as Pawan_Robo_Program

Ctr = 50
#The loop below moves the pointer in a parabolic manner
while Ctr < 1000:
	Pawan_Robo_Program.moveTo(Ctr,((Ctr/2) + 10))
	Ctr = Ctr + 10

#Here we use the typewrite function to input the text onto screen
Pawan_Robo_Program.typewrite("ls")
Pawan_Robo_Program.typewrite(["enter"])

#Python message box functions
Pawan_Robo_Program.alert('This displays some text with an OK button.','join')
Pawan_Robo_Program.confirm('This displays text and has an OK and Cancel button.','locals')
Pawan_Robo_Program.prompt('This lets the user type in a string and press OK.','partition')

#IScreenshot using PyAutoGUI
Image1 = Pawan_Robo_Program.screenshot('Local_File.jpg')

#Here it prints the current position of the cursor
print(Pawan_Robo_Program.position())


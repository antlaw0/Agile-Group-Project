import tkinter

#main root for window
root = tkinter.Tk()

#arg1: width, arg 2: height, arg3: screen x, arg4: screen y
root.geometry("640x480+0+0")

#just for testing for now, eventually search function will go here
def on_button_click():
	global entry, checkButtonVar1, checkButtonVar2, checkButtonVar3
	print("Entry is: "+entry.get())
	print("Checkbox 1 state is: "+str(checkButtonVar1.get()))
	print("Checkbox 2 state is: "+str(checkButtonVar2.get()))
	print("Checkbox 3 state is: "+str(checkButtonVar3.get()))
	
	

	#insert text box for searching
entry = tkinter.Entry()
entry.grid(row=0,column=0)

#search button
button = tkinter.Button(text="SEARCH", command=on_button_click)
button.grid(row=0, column=1)

#first checkbox
checkButtonVar1= tkinter.IntVar()
checkButton1 = tkinter.Checkbutton(text="Wikipedia", variable = checkButtonVar1)
checkButton1.grid(row=1,column=0)
        
#second checkbox
checkButtonVar2= tkinter.IntVar()
checkButton2 = tkinter.Checkbutton(text="Option 2", variable = checkButtonVar2)
checkButton2.grid(row=2,column=0)

#third checkbox
checkButtonVar3 = tkinter.IntVar()
checkButton3 = tkinter.Checkbutton(text="Option 3", variable = checkButtonVar3)
checkButton3.grid(row=3,column=0)

		
root.mainloop()

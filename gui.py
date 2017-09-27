import tkinter

searchText=""

#main root for window
root = tkinter.Tk()
root.title("Encyclopedia")

#arg1: width, arg 2: height, arg3: screen x, arg4: screen y
root.geometry("640x480+0+0")

#just for testing for now, eventually search function will go here
def on_button_click():
	global searchText, entry, checkButtonVar1, checkButtonVar2, checkButtonVar3
	#assigns searchText to string in entry
	searchText=entry.get()
	print("Entry is: "+entry.get())
	print("Checkbox 1 state is: "+str(checkButtonVar1.get()))
	print("Checkbox 2 state is: "+str(checkButtonVar2.get()))
	print("Checkbox 3 state is: "+str(checkButtonVar3.get()))
	destroy_main_window()
	create_results_window()
	
#create main window
def create_main_window():
	#insert text box for searching
	global searchText, entry, searchButton, checkButton1, checkButton2, checkButton3, checkButtonVar1, checkButtonVar2, checkButtonVar3
	
	
	entry = tkinter.Entry()
	entry.delete(0, len(searchText))
	entry.insert(0, searchText)
	entry.grid(row=0,column=0)

	#search button
	searchButton = tkinter.Button(text="SEARCH", command=on_button_click)
	searchButton.grid(row=0, column=1)

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

#clear main window
def destroy_main_window():
	entry.destroy()
	searchButton.destroy()
	checkButton1.destroy()
	checkButton2.destroy()
	checkButton3.destroy()

#creates tabbed results window
def create_results_window():
	global labelFrame, buttonFrame, tab1, tab2, tab3, goBackButton, label
	#create three tab buttons
	buttonFrame = tkinter.Frame()
	buttonFrame.grid(row=0,column=0)
	
	tab1 = tkinter.Button(buttonFrame, text="Wikipedia", command=display_option1)
	tab1.grid(row=0,column=0)
	tab2 = tkinter.Button(buttonFrame, text="Option 2", command=display_option2)
	tab2.grid(row=0,column=1)
	tab3 = tkinter.Button(buttonFrame, text="Option 3", command=display_option3)
	tab3.grid(row=0,column=2)
	labelFrame = tkinter.Frame()
	labelFrame.grid(row=1,column=0)
	label = tkinter.Label(labelFrame, text="This is where text would go for the content of the API.")
	#label.config(justify=tkinter.LEFT)
	#label.config(wrap=320)
	label.grid(row=1,column=0)
	goBackButton= tkinter.Button(text="Go Back", command=go_back_to_main_window)
	goBackButton.grid(row=0,column=3)

def go_back_to_main_window():
	destroy_results_window()
	create_main_window()
	
#display option 1 results, currently Wikipedia
def display_option1():
	#todo: Wikipedia API call
	print("Wikipedia")
	
def display_option2():
	#todo: put option 2 api call here
	print("option 2")
	
def display_option3():
	#todo: option 3 goes here
	print("option 3")
	
#clears the result window
def destroy_results_window():
	tab1.destroy()
	tab2.destroy()
	tab3.destroy()
	buttonFrame.destroy()
	labelFrame.destroy()
	label.destroy()
	goBackButton.destroy()
	
create_main_window()
root.mainloop()

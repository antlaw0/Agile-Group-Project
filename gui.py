import tkinter
import wikipedia

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
	display_option1()
#create main window
def create_main_window():
	#insert text box for searching
	global searchText, entry, searchButton, label
	
	entry = tkinter.Entry()
	entry.delete(0, len(searchText))
	entry.insert(0, searchText)
	entry.grid(row=0,column=0)

	#search button
	searchButton = tkinter.Button(text="SEARCH", command=on_button_click)
	searchButton.grid(row=0, column=1)

	
	#create three tab buttons
	buttonFrame = tkinter.Frame()
	buttonFrame.grid(row=1,column=0)
	
	tab1 = tkinter.Button(buttonFrame, text="Wikipedia", command=display_option1)
	tab1.grid(row=0,column=0)
	tab2 = tkinter.Button(buttonFrame, text="Option 2", command=display_option2)
	tab2.grid(row=0,column=1)
	tab3 = tkinter.Button(buttonFrame, text="Option 3", command=display_option3)
	tab3.grid(row=0,column=2)
	labelFrame = tkinter.Frame()
	labelFrame.grid(row=2,column=0)
	label = tkinter.Label(labelFrame, text="This is where text would go for the content of the API.")
	#label.config(justify=tkinter.LEFT)
	label.config(wrap=600)
	label.grid(row=1,column=0)
	
		
#display option 1 results, currently Wikipedia
def display_option1():
	global wikiSummaryText
	wikiSummaryText = wikipedia.summary(searchText)
	label.config(text=wikiSummaryText)
	
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

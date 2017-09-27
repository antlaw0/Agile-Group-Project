import tkinter
from tkinter import *
import wikipedia
from flickrapi import FlickrAPI
import requests
import shutil
import os
from PIL import Image

searchText = ""

# main root for window
root = tkinter.Tk()
root.title("Encyclopedia")

# arg1: width, arg 2: height, arg3: screen x, arg4: screen y
#todo: get user's screen resolution instead of hard coding
root.geometry("1280x1024+0+0")


# just for testing for now, eventually search function will go here
def on_button_click():
    global searchText, entry, checkButtonVar1, checkButtonVar2, checkButtonVar3
    # assigns searchText to string in entry
    searchText = entry.get()
    print("Entry is: " + entry.get())
    display_option1()


# create main window
def create_main_window():
    # insert text box for searching
    global searchText, entry, searchButton, label

    entry = tkinter.Entry()
    entry.delete(0, len(searchText))
    entry.insert(0, searchText)
    entry.grid(row=0, column=0)

    # search button
    searchButton = tkinter.Button(text="SEARCH", command=on_button_click)
    searchButton.grid(row=0, column=1)

    # create three tab buttons
    buttonFrame = tkinter.Frame()
    buttonFrame.grid(row=1, column=0)

    tab1 = tkinter.Button(buttonFrame, text="Wikipedia", command=display_option1)
    tab1.grid(row=0, column=0)
    tab2 = tkinter.Button(buttonFrame, text="Flickr", command=display_option2)
    tab2.grid(row=0, column=1)
    tab3 = tkinter.Button(buttonFrame, text="Twitter", command=display_option3)
    tab3.grid(row=0, column=2)
    labelFrame = tkinter.Frame()
    labelFrame.grid(row=2, column=0)
    label = tkinter.Label(labelFrame, text="This is where text would go for the content of the API.")
    # label.config(justify=tkinter.LEFT)
    label.config(wrap=600)
    label.grid(row=1, column=0)


# display option 1 results, currently Wikipedia
def display_option1():
    global wikiSummaryText
    wikiSummaryText = wikipedia.summary(searchText)
    label.config(text=wikiSummaryText)


def display_option2():
    # todo: put option 2 api call here
    print(searchText)
    flickrAPI(searchText)

    searchPicFileGif = 'search.gif'
    picture = PhotoImage(file=searchPicFileGif)
    panel = label.config(image=picture)
    panel(side="bottom", fill="both", expand="yes")


    print("option 2")


def display_option3():
    # todo: option 3 goes here
    print("option 3")


# clears the result window
def destroy_results_window():
    tab1.destroy()
    tab2.destroy()
    tab3.destroy()
    buttonFrame.destroy()
    labelFrame.destroy()
    label.destroy()
    goBackButton.destroy()

def flickrAPI(searchText):

        search = searchText
        print(search)
        #Frame.__init__(self)
        #self.grid()

        #code to call API from here http://joequery.me/code/flickr-api-image-search-python/
        FLICKR_PUBLIC = os.environ['FLICKR_PUBLIC']
        FLICKR_SECRET = os.environ['FLICKR_SECRET']
        flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
        print ('n',flickr)
        extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
        results = flickr.photos.search(text=search, per_page=5, extras=extras)
        print(results)
        photos = results['photos']

        from pprint import pprint
        pprint(photos)


        fetchPhotoURL = results['photos']['photo'][0]['url_l']
        print(fetchPhotoURL)  # Again, just checking

        # Reference: http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests

        searchPicFileNameJpg = 'search.jpg'
        searchPicFileGif = 'search.gif'
        Image.open(searchPicFileNameJpg).save(searchPicFileGif)


        resp = requests.get(fetchPhotoURL, stream=True)
        with open(searchPicFileNameJpg, 'wb') as out_file:
            shutil.copyfileobj(resp.raw, out_file)
        del resp




create_main_window()
root.mainloop()
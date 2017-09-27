from tkinter import *
from flickrapi import FlickrAPI
import requests
import shutil
from PIL import Image
import os
#used some code from Claras git hub repository https://github.com/minneapolis-edu/HelloFlikrGUI/blob/master/FlickrGUI.py

class Flickr(Frame):


    def __init__(self):

        search = input('searching for')
        Frame.__init__(self)
        self.grid()

        #Add a label to GUI
        self._label = Label(self, text="Here are some pictures of " + search)
        self._label.grid()
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


        fetchPhotoURL = results['photos']['photo'][0]['url_o']
        print(fetchPhotoURL)  # Again, just checking

        # Reference: http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests

        catPicFileNameJpg = 'cat.jpg'
        catPicFileGif = 'cat.gif'


        resp = requests.get(fetchPhotoURL, stream=True)
        with open(catPicFileNameJpg, 'wb') as out_file:
            shutil.copyfileobj(resp.raw, out_file)
        del resp

        # Flickr returns a jpg. Tkinter displays gif. Use pillow to convert the JPG to GIF
        # Reference https://pillow.readthedocs.org/handbook/tutorial.html
        Image.open(catPicFileNameJpg).save(catPicFileGif)

        # Add PictureImage to GUI
        _catPic = PhotoImage(file=catPicFileGif)
        _catPicLabel = Label(self, image=_catPic)
        _catPicLabel.image = _catPic
        _catPicLabel.grid()

def main():

    Flickr().mainloop()

main()
import youtube_dl
import subprocess
import os

import kivy
#import logging
#logging.getLogger("kivy").disabled = True
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (400, 600)
class StartScreen(Screen):
    pass
class SelectScreen(Screen):
    pass
class VideoScreen(Screen):
    def downloadAudio(self):
        url = self.ids.vidtxt.text
        frmt='140'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        } 
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestaudio/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
    def download360(self):
        url = self.ids.vidtxt.text
        frmt='134'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestvideo/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
    def download480(self):
        url = self.ids.vidtxt.text
        frmt='135'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        } 
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestvideo/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
    def download720(self):
        url = self.ids.vidtxt.text
        frmt='136'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        } 
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestvideo/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
    def download1080(self):
        url = self.ids.vidtxt.text
        frmt='137'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        } 
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestvideo/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

class PlaylistScreen(Screen):
    def downloadAudio(self):
        url = self.ids.playtxt.text
        frmt='140'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        } 
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestaudio/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
    def download360(self):
        url = self.ids.playtxt.text
        frmt='134'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestvideo/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
    def download480(self):
        url = self.ids.playtxt.text
        frmt='135'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        } 
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestvideo/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
    def download720(self):
        url = self.ids.playtxt.text
        frmt='136'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        } 
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestvideo/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False,  
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
    def download1080(self):
        url = self.ids.playtxt.text
        frmt='137+bestaudio/best'
        try:
            ydl_opts = {
                        'format': frmt,       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False
                        } 
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            ydl_opts = {
                        'format': 'bestvideo/best+bestaudio/best',       
                        'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',
                        'noplaylist' : False
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

class EndScreen(Screen):
    pass

class aTubeCatcherApp(App):
    def build(self):
        return Builder.load_file('gui/screen.kv')

if __name__ == '__main__':
    aTubeCatcherApp().run()
    

#Media Launcher Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#This program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")
#!/usr/bin/env python
import sys,os, subprocess
from gi.repository import Gtk, Gdk, GObject
from subprocess import Popen
class Media(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(Media, self).__init__(*args, **kwargs)
    def __init__(self):    
    # Create THE WINDOW
        self.window1=Gtk.Window()
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.set_default_size(400, 20)
        self.window1.set_title("Media Launcher")
        self.window1.connect("destroy", Gtk.main_quit)
        self.window1.set_resizable(False)

#Veritas
        self.veritas_button=Gtk.Button()
        self.veritas_button.connect("clicked", self.veritas)
        self.veritas_button.set_label("Veritas Player")

#Albix
        self.albix_button=Gtk.Button()
        self.albix_button.connect("clicked", self.albix)
        self.albix_button.set_label("Albix Player")         
#RipperX
        self.sound_button=Gtk.Button()
        self.sound_button.connect("clicked", self.sound)
        self.sound_button.set_label("RipperX")               
#HTML-Gtk
        self.html_button=Gtk.Button()
        self.html_button.connect("clicked", self.html)
        self.html_button.set_label("HTML5-GTK Player")        


#####################################
#Main Box
        self.hbox=Gtk.HBox()
        self.hbox.pack_start(self.veritas_button, False, False, 2)
        self.hbox.pack_start(self.albix_button, False, False, 2)
        self.hbox.pack_start(self.sound_button, False, False, 2)
        self.hbox.pack_start(self.html_button, False, False, 2)
                
        self.vbox2=Gtk.VBox()
        self.vbox2.pack_start(self.hbox, False, False, 0)
        
#Show everything		
        self.window1.add(self.vbox2)
        self.window1.show_all()   
#Functions
################
    def veritas(self,widget):
        get_going="/usr/share/Veritas/veritas.py"
        subprocess.Popen(['python', get_going])
  
    def albix(self,widget):
        get_going="/usr/share/albix.py"
        subprocess.Popen(['python', get_going])

    def sound(self,widget):
        get_going="ripperx"
        subprocess.Popen([get_going])
               		  		                    	        
    def html (self, widget):
        get_going="/usr/share/html5.py"
        subprocess.Popen(['python', get_going])        
if __name__ == "__main__":
    Gtk.init(sys.argv)
    browser = Media()
    Gtk.main()

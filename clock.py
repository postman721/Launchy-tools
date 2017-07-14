#!/usr/bin/env python
#Clock Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#The program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")
from gi.repository import Gtk, Gdk, GObject, GLib, Gio
import pygtk, os, sys, time
class Clock(Gtk.Window):  	     
#Show clock 
    def update_clock(self, timer):
        real_time=time.strftime ("%d %b %Y \n %H:%M")
        a=str(real_time)
        self.timer.set_text(a)
        return True  
#Close function
    def destroy (self, widget, data=None):
        Gtk.main_quit()            	        
    def __init__(self):    
    # Create THE WINDOW
        self.window1=Gtk.Window()
        self.window1.set_decorated(False)
        self.window1.set_size_request(100,60)
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.move(500,0)
#Make Clock Label 
        self.timer=Gtk.Label()
        self.timer.set_justify(Gtk.Justification.CENTER)        
#Make Frames
        self.frame=Gtk.Frame()
        self.frame.add(self.timer)         
        self.frame.set_size_request(100,60)
        self.vbox=Gtk.VBox()
        self.vbox.pack_start(self.frame, False, True, False)
#Show everything		
        self.window1.add(self.vbox)
        self.window1.show_all()         
#Making window resizable and enabling the close window connector        
        self.window1.set_resizable(False)
        self.window1.connect("destroy", Gtk.main_quit)                       
def main():
    Gtk.main()
    return 0
if __name__ == "__main__":
    cc=Clock()
    GLib.timeout_add(200, cc.update_clock, None)
    main()

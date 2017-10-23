# Launchy-tools
Launchy panel and associated tools(Pyqt5)


![launchynew](https://user-images.githubusercontent.com/29865797/31877051-afb550c6-b7dd-11e7-8613-0b6180018bb0.jpg)

![media_launcher](https://user-images.githubusercontent.com/29865797/28211946-ddce9d08-68a7-11e7-8c01-62df60f665d6.jpg)


From this repository you will find: 
Launchy Panel, an improved toggle script, clock program and a Media Launcher. These tools appeared all as parts of PostX 0.4.4.

It is adviced that you place this entry to .xbindkeysrc for quick launching.

----------------------------
#Launchy Toggle function

“bash /usr/share/launchy_toggle.sh”

F6

---------------------------
Place this entry(or similar) to your autostart file(.xinitrc etc). The entry will make sure that Launchy starts as hidden and that the toggle between hide and show works.

touch $HOME/.toggle_launchy &

Place all the programs to /usr/share pathway.

The toggle script executes and ends both Launchy Panel and the clock upon a keypress. Procps is now a needed dependency, which means that the full list should be as  below. On some distributions, you might need to adapt the dependency list.

python3 

python-pyqt5 

python-minimal 

procps 

python-gi


_______________________
Original post is at:
http://www.techtimejourney.net/launchy-qt/

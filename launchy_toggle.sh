#!/bin/bash

TOGGLE=$HOME/.toggle_launchy

if [ ! -e $TOGGLE ]; then
    touch $TOGGLE
    pkill -f clock.py & 
	pkill -f launchy &

    
else
    rm $TOGGLE
	python /usr/share/clock.py &
	python /usr/share/launchy &
	
fi

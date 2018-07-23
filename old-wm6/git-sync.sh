#!/bin/bash
wget -N http://people.ds.cam.ac.uk/ssb22/gradint/wm65favs.py
wget -N http://people.ds.cam.ac.uk/ssb22/gradint/timer-adjust.py
wget -N http://people.ds.cam.ac.uk/ssb22/gradint/SBminutes.py
git commit -am update && git push

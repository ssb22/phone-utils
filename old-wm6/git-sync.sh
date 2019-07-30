#!/bin/bash
git pull --no-edit
wget -N http://people.ds.cam.ac.uk/ssb22/gradint/wm65favs.py http://people.ds.cam.ac.uk/ssb22/gradint/timer-adjust.py http://people.ds.cam.ac.uk/ssb22/gradint/SBminutes.py http://people.ds.cam.ac.uk/ssb22/gradint/wmSMSsend.py
git add *.py
git commit -am update && git push

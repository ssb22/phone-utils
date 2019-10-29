#!/bin/bash
git pull --no-edit
wget -N http://ssb22.user.srcf.net/gradint/wm65favs.py http://ssb22.user.srcf.net/gradint/timer-adjust.py http://ssb22.user.srcf.net/gradint/SBminutes.py http://ssb22.user.srcf.net/gradint/wmSMSsend.py http://ssb22.user.srcf.net/s60/pwi2txt.sh http://ssb22.user.srcf.net/s60/csc2vcf.py http://ssb22.user.srcf.net/s60/csm2txt.py
git add *.py
git commit -am update && git push

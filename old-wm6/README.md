# Python utilities for old Windows Mobile 6 phones
from https://ssb22.user.srcf.net/wm/61notes.html and https://ssb22.user.srcf.net/s60/ etc

(the above two pages are also mirrored at https://ssb22.gitlab.io/wm/61notes.html and https://ssb22.gitlab.io/s60/ just in case)

* [csc2vcf](csc2vcf.py) for copying WM6 PIM Backup contacts lists to Android or S60
* [csm2txt](csm2txt.py) for formatting WM6 PIM Backup message dumps
* [pwi2txt](pwi2txt.sh) script to recover text from the Windows Mobile Notes app
* [SBminutes](SBminutes.py) call-time checker that accounts for minimum call times
  * also [timer-adjust](timer-adjust.py) to adjust the built-in timer (and log signal strength)
* [send-sms](send-sms.py), [wmSMSsend](wmSMSsend.py): two versions of a library function to send SMS messages from Python (I'm not sure how I ended up with two versions of this)
* [IE Favorites indexer](wm65favs.py)

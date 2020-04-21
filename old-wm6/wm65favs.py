# Update index.html from \Windows\Favorites
# (for IE 6 on Windows Mobile 6)
# Silas S. Brown - public domain - no warranty

# In theory this code is compatible with both Python 2 and
# Python 3, but Python 3 was not available for WM phones.

# This is so you can set your MSIE start page to
# file://\Windows\Favorites\index.html
# to save having to tap twice to get them.

# (You could just set it to the directory instead, but
# then they'll open in the File Explorer and you might
# not see their full titles.  And on 6.5 it no longer
# works to add a shortcut to the Favorites directory on
# the Start Menu.)

# You could also use this on earlier versions of
# Windows Mobile (although it's less needed as they
# let you set shortcuts to the Favorites directory),
# but some versions of IE6 (e.g. IEMobile 6.12 on WM6-Smartphone)
# lack the option to set a new home page (and the default
# home page file in \Windows is protected from alteration)
# so you'd have to do it via the registry, probably
# HKLM\SOFTWARE\Microsoft\Internet Explorer\AboutURLs\home
# (set it to file://\Windows\Favorites\index.html )
# but I haven't checked this on all devices.

# Where to find history:
# on GitHub at https://github.com/ssb22/wm6-utils
# and on GitLab at https://gitlab.com/ssb22/wm6-utils
# and on BitBucket https://bitbucket.org/ssb22/wm6-utils

import os
out = open("\\Windows\\Favorites\\index.html","w")
out.write('<html><head><meta name="mobileoptimized" content="0"><meta name="viewport" content="width=device-width"></head><body><h1>Bookmarks</h1>') # heading helps because top part of page might be obscured on first load
for f in sorted(os.listdir("\\Windows\\Favorites")):
  if f.endswith(".url"):
    for l in open("\\Windows\\Favorites\\"+f):
      if l.startswith("URL="): out.write("<h3><a href=\"%s\">%s</a></h3>" % (l[4:].strip(),f[:-4]))

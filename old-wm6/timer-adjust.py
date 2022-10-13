# timer-adjust.py version 1.1, Silas S. Brown 2011, Public Domain, no warranty

# Requires Python to be installed on the phone (see Gradint page).
# This is Python 2 code; Python 3 was not available for WM phones.

# This is a Python script to adjust the built-in outgoing call timer
# on no-touchscreen Windows Mobile phones, configure the
# "wm6minutecount" program on with-touchscreen WM6 phones, or
# log signal strength on WM phones.

# No-touchscreen phones have an outgoing calls timer which can be
# reset to 0, but this script allows you to set it to any value you
# like, for example if you made a free call that you don't want to be
# counted, or if you made extra calls when the SIM was in another phone.

# Note however that this call timer does NOT support the "minimum call
# lengths" that networks are increasingly using (e.g. a call less than 30
# seconds counts as 30 seconds) - you need wm6minutecount for that,
# which requires a touchscreen phone (otherwise installs but won't display),
# or use my later script SBminutes.py.
# This script can help set up the correct registry entries for wm6minutecount
# after you have installed it.

# Note that, besides not working on no-touchscreen phones, wm6minutecount has
# been known to fail to read logs on WM6.5 phones, and also won't "un-count"
# non-eligible numbers.  So you might prefer to use my SBMinutes script
# instead of this (older) one.

# SIGNAL STRENGTH LOGGER:
# Instead of adjusting the settings, enter S (or s) to make the
# script start logging signal strength, which you can use to
# compare networks etc.  Note the average strength may be misleading if
# the phone is switching between 2G and 3G, because their scales are
# different.  But "% uptime" should still be useful.  If you do start
# the logger, then to completely stop it you sometimes have to switch off.

# Where to find history:
# on GitHub at https://github.com/ssb22/wm6-utils
# and on GitLab at https://gitlab.com/ssb22/wm6-utils
# and on BitBucket https://bitbucket.org/ssb22/wm6-utils
# and at https://gitlab.developers.cam.ac.uk/ssb22/wm6-utils
# and in China: https://gitee.com/ssb22/wm6-utils

import ctypes
HKEY_LOCAL_MACHINE = ctypes.c_long(0x80000002)
HKEY_CURRENT_USER  = ctypes.c_long(0x80000001)
KEY_READ = ctypes.c_long(0x20019)
KEY_ALL_ACCESS = ctypes.c_long(0xf003f)

def read_registry(branch,key):
 hkey = ctypes.c_long() ; d = {}
 if ctypes.cdll.coredll.RegOpenKeyExW(branch,ctypes.c_wchar_p(key),0,KEY_READ,ctypes.byref(hkey))==0:
  i=0
  while i<200:
    entryType = ctypes.c_long()
    name = ctypes.c_wchar_p(' '*128) ; nameLen = ctypes.c_long(128)
    data = ctypes.c_wchar_p(' '*128) ; dataLen = ctypes.c_long(128)
    if ctypes.cdll.coredll.RegEnumValueW(hkey, i, name, ctypes.byref(nameLen), 0, ctypes.byref(entryType), data, ctypes.byref(dataLen)): break
    name = name.value[:nameLen.value]
    def ordor0(a):
        if a: return ord(a)
        else: return 0
    if entryType.value == 4: data = ordor0(data.value[1:2])*0x10000+ordor0(data.value[0:1]) # TODO 2's-complement?
    else: data = data.value[:dataLen.value] # (TODO other types)
    d[name] = data
    i += 1
  ctypes.cdll.coredll.RegCloseKey(hkey)
 return d

def write_dword(branch,key,name,value):
  hkey = ctypes.c_long() ; action = ctypes.c_long()
  if ctypes.cdll.coredll.RegCreateKeyExW(branch,ctypes.c_wchar_p(key),0,0,0,KEY_ALL_ACCESS,0,ctypes.byref(hkey),ctypes.byref(action))==0:
    ctypes.cdll.coredll.RegSetValueExW(hkey,ctypes.c_wchar_p(name),0,4,ctypes.c_wchar_p(unichr(int(value%0x10000))+unichr(value/0x10000)),4) # (TODO negative values?)
    ctypes.cdll.coredll.RegCloseKey(hkey)
    # TODO error checking

def signalLog():
 import time
 d = read_registry(HKEY_LOCAL_MACHINE,r"System\State\Phone")
 if "Signal Strength" in d:
  start,avg,nUp,nDown = time.time(),0,0,0
  print "secs (signal) uptime x average strength"
  while True:
    s = d["Signal Strength"]
    if s>10: # a reading of 10 seems to mean 'switched off' on v1415
      avg = (avg*nUp+s)*1.0/(nUp+1) ; nUp += 1
    else:
      nDown += 1 ; s = 0
    print "%4d (%d) %d%% x %d" % (int(time.time()-start),s,nUp*100/(nUp+nDown),int(avg))
    # (can't do it with \r - doesn't work)
    time.sleep(30)
    d = read_registry(HKEY_LOCAL_MACHINE,r"System\State\Phone")

d = read_registry(HKEY_LOCAL_MACHINE,r"Software\Microsoft\Shell\CumulativeCallTimers\Line_0")
if "OutgoingVoiceCurrent" in d:
  secs = d["OutgoingVoiceCurrent"]
  if secs>3600: extra = " = %d:%02d" % (secs/60,secs%60)
  else: extra=""
  ip = raw_input("Enter h.m.s or +m.s or -m.s\n(currently %d:%02d:%02d%s)" % (int(secs/3600),int((secs%3600)/60),secs%60,extra))
  if ip.lower()=='s': signalLog()
  elif ip:
    if ip[0]=='+': add,ip = 1,ip[1:]
    elif ip[0]=='-': add,ip = -1,ip[1:]
    else: add=0
    newsecs = 0
    for p in ip.replace(":",".").split("."):
        newsecs = newsecs*60 + int(p)
    if add: secs += (add*newsecs)
    else: secs = newsecs
    write_dword(HKEY_LOCAL_MACHINE,r"Software\Microsoft\Shell\CumulativeCallTimers\Line_0","OutgoingVoiceCurrent",secs)
else: # it seems we're on a touchscreen phone, so configure wm6minutecount instead
  d = read_registry(HKEY_CURRENT_USER,r"Software\nGotme\minutecounter")
  if "g_wDDay" in d:
    for thing,desc in [
        ("g_wDDay","Start day of month"),
        ("g_maxMinutes","Minutes allowance"),
        
        # TODO check these two are described correctly:
        ("g_FirstMinute","Min secs per call"),
        ("g_RestMinute","Min secs per min")]:
      
        ip = raw_input(desc+" ("+str(d[thing])+"): ")
        if ip.lower()=="s": signalLog()
        elif ip: write_dword(HKEY_CURRENT_USER,r"Software\nGotme\minutecounter",thing,int(ip))

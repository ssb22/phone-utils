# SBMinutes version 1.2, Silas S. Brown 2011-2013,2015, Public Domain, no warranty

# Requires Python to be installed on the phone (see Gradint page).

# Checks call logs and calculates outgoing usage,
# accounting for minimum call times (unlike WM-Smartphone's built-in counter)

# Displays mins used so far, and mins that "should be" used so far if the
# monthly allowance were being used at an equal rate
# (so you can see if you're "ahead" or "behind" with your minutes)

# I wrote SBMinutes because I couldn't get LCMinutes to work
# and wm6minutecount requires a touch-screen phone.

# You can change the values below according to your contract:

start_day_of_month = 14
monthly_allowance = 600
minimum_secs_per_call = 60
secs_increment = 1
allow_phone_error = 3 # seconds added to each call just in case
numbers_not_affecting_allowance = [
  # List here any numbers you might call that shouldn't affect the
  # minute count.  A prefix of a longer number is also allowed.
  # (Note: these numbers are not necessarily free - in fact some
  # of them are very expensive - but they don't affect the minutes.)
  "1","05","08","076","070","07744","07755","09","44555",
  ]
strip_prefixes = [ "141" ] # to be stripped before testing the above

# If your logs are incomplete but you know that your usage (including
# roundup) does not exceed N minutes up to and including date Y-M-D,
# you can set known_usage = ((YYYY,M,D), N)  (do NOT prefix m/d with 0)
# and this will then be used instead of the logs on or before that date.
known_usage = None

# If you know you will be without phone access for a future period, you
# can set avoid_usage = ((YYYY,M,D), (YYYY,M,D)) with the start and end dates
# of the no-usage period.  This will be factored into the report that tells
# you if you're "ahead" or "behind" with your minutes.
avoid_usage = None

# ----------------------------------------------------------------------

import ctypes, math
import ctypes.wintypes as wintypes

IOM_MISSED,IOM_INCOMING,IOM_OUTGOING = range(3) # enum
CALLLOGSEEK_BEGINNING = 2

CallLogEntrySize = 48
class CallLogEntry(ctypes.Structure): _fields_ = [
  ("cbSize",wintypes.DWORD),
  ("ftStartTimeL",wintypes.DWORD),
  ("ftStartTimeH",wintypes.DWORD),
  ("ftEndTimeL",wintypes.DWORD),
  ("ftEndTimeH",wintypes.DWORD),
  ("iom",wintypes.DWORD), # enum
  ("flags",wintypes.DWORD), # (fOutgoing, fConnected, fEnded, fRoam)
  ("callerIDtype",wintypes.DWORD),
  ("number",wintypes.LPWSTR),
  ("name",wintypes.LPWSTR),
  ("nameType",wintypes.LPWSTR),
  ("note",wintypes.LPWSTR)
]

def ftToUnixTime(ft): return (ft-116444736000000000)/10000000

import time
timeNow = time.time()
y,m,d = time.localtime(timeNow)[:3]
timeNow = time.mktime((y,m,d,23,59,59,0,0,-1)) # by just before midnight tonight
yUp,mUp,dUp = time.localtime(timeNow)[:3]
if dUp >= start_day_of_month:
  mUp += 1
  if mUp>12: mUp,yUp = 1,yUp+1
yStart,mStart,dStart = time.localtime(timeNow)[:3]
if dStart < start_day_of_month:
  mStart -= 1
  if mStart==0: mStart,yStart = 12,yStart-1
dUp=dStart=start_day_of_month
tUp = time.mktime((yUp,mUp,dUp,0,0,0,0,0,-1))
tStart = time.mktime((yStart,mStart,dStart,0,0,0,0,0,-1))
if avoid_usage:
  avoidStart = time.mktime(avoid_usage[0]+(0,0,0,0,0,-1))
  avoidEnd = time.mktime(avoid_usage[1]+(0,0,0,0,0,-1)) + 24*3600 # end of that day
  if avoidEnd > tStart and avoidStart < tUp: # overlaps current period
    if avoidEnd > tUp: avoidEnd = tUp
    if avoidStart < timeNow: avoidStart = timeNow # no point accounting for scheduled avoids in the past (if changing, need to fix some of the formulae below)
    if avoidStart < avoidEnd <= tUp: tUp -= avoidEnd-avoidStart
if tUp>timeNow: proportionLeft = (tUp-timeNow)*1.0/(tUp-tStart)
else: proportionLeft = 0 # probably in an avoid_usage period at the end of an allowance
minsUsed_ifEven = math.ceil(monthly_allowance*(1-proportionLeft))

seconds = added = addedCalls = totalCalls = errorCalls = 0

if known_usage:
  tStart2 = time.mktime(known_usage[0]+(0,0,0,0,0,-1)) + 24*3600 # end of that day
  if tStart2 > tStart:
    tStart = tStart2
    seconds += known_usage[1]*60

def rounding(length):
  if length < minimum_secs_per_call:
    return minimum_secs_per_call - length
  if secs_increment > 1:
    remainder = length % secs_increment
    if remainder: return secs_increment-remainder
  return 0

def inAllowance(number):
  for n in strip_prefixes:
    if number.startswith(n): number=number[len(n):]
  for n in numbers_not_affecting_allowance:
    if number.startswith(n): return 0
  return 1

handle = ctypes.c_long()
if ctypes.cdll.phone.PhoneOpenCallLog(ctypes.byref(handle))==0:
  # 3rd param of PhoneSeekCallLog is the Nth item (asking for 0)
  iRecord = ctypes.c_long() # the index value of the record actually found
  ctypes.cdll.phone.PhoneSeekCallLog(handle,CALLLOGSEEK_BEGINNING,0,ctypes.byref(iRecord))
  entry = CallLogEntry() ; entry.cbSize = CallLogEntrySize
  ape = 0 # allowed phone error
  while ctypes.cdll.phone.PhoneGetCallLogEntry(handle,ctypes.byref(entry))==0:
    start,end = ftToUnixTime(entry.ftStartTimeL|(entry.ftStartTimeH<<32)),ftToUnixTime(entry.ftEndTimeL|(entry.ftEndTimeH<<32))
    if start < tStart: break # we're into calls that happened before start_day_of_month
    if (entry.flags & 3) == 3 and inAllowance(entry.number): # 3 = fOutgoing + fConnected
      rTmp = rounding(end-start)
      total_if_phone_correct = end-start + rTmp
      length = end-start + allow_phone_error
      ar = rounding(length)
      total_if_phone_wrong = length + ar
      # Don't double-count allow_phone_error and rounding in the report:
      if total_if_phone_correct == total_if_phone_wrong:
        # rounded-up value would be the same anyway, so ignore phone error
        length = end-start ; ar = rTmp # rounding(end-start)
      else:
        ape += allow_phone_error # stet length and ar
        errorCalls += 1
      added += ar
      if ar: addedCalls += 1
      seconds += length ; totalCalls += 1
  ctypes.cdll.phone.PhoneCloseCallLog(handle)
  minsUsed = int((seconds+added+59)/60)
  if minsUsed < minsUsed_ifEven: stuff=" (%dm behind)" % (minsUsed_ifEven-minsUsed)
  elif minsUsed > minsUsed_ifEven: stuff=" (%dm AHEAD)" % (minsUsed-minsUsed_ifEven)
  else: stuff = " (on schedule)"
  stuff += ", incl %d:%02d+%d:%02d round+error (%d,%d calls out of %d)" % (added/60,added%60,ape/60,ape%60,addedCalls,errorCalls,totalCalls) # might be only partially visible
  raw_input("Time used = %dm%s included" % (minsUsed,stuff))
  if start > tStart: raw_input("Warning: logs go back only to %d-%02d %d:%02d (incomplete?)" % time.localtime(start)[1:5])
else: raw_input("Could not open call logs")

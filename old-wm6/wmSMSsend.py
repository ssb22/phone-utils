# Python 2 code to send SMS message programatically on Windows Mobile (2003SE/5/6/6.5)
# Silas S. Brown - public domain

# Where to find history:
# on GitHub at https://github.com/ssb22/wm6-utils
# and on GitLab at https://gitlab.com/ssb22/wm6-utils
# and on BitBucket https://bitbucket.org/ssb22/wm6-utils
# and at https://gitlab.developers.cam.ac.uk/ssb22/wm6-utils
# and in China: https://gitee.com/ssb22/wm6-utils

def send_SMS_message(number, unicode_text, delivery_confirmation=1):
  print "Sending to "+number+"..."
  handle = wintypes.DWORD()
  ret = ctypes.cdll.sms.SmsOpen(u"Microsoft Text SMS Protocol",
      wintypes.DWORD(2),ctypes.byref(handle),None)
  if not (ret==0 and handle): raise Exception("SmsOpen error")
  class SMSaddress(ctypes.Structure):
    _fields_ = [("smsatAddressType",ctypes.c_int),
      ("ptsAddress",ctypes.c_wchar * 256)]
  unicode_text = u"" + unicode_text # make sure it's Unicode
  if delivery_confirmation: byte1="\2"
  else: byte1="\0"
  ret = ctypes.cdll.sms.SmsSendMessage(handle,None,
      ctypes.byref(SMSaddress(0,number)),None,unicode_text,
      wintypes.DWORD(2*len(unicode_text)),byte1+"\0\0\0\3\0\0\0\0\0\0\0",
      wintypes.DWORD(12),ctypes.c_int(0),wintypes.DWORD(0),None)
  if not ret==0: raise Exception("SmsSendMessage error")
  print "OK, closing"
  ctypes.cdll.sms.SmsClose(handle)
  print "closed"

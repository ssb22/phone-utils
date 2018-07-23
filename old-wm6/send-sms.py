# Send SMS message on WM6 phone from Python 2
# Silas S. Brown - public domain

import ctypes
import ctypes.wintypes as wintypes
def send_SMS_message(number, unicode_text, confirm_delivery=True):
  print "Sending to "+number+"..."
  handle = wintypes.DWORD()
  ret = ctypes.cdll.sms.SmsOpen(u"Microsoft Text SMS Protocol",
      wintypes.DWORD(2),ctypes.byref(handle),None)
  if not (ret==0 and handle): raise Exception("SmsOpen error")
  class SMSaddress(ctypes.Structure):
    _fields_ = [("smsatAddressType",ctypes.c_int),
      ("ptsAddress",ctypes.c_wchar * 256)]
  unicode_text = u"" + unicode_text # make sure it's Unicode
  if confirm_delivery: ss="\2"
  else: ss="\0"
  ss += "\0\0\0\3\0\0\0\0\0\0\0"
  ret = ctypes.cdll.sms.SmsSendMessage(handle,None,
      ctypes.byref(SMSaddress(0,number)),None,unicode_text,
      wintypes.DWORD(2*len(unicode_text)),ss,
      wintypes.DWORD(12),ctypes.c_int(0),wintypes.DWORD(0),None)
  if not ret==0: raise Exception("SmsSendMessage error")
  print "OK, closing"
  ctypes.cdll.sms.SmsClose(handle)
  print "closed"

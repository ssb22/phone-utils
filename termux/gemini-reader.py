#!/usr/bin/env python3

"""Android Termux script to read clipboard changes
using Gemini TTS free-tier API key (can be more expressive
than the onboard TTS)
Silas S. Brown 2025 - public domain - no warranty

To set up:
pkg install python3 rust sox
# ensure aaudio-sink is not commented out in /data/data/com.termux/files/usr/etc/pulse/default.pa
pip install google-genai # takes time
GEMINI_API_KEY=your_api_key_here python gemini-reader.py
# or set os.environ['GEMINI_API_KEY'] after imports below

Can get "model overloaded" errors if Google servers are busy.
"""

from google import genai
from google.genai import types
import sys,os,tempfile,subprocess,wave,time
os.system("pluseaudio --start &")
client = genai.Client()
last=None
while True:
  try: clip=subprocess.getoutput("termux-clipboard-get")
  except KeyboardInterrupt: break
  if last is None:
    last=clip
    print("Waiting for clipboard changes")
  elif clip==last or not clip.strip(): time.sleep(1)
  else:
    last=clip
    response = client.models.generate_content(model="gemini-2.5-flash-preview-tts",contents=clip,config=types.GenerateContentConfig(response_modalities=["AUDIO"],speech_config=types.SpeechConfig(voice_config=types.VoiceConfig(prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name='Sulafat')))))
    with tempfile.NamedTemporaryFile(suffix='.wav') as tmp_file:
        w=wave.open(tmp_file,'wb')
        w.setnchannels(1),w.setsampwidth(2),w.setframerate(24000),w.writeframes(response.candidates[0].content.parts[0].inline_data.data),w.close()
        # subprocess.run(['termux-media-player','play',tmp_file.name],check=True) # won't work on Google Play version of Termux
        subprocess.run(['play',tmp_file.name],check=True)
        time.sleep(1)

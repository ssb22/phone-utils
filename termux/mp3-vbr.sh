#!/bin/bash

# Termux script to re-code the last recorded OGG file from the
# StereoMatch Amazing MP3 Recorder app into VBR MP3 (which is not an
# option in the app's MP3 screen: it has 64-bit, 32-bit etc CBR but
# no VBR).  Record as ogg and run this: it removes the OGG, leaves the
# MP3 in Downloads (with size guide) and Sends it (to Telegram, Discord
# or whatever) so it can be played on iOS devices that lack OGG support

# Silas S. Brown 2025 - public domain - no warranty

# Needs termux-setup-storage and pkg-install vorbis-tools lame

set -e
SrcDir="$(date +/storage/emulated/0/Amazing_AVR/%Y_%m_%d)"
Out="$(date +/storage/emulated/0/Download/%Y-%m-%d.mp3)"
if ! cd "$SrcDir"; then echo "No Amazing_AVR directory found for today"; exit 1; fi
R="$(ls --color=none *.ogg|sort|tail -1)"
if ! [ -e "$R" ]; then echo "No ogg found for today"; exit 1; fi
oggdec -o - "$R" | lame --vbr-new -V 9 -h - -o "$Out"
rm -v "$R"
cd ; rmdir "$SrcDir" || true # rm dir if empty
du -h "$Out"
termux-open --send "$Out"

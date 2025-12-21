
from https://ssb22.user.srcf.net/s60/video.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/s60/video.html) just in case)

# Notes on video conversion with `mencoder`

These are some quick notes I made to provide starting points for `mencoder` command lines. It is meant for conversions that are legal (own work, personal use of products without DRM, etc). I am not an `mencoder` expert but just collected some options that worked for me.



## Input options

### DVD
* Track 1, default language, subtitles off:

   `dvd://1 -dvd-device PATH -sid 31` (where `PATH` is the path to the DVD image)
* To select language and subtitles: pass numbers to `-aid` and `-sid` (see what’s printed by `mplayer`); goes *after* the input it applies to
* If the disc was not “finalised” by the DVD recorder, mplayer may be able to read the device node directly (on GNU/Linux `/dev/sdc` or similar; `/dev/rdisk1` on a Mac)
* If `mencoder` doesn’t work well on a particular DVD, you could also try `ffmpeg`:

   `cd $DVD_DIR/VIDEO_TS && ffmpeg -i "concat:$(echo *.VOB|tr ' ' '|')" -map 0:1 -map 0:3`

  or `cat $DVD_DIR/VIDEO_TS/*.VOB | ffmpeg -i - -map 0:1 -map 0:3`

  where for a multi-title DVD you’ll need to figure out the correct set of VOB files, and `-map 0:1` and `-map 0:3` might need to be refined according to ffmpeg’s output of the language list; you’ll also need to add some ffmpeg *output* options, e.g. `-vcodec mpeg4 -b:v 600k -strict -2 -g 50 -vf yadif -c:a aac -b:a 160k output.mp4`

  These commands do *not* handle subtitles.

  Some discs work better with `mencoder`, while other discs work better with `ffmpeg`, so *both* commands are useful to keep.

### .flv and other video files
* Just specify the filename
* Can trim with `-ss` start-second and/or `-endpos` length
* Can save a clip to a separate file using `-o clip.avi -oac lavc -ovc lavc` and then combine multiple clips by specifying all their filenames on an `mencoder` command (when doing this it might be necessary to list the scaling and output options *before* the inputs)
* If the sound is not synchronized, try setting the framerate explicitly with `-fps 24` (or 27 or whatever) after each input file, maybe even adding `-mc 0` in older versions

### rtmp streams embedded in complex Javascript etc

You need root access to a GNU/Linux machine with `rtmpdump`
* As root, do:

  `iptables -t nat -A OUTPUT -p tcp --dport 1935 -m owner \! --uid-owner root -j REDIRECT

  rtmpsuck`
* Leave it running while playing the video in a Flash-enabled browser like Google Chrome (which must be run as a non-root user for this to work)
* Check rtmpsuck output for captured files, then proceed as above
* If you get issues due to reconnection near the start of the stream, you may have to edit out a small section of the video. For example if the problem occurs around 64 seconds in, try `-mc 0 -noskip -edl <(echo 63 65 0)`

### Flash audio

On a GNU/Linux machine with `~/.asoundrc` set to

`pcm.teeraw { type empty

slave.pcm "tee:default,'/tmp/out.raw',raw" }`

use `FLASH_ALSA_DEVICE=teeraw firefox` and (e.g.) `sox -t raw -r 44100 -c 2 -b 16 -s /tmp/out.raw /tmp/out.wav` then proceed with out.wav. (To reduce risk of `/tmp/out.raw` being overwritten, start `sox` *before* interacting with the browser to stop the stream.) This method was last tested in 2017 and is unlikely to work in the latest non-Flash browsers.

### Edit decision lists

Use `-edl` filename, where each line of the file is start-second end-second 0 (use mplayer to find the seconds and to test the EDL). You can add up the total number of minutes you’ve cut by piping the EDL through `python -c 'import sys;print(sum(float(l.split()[1])-float(l.split()[0]) for l in sys.stdin)/60.0)'`

### Audio file (static or blank picture)

This might be useful for porting audio to old DVD players that don’t support MP3 etc. You need to first add the audio to blank video using ffmpeg: (command adapted from Stefano Sabatini’s suggestion on ffmpeg-user)

`ffmpeg -i input-audio.wav -s 640x480 -f rawvideo -pix_fmt rgb24 -r 25 -i /dev/zero -shortest -vcodec libx264 -preset medium -tune stillimage -crf 24 -acodec copy output.mkv`

then proceed with output.mkv (convert it to `.mpg` as per DVD output below, etc)
* Output file might not concatenate well with other tracks, but the `dvdauthor` command (below) can take multiple `mpg` inputs

You can also use ffmpeg to attach audio to a **still image**:

`ffmpeg -i audio.mp3 -loop 1 -i picture.jpg -shortest -vcodec mpeg4 -b:v 800k audio.avi`

(then convert `audio.avi` into the required output format)

Or to **replace the soundtrack** of an existing video (for language dubbing etc),

`ffmpeg -i video.mp4 -i sound.wav -map 0:v -map 1:a -vcodec copy output.mkv`

then proceed with output.mkv

### FM radio

As above, but if recording the audio to MP3 you might want to avoid wasting space encoding any frequencies above 15kHz. This is because FM stereo requires a 4kHz guard band around the 19kHz pilot signal, therefore any audio you get above 15kHz *must* be the result of equipment noise; therefore the option of a 32kHz sample rate (Nyquist cutoff 16kHz) makes sense, but your ADC circuitry might not do that well so it’s probably best to convert in software:

`rec --input-buffer=1048576 -t raw -r 44100 -c 2 -b 16 -e signed-integer - | sox -t raw -r 44100 -c 2 -b 16 -e signed-integer - -t raw -r 32000 -c 2 -b 16 -e signed-integer - | lame -h -s 32 -r - -o output.mp3`

(older versions of `sox` might need `-2 -s` or `-w -s` instead of `-b 16 -e signed-integer` in three places of the above command)

### Two language versions

If a video is available in two versions with different-language sound tracks:
* Fast command to keep just the sound from videoS and the picture and subtitles VideoP (useful if the speaker of VideoP’s language wants only subtitles):

  `ffmpeg -i videoS.mp4 -i videoP.mp4 -map 0:a:0 -map 1:v:0 -map 1:s:0 -c copy -c:s mov_text output.mp4`

   *this might require subtitles to be switched on in the player*
  * To specify that the subtitles are Chinese, add `-metadata:s:s:0 language=zho` (this only affects player menus)

To play the two videos on separate devices but time-synchronised over a local network:
* on the first device,

   ` mplayer -udp-$'m\!x61s\x74\x65r' -udp-ip `(second device’s IP)` video1.mp4 `
* and on the second device,

  ` mplayer -udp-$'\x73\x6c\x61\x76e' -udp-seek-threshold 0.1 -udp-ip `(second device’s IP)` video2.mp4 `

(press `v` to toggle subtitles or `f` to toggle full-screen; I’ve obfuscated the options that use technical terms which some viewers might misunderstand as a racist insult)

To play the two videos on the same machine, one with sound only and sent to HDMI, the other with full-screen picture, and sound sent to Bluetooth, set the system to use PulseAudio (not PipeWire: Raspberry Pi OS 12 needs `sudo raspi-config` / Advanced / Audio to set it back to PulseAudio) and do:

`mplayer -noconsolecontrols -vo null -udp-$'\x73\x6c\x61\x76e' -udp-seek-threshold 0.1 -ao pulse::alsa_output.platform-`(value from `pacmd list-sinks`)`.hdmi.hdmi-stereo video2.mp4 & mplayer -fs -nosub -udp-$'m\!x61s\x74\x65r' -ao pulse::bluez_sink.`(MAC address)`.a2dp_sink video1.mp4`

(also works with URLs instead of saved video files, in which case I suggest adding `-cache-min 1 -cache 1048576` to each command if you have 4GB+ of RAM)

To have the two languages in two stereo channels on the same player, first create a WAV file:
* For older versions of ffmpeg:

  ` ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex '[0:a]aconvert=s16:mono[l]; [1:a]aconvert=s16:mono[r]; [l][r]amerge[snd]' -map '[snd]' audio.wav `
* For newer versions of ffmpeg (e.g. 3.1.3):

  ` ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex '[0:a]aformat=sample_fmts=s16:channel_layouts=mono[l]; [1:a]aformat=sample_fmts=s16:channel_layouts=mono[r]; [l][r]amerge[snd]' -map '[snd]' audio.wav `

Then, to keep the picture from the first file, do:

`ffmpeg -i input1.mp4 -i audio.wav -map 0:v -map 1:a -vcodec copy output.mkv `

and proceed with output.mkv (if it lacks sound, it’s probably an ffmpeg version issue: try `-b:v 10000k output.mp4` instead of `-vcodec copy output.mkv`).

Or if the pictures differ as well (for example on-screen text has been translated) then you might wish to show both pictures at once. The following command will do that, positioning them diagonally to reduce peripheral-motion annoyance when trying to watch only one; it works only if both videos are the same size.

` ffmpeg -i input1.mp4 -i input2.mp4 -i audio.wav -filter_complex '[0:v]pad=iw*2:ih*2:0:ih[tmp]; [tmp][1:v]overlay=W/2:0[pic]' -map '[pic]' -map 2:a -b:v 3000k output.mp4 `

If the videos are additionally of different sizes, you’ll need a longer version of this command:

` W1=$(ffprobe -show_entries stream=width input1.mp4 |grep ^width=|head -1|cut -d= -f2); W2=$(ffprobe -show_entries stream=width input2.mp4 |grep ^width=|head -1|cut -d= -f2); H1=$(ffprobe -show_entries stream=height input1.mp4 |grep ^height=|head -1|cut -d= -f2); H2=$(ffprobe -show_entries stream=height input2.mp4 |grep ^height=|head -1|cut -d= -f2); ffmpeg -i input1.mp4 -i input2.mp4 -i $Audio -filter_complex "[0:v]pad=$[$W1+$W2]:$[$H1+$H2]:0:$H2[tmp]; [tmp][1:v]overlay=$W1:0[pic]" -map '[pic]' -map 2:a -b:v 3000k output.mp4 `

### Recording the desktop

Linux/X11 region around mouse, audio from microphone:

`ffmpeg -f alsa -i pulse -f x11grab -follow_mouse 100 -show_region 1 -r 25 -i "$DISPLAY" output.mkv`
* Omit `-f alsa -i pulse` for no audio. Region size defaults to 640x480, override with `-s`. To capture full screen use `-f x11grab -s $(xrandr -q|head -1|sed -e 's/.*current//' -e 's/,.*//'|tr -d ' ') -r 25` etc
* Fedora 34+ requires `-i pipewire` instead of `-i pulse` (and is likely to give buffer underruns and drop audio—use a different distribution if possible)
* To record a vertical section of camera to the right of the desktop area, with slightly-delayed ‘viewfinder’ window on the camera section, and a 60-second timeout:

  `ffmpeg -f alsa -i pulse -f x11grab -s 480:480 -follow_mouse 100 -show_region 1 -r 25 -i "$DISPLAY" -f video4linux2 -i /dev/video0 -filter_complex '[2:v]crop=160:480:240:0,split=2[d][D];[d]pad=640:480:480:0[c];[c][1:v]overlay=0:0[o]' -map '[o]' -map 0:a -t 60 -y output.mkv -map '[D]' -f matroska -t 60 - | ffplay -autoexit -noborder -left 0 -`
* To record *just* the camera, with viewfinder:

  `ffmpeg -f alsa -i pulse -f video4linux2 -i /dev/video0 -filter_complex '[1:v]split=2[d][D]' -map '[d]' -map 0:a -y output.mkv -map '[D]' -f matroska - | ffplay -autoexit -noborder -left 0 -`

  (press `q` on the original command terminal to stop the recording)
* If you then find somebody wanted mp4 format:

  `ffmpeg -i output.mkv -codec copy output.mp4`

  (but for some applications you might also need to recode h264)

DOSBox (audio from programs): in `dosbox.conf` (or `~/Library/Preferences/DOSBox*` on Mac) set the `captures=` directory to something (e.g. `/tmp`) and the default start/stop keybinding Ctrl-Alt-F5 (or Ctrl-F6 for audio only). **Beware** at least some versions of DOSBox can partially lose videos in some circumstances.

Mac OS X: “QuickTime Player” despite its name is not just a player. Its File menu contains options to record the screen with optional microphone narration, or to record from camera. Results are placed in `~/Movies` and I think version 10.9+ of OS X also lets you record *part* of the screen (otherwise you have to post-process with mencoder’s `-vf crop=w:h:x:y` if you don’t want the whole screen).

### Series of pictures

You *could* just do (for example) `mencoder 'mf://*.jpg' -mf fps=0.2` but it’s sometimes possible for mencoder to crash on signal 11 as it tries to scale pictures, so it might be worth pre-scaling, for example for PAL DVD: `for N in *.jpg ; do jpegtopnm "$N" | pnmscale -xysize 720 576 | pnmpad -black -width 720 -height 576 | pnmtopng > "$(echo "$N"|sed -e s/jpg$/png/)";done` (followed by the mencoder command on `*.png`, or on `@listfile` to ensure it processes them in the correct order)

## Output options

### Android, iPhone or Mac

`-of lavf -lavfopts format=mp4 -vf dsize=480:352:2,scale=0:0,harddup -ovc x264 -sws 9 -x264encopts bitrate=512:bframes=0:chroma_me:me=umh:frameref=6:global_header:level_idc=30:nocabac:partitions=all:subq=5:threads=auto:trellis=1 -oac faac -faacopts mpeg=4:object=2:raw:br=128 -o output.mp4`
* If you get “MPlayer was compiled without libfaac” try using `-oac mp3lame` instead of `-oac faac -faacopts mpeg=4:object=2:raw:br=128` (should still play on modern devices) or use `ffmpeg` instead e.g. `ffmpeg -i video.avi -b 512k output.mp4` (errors at the very end of the stream can be ignored)
* This can also be used to work around WeChat’s error “Unable to share this video due to unspported format”
* If you get “x264encopts is not an MEncoder option” on a Mac, please note the MacPorts and Homebrew versions no longer support x264: you have to compile from SVN source using the instructions at mplayerhq (but you might want to keep the packaged m *player* in case the SVN version segfaults on playing)

### Nokia S60, S40 etc

`-ofps 24 -of lavf -lavfopts format=mp4 -vf dsize=320:240:2,scale=0:0 -oac lavc -ovc lavc -lavcopts aglobal=1:vglobal=1:acodec=libfaac:abitrate=96:vcodec=mpeg4 -o output.mp4`
* Don’t try sending a multi-megabyte MP4 via Bluetooth to an S40 phone: some models get permanently bricked as a result (infinite reset loop on power-on with no reformatting possible)

### Windows 10 or Mac with large screen

Playable on *recent* versions of Windows Media Player (Windows 10 should work), and also playable on Mac QuickTime:

`-of lavf -lavfopts format=mp4 -ovc x264 -sws 9 -x264encopts bframes=0:chroma_me:me=umh:frameref=6:global_header:level_idc=30:nocabac:partitions=all:subq=5:threads=auto:trellis=1 -oac faac -faacopts mpeg=4:object=2:raw:br=128 -o output.mp4`
* Press **Alt-Enter** to make WMP play full-screen (in VLC it’s `F`, plus you might need Ctrl-H to hide the controls)

### Zoom Cloud Meetings

Zoom added a built-in video-share function to version 5.4.3 but only on Windows and Mac (use **Share Screen / Advanced / Video** and choose a file), but on GNU/Linux the method below is still needed (and might also work for other video-conferencing software that has “screen sharing” but no option to feed a video to it directly).
* If nobody at *your* location needs to view the video full-screen, then it’s likely more efficient to feed the video to Zoom *at its original size*, avoiding an extra level of rescaling. Try a command like:

   `echo pause | mplayer $'-as\x73' $'-\x73\x6c\x61\x76e' -noborder video.mp4`

  (I’ve obfuscated the options for enabling subtitle fonts and waiting on standard input, because some might misunderstand these technical terms as a racist insult if accidentally shown on a conference screen—beware they might still show up if you’re using a terminal that shows the currently-executing command on its title bar.) Optionally add `-ss` start-second and/or `-endpos` length before the video.

  Mplayer then starts paused so you can set up the screen-share on that window.
  * On a recent Mac, the above command is **not** likely to work. As mentioned above, “Share Screen / Advanced / Video” is better, but if you’re running some *other* video-conferencing software that cannot share video directly, you might still want to play without scaling: if you can run MacPorts you can `sudo port install mpv` and run something like:

    `mpv --geometry=1280x720 --video-unscaled=yes --pause video.mp4`

    (needs adjusting for the video size)—and the first use of Share Screen is likely to require a restart of the video-conferencing software after you’ve been prompted to change the Mac’s security settings, so I’d advise running a test meeting first.
  * Due to Zoom’s broken accessibility code on the GNU/Linux version, it is not possible to select “share computer sound” and “optimise screen sharing for video clip” without using the mouse: as of 2020, attempts to press Space or Enter on these checkboxes give the *appearance* of a tick-mark appearing but do not actually set the underlying variable. (And if it were open-source I could have fixed that for them, but it’s closed-source proprietary software, so all I can do is fill in their feedback form—my 17<sup>th</sup> bug report to them as it happens; I don’t know how many they’re managing to process.)
  * This situation also makes the procedure **not** compatible with [high-DPI displays](https://ssb22.user.srcf.net/setup/dpi.html) if the monitor is not physically large enough: the desktop Zoom application is notoriously bad at allowing small window sizes, so the controls often end up being off-screen, which means if they are mouse-only then they cannot be operated no matter how many keyboard shortcuts you know. Some window managers e.g. Gnome 3 let you use Alt-F7 + arrow keys (or Super key + drag) to move Zoom windows partially off-screen at the top in order to access off-screen controls at the bottom.
  * If you *do* have a physically large enough monitor (or if you have enough eyesight to cope with normal DPI settings) and you are able to use the physical mouse, then Share-screen, select the Mplayer window (remembering to share audio, optimise for video unless it’s slides, and mute the microphone) and press Space to start Mplayer. This single-window screen-share should then stop automatically when Mplayer closes itself at the end of the video, or press `q` to stop early.
* If the video should additionally be full-screen at your location then you can use VLC:

  `vlc -f --start-paused video.mp4 vlc://quit`

  (with optional `--start-time` and `--stop-time` after the `--start-paused`)—VLC starts paused so you can set up the screen-share on that window before pressing Space to play, and VLC quits at the end so the screen-share stops automatically.

If your PulseAudio distorts the video’s sound on the remote side due to bad resampling, you can correct this in `.config/pulse/daemon.conf`—Charles Z Henry suggests:

`resample-method = speex-fixed-7

default-sample-rate = 48000

alternate-sample-rate = 44100`

—this might need a restart of your desktop session.

“Share computer audio” can silently fail on some Fedora 34 setups, reportedly because Fedora changed from PulseAudio to PipeWire and PipeWire’s PulseAudio plugin is not supported as well as real PulseAudio (it seems it works on some machines but not others). It may be necessary to unmute, set “Suppress background noise” as low as possible, be quiet, hope the fan doesn’t spin up, and accept degraded audio going from the speaker to the microphone.

To show **static pictures** (e.g. slides) : VLC can take multiple images on the command line (and can set “minimal interface” on the menus + not full-screen); by default each image is played for 10 seconds, but Space pauses, then on each slide advance, press **`n` and Space** to advance to the next slide and re-pause.

### Patching one Zoom meeting into another Zoom meeting

The Mac version of Zoom lets you run a second instance if you launch it via a `/j/` URL, and this second instance can be set to share the screen of the first instance of Zoom (tested on Zoom 5.9.1 on macOS 12.2.1). This might be useful if a group wants to watch a presentation and then break off for separate discussion without needing control of the main meeting’s breakout-room facility. The “share computer audio” option does *not* work when sharing the screen of another Zoom instance: you must use speaker to microphone. But if you’ve installed BlackHole (or SoundFlower on older Macs) you can set one Zoom instance to output sound to a Multi-Output Device (created in the “Audio/MIDI Setup” application) and the other instance to take microphone input from the BlackHole device (you’ll then need to change this setting if you want to speak later).

### Old Windows or Windows Mobile
* For QVGA displays (320x240):

   `-ovc lavc -lavcopts vcodec=wmv2 -oac lavc -lavcopts acodec=wmav2 -of lavf -vf dsize=320:240:2,scale=0:0 -o output.wmv`
  * If you’re using a version of mencoder you haven’t tested before (e.g. on a server you’re SSH’ing into), **be sure to test that sound works** when Windows plays the WMV file. Some mencoder installations can generate silent WMVs without warning, and you might need to reinstall mencoder.
* Desktop or high-end WM systems with larger displays might not need the `-vf dsize=320:240:2,scale=0:0` option
* Streaming via slow-connection m3u: try substituting `vcodec=wmv2:vbitrate=100` and (e.g.) `-vf dsize=160:120:2,scale=0:0` but total may still need 150-200kbit/sec (18-24kB/sec); might stream on GSM EDGE but not plain GSM (and the default Windows Mobile installation can’t stream from M3U)

### MP3 audio

(any picture will be discarded)

`-ovc copy -of rawaudio -oac mp3lame -lameopts vbr=2:q=9:aq=0 -o output.mp3`
* Some versions of mencoder say “video stream is mandatory”; in this case try `mplayer -ao pcm:file=output.wav` and `lame`
* If the result is to be written to an audio CD, you can skip the MP3 encoding and output a `cdda` file via sox: `-ovc copy -of rawaudio -oac pcm -srate 44100 -really-quiet -o - | sox -t raw -r 44100 -c 2 -s -b 16 - output.cdda` (you might want to use `-endpos 4797` or whatever on the input side to ensure the result is not too long). cdda files can be recorded with `cdrecord -audio` on GNU/Linux; on Mac you should specify `wav` instead, put it in an empty directory and do `drutil burn -audio` (dirname)
* **Some Apple-recorded audio files** can’t be read by (many installations of) mencoder. Converting these requires a Mac and something like `afconvert rec.aif -d LEI16 rec.wav && lame --vbr-new -V 9 rec.wav -o rec.mp3` (afconvert can’t directly write mp3, at least not on any Mac I was able to test)

### “Play All” bookmarklet

If you are on a (probably RedHat) setup where the only working audio player is the browser, you can drag this link to your bookmarks bar: [Play All](javascript:var l=document.links,a=false;for(var i=0;i<l.length;i++)if(l[i].href&&l[i].href.match(/.*(mp3|ogg|wav)$/)){var o=a;a=document.createElement(’audio’);a.setAttribute(’id’,’au’+i);a.setAttribute(’controls’,’controls’);a.setAttribute(’src’,l[i].href);l[i].parentNode.insertBefore(a,l[i]);if(o)o.onended=function(a){return function(){a.play()}}(a);else a.play()}) then press it after loading a `file://` directory listing containing sound files. (Alternatively, serve that directory to a mobile device with headphones and arrange for the script to be injected into the directory listing. Or install mocp.)

### DVDs and VCDs

(based on mencoder documentation with some changes)
* For a PAL DVD try this:

   `-oac lavc -ovc lavc -of mpeg -mpegopts format=dvd:tsaf -vf expand=:::::16/9,scale=720:576,harddup -srate 48000 -af lavcresample=48000 -lavcopts vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:keyint=15:vstrict=0:acodec=mp2:aspect=16/9 -ofps 25 -o output.mpg`

  Check the size of the .mpg (note DVD-5’s “4.7G” is 4.38GiB and allow for overheads); if too big, add `:vbitrate=4000` or whatever to the `-lavcopts` list
* Also check the A/V sync; if `mencoder` can’t get it right then you might need to use `ffmpeg` instead: first convert it to a file if it’s not already, then do `ffmpeg -i file.avi -aspect 16:9 -target pal-dvd output.mpg` (perhaps with `-b:v 4000k` or similar just before the output filename if the bitrate needs limiting). If this still doesn’t work, try a separate run of ffmpeg to fix the video first using `-vcodec copy -acodec copy` and/or use `-ac 4` etc.

  (Ffmpeg’s concatenation is more complex than mencoder’s: it’s best done *after* all files are converted, and you’d need to do something like `ffmpeg -i file1.mpg -i file2.mpg -i file3.mpg -filter_complex '[0:0][0:1] [1:0][1:1] [2:0][2:1] concat=n=3:v=1:a=1[v][a]' -map '[v]' -map '[a]' -target pal-dvd output.mpg` which requires ffmpeg 1.1+; the 0..2 and the =3 need changing according to the number of input files, and any bitrate limit might need to be added again. Such concatenation might not be necessary if the `dvdauthor` command below takes multiple `mpg`s, but it doesn’t always.)
* When you have `output.mpg` (from either `mencoder` or `ffmpeg`), run this (again changing the 16:9 if necessary):

   `mkdir DVD/ && export VIDEO_FORMAT=PAL && dvdauthor -o DVD/ -t -v 16:9 output.mpg && dvdauthor -o DVD/ -T && rm output.mpg && mkisofs -dvd-video -v -o DVD.iso DVD && rm -r DVD`
* On GNU/Linux, use `sudo cdrecord -data DVD.iso`; on a Mac, use `hdiutil burn DVD.iso` (**don’t** use the Finder to right-click on DVD.iso and select “Burn to Disc”, as this creates a *new* filesystem containing just the ISO file, which most DVD players will reject as “CDROM”)
* Some (but not all) DVD players can also play VCD. For a PAL VCD (format is constrained, you can’t change the bitrate etc):

  `-oac lavc -ovc lavc -of mpeg -mpegopts format=xvcd -vf dsize=352:288:2,harddup -srate 44100 -af lavcresample=44100 -lavcopts acodec=mp2:abitrate=224:vcodec=mpeg1video:keyint=15:vrc_buf_size=327:vrc_minrate=1152:vrc_maxrate=1152:vbitrate=1152:aspect=16/9 -ofps 25 -o output.mpg`

  Then run `vcdimager output.mpg` and write with `cdrdao write videocd.cue` or convert to ISO with `bchunk videocd.bin videocd.cue videocd.iso`
* If you have less than 35 minutes to put on a video CD then you can try SVCD (*if* supported by the player), e.g.:

   `-oac lavc -ovc lavc -of mpeg -mpegopts format=xsvcd -vf dsize=480:576:2,harddup -srate 44100 -af lavcresample=44100 -lavcopts vcodec=mpeg2video:mbd=2:keyint=15:vrc_buf_size=917:vrc_minrate=600:vbitrate=2500:vrc_maxrate=2500:acodec=mp2:abitrate=224:aspect=16/9 -ofps 25 -o output.mpg`

  then run `vcdimager -t svcd output.mpg` and burn with `cdrdao write videocd.cue`.

See also [spaced-out audio tracks with `cdrdao`](https://ssb22.user.srcf.net/s60/cdrdao.html)

Copyright and Trademarks:
All material © Silas S. Brown unless otherwise stated.
Android is a trademark of Google LLC.
Apple is a trademark of Apple Inc.
Bluetooth is a registered trademark held by the Bluetooth Special Interest Group.
Google is a trademark of Google LLC.
HDMI is a trademark or registered trademark of HDMI Licensing LLC in the United States and other countries.
iPhone is a trademark of Apple in some countries.
Javascript is a trademark of Oracle Corporation in the US.
Linux is the registered trademark of Linus Torvalds in the U.S. and other countries.
Mac is a trademark of Apple Inc.
MP3 is a trademark that was registered in Europe to Hypermedia GmbH Webcasting but I was unable to confirm its current holder.
Raspberry Pi is a trademark of the Raspberry Pi Foundation.
WeChat is a trademark of Tencent Holdings Limited.
Windows is a registered trademark of Microsoft Corp.
Zoom is a trademark of Zoom Video Communications, Inc.
Any other [trademarks](https://ssb22.user.srcf.net/trademarks.html) I mentioned without realising are trademarks of their respective holders.

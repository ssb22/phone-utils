
from https://ssb22.user.srcf.net/setup/asound.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/setup/asound.html) just in case)

# Sound-recorder applications on Android OS

Students recording lectures etc have generally moved from [dedicated hardware](https://ssb22.user.srcf.net/gradint/dvr.html) to mobile ‘apps’ (applications). Below are my notes comparing some of the available alternatives on the [Android](android.md) platform. Usual disclaimers apply.

I only list apps that:
1. Work in the background and/or with screen off (saving battery),
2. can record a long talk even in the unpaid version of the app.

Android 9 and above does not allow telephone calls to be recorded: any recording happening at the same time as a call will get silence for the duration of the call. Therefore if you plan to both record a talk and call somebody to listen live, you’ll need two separate devices (unless you’re running an older version or you managed to ‘root’ it).
* StereoMatch “Amazing MP3 Recorder” (removed from “Play Store” in May 2024; APK at `stereomatch.com`): Pros:
* Works with screen readers
* Large controls, easy to operate (problems with early versions have been fixed)
* Visual indication of microphone pick-up on the left of the screen

Cons:
* Closed source (although currently without advertisements apart from suggestions to upgrade to Pro)
* If you don’t like reading about voice changers and what people do with them, you might not appreciate some of the “what’s new” updates (but there haven’t been so many of these recently)

If you record OGG (MP3 encoding is a paid add-on but OGG is provided), the default settings give about 72 kbps for speech (31M/hr, variable).
* Onall Sound Recorder No Ads (removed from “Play Store” in March 2019): Pros:
* Unpaid version can record to MP3, which might be useful if you need to share the recording with someone who can’t play OGG and you can’t first recode it (although recoding might still be a good idea for speech, as when set to 44.1k it seems to approximate lame’s `--abr 80` setting)
* Decibel readout during recording (might be useful for making noise complaints?)

Cons:
* Closed source
* Small controls
* Switching off the screen during recording results in the app being backgrounded, which makes pause/stop take longer later
* Triveous Voice Recorder (removed from “Play Store” in January 2025): Pros:
* Visual indicator of microphone pick-up

Cons:
* Closed source
* Poor use of storage space. Although Triveous *can* compress to AAC (or M4A in version 5; 128 kbps = 55M/hr, convertible via `mplayer -ao pcm:file=output.wav` or some installations of Audacity), it *also* makes an uncompressed WAV of the current track while encoding, so **you need to allow space for this** and/or keep each track short,
* and the old Version 3 even fails to delete them (for tracks exceeding about 18 minutes depending on hardware)—this was fixed in Version 4, but the device still needs space for the WAV of each track while recording that track, regardless of the “realtime” setting (non-realtime results in an extra encoding step taking about 50% of the recording time).
* If you *do* have space for WAV (3.3hr/G) then for distant sources it’s (usually) better to *just* use WAV and re-code it later, but this is no longer an option in version 5 which is M4A-only (but *still* has the “need to leave room for the WAV as well” limitation that StereoMatch doesn’t have).
* Triveous also requires Android 4.4 or above, so won’t work on old 4.1 phones like the Galaxy S2
* Rehearsal Assistant (removed from “Play Store” in December 2017): Pros:
* GPL

Cons:
* Serious bug when recording uncompressed (see its SourceForge Bug 4)—on some devices, if you do too much in other apps such as the browser, background recording can be aborted *without* clearing the red indicator on the notification bar, leaving an incomplete wav file that needs `sox --ignore-length` to play.
* For nearby sounds you could try the 48 kbps AMR-NB .3gp (loadable in Audacity, mplayer etc) but the quality is lower.

iPhone ships with Voice Memos (possibly under Extras); this too works with the display switched off or in the background, and records 64kbit AAC (.m4a). Some other iOS programs output `.aif` files that might need [converting on a Mac](video.md).

Copyright and Trademarks:
All material © Silas S. Brown unless otherwise stated.
Android is a trademark of Google LLC.
iPhone is a trademark of Apple in some countries.
Mac is a trademark of Apple Inc.
MP3 is a trademark that was registered in Europe to Hypermedia GmbH Webcasting but I was unable to confirm its current holder.
SourceForge is a trademark of VA Software Corporation.
Any other [trademarks](https://ssb22.user.srcf.net/trademarks.html) I mentioned without realising are trademarks of their respective holders.

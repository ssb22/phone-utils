# Notes and utilities for old Windows Mobile 6 phones
from https://ssb22.user.srcf.net/wm/ and related pages
(also [mirrored on GitLab Pages](https://ssb22.gitlab.io/wm/) just in case)

## List of vaguely-usable old Windows Mobile phones

I used second-hand Windows Mobile phones from 2009 to 2019, primarily for a reference CD-ROM which, for its 2008 through 2014 versions, had an option to run on Windows Mobile 2003SE, 5 or 6.x but not the more recent devices. To assist with finding equipment, I created a “wiki” page called “List of Windows Mobile Devices”, but it was also useful to place the following more-opinionated list on my own site.

To get on *this* list, a phone must:
* Have a physical QWERTY keyboard that’s **wide enough to allow *at least* ¾cm per column**—frontal “thumb boards” don’t count (a Revo has 1cm+ *and* a ; key that’s well-placed for reassignment in Dvorak-like or Colemak layouts, but no WM phone has that)
* Run 2003SE, 5 or 6 (**not** 6.1+) for compatibility with Wenlin, eSpeak etc
* Support GSM (and UMTS if it’s a 3G phone) so it worked in the UK, Europe etc. This is less useful as 2G and 3G networks get switched off; no WM phone supports the more modern 4G or 5G signals (the “HTC Max 4G” was a misnomer).

Some “marketplace” websites with “advanced search” functionality let you search for an OR combination of quoted phrases. This is useful because identical or very similar phones have different names. Depending on the marketplace, you might need to insert commas between the quoted items, and perhaps parenthesise the whole query. You might be given a choice between “all words” and “any words”, but this choice **might be best left unchanged** as the site’s developers don’t always test it on complex queries (for example in late 2012 a famous site’s search function started ignoring quote marks when “any words” was set, whereas it worked if you said “all words” but inserted commas).

You may also wish to “exclude” words like adapter adaptor battery cable card case charger cover chassis cradle earpiece film for games guard handsfree headset holder kit mechanism membrane mount pouch protector protectors replacement sock spare stylus unlock to reduce the “clutter” of spare-parts listings.
**All these phones can develop faults**, even when left in a drawer, so try not to pay *too* much for a working one—you might need to replace it from time to time. (I don’t usually bother with auctions—I’ve wasted too much time losing them. You can search for fixed-price immediate sales within your range.)

## 2G phones with touchscreens

Some of these phones’ microphones (designed for use near the cheek) don’t work so well in speakerphone positions—they pick up too much when in front, or lose sound when too far. The effect may not be so bad on a 3G signal, but if you’re on 2G and use speakerphone (for SAR reductions or to see the display), try having the mic a fingertip away from your cheek and the speaker further away (you can still check the screen when not speaking).
* "Dopod C800" "Dopod C858" "HTC Herald" "HTC P4350" "HTC P4351" "XDA Terra" "T-Mobile Wing US" "VPA Compact IV"
* "UBiQUiO 601" (keyboard twists open)
* "I-Mate K-JAR"
* "RoverPC Q5" "Kinpo Saturn"
* "MDA Vario" "SPV M3000" "HTC Wizard 200" "i-mate K-JAM" "Qtek 9100" "XDA Mini S"
* "Eten Glofiish M700"
* "XDA Mini Pro"
* "VPA Compact II" "HTC Wizard 110" "HTC P4300"

## 2G no-touchscreen phones (with number pads)

Here is a [script to adjust the outgoing call timer](timer-adjust.py) (can also log signal strength), and [SBminutes](SBminutes.py) to check call time more accurately.
* "Vodafone v1415" "HTC S710" "HTC S711" "HTC Vox" "SPV E650" "Dopod C50" (front number pad, slide-out QWERTY)
* "Pantech Duo C810" (slide-out number pad, slide-out QWERTY; also has 3G but only on 850/1900 and no Wi-Fi—although the latter is no great loss because old-WM increasingly has problems with modern Wi-Fi access points anyway.)

## 3G phones with touchscreens

3G phones can improve voice quality **even in a 2G-only area or building** if your 2G network supports 3G’s AMR compression, although this does increase 2G’s power load slightly. Where 3G signal is available it also gives faster data and causes no 217 Hz burst-interval noise on sensitive audio equipment, but its continuity can be too much for an ailing second-hand battery. 3G WM phones can be switched to 2G-only if necessary; if option not shown, try editing registry and setting “3G” instead of “ActiveSync” in HKLM / Software / HTC / CommManager / 8.
* "CHT 9000" "HTC Hermes 200" "TyTN 200" "HTC P4500" "SoftBank X01HT" "Swisscom XPA v1605" "VPA Compact III" "Vodafone v1605"
* "Dopod 838 Pro" "HTC Hermes 100" "HTC TyTN 100" "NTT DoCoMo hTc Z" "XDA Trion" "SPV M3100" "Qtek 9600" "i-mate JASJAM"
* "MDA Vario II" "HTC Hermes 300" "TyTN 300"
* "XDA Zinc"
* "Toshiba G900" "Toshiba Portege G900" "Softbank X01T"
* "HTC Universal" "Dopod 900" "E-Plus PDA IV" "Grundig GR980" "MDA Pro" "Qtek 9000" "SFR v1640" "SPV M5000" "SPV M5000" "VPA IV" "Vodafone v1640" "XDA Exec" "i-mate JASJAR" (keyboard twists open)

## 3G phones with touchscreens and GPS

GPS usage affects battery life (tracking the signal needs lots of maths, and if you lose track then it takes time to re-acquire even with aGPS). So pedestrians probably won’t use GPS much and therefore won’t need to insist on it. (Cell-based location is usually sufficient and takes less power.)
* "Dopod U1000" "HTC Athena 100" "MDA Ameo" (large, keyboard has to be attached so I don’t know how easy/hard it is to get out quickly)
**If you don’t mind version 6.1** (which won’t run the published binaries of Wenlin or eSpeak, but it should still run Python and it can manage more RAM than WM5/6), you could try:
* "MDA Vario III" "TyTN II" "HTC P4550" "HTC Kaiser" "v1615" "XDA Stellar" "VPA Compact V" (this group might have a higher fault rate and trouble sourcing good batteries)
* "Touch Pro" (has double resolution so you might have text size problems in older programs; also has a rather small screen which may give DPI issues)
* "HTC Tilt2" "Tytn III" "Touch Pro 2" "Touch Pro2" (also double resolution but larger screen; check it hasn’t been upgraded to 6.5 if you want to ensure PythonCE will run, as PythonCE has been known to fail on *some* 6.5 releases—but not all, so if you *do* accidentally acquire a 6.5 phone then you can still try installing PythonCE as it *might* work anyway; in 2019 a TP2 I’d been using for a while suddenly stopped responding to its touch screen, meaning I couldn’t unlock it to retrieve messages received since my last SD-card backup, but I was able to revive it by prying off the top layer of the display—the one with the black border and “htc” logo—with a small flat-head screwdriver starting to the right of the ‘hangup’ button; usual disclaimers apply if you try this, but in my case it worked for 10 days and then an accidental 30cm drop took out most of the pixels)
* "Sony Ericsson Xperia X1" "HTC Kovsky" "HTC Venus" (again beware of 6.5 upgrades)
**If you don’t mind WM 6.5** (see above re PythonCE), you could also try:
* "LG GW820 eXpo"
* Sony Ericsson Xperia X2
* "LG Fathom VS750" (takes Mini-SIM)

## Non-QWERTY phones with larger screens

If you need to find a WM phone and you **don’t** need QWERTY or compatibility with eSpeak etc, but need a larger screen, try searching for "HTC Touch HD" "HTC Max 4G" "HTC HD2" "Garmin-Asus M10" "Acer F900" "Samsung Omnia II"—these are WM6.1+ phones with screens from 3.5 to 4.3 inches and without potentially-‘dodgy’ sliding mechanisms. Do check the software you’ll use works on 6.1+ though. Some old 2003SE phones also have 3.5in screens: "HTC Alpine" "O2 Xda III" "O2 Xda IIs" "Orange SPV M2000" "Orange SPV M2500" "Qtek 9090" "Siemens SX66" "T-Mobile MDA III" "i-mate PDA2k"

This data is* for pointers only; I can’t guarantee it’s correct or that these phones will suit your needs. Always check what you are actually getting.

(* I believe the word “data” can now be used as an **un**countable “mass” noun like “water” or “milk”, not just the countable plural of “datum”.)

## Windows Mobile 6.1 setup notes

(see also list of vaguely-usable old Windows Mobile phones)
* Disable 6.1 threaded-SMS (which takes up too much screen real-estate with copyself messages) and restore the simpler 6.0 approach: edit the registry under HKCU / Software / Microsoft / Inbox / Settings / (possibly OEM) SMSInboxThreadingDisabled DWORD 1 + reboot. (There’s also a SystemFontPercent value, but it doesn’t seem to honour changes.)
  * Some WM6.5 phones also ship with “HTC Messaging” which has trouble displaying large fonts (or Chinese etc, even when a suitable font is installed on the device): this requires a patch to disable: install NETCFv35.wm.armv4i.cab, restart, check it’s enabled in HKLM / Software / Microsoft / .NETCompactFramework, restart, install Zenyee_Disable_HTC_Messaging_1.2.cab, restart.
  * **Beware** this patch seems to have a **race condition** on startup: if you have a *lot* of messages stored, and you restart your phone while the Messaging application is hung, and the startup is being unusually slow, and you attempt to re-launch Messaging before the patch’s startup script has finished running, then you can lose *all* your SMS messages (since your last backup) and your email accounts.
  * Even with the patch, SMS will be omitted from the “Today” screen count if you’re using the “Messaging” item, but if you’re used to using that item as a shortcut to messaging, note that on WM6.5 you’ll need to manually organise the Start Menu anyway: the top-level shortcuts are gone, so the only way to reduce clutter from less frequently-used programs is to move them to a subdirectory, and while you’re at this you might as well remove HTC Messaging and leave “Email” in a prominent place for both tasks. You’ll then need to address the threaded-SMS issue above (at least this isn’t an issue if you *don’t* disable HTC Messaging, but that’s small consolation if HTC Messaging has font problems).
  * If customising the WM6.5 start menu, don’t be tempted to copy the resulting “Start Menu” or “Programs” folders as-is to a new device: doing so can render the start menu empty on boot (meaning you’ll have to look up how to hard-reset your phone using only the hardware buttons). The *contents* of the Programs folder can be copied.
* After installing the Chinese font, on some devices you also need to set HKLM / Software / HTC / HTCMenus / FontFace to MS Song and restart
* **Microphone sometimes mutes during speakerphone calls**: some versions of the Touch Pro 2 (and possibly others) do this; to avoid it, set “Reduce noise in phone calls” to “Never” in Settings / Personal / Phone / Advanced, and in the registry set HKCU / ControlPanel / Phone / Sleep to 0. Otherwise try toggling Speakerphone off and on again when the other party indicates your microphone has muted. If the problem then returns much later, try rebooting the phone at that time.
* **Problems playing MP3 files on SD card**: Use GSPlayer (it has better buffering). TCPMP crashes on 6.5.
* **Disable the “connect to a Windows PC for updates” nag** that’s present on some HTC WM6.5 phones (the update process wouldn’t work nowadays even if you *did* have a Windows PC): set HKLM / Software / HTC / HTCSettings_Improvement / DisableWindowsUpdate to 1
* Internet Explorer on 6.5: you might want this [Python script to index the “Favourites” bookmarks](wm65favs.py)
* Opera Mini 5.1 (2010): contains CSS rendering bugs that can result in excessive spacing. Try turning on “Mobile View” in Settings (among other things, this sets the CSS @media type to handheld instead of screen; version 15 on Android etc calls it “Data savings / Single column view”). In 2016 Opera started inserting advertising links above pages in Mini, giving the *false* impression that the site itself is involved in third-party advertising when it *isn’t*. Mid-2017’s ‘interstitial’ advertising wasn’t much better: it gives the false impression that a site *linked* you to an advertisement when it didn’t. If you *must* continue to use Opera Mini despite this unethical behaviour, please try not to judge the sites you visit by the advertising that Opera sometimes adds without their consent.
* **Contact photographs** (in case you want to copy some from IM or similar):
  * In WM6.5 high-DPI (480x800) phones, Album’s “set as contact icon” option appears to require a picture of size **270 × 270** (but saves as 268 × 268). Smaller pictures can be scaled up, but larger pictures can only be cropped, so any scaling down must be done before the picture is loaded onto the phone. (If the picture shows rotated when the device is in Portrait orientation, try putting the device into Landscape orientation before using this function.)
  * Older WM phones usually use size 72 or 144, although they will display other sizes in contacts imported from MMS.
* **Phone unlocking itself**: Some 6.1 phones can unlock themselves due to spurious triggering of the “keyboard slide” sensor by magnetic fields, dust etc. An obvious workaround is to set a 4-digit PIN in Settings / Lock, but you might prefer to set HKLM / HARDWARE / DEVICEMAP / KEYBD / SlideWakeup to 0 and restart. This setting is a misnomer: the phone still “wakes” but does not automatically unlock. It can still be unlocked by screen rubs in a pocket, so if people still tell you your phone has been calling them from your pocket, you may have no option but to set a PIN, even though doing so gives very little added security and greatly reduces convenience (especially if you want to put incoming calls into ‘speakerphone’ mode for SAR reduction, as this will now require *seven* taps, during which time you might not be able to hear the caller).
* **High CPU usage, battery drain and missed keyboard/screen events**—first thing to check for is an **improperly-fitted screen protector** that could be “confusing” the touch-screen’s scanning circuitry. Removing this might not *completely* solve the problem however.
  * **Faulty or missing direction pads** can sometimes be worked around by using a combination of the touchscreen and the up/down slider on the side of the device.
  * Some Task Manager programs can interfere with the ability of the hardware ‘softkeys’ on some 6.1 devices to pop up the ‘softkey’ menus. This change takes effect until the next reboot, although softkey screen taps still work in the meantime. (These task managers might still be useful for checking for runaway processes, but will need to reboot after to get softkeys back)
* WM5torage on 6.1 is likely to need ‘disable RNDIS on activate’ (the check mark might not show; try registry HKLM / Drivers / USB / FunctionDrivers / WM5torage_Class / Tbs_RNDIS = 0). Use WM5torage or equivalent if the phone does not ship with working “USB disk” software of its own.
* Bluetooth problems: try switching on “Receive all incoming beams” under Beam. (This is no longer to do with IR as it might have been in early models, and leaving it off can lead other devices to give misleading error messages like “another application is transferring data with the device and it may not accept additional connections”, so it may be best to leave Beam on and just use Comm Manager to switch off the entire Bluetooth stack when not in use.) If Beam is not available, try Bluetooth / Advanced / File Transfer / Allow incoming file transfer connections.
  * Some WM6.x phones have an IR facial proximity sensor, which can be seen on IR cameras as a small strobing light. This runs continuously and is not related to or affected by Beam settings.
* Home screen key reassignment (also on WM6.0 and WM6.5): registry / HKCU / Software / Microsoft / {Today|Home} / Keys / {112|113} set default to key’s label and set Open to e.g. \Windows\CommManager to launch Comms Manager when that key is pressed (you can also set it to a shortcut, e.g. \Windows\Start Menu\Programs\Contacts.lnk).
* On WM6.5 the “Phone” settings are now hidden in Comm Manager: tap to the left of the toggle switch to access them. Disabling 3G is in the “Band” setting.
* Wenlin—this *is* possible to run on 6.1, but you have to compile it with MSVC 2005 or 2008 (not cegcc, and not newer versions of MSVC which have dropped support for Windows Mobile). I was able to compile it on an old MSVC-2008 “non-commercial” installation, but Wenlin probably can’t distribute the resulting binary as they’re commercial.
* Gradint—still works on 6.1+ but without GUI and without eSpeak (you can use synth-noTk.py to demonstrate some syllables); if there are errors about NoneType unicode coerce, try reinstall. (eSpeak and Tk files can be deleted)
* My [SBminutes](SBminutes.py) call time checker should still work if you don’t want to use wm6minutecount (anyway wm6minutecount can have trouble reading logs on 6.5 and is not quite as configurable as SBMinutes)
* PocketPuTTY: on some 6.1 phones this fails to open connections unless a data connection has already been activated (by the Web browser or whatever), and beware timeouts; might pop up a question about server keys *behind* the main window (going back to the Today screen should reveal it); use terminal-type string putty if server supports it (e.g. Debian ncurses-term package), otherwise try vt220 (the default xterm can have arrow-keys issues in some programs)
* You might want to turn on the TCP/IP compression options under Settings / Connections / Connections / Manage / Edit / Next / Next / Advanced.
* SMS validity period: This appears to be fixed at “network default” (typically 3 days), with no way to change it, perhaps because Microsoft’s own developer documentation is vague. For the fourth parameter of its SmsSendMessage function, they said “This is not interpreted as a normal SYSTEMTIME structure”, but did not explicitly say how it *is* interpreted (other than citing the GSM 03.40 specification, which describes a 7-byte BCD-like expiry format, but that doesn’t tell us which of SYSTEMTIME’s 16 bytes we have to set to make Microsoft’s library map onto it), so I expect application developers leave this parameter alone. There does not appear to be any standard way of asking the network to change its default either.
  * [send-sms](send-sms.py) and [wmSMSsend](wmSMSsend.py) are two versions of a library function to send SMS messages from Python (I'm not sure how I ended up with two versions of this)
* DPI issues: in the registry under HKLM / Drivers / Display / GPE there is LogicalPixelsX and LogicalPixelsY, which are normally set to 96 (decimal) on QVGA (240x320) and 192 on VGA (480x640) and seem to represent 3/4 of the device’s “real” DPI (128 or 256); these figures would be correct if the screen were 3⅛in at 3:4 aspect (3.64in at 3:5) and larger is a bonus, but 2.9/2.8in screens shrink it. If your favourite application’s largest font setting is “20 points” then it’ll be more like 18.4pt on a TyTN II or 17.9pt on a Touch Pro (the 3% shrink when moving from a TyTN to a Touch *is* noticeable, even though spec lists often approximate them to the same screen size). You *could* try increasing those registry values (e.g. from 192 to 198 or even 214) and reboot, but doing this can cause display problems such as:
  * Irregular-width bars in battery and signal gauges
  * Disappearing but still functional Start and Window-dismiss buttons
  * File Explorer displays incorrect folder icons
  * File Explorer is missing its drop-down navigation (but can still navigate with soft-keys)
  * Settings has some missing icons (but text is still there)
  * Intermittent “No program memory available” messages when memory is nowhere near full (it’s probably a general failure handler misfiring)
  * Comms Manager displays very small and is navigable only by keyboard
  * Contact details view is blank in both portrait and landscape modes

the latter issue being a probable show-stopper if you want to use the phone function.

## Windows Mobile email setup

These notes are old: I stopped running this configuration in April 2019, so it was *not* tested on the newer Raspbian 10 which was released later that year, nor any version of Raspberry Pi OS from 2020+.

This section has some notes on running old Windows Mobile phones (dating from 2003 to 2009/10) with modern email systems.

### SSL encryption problem with built-in client

Email is no longer likely to work on Windows Mobile’s built-in client because its SSL encryption options are now considered insecure and are usually disabled server-side. Cambridge’s server switched off RC4 in January 2016 and GMail’s in June, by which time Yahoo, Hotmail and iCloud had also stopped working. AOL still worked until November 2017 if you didn’t mind connecting to their *non-*SSL server—I suggested using ImapFix’s secondary_is_insecure setting to remove addresses from the plaintext copy—but then they shut this down and their SSL server didn’t work with WM.

Personally I didn’t think the known RC4 attacks on Web traffic are also feasible on IMAP unless poll frequency is set way too high, so I think there’s a valid argument for re-enabling older ciphers *for email only* so as to allow old WM phones to connect. But the sysadmins were worried I might be wrong, and eventually GNU/Linux distributions started disabling these ciphers at the SSL *library* level (e.g. Debian bug #875423), so sysadmins can’t now turn them back on even if they *want* to, unless they recompile their system libraries from source or risk running outdated distributions. This also means you can’t just set up Dovecot on a Raspberry Pi or something and expect a quick ssl_cipher_list = ALL to solve your problem: you’d be left with log entries that say SSL routines:tls_process_client_hello:version too low, and the WM device will probably say “A secure sockets layer (SSL) connection could not be established” when “require SSL” is turned on, or perpetually re-request your password when “require SSL” is turned off (but its exact message may vary).

You *can* still run on a home server what used to be possible with AOL: use IMAP *without* SSL, and ImapFix’s secondary_is_insecure setting to remove addresses from the plaintext copy of your inbox. To do this with dovecot-imapd you’ll need to set `disable_plaintext_auth = no` in `/etc/dovecot/conf.d/10-auth.conf` and I **strongly** recommend changing the `passdb` section in `/etc/dovecot/conf.d/auth-system.conf.ext` so it uses `driver = passwd-file` instead of `driver = pam`, with args = a path to some alternate passwd file you set up specially for email (use `echo $(whoami):$(doveadm pw -s CRYPT) > passwd)`, so you don’t have to send your system login password in the clear whenever you check your email. You might also want to edit `10-mail.conf` commenting out mbox and uncommenting `maildir` options to reduce the disk writes needed for small incremental updates. (With some Dovecot versions you also need to ensure the mailbox is *not* on a fusecompress mount.) Then do `/etc/init.d/dovecot restart`, open port 143 on your firewall (or set up a script to open it temporarily when requested in some way), and use ImapFix to synchronise your mail there.

For *sending* email from the phone, you’ll also need an SMTP server it can connect to—and this will have the same issues with SSL libraries. I wouldn’t recommend connecting to *SMTP* with a plaintext password—there’s a *big* difference between “sniffing your password to read an inbox from which the most sensitive information has already been redacted” and “sniffing your password to send emails *from* your server”, especially if you have scripts that say emails provably from that server can run certain commands. But the lack of SMTP is not a *major* issue, because it’s hard to type much on a small WM keyboard anyway, and it’s rare that urgent matters can’t be dealt with by SMS or voice call until you get to a proper keyboard.

### Other notes on built-in client

If you have a server to which the phone *can* connect:
* Messages must be in Unicode; try ImapFix (to fetch folders other than the inbox, use Tools / Manage folders / Select folders for synchronisation
* If you have SMTP but sending results in “message(s) could not be sent” and the recipient gets a truncated version, try adding more newlines and/or sending attachments separately: it’s a bug in WM6.1 for which I haven’t found a reliable workaround
* WM6.5, unlike earlier versions, refuses to open message/rfc822 attachments in IMAP accounts, so ImapFix’s max_size_of_first_part option can no longer be used to expand the range of choices for “Message download limit” in “Download Size Settings” (which is stored in the system `\cemail.vol` file that you can’t access with Python etc, so it’s not easy to expand the GUI choices); you can still set `max_size_of_first_part` as a protection, but you won’t then have the option of viewing it anyway from WM6.5’s Messaging.
* “Insert Voice note” records WAV as PCM or GSM (set format in Start/Settings/Input/Options); if you accidentally Send before stopping, recording will **not** be attached, but it’ll still be around as a hidden file in My Documents which can be attached to another email via Insert File (named ~VRec_0.wav etc) or deleted from Python

### Third-party clients

You could try (the old WM version of) profimail.cab which supports more SSL options than the built-in client, but even this began to fail to connect to Cambridge servers in December 2016 (reporting error 10022, which is Microsoft speak for an invalid parameter somewhere). If it *does* connect to your server:
* Be sure to set “Use system font” if you’ve installed Chinese fonts or whatever, since ProfiMail’s built-in font is English-only. Using the system font also increases the size slightly.
* Pressing Menu from a new-message body causes a display bug that involves the menu shifting vertically after about a second, placing the “Send” option where the “Edit” option was. To avoid premature sending, wait for this vertical shift to happen before deciding where to tap.
* I haven’t tested ProfiMail on the non-touchscreen models (WM6-Smartphone).

Otherwise you might have to use PocketPUTTY, which is not suitable for offline use (although you can long-press to paste in a pre-written email when signal becomes available). It won’t work on non-touchscreen models although a more-awkward SSH “midlet” does.

Usual disclaimers apply—all the above is at your own risk.

## Copyright and Trademarks
All material © Silas S. Brown unless otherwise stated.
Android is a trademark of Google LLC.
Bluetooth is a registered trademark held by the Bluetooth Special Interest Group.
Debian is a trademark owned by Software in the Public Interest, Inc.
Ericsson is a trademark or registered trademark of Telefonaktiebolaget LM Ericsson.
Garmin is a trademark of Garmin Ltd. or its subsidiaries, registered in the USA and other countries.
HTC and Touch are trademarks of HTC Corporation.
Linux is the registered trademark of Linus Torvalds in the U.S. and other countries.
Microsoft is a registered trademark of Microsoft Corp.
MP3 is a trademark that was registered in Europe to Hypermedia GmbH Webcasting but I was unable to confirm its current holder.
Python is a trademark of the Python Software Foundation.
Raspberry Pi is a trademark of the Raspberry Pi Foundation.
Samsung is a registered trademark of Samsung.
Siemens is a trademark of Siemens Aktiengesellschaft.
Sony Ericsson is probably a trademark of Sony Ericsson Mobile Communications AB.
Toshiba is a trademark of Tokyo Shibaura Denki Kabushiki Kaisha, also called Kabushiki Kaisha Toshiba.
Unicode is a registered trademark of Unicode, Inc. in the United States and other countries.
Vodafone is a trademark of Vodafone Group Plc.
Wenlin is a trademark of Wenlin Institute, Inc. SPC.
Wi-Fi is a trademark of the Wi-Fi Alliance.
Windows is a registered trademark of Microsoft Corp.
Xperia is a trademark of Sony Ericsson Mobile Communications AB.
Any other trademarks I mentioned without realising are trademarks of their respective holders.

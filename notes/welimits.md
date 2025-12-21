
from https://ssb22.user.srcf.net/s60/welimits.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/s60/welimits.html) just in case)

# WeChat (Weixin) limitations


Many Chinese people now prefer to manage their contacts using a proprietary mobile messaging and social networking application called [WeChat](wechat.md) (微信 Wēixìn). This page notes some limits I found when sending documents etc on this platform.

## Image and video limits

If pasting a scanned document into a WeChat conversation as an image, the size limit is 300KiB, after which the image is shown only as a blurred preview unless the recipient presses a small button they might not notice. So it’s best to stay below 300KiB.
* Beware a **lower limit** of about **128K** applies if you do any of the following on WeChat’s *Android* app:
  * Forward the image from one conversation to another (or from the Favourites list to a conversation) via the “Send to Chat” option;
  * Add the image to a conversation via “+” and “Album”;
  * Send the image from a file manager to WeChat and choose a chat.

In each case the image can appear clear on your side but blurred for the other party. To work around this on Android, first add the image to Favourites (either by sending from a file manager to WeChat Favourites, or by adding from a conversation where you already have a clear copy), then be in the new chat and press “+” to add *from* Favourites.
  * The iOS version of WeChat does not appear to be affected by this lower limit—it can forward images of the full 300KiB from one chat to another without degrading them.
  * But the Mac OS X version—at least version 1.2.2.1 on OS 10.7—has been known to apply a lower limit if you drag an image file from the desktop into a conversation.
* An ordered sequence of up to 30 images may be placed in a WeChat “Note”, created by tapping the “+” icon at top right of “Me / Favourites” screen (large images are automatically compressed to JPEGs under 300KiB). This “Note” approach can be useful for things like showing how to get to a place if they can’t read a map; placing the images in a “Note” reduces the chance of their being received out of sequence or with some missing. However it has been known for “Note” images to go missing when WeChat’s history is moved from one device to another:
  * in 2019, using WeChat “Cloud Backup” to restore chat history when moving to a new device resulted in “Note” images and recordings being replaced by placeholders, although non-Note images and audio were kept;
  * in 2022, the same thing happened when using backup and restore via WeChat for Windows 3.2 (XP/Vista version) and 3.5 (Win7+ version) both running on WINE 7 under Fedora 35, having failed to connect WeChat 3.3 for Mac under macOS 12.1; WINE 7 generally worked for backups apart from minor issues like dialogues popping up behind the main window which then needed to be moved out of the way
  * If the receiver stores a Note as a “Favourite” then *that* copy is kept on the server and eventually downloaded to any new device
  * WeChat enforced a maximum of one phone logged into the account at a time, but did not delete history when forcing a logout: you could log back in and still see the old Notes etc on the old device. (KakaoTalk on the other hand completely wipes history on your old device, so if you didn’t back it up before migration then you won’t be able to get it back.)
* WeChat normally uses the JPEG format, but also accepts PNG (useful for screenshots etc). If you give it <300KiB PNG and later save/export, WeChat will use a `.jpg` extension but it will still be your PNG file.

I have a separate page for technical information on [creating narrow-column screenshots](https://ssb22.user.srcf.net/adjuster/screenshot.html).

For inline **videos**:
* In older versions of WeChat, the time limit is just under 5 minutes (4:59 is accepted but 5:00 is “Video length too long”), the file size limit is just under 14MiB (so if using the full 4:59, the bitrate limit is about 384k, e.g. 256k video + 128k audio), and the *mobile* application should be used to introduce these into the WeChat network (i.e. by ‘Share’ or ‘Send’ from another mobile application)—older versions of the *desktop* application send videos as “files” that need extra action to view. Attempts to send videos larger than 14MiB on the older mobile application got the error “unable to import”, although the “say something” caption (if any) is sent anyway.
* WeChat 8+ can handle longer videos inline, and these can be sent via version ~3.7+ of the desktop client, which recompresses the video to about 70kbps.

The error “Unable to share this video due to unspported format” (e.g. if trying to post a short video to Moments) probably means you need to [recode to h264](video.md).

By comparison, [WhatsApp](whatsapp.md) usually compresses inline images to around 250k (with no option to see full size) and limits video to 16MiB (as of 2017; best sent from the mobile application), and Telegram Messenger scales down to max 1280 pixels per dimension and sends the result as an 87%-quality JPEG (unless uploaded as a file) but has a much more generous video limit.

## Audio recordings

MP3 files are sent as “files” no matter what, so the desktop application can be used (“drag and drop”); if using the mobile application, shared files (unlike videos) need to be added to “WeChat Favourites” before they can reliably be sent to a chat. Once in Favourites, the option to “forward” from the “Favourites” screen is unreliable; it seems better to go into the chat itself and press the + button, scroll to the Favourites option, and find the MP3 that way. Ensure it is uploaded before deleting from Favourites. After you delete it from Favourites, you will get the message “This file is no longer available” when you try to open it in the chat, but the other party should still be able to access it for a few days.

## Cache bloat and hardware requirements

The [Android](android.md) version of WeChat can build up multiple gigabytes in a directory with a 32 hex-digit name under `/sdcard/tencent/MicroMsg`. These files are *not* the chat logs—they’re just cache (and I haven’t found an option to clear it; Android’s built-in cache-clearing option does not affect this).
* Removing the `video` subdirectory results in all videos in chat history (including 10-second “sights”) being replaced by placeholders; you might need to do this to reclaim space after you’ve sent a video clip to many contacts. Videos saved in “favourites” are not affected.
* At least the `avatar`, `emoji`, `sfs` and `sns` directories are *always* safe to delete without losing *any* history, pictures, files or “favourites”.
* One level above the directory with the long name, there is also a `Download` directory containing files sent or received in chats: you might wish to clean this up from time to time as well.

If a Chinese friend asks you to “fix” their WeChat on an older phone with internal storage measured in megabytes (such as the ChinaMobile-branded ZTE U809, which runs a version of Android 4.2 with only 177M of usable internal storage), beware this might no longer be possible because WeChat tends to insist on updating to its latest version, which now requires Android 5+ (partly because Tencent’s own back-end servers now use HTTPS certificates not recognised by Android 4) and hundreds of megabytes of internal storage. Installing a very old smaller version of the APK will **not** work. The quickest solution could be to ask if they have a tablet or something to run it on instead: in one case I wasted 2½ hours trying ‘hacks’ only to find the person had already installed it on a tablet and didn’t want it on their old phone that badly.

## Length limits

If you rename your contacts, the new names are limited to 29 Unicode characters, and you are given a “too long” message if you try to set anything longer—so if your Chinese character skills are limited you can’t write yourself *too* much of a reminder of how you met a person etc (unless you develop a terse shorthand code). Before the limit of 29 characters was implemented, there used to be a limit of 50 characters and the name would be truncated without warning; before *that* truncation was implemented, there used to be no practical limit. LINE’s limit is only 20 characters, but at least there’s a count (LINE also has [other problems](line.md)).

Comments on WeChat “official account” posts are limited to 600 characters—there is no warning until you try to post, and there is no character-count indicator, so if you run into problems there you may have to use a different editor *with* character count and paste in the result (unless you want to go back to 1960s/70s programming where you had to manually count out the number of characters you typed into a Hollerith constant!)

Chinese programmers might assume “one character” carries as much information as a Chinese character, so they may not realise how easy it is for English users to reach their limits. But the American developers of WhatsApp inexplicably limited group-chat titles to a mere 25 characters! (At least *that* limit is made obvious as you type.)

Disclaimer: The notes on this page are provided in the hope that they are useful, but they are not official instructions and may contain mistakes. Your use of them is at your own risk.

Copyright and Trademarks:
All material © Silas S. Brown unless otherwise stated.
Android is a trademark of Google LLC.
Mac is a trademark of Apple Inc.
MP3 is a trademark that was registered in Europe to Hypermedia GmbH Webcasting but I was unable to confirm its current holder.
Telegram is a trademark of Telegram Messenger LLP.
Unicode is a registered trademark of Unicode, Inc. in the United States and other countries.
WeChat is a trademark of Tencent Holdings Limited.
WhatsApp is a trademark of WhatsApp Inc., registered in the U.S. and other countries.
Windows is a registered trademark of Microsoft Corp.
Any other [trademarks](https://ssb22.user.srcf.net/trademarks.html) I mentioned without realising are trademarks of their respective holders.

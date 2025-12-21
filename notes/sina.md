
from https://ssb22.user.srcf.net/s60/sina.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/s60/sina.html) just in case)

# Using weibo.com’s S60 client

These notes were written some time ago and might or might not apply to the latest version. I cannot re-test because my S60 device broke down; moreover in November 2015 [my Weibo account was stolen](stolen.md), and the Chinese professor who had set it up for me felt Weibo is no longer relevant. [Weixin/WeChat](wechat.md) seemed to replace it for many.

Here are some notes on using weibo.com’s (previously t.sina.com.cn’s) S60 client on English phones which cannot display Chinese characters.

(You could get your phone reflashed with a Chinese version, but you might not want to do that for several reasons e.g. it would erase your mobile network’s settings. Or you could find a trial version of “Psiloc Crystal Chinese S60”, but it seems Psiloc are no longer around to extend its usage period, and beware that if you install it to storage card you won’t be able to use the USB Mass Storage function while Psiloc is on. The Nokia text-to-speech download had a Mandarin language pack for reading incoming SMS messages but it didn’t help in applications.)

## Setup
1. Download (I previously provided links here, but they’ve changed and I think it’s now available only from old-version caching services; I don’t know which are genuine and if the old version even still works with the server)
   * There’s also a [Windows Mobile](../old-wm6/README.md) version (WM5+, last updated 2011), but it cannot be navigated without a touchscreen, and fails to make connections on some 6.1+ phones. This version has English menus, but seems to offer no way of putting other people’s posts onto the clipboard (you can still paste text into new posts).
   * Or you could try the low-bandwidth “mobile” version on weibo **.cn** (not .com): first link is log in, then first button under text entry box is send and 3rd is attach picture.
2. Put the .sis or .sisx file onto your S60 mobile and install it
3. **If you want the application to be silent** then you can remove its sound data. Install to the SD card (not to phone memory), and inspect the SD card on a computer (using the phone’s “USB mass storage” or a card reader) and you should be able to find `Private/*/apps/msgcome.mp3` (correct in v2.2.0) where `*` is a random directory name like `200294b6`. This MP3 file is played loudly when new messages arrive, even if the phone is on silent. But you *can* customise or delete it by accessing the SD card in this way.
4. After launching the application from the menu for the first time, you will need to type your weibo email and password into the small boxes and press the left softkey (not the button on the form; that’s a sign-up button). On subsequent launches you won’t have to do this.

## Left softkey options

This is for version 2.2.0 Beta.
1. Refresh (*)
2. Post new message (0): you can type using T9; 1st on-screen button inserts smileys, 2nd resets the phone (!), 3rd selects a picture from your image gallery. Left softkey confirms the post, right softkey cancels. You can also press the phone’s camera button to capture a picture (remember to hold it landscape), and some versions also intercept the phone’s camera application so that taking a picture at any time results in a prompt asking if you want to launch weibo and post this picture.
3. Search (#)
4. ? (9)
5. Forget your login info (you’ll have to log in again)
6. Settings (none of which are readable without hanzi fonts)
7. More:
   1. Draft an SMS message to invite someone to weibo
   2. Post your phone’s OS version
   3. Show memory info
   4. Show some other info
   5. Show client version info
   6. ? (runs a query and pops up a message that can’t be read)
8. Quit

## Options that appear when you press OK on a post

On other people’s posts:
1. Forward the message to your own blog (left softkey = OK, right = cancel)
2. Write a comment (same softkeys)
3. Cancel (this middle option is highlighted by default)
4. *Maybe* View picture and/or View link: these options, each with 2 hanzi, appear just to the right of the middle option **if and only if** there is a picture or a link respectively. The options appearing under the picture include show local path; cancel; view at full zoom (may require panning). As well as choosing from these options, you can also use the Up and Down navigation keys to change the picture’s size.
5. View comments for selected post (3 hanzi)
6. Forward the selected post as a text (SMS) message (which incidentally gives a way to get it into the S60’s clipboard) (2 hanzi)
7. *Maybe* remove post from the @me list if this is the @me list
8. View post author’s profile (6 hanzi)
9. *Maybe* view profile of original author if this is a forwarded post (4 hanzi; this option appears only on forwarded posts)
10. ? (just pops up a message)
11. ? (gives a comment box that apparently does nothing)

On your own posts:
1. Forward the message
2. Write a comment
3. Cancel (default)
4. *Maybe* View picture (2 hanzi)
5. View comments (3 hanzi)
6. Forward as SMS
7. Delete post (2 hanzi; NB there is no confirmation!)
8. ? (just pops up a message)
9. ? (gives a comment box that apparently does nothing)

On a comment in the “comments to me” tab:
1. Delete (no confirmation!)
2. Reply
3. Cancel (default)
4. View commenter’s profile
5. View own profile

On a comment in the “view comments for this post” screen:
1. Reply
2. Cancel (default)
3. View author’s profile

(Note you cannot delete your own comments, even if they are to yourself, because these don’t appear in the “comments to me” view which is the only one that has the Delete option. However, deleting a post deletes all comments.)

## Tabs on the main screen
1. Home page (all microblogs you’re following)
2. @me (posts that mention your user ID)
3. comments (left by others on your posts)
4. private messages
5. misc. (including your profile, popular people, etc).

Right soft key = refresh

## Tabs on a “view author’s profile” screen
1. main
2. all blog posts
3. people this author follows
4. people following this author (“fans”)
5. ?

Right soft key = pop up a menu, the top item of which is to leave this screen and the other options go to other people’s profiles

## Older client

Some older versions of the client have a different interface: after installation, use the *second* option to log in with your weibo email and password, then the right softkey refreshes the current view, and the left softkey has options including:

1st option = post message (can add a picture by using the phone’s camera key; T9 etc is not available), 4th to make a draft invite SMS, 8th to quit.

“OK” button selects a post to read, then 1st option adds a comment, 2nd views comments, last (with 6 hanzi) goes to the poster’s blog.

Tabs along the top are: homepage (all watchlisted blogs), @me (messages forwarded to you etc), comments, ?, ppl you’re watching, fans, my blog, ?.

There’s a background thread consuming RAM even when the app’s not running, and this starts automatically on phone startup. If you installed it to the memory card, it will tie up the memory card so you can’t use it as a USB Mass Storage device. *Sometimes* physically removing the memory card will shut down this thread, but the only way to make really sure is to uninstall the weibo application. (This does not seem to be a problem with the newer version.)

Disclaimer: The notes on this page are provided in the hope that they are useful, but they are not official instructions and may contain mistakes. Your use of them is at your own risk.

Copyright and Trademarks:
All material © Silas S. Brown unless otherwise stated.
MP3 is a trademark that was registered in Europe to Hypermedia GmbH Webcasting but I was unable to confirm its current holder.
WeChat is a trademark of Tencent Holdings Limited.
Weibo is a trademark of Sina.Com Technology (China) Co. Ltd.
Windows is a registered trademark of Microsoft Corp.
Any other [trademarks](https://ssb22.user.srcf.net/trademarks.html) I mentioned without realising are trademarks of their respective holders.

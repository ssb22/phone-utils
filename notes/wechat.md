
from https://ssb22.user.srcf.net/s60/wechat.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/s60/wechat.html) just in case)

# Understanding rejection on WeChat (Weixin)

(See also [audio/video etc limitations](welimits.md) and [URL encoder for mobile chat](https://ssb22.user.srcf.net/s60/chat.html).)

Many Chinese people now prefer to manage their contacts using a proprietary mobile messaging and social networking application called WeChat (微信 Wēixìn). If you frequently meet them, you might be tempted to set up your own WeChat ID for their convenience. This can however lead to some quite ephemeral contact sharing (e.g. someone you met on a bus adds you but later deletes you). Since I found very little English documentation about how this manifests itself, I experimentally confirmed the following in 2015:

Other party’s action - Result on your side

Delete conversation - No immediate effect. If you send further messages, a new conversation is started on the other device, but it still looks like one continuous conversation on yours.

Clear chat history - Similar to “Delete conversation” above

Delete and Leave (in a group chat) - Deletes *their* copy of the chat history and removes them from the group. The group continues to exist, and is not notified of their departure unless other members actively re-read the membership list. (WeChat version 8 added an option to *really* shut down a group; earlier versions required the administrator to remove each member. Even then, each member continues to keep a copy of the group chat history for the time they were a member, until they delete it themselves or reinstall etc, although at least some versions of WeChat will delete their copy of the history if they accept an invitation to *re-join* the group. For larger groups there is also a limit to the number of members displayed in “Chat info”, leading to some members being ‘invisible’ unless you tap the words “All members” below the list, the Chinese of which is 查看全部群成员 which is more obviously a ‘command’ than the English in WeChat Version 7, which was clarified to “View All Members” in Version 8.)

Block (加入 jiārù 黑名单 hēimíngdān) - No immediate effect unless you check their Album (Moments), which behaves as if they’d selected “Delete contact” (below). But if you send further messages, you are told “The message is successfully sent but rejected by the receiver” and the other party is told nothing. (The word “receiver” here evidently means the receiving *account*, not the receiving *device*—the “rejected” text still appears even if the other party’s phone is powered off at the time.) They can still send *you* messages. Note also that if you send a “broadcast message” (群發, for some reason located under Me / Settings / General / Features in WeChat 7 and Me / Settings / General / Tools in WeChat 8), you are **not** told which recipients reject it; you must send *individual* messages to be told.

Delete contact (删除 shānchú) - No immediate effect unless you check their Album (Moments), which will be blank if they’ve turned off “Public Moments” in the privacy settings (but this could also mean they’ve seleted “Don’t share my moments” with you, or simply haven’t ever posted anything for non-Tagged contacts); if they have “Public Moments” turned on then you will see the message “Only 10 posts of this user are visible” (the Chinese version of this message begins “non good-friend” which was lost in translation prior to 2019—the English version has since been updated to “Only the last 10 Moments are shown because you aren’t friends on WeChat”), and the options to Like or comment on the posts are not displayed (but some versions of WeChat still let you “Like” the album “cover”). Not to be confused with the message “Only 3 days of Moments are viewable” (which happens if they set Settings / Privacy / Set a time limit for Moments viewable by others)—*that* one applies whether or not you’ve been deleted, and still lets you comment if not.

If they deleted you and you try to send further messages outside the Album, you are automatically put back through the process of adding yourself to their contacts: if they’ve turned on “friend confirmation”, you’ll see “(Person) has requested friend verification. Please send a friend request to chat” with a link to do it; otherwise your message goes through immediately and they are given the message along with the option to add you. Previous conversations are deleted from their side but not from yours. “Broadcast messages” are silently dropped as above.

If you attempt to create a group chat via “+” / “New chat” (which lets you select up to 39 people) and select 2 or more: if *none* of the people you select have you in their contacts (or if all the ones who do are blocking you), you get the message “Unable to start group chat” with “hasn’t added you as a friend yet” (you can then press Cancel and review the selection); if *some* have you in their contacts (and are not blocking you) then the group chat *will* be created but you’ll get a message at the top saying which ones were not added. Do not do this just to test though, as anyone who has their account set not to be automatically added to groups will be sent an immediate invitation (some websites claim nobody is notified about a group until you send the first message, but that’s inaccurate). The invitation is automatically declined by anyone who has you as a blocked contact, and you get told about this action, but those who have not blocked you might see an invitation.

Chinese words for Moments:

It may be worth knowing that the Chinese version of “Moments” is, not 片刻 piànkè as the English word might suggest, but 朋友圈 péngyouquān “circle of friends” (sometimes colloquially abbreviated to 票圈 piàoquān because 票 piào has the ‘p’ and the ‘y’ sound). But I’ve seen it used with the measure word 条 tiáo (strip), which suggests at least some users still think of 朋友圈 péngyouquān as referring to *the list of posts* rather than the people to whom they’re attributed.

Block *and* delete contact - Behaves exactly like Delete contact alone, since deleted contacts are also removed from the Blocked List

拉黑 Lā hēi (拉进 lājìn 黑名单 hēimíngdān) - As far as I can tell, these are not actual WeChat options but are colloquial terms for the above ‘block’ or ‘delete’ operations, probably carried over from other software. However I have not tried *every* version on *all* platforms—there might be variation in terminology between WeChat versions.

Report (投诉 tóusù) - In 2021 I submitted a real one as a contact’s account was taken over by someone who used it to send me dirty pictures. I was asked to choose messages to send as evidence; WeChat responded with “Violation confirmed” and “User handled with Temporary Block” and the person was no longer listed on my Chats or Contacts view but was still findable on Search and on Me / Settings / Privacy / Blocked List (so, blocked for me, but also prevented from logging in to WeChat).

Uninstall the WeChat application - No effect. They’re just offline until they reinstall. I don’t know how long it takes for an unused account to expire.

Delete account - Contact is greyed out and marked “Account deleted”; selecting it says “account deleted by other user” and presents a Delete button which, if pressed, also deletes the conversations; otherwise any attempt to send more messages is met with “The other user cannot receive message”

**Spontaneous “Delete contact” is also possible.** This is when WeChat deletes one of your contacts, resulting in the person and all previous chats disappearing without trace, as if you’d deleted it yourself. Since “Delete contact” takes 5 screen taps, it cannot easily be blamed on an overly-sensitive touch-screen, and since I was unable to reproduce it, I can only conclude it’s either a race-condition bug or else a user action available only in the China version of the software and/or to an administrator. (Please don’t ‘gaslight’ me: I *know* that contact existed before it disappeared! On 7th August 2015 a *Shanghai Daily* reporter used the sentence “The woman vanished from Wang’s WeChat contacts afterward”, which might imply a “completely disappear from the other party’s contacts” function somehow being available in China, unless the word “vanish” was here used metaphorically.)

## Error message when adding people

In early 2021 WeChat started to display the Chinese-only error message 请先设置朋友权限 when you try to add a contact. This message was displayed too fast for me to read and it could not be copied: I had to screen-shot it and use OCR to find out what it said—it’s basically “please set friend permissions first” and refers to a new setting at the bottom of the Add screen (you might have to scroll down if you’re in large print on a small device) that lets you choose whether or not to also share your “Moments” with this person. It might have been better if the developers had set it to *focus* those controls when this happens, but at least we now know. (In particular, this message *doesn’t* say the person is refusing your Add request.)

After a few months, sharing Moments seemed to be always set by default, so that message was no longer an issue.

## Emoji warning

In 2020 it was pointed out to me that the standard WeChat “smile” emoji (the one that can be produced by typing `[Smile]` or `[微笑]` in your text, or selecting the closed-mouth smile from the menu) is seen by some as mocking rather than happiness, and it is now safer to use `[Chuckle]` (`[偷笑]`), `[Grin]`, `[Joyful]`, `[Laugh]` or the Unicode emojis `U+1F600`, `U+1F601` or `U+1F604` (I’m not sure where the older `U+263A` fits into this).

A related issue is “stickers” (called “emoji packs” in the Chinese version)—some youngsters have sticker-packs with seizure-inducing strobic flashes. I have contacted Tencent urging them to implement a “disable animations” option and I suggest you do the same (they might notice if more people ask); meanwhile if you have photosensitive epilepsy you’d better stay out of any chat that might include young people, in case in their innocence they post one of those or (even worse) a whole series of them and accidentally give you a seizure. (In 2022 some people also had Chinese New Year greeting stickers that strobed, and sent these to all their contacts, unaware that the flashing can create problems.)

## Don’t bother with “red packets”

If someone tries to send you a “red packet”, the funds they deposited will be returned to them if you don’t open it within 24 hours.

WeChat used to allow non-Chinese accounts to open “red packets” and later forward the balance to other Chinese friends (it could not be spent outside China), but in 2019 they began to require a China bank card for any transaction—and the app takes you through a lengthy “real-name confirmation” process before it even tells you this requirement.

## Commenting on livestream “Channels”

During the pandemic, the “real-name confirmation” process stopped working outside China entirely, plus it was no longer possible to comment on or participate in live-stream videos on Channels without a China bank card, although basic WeChat functionality remained available.

By 2024 it was possible again for “real-name confirmation” to work outside of China by binding a bank card, passport and phone number, although the process to do this was likely to crash or hang, typically needing four to five attempts to succeed and taking up the best part of an hour.

Additionally, the livestream screen layout is such that if Me / Settings / General / Text size is large, commenting will not be possible on most phone devices: it is necessary to restart WeChat at a small text setting and struggle with that if you want to make a comment. On a Samsung S21 with Display / Screen Zoom set to maximum, only the smallest two size settings of WeChat allowed comments to be sent on a livestream. (WeChat’s Landscape mode did not apply to Channels screens.)

## Websites

For a time starting in late 2021, WeChat had a partially-translated message whenever any non-Tencent URL is tapped: “This webpage may not be provided by Weixin/WeChat” with a button 继续访问 that means ‘continue visiting’—that “may not” could be less ambiguously translated *might* not (it’s not a “site blocked” message). These ‘external’ pages are now opened in a browser that lacks the WeChat-specific Share controls, although any pages previously shared in the ‘WeChat link’ format (i.e. without a visible URL) could still be re-shared as such (this is likely a bug to be fixed later). A 2022 update removed the warning message.

## Network effect

WeChat’s dominance in China was perhaps assisted by the company’s good relationship with that country’s network police, with its mobile operators (SIM cards with WeChat-specific data allowances are not unheard of), and with integrated shopping and payment services and “portals” to local facilities. Outside China, WeChat tends to lack these advantages, but many mainland Chinese visitors and immigrants keep using it anyway due to their existing network of contacts, and due to the convenience of WeChat’s automatic contact-exchange facilities. Scanning a QR Code seems to have become the most popular method (this wasn’t introduced to WhatsApp until mid-2020). A WeChat update in mid-2017 prevented the generation of QR codes while offline: if you expect patchy signal coverage, you now have to prepare by taking a screenshot of your QR code while connected. For most of 2017 it seemed these codes needed re-generating every 4 weeks, but in 2018 one of mine still worked after 28 weeks.

The network effect does not appear to be very much diminished by the need for their data to be sent through Chinese servers (which, apart from anything else, can be slow when you’re outside China), nor with the “vanishing contacts” issue or WeChat’s limited functionality on the desktop. At least its sound compression ratio is reasonable, and Version 7 made a [dark mode](https://ssb22.user.srcf.net/css/dark.html) available (although not on the desktop version) and improved the range of font sizes under Settings / General (Version 8 fixed some layout issues this caused on small screens).

Sometimes they’ll accept an alternative installed alongside WeChat for use while they’re in the UK. My current recommendation is Telegram Messenger, which is run by a non-profit, can be set to larger fonts, has a good range of desktop clients, etc. But not everyone even understands what it *means* to install a different application. Some of the older generation I met evidently had it installed by the manufacturer, a shop, or a friend or relative, and don’t know what I mean by “install something else”. Additionally, some older devices (e.g. iOS 4.x) cannot run recent versions of many applications, so it would be necessary to find an old version and somehow ‘side-load’ it, or risk an OS replacement.

## Scams

As with any form of messaging, it’s probably best not to accept an ‘add’ if you don’t know who it is, especially if you actually *visit* an Asian country: con artists have reportedly tricked victims into going to a particular location for a “first meeting in person”, only to be held to ransom by gangsters on arrival (this crime is easier to commit in small countries like Singapore). In June 2016 my WeChat ID (which I had given only to selected Chinese people I met in Cambridge) suddenly received an ‘add’ request claiming to be from Malaysia and not giving me any clue who it was; to give them the benefit of the doubt I wrote “Apa khabar?” but received no reply and the next day eight other anonymous “Malaysians” had tried to add me. I find this highly suspicious. My ID could have been found via brute-force search, most likely of QQ numbers: I had my old QQ number linked to the account, but disabled “find by QQ ID” after this incident because I believe none of my genuine earlier contacts who had my QQ number are still likely to use it to find me. (I later discovered [that QQ number was stolen](stolen.md) so I unlinked it from the WeChat account completely.)

### Malware

On iOS, a pre-6.2.6 version of WeChat was infected by malware due to its developers having accidentally downloaded “XcodeGhost” instead of Xcode. Additionally, we don’t know what Tencent itself does with the information WeChat can read, so it’s probably best to avoid storing things like company-confidential documents on the same device, just in case.

Disclaimer: The notes on this page are provided in the hope that they are useful, but they are not official instructions and may contain mistakes. Your use of them is at your own risk.

Copyright and Trademarks:
All material © Silas S. Brown unless otherwise stated.
QR Code is the UK registered trademark of Denso Corporation.
Samsung is a registered trademark of Samsung.
Telegram is a trademark of Telegram Messenger LLP.
Unicode is a registered trademark of Unicode, Inc. in the United States and other countries.
WeChat is a trademark of Tencent Holdings Limited.
WhatsApp is a trademark of WhatsApp Inc., registered in the U.S. and other countries.
Zoom is a trademark of Zoom Video Communications, Inc.
Any other [trademarks](https://ssb22.user.srcf.net/trademarks.html) I mentioned without realising are trademarks of their respective holders.

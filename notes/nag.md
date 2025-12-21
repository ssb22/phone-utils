
from https://ssb22.user.srcf.net/setup/nag.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/setup/nag.html) just in case)

# How to deal with “rate us” boxes on mobile apps

These notes are old: the Google Play In-App Review API introduced in 2020 allows public ratings to be collected in the app for real, but limits the frequency of the nags to monthly.

You may have been using an application on a mobile device and suddenly it pops up a box asking you to “rate” it on a review site. These boxes sometimes have a number of stars for you to tap directly on your chosen rating.

Now you might be thinking “I’m not sure I want the whole world to be able to find out that I’ve used this app” or similar. So you try to cancel the “rate us” question (perhaps by tapping outside of it) and it goes away for a while—but it comes back later. You realise the developers of this thing have the nerve to keep nagging you for a rating until they get one.

The first thing to realise is that any “stars control” is deceptive. If you tap 5 stars, the application itself *cannot* directly put that into the reviews for you. If it could, it would be able to give *itself* a five-star rating without asking you at all.

Here is an example of what *really* happens, taken from the source code of MAPS.ME on Android. (There are forks that remove the annoyances, but it’s still instructive to consider the original source: many other apps use the same idea.)
```
if (rating >= BuildConfig.RATING_THRESHOLD)
 {
   Config.setRatingApplied(RateStoreDialogFragment.class);
   dismiss();
   Utils.openAppInMarket(getActivity(), BuildConfig.REVIEW_URL);
 }
```
In other words, if the user taps a rating that the developers consider to be high enough, it opens the Android Market (later renamed to Play Store because we’re all children apparently), and points it at the page where the user can *repeat* their rating. It also remembers that you have “given it a rating” so it won’t ask again. There’s also an `else` branch of the code that pops up more stuff if the user “gives” a rating that’s too low.

But the main point is, whatever you tap on that box *does not actually publish a rating*. So you can work around it by:
1. When the app asks for a rating, tap 5 stars. The app itself will then remember that you’ve given it a high rating, and hopefully not nag you again.
2. It will then open the Play Store to let you rate it “for real”. At this point, just quit out of the Play Store if you don’t *really* want to rate it. The app itself won’t ‘know’ that you didn’t really do it.

Is it dishonesty on my part to tell an app I will rate it 5 stars and then not actually do it? I don’t think so, because:
* The exact words of the instruction printed at the top of that box (in the version of the code I looked at) are “Tap a star to rate our app.” It doesn’t say “Tap a star to promise us what you are going to say on the Google Play Store”. Having seen the source code, I now know that this is what they *meant* , but it’s not what they *said*. I can in good conscience give them a *private* rating, which they can, if they like, collect via their own internal anonymous feedback system (if not now, then in a future version of the app)—and my choosing to answer them privately is not the same as agreeing to give that answer in public. It’s like going into the supermarket and having this conversation with the manager:

> Manager: Excuse me, may I ask, how was your shopping experience today?

> Me: It was excellent, thank you very much.

> Manager: Good. Behind me is a reporter from a national newspaper who will now take your picture and print what you just said.

> Me: Hold on, I never agreed to *that*....
* If some developer tries to work around this situation by writing into the license agreement that by giving them feedback you hereby undertake to repeat it on the review site, they will probably be in violation of the review site’s terms and conditions and/or various countries’ free speech legislation. They certainly wouldn’t have *my* promise to abide by such a condition.

## Other nags

The code I looked at also contained a “nag” screen to “like” the application on Facebook. That gave me serious reservations about recommending the application to others, since I do **not** want to encourage *anybody* to join Facebook—for example because Facebook have been known to do things like:
1. Email your contacts in *your* name without your knowledge;
2. Use *your* name in advertising to your contacts without your permission;
3. Making it practically impossible to delete an account once you’ve opened one

and so on. However, I did notice that, in the version of the code I looked at, the situation with *this* nag is very similar to that of the “rate us” nag:
```
mHasInvited = true;
 showAppInviteDialog();
 Statistics.INSTANCE.trackEvent(Statistics.EventName.FACEBOOK_INVITE_INVITED);
```
where `showAppInviteDialog` passes control to `FacebookSdk` and cannot confirm you’ve actually gone ahead with signing up and logging in to Facebook to promote it for them. Additionally, there was nothing in the instructions (at least not in the version I looked at) which actually said the “Share” button means Facebook—I can in good conscience say I’ll share it if I get to choose my *own* sharing method, without having agreed to do so on Facebook. (On the other hand, I wouldn’t share it with anybody without first lecturing them *not* to follow the instructions about signing up to Facebook!)

If they change that button to say “Share on Facebook”, my position would be more awkward—but it’s still possible to argue that pressing it and then declining to actually go through with the transaction on Facebook would be like the following conversation with the supermarket manager:

> Manager: Excuse me, may I ask, do you want to recommend us in the newspaper?

> Me: OK, tell them I like it.

> Manager: Good. Behind me is the reporter who will now take your picture and all the details about your home address and occupation and...

> Me: Wait, you mean you can’t just tell them I like it *without* all those details? In that case I have to back off.

That’s legitimate, because my initial response was not an agreement to sign up—how *could* it be, unless they show me the entire terms and conditions before letting me tap that button? I already know how bad they were last time I saw them, but I don’t check *that* often—they might have been improved in the last 5 minutes for all I know—so it’s still valid to give an initial “yes” and mean “yes on condition I’m willing to agree to the conditions you’re about to show me”. So it’s not dishonest to tap a “share” button and then back out when you see what’s involved; it’s probably less annoying to do that than it is to say “no” to the application if this merely causes it to nag you again later.

It does still mean that you can’t genuinely recommend the application to others without making sure they understand how to cope with the nag screens. In the case of MAPS.ME there were other problems, e.g. a prompt encouraging users to engage in the objectionable and dangerous custom of “trick or treat” and the later removal of the option to disable general advertising that has promoted scam get-rich-quick schemes, which *definitely* takes it off my “safe to recommend to people” list, so I’m glad there are forks I can still recommend.

Copyright and Trademarks:
All material © Silas S. Brown unless otherwise stated.
Android is a trademark of Google LLC.
Facebook is a trademark of Facebook, Inc.
Google is a trademark of Google LLC.
Google Play is a trademark of Google LLC.
Any other [trademarks](https://ssb22.user.srcf.net/trademarks.html) I mentioned without realising are trademarks of their respective holders.


from https://ssb22.user.srcf.net/law/cisas.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/law/cisas.html) just in case)

# iPhone UK billing and messaging issues with Virgin and Vectone (with workarounds)

This page is now for historical interest only. It was written in 2017. Since then, Virgin Mobile folded into O2 in 2021, and Vectone turned off services (without informing customers) in December 2023 (and their website disappeared mid-2024) so it’s unlikely that these notes will be directly useful to any current network users.

These technical problems seem poorly understood, so I’m putting this here in the hope that affected customers can find it via search.


Initial complaint sent to CISAS mid-October 2015:

> Dear CISAS, I am writing regarding the **inability of Virgin Mobile billing software to recognise +44 numbers as UK numbers.**

> A local Chinese family on low income, who speak very little English, asked me to help track down the reason for Virgin Mobile direct-debit payments from their bank. It turned out they had somehow been sold a Virgin Mobile contract SIM without being aware of it, and Virgin’s envelope containing the SIM was still unopened in their drawer. The contract had already run for 2 months so Virgin said it was too late to cancel, so the family kindly decided to let my wife use that SIM for the remaining 10 months, but without actually transferring the contract because my wife was not a Virgin customer and therefore not eligible for the discounted contract they had.

> The deal supposedly included “unlimited” minutes and texts to UK numbers, but over the last 3 months Virgin has overcharged by a total of £52.35, and their call centre said this was because 349 UK texts were sent to numbers starting with +447 instead of 07, causing their system to bill them as “premium” text messages at 15p each, instead of being included in the “unlimited” bundle.

> Unfortunately, my wife uses an iPhone. The iPhone’s Messaging application seems to silently add the +44 prefix on some outgoing messages even though +44 is not stored in the contact that is being messaged. Despite the fact that I hold a PhD in Computer Science, I was not able to figure out how to prevent this behaviour, other than by urging my wife to abandon her beloved iPhone and instead use a phone that clearly displays exactly what number is being texted. I suspect that incoming messages are arriving with a +44 prefix and that the iPhone is abstracting this away on its “threaded conversation” screens, hence leading the user to send replies to the +44 version of the number unawares.

> One Virgin operator initially offered to refund the £52.35, but he then passed the call to the technical team with a view to helping us change the phone’s behaviour. The technical team were not able to help, and passed us back to the main menu. The next operator we spoke to said the £52.35 could not be refunded, but at least he issued a PAC so we could switch my wife to a more suitable network. (By this time we were in the final month of the contract.)

> I checked through all the printed matter that came with the SIM, and there was nothing in there to imply calls or texts starting with +44 instead of 0 would be excluded. I believe this was an amendment to their system made in mid-2015 (because it didn’t overcharge before that time, and there was no change on our side; contrary to repeated suggestions from call centre staff, we have not been abroad during that time). The change clearly makes this SIM unsuitable for use with an iPhone, and I believe it **should be more clearly advertised**, so potential customers of Virgin Mobile understand they are getting a deal that includes calls/texts to UK numbers *only when they start with 0* and not when they start with the equivalent +44, even though incoming calls and texts sometimes arrive with the +44 prefix and every sensible UK network doesn’t mind.

> The account holder is a “Miss [name deleted]” and the SIM was sent to [address deleted], but she has since moved to [address deleted] (and she is Mrs, not Miss, so mistakes were clearly made on a form somewhere). She has forgotten her account password (we’ve had her answer some security questions every time we called the help desk) and she has not set up any Internet access to the account. The phone number of the SIM (soon to be ported away) is [number deleted] and the contract was for unlimited minutes and texts and 250M/month of data.

> Many thanks.

> Silas

CISAS responded 1 week later saying I should try to resolve this more formally with Virgin Mobile before escalating to them. I therefore sent much the same text to VM via the resolver.co.uk service. VM responded the next working day (but I didn’t see it for a week; I later discovered Resolver *had* tried to alert me but my filters had misclassified it as “spam”), saying the charges to +447 were “a known error from our end” and “the account will be noted to advise that a refund for these charges is required” but they need the account holder to telephone with security details. I did it with her a few days later and they said a refund should be sent to her bank within a week.

Three weeks later the account holder said the refund had still not been deposited, so I tried to send Virgin another message via Resolver but it failed; Resolver’s support confirmed Virgin “appear to have completely removed their customer service email option” and suggested trying to resolve via telephone “until we can rearrange this with the company”. I phoned again when next with the account holder: the operator promised to chase it through with management and call me back, but she didn’t call. One week later, the Resolver system allowed us to escalate the case to CISAS, who responded in 4 days with a standard letter asking us to fill in a form, submit evidence and ask for compensation. I submitted the Resolver case file as evidence and asked for the £52.35 refund plus £50 for our trouble (possibly an undervaluation, but I wanted the adjudicator to feel this was a “no-brainer” case). They formerly opened the case on 26 January, giving Virgin 2 weeks to respond. However, I then discovered that the account holder had left me a message that morning saying that Virgin had in fact returned the £52.35 to her bank 13 days earlier (5 days after our last call to Virgin) but she’d only just noticed, so I had to apologise to CISAS for having opened a case saying the refund still hadn’t been paid when it had.

## Vectone

After porting the number to Vectone, messages to affected contacts were not sent at all. We caused the iPhone’s “Messages” application to display the actual number in use by adding an extra digit to the number in the contacts so it wouldn’t match, and the “Messages” application then displayed the number using 44 *without* a plus. I don’t know if that means it tried to *send* the number in this format: if so then we were misinformed by the Virgin call centre which had told us the messages had gone to +44, but it’s plausible that the iPhone had somehow tried to send it *without* the + and Virgin’s system had somehow delivered it anyway but overcharged and the call centre operators didn’t realise this lack of + was significant.

Deleting a conversation did *not* fix the inability to send messages to that contact on Vectone. But we then noticed an affected contact also had *another* number attached, which was not a well-formed UK number. (It was in fact the Hong Kong landline number of a calling-card company once used to cheaply call this contact from there, but it didn’t have an international dialling code and therefore wasn’t valid from the UK.) It turned out *this* number had to be deleted from the contact before outgoing messages would work *even though it was not the number we were selecting when trying to send the message*.

I’m tempted to say the short version of all this is “don’t buy an iPhone”. But if you do, beware of storing local phone numbers of more than one country in the same contact: doing this somehow confuses Apple’s Messages application into sending text messages that are either not delivered (with Vectone) or result in a bill shock (with Virgin). As we’re not allowed to see the source code of either Apple’s iOS 9.1 or the mobile networks’ systems, I’m not able to give any more insight as to *why* this happens, but at least we’ve identified the problem (I think).

(Another ‘quirk’ we found was an apparent inability of Vectone to pass caller ID to a long-distance company called Rebtel, which relies on caller ID to identify its customers. The workaround was to log in to Rebtel’s website and choose to have “local numbers” with a Birmingham code instead of a London “020 3” code.)

Unfortunately we later had problems with Vectone’s billing system as well, and I had to open *this* case on Resolver:

> Dear Customer Service Team,

> I am contacting you as I believe that I am being overcharged. To explain in more detail:

> We topped up £5 initially, then £30 on 5 November to get the £15 bonus credit for porting a number in. We verified that the balance was now £50. Then we activated a “Pocket Saver 10” bundle, and confirmed that it was active and that the balance had now dropped to £40. We expected this to last 5 months, auto-renewing at £10 a month. But on 27 December we had only 18p credit left.

> Checking the payment and usage logs online, we saw the £30, but we didn’t see the original £5, and we didn’t see the £15 bonus. Additionally we saw that UK calls (to 01, 02, 03 and 07), UK texts (to 07) and data had all been charged for, even though that was supposed to be included in the bundle. The charge seemed to be 1p a minute, 1p a text, and data seemed random (sometimes 0, sometimes not). When we phoned a customer service representative, she said her system was not able to load our account details and asked us to call back another day.

> The only unusual thing we did was, just before discovering the credit was only 18p, we tried to send a very long SMS message with over 100 fragments. I understand from the terms and conditions that this might have led to the SMS service being suspended until reactivated by customer services, but would that result in back-dated charges being added to all calls, texts and data?

> I would like you to unblock the SMS facility on the account, give us back £30 credit (i.e. our original £50 minus £20 for 2 months of Pocket Saver 10), and let us know how to avoid these extra charges in future.

Although SMS started working again the following day, on 4 January outgoing calls started redirecting to the “top-up menu” and we received a generic email saying our case is being handled and nothing else. We received nothing for months and then escalated to CISAS, which asked us to submit a formal application, which we finally did in October 2016 (prompted by new students asking advice—it would be nice to get to the bottom of this so as to have a good answer for such questions); we said:

> Between 16 October 2015 and 27 December 2015, we paid a total of £35 and bought three £10 bundles (auto-renewing); we were also given some “bonus credit”.

> However on 27 December 2015 we discovered our credit balance was 18p, and we had been charged for most of the calls despite their supposedly being covered by the bundle.

> Subsequent investigation showed that Vectone’s billing system exhibits the following flawed behaviour: if your credit balance is non-zero, you will often be charged for calls that should have been covered by your bundle, but if your credit balance is zero, the calls will come out of the bundle as they should.

> Therefore it seems the correct way to use Vectone is to make one-off top-ups in amounts that are only just enough to buy a bundle, then buy the bundle and leave the balance at zero. This needs to be manually repeated each month. If this is done, Vectone’s system behaves as it should. But if you try to top up large amounts (for example to take advantage of a bonus offer), you will lose.

> *What action would you like to be taken?* Investigate why the billing system is behaving badly, and fix the program.

> I might be able to help if you send me the source code (I am a software developer).

> If the system cannot be fixed, warn customers that if they choose to use bundles they should not top up any more than the bundle amount and they should not activate auto top-up (they may lose money if they do).

> *Please provide details of the apology you are seeking:* It would be nice not to have been ignored so much. Please recognise that I am trying to help your business by pointing out a bug in your software that can be fixed. I just get fobbed-off or ignored on the phone and emails get no replies.

On 20<sup>th</sup> October we had a call from Vectone and the operator said the excess charging was due to that 100-fragment SMS. Her computer told her that “over 500” text messages were sent in one day, which, she said, triggered a “commercial use” penalty after the 300th message, causing everything to be charged for. That behaviour didn’t match their Terms and Conditions, which said at the time:

> SMS usage is subject to a fair use policy of 100 SMS per day. Once your usage reaches this amount, your SMS feature will get blocked

so if the operator’s explanation is correct, the implications are:
1. The system somehow managed to count 400 extra messages *after* the point at which it was *supposed* to block. Either the system failed to block at the correct time (and the handset somehow sent far more messages than we were aware of sending), or else the system correctly blocked but then somehow went on counting (was the handset automatically retrying and the system was counting its failed attempts? or did the billing software get stuck in some kind of loop counting imaginary extra messages after the block?)
2. If the programmers implemented a block at 100 messages and *also* a “penalty detector” at 300 messages, then either they *knew* it’ll carry on counting after the block, or there was a lack of coordination between different developers.
3. The software for that “charge for everything” penalty would have to *back-date* the higher billing behaviour to much earlier than the time of the offence. (Otherwise, we wouldn’t have seen the extra charges in the online usage logs for dates *before* that of the offending SMS usage.)
4. Since others have also reported disappearing Vectone credit, it’s possible that this “apply a penalty tariff” logic can also (incorrectly) activate under other circumstances.

Anyway, they kindly said they’d refund the £15 and, while they didn’t say they’d fix the system, we felt we’d now drawn it to their attention as much as we reasonably could. (Unfortunately, they got my wife to agree to receive the £15 as phone credit rather than a cheque; this credit was mostly wasted due to failure to cancel an auto-renewing bundle when she was out of the UK. But at least we’d tried hard to get them to look at the issue.)

### Workaround

It was a mistake to top up as much as £30 just to get a £15 “bonus”: it turns out the Terms and Conditions say “promotional credit” cannot be used to buy bundles, so we wouldn’t have much use for it anyway, and seeing as Vectone’s billing system is apparently more likely to overcharge if there is credit on the account, the best strategy is:
1. Don’t choose a bundle whose price is not available as a top-up amount;
2. Top-up only as much as is needed to subscribe to a bundle immediately, leaving (near-)0 balance (and *do not* activate auto top-up, which will try to keep the balance above £2 and therefore vulnerable to overcharging);
3. Ensure the phone’s “mobile data” is switched off before starting the top-up process, and switch on only after receiving the bundle’s confirmation message.

This needs to be manually repeated each month.

### Other Vectone notes
* As of 2017 there is a 1-hour limit on *all* outgoing calls, including calls to the help desk (queuing time is counted), and excessive use of the Mute function is likely to terminate a call earlier.
* If calls cannot be placed, try accessing the “SIM applications” and running “Manual” / “in the UK”.
* If text messages can be sent but not received, this needs to be fixed by the help desk. It might take two calls and an escalation.

In February 2017 we moved away from Vectone, as they’d reduced the value of our bundle 3 times during the previous year and were no longer competitive. Obtaining their PAC was a 3-minute call with no questions asked.

Copyright and Trademarks:
All material © Silas S. Brown unless otherwise stated.
Apple is a trademark of Apple Inc.
iPhone is a trademark of Apple in some countries.
Vectone is a trademark of Vectone Group Holding Plc.
Any other [trademarks](https://ssb22.user.srcf.net/trademarks.html) I mentioned without realising are trademarks of their respective holders.

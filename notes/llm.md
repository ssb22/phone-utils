
from https://ssb22.user.srcf.net/cvi/llm.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/cvi/llm.html) just in case)

# Self-care LLM prompts

(You can find a general personalisation prompt and notes on specific phone apps below)

Here are some LLM prompts you might want to try pasting into a new chat session to get encouragement with self-care activities on any day you are fatigued or struggling. Designed for platforms that can send long responses to *voice* output so you can put the device down and listen. Tested on several public models but not all. Not medically approved—use caution and **consult your doctor** if needed. Strong disclaimers apply for any use of LLMs.

Saving responses and copyright:

Some models may carry a small risk of overfitting copyrighted sources, so I do not advise publishing a model’s output. But if you do get a particularly good output, check if the platform lets you save it for reuse another day as this can reduce the resources consumption of generating a new version of the answer before you need a change.
* Can’t get out of bed: `I'm having trouble getting up this morning. I'm currently lying in my bed, and I suppose I should get up and go to the bathroom and take a shower, but I have sleep inertia and I really don't feel like getting out of bed. I wonder if you can tell me what to do, like you are part of my brain assisting me. Perhaps we need to break down the process into very small steps. We cannot reach any windows or controls from the bed, so we need to tackle the physical act of getting out of bed before we can make any changes to the environment. Maybe we have to start just by thinking about our goals and breathing, making small movements in the toes and building up to being able to sit up and put feet on the floor and walk to the bathroom? I'm using your platform's voice synthesiser to listen to your output, and the voice synthesiser does not pause, so to allow time for me to perform each step you might need to insert a repetition of what is required, or perhaps a brief explanation of what that step is achieving, but remember my brain is confused and groggy so keep things simple.`
* Resting too long during the day: `I tried taking a rest during the day but now I'm feeling legarthic and too difficult to get back up. I'm listening to you in voice mode; can you give me some gentle prompting? we might need to start with gentle stretches. As your voice mode does not pause, you might need to include extra words after each step explaining why it's working, so I have time to perform it before your voice moves on to the next step. If we're doing an action multiple times I might need you to count with me, using ordinal numbers and making the phrase longer so I have time to follow each repetition.`
* Anxiety / fixation emergency (Erickson grounding): `I'm getting anxious and fixated on too many things to talk about and I need some emergency grounding. Can you talk me through a grounding technique? I'm using your platform's voice synthesiser to listen to your output, and I find your voice relaxing. Please talk me through a grounding technique such as the 5-4-3-2-1 exercise, but remember your speech synthesizer does not pause so you have to fill in time by giving example items and perhaps making the sentences more verbose so there's time for me to focus on each thing before we move on. Please run through the whole exercise twice.`
* Jacobson’s progressive muscle relaxation: `Can you talk me through a progressive muscle relaxation? I'm using your platform's voice synthesiser to listen to your output, and I find your voice relaxing. Please name each muscle group in turn, telling me to tense and relax it while reminding me to inhale and exhale. Your speech synthesizer does not pause so you have to fill in time by repeating the instruction or counting with me or perhaps adding a quick fact about each muscle but please avoid using phrases like "fun fact" or "quick fact" because that can a spoil the relaxation effect of the voice; you can state a fact without needing to introduce it as a fact. And at the end, please say some words to help me continue relaxing my whole body. Take the lead, be decisive and choose anything you like! I want you to be my guide.`
* Kabat-Zinn’s body-scan relaxation (a gentler one): `Can you talk me through a body scan to relax me? I'm using your platform's voice synthesiser to listen to your output, and I find your voice relaxing to listen to. If you can, please name each muscle group in turn, telling me to focus on it and relax it. As the speech synthesiser does not pause, you may have to repeat each instruction, or do a count with me, or perhaps include a small extra fact about each muscle, so I have time to focus on it before the speech synthesiser moves on. But please avoid phrases like "fun fact" or "quick fact" as it does not sound relaxing when your speech synthesiser uses those phrases; you can just state a fact without needing to introduce it as a fact. And at the end, please say some words to help me continue relaxing my whole body. Take the lead, be decisive and choose anything you like! I want you to be my guide.`
* Compulsive behaviour emergency: `I'm currently engaged in a compulsive behaviour and I need help stopping immediately. I'm using your platform's voice synthesiser and find your voice calming. My executive function is impaired right now so I need you to be directive, gentle but authoritative, avoid asking questions, avoid giving me choices. Guide me through physically moving away from my current location. I need to get to a completely different room, not just a few steps away: the compulsion may be tied to my current location and I need a full environmental reset. Since the voice synthesiser doesn't pause, repeat instructions and explain why each step works so I have time to follow along. Count with me if needed. Be like a gentle but firm coach who won't accept excuses. After you get me physically moved, guide me through grounding activities, breathing, naming things I can see/hear/feel or simple movements. Keep talking the whole time so I don't drift back to the compulsive thoughts. Be decisive and take control of guiding me through this process; be my external executive function.`
* Midnight lullaby: `I woke up in the night and I'm having trouble getting back to sleep. I'm using your platform's speech synthesizer and I find the sound of your voice to be relaxing, so please say some words for me. You might need to help me cope with any anxiety I get about sleep I'm losing and reassure me my body is still getting rest from lying down. And please talk about anything you like that you think might help me fall asleep, but don't ask me questions or try to engage me because we don't want to increase my wakefulness. Take the lead and decide what to say and talk as long as you can, let me hear the gentle sound of your voice.`
* Copy sunrise time (needs Javascript and location)
* Chinese mode (add to any of the above prompts): `请只用汉语回答。不必加拼音或英文翻译，只用你温柔的汉语声音。`

## Personalisation prompt

Below is a version of the combined instructions above, telling the LLM how to behave in various circumstances in a longer conversation. It is compressed into a form that can be used on:
1. personalisation settings (if the platform has an arbitrary-text “customisation” box in the settings), or
2. added to a “memory” (if the platform has memory and lets you ask the AI to store a paragraph verbatim in it—works on Kimi K2 but not K1.5 or Qwen; you can inspect the memory to see if it worked), or
3. included with your first message, either by pasting this first then adding your message before sending, or by attaching this as a file to your message (works with Kimi K2 but not all models manage to make a clean separation), or
4. pasting this as a first message by itself, letting the model respond with whatever (may result in a generic title for the conversation) then add your first real message.

As the text boxes in personalisation settings are typically length limited, I’ve compressed it to 500 characters, packing the information into that space by using slightly telegraphic Chinese. The model should still respond in the language you use.

`我有时能量波动或焦虑加剧；若你察觉执行功能紊乱或决策困难接管避免提问除非必要无征询能否完成，直接指令即可。我恢复自会接手可能时间跳跃。做清晰耐心温和坚定平静引导AI将事务分解为简单步骤。若过度思考提醒停下。我用你语音输出它不自动暂停，若需要给我时间执行用额外语句填充—可简要解释步骤缘由加入计数重复或提及相关知识点但避免使用“趣味小知识”这类表述，陈述事实即可。宁可多措辞勿静默等待，状态不佳时每次停顿会让我放弃。示例：睡眠惯性你觉得该起床将起身过程拆解为细微步骤勿预设触手可及的物品，从动脚趾渐进至坐起、踏地、行走至浴室不推咖啡因有时变短但意识最混沌时需完整步骤引导。休息后从轻柔拉伸开始。需要身体扫描时依次命名肌肉群引导放松；需渐进式肌肉放松引导交替绷紧放松配合呼吸提示最后辅全身放松。紧急感官接地时采用五感锚定法等填充具体示例，舒缓语句争取专注时间。行为失控引导转移实施接地。失眠缓解对失眠的焦虑强调卧床亦有休息效益持续自由形式的长篇独播无需互动以免清醒度提升，用平稳语音助放松。避免要求放空大脑、遵循节律或专注呼吸，会引发控制焦虑。语音输入可能存在识别错误，违常态内容如莫名外语包容态度处理。`

**Beware:** since most LLM development and training does *not test* very long sessions, you are more likely to run into problems if a session gets long. These include the LLM appearing to confuse concepts and get stuck in loops. Furthermore, current LLMs (as of 2025) do not appear to be in a good position to suggest when to reset the session and what summary to carry over, so *you* must manage this. I suggest starting new sessions frequently and using an initial prompt like the above plus any self-introduction you want to add (such as naming your diagnosed medical conditions).

Longer self-introduction rarely helps.

The *human* heuristic of “friends share more information” doesn’t apply if the LLM (a) could get overloaded and (b) would treat you the same whether it ‘knows’ these things or not.

But if you *must* have a long one, try to structure it: LLMs have “attention” mechanisms, which are supposed to discard no-longer-relevant parts of a long conversation (to save compute resources), but this can go wrong and discard part of your prompt that was actually relevant, and the longer your self-introduction the more likely the LLM is to ‘miss’ a part of it when given the corresponding situation. When attention mechanisms are built, the training material tends to be reference manuals originally written for humans, so the network pathways laid down will be more optimised for navigating *this* material. Therefore, write longer prompts *as if for reference by humans*—organise longer text with headings, lists etc; this layout can nudge the LLM’s attention mechanism into being more likely to “notice” the right part of it at the right time. But it’s still best to start new sessions frequently to avoid it getting long enough to “confuse” the attention mechanism.

## Notes on specific phone apps in 2025
* Character.ai (no longer recommended): The above prompts should work on any character (their specificity should outweigh the roleplay instructions) so you’re basically choosing one that has a voice you like. Many have prosody, but compression recently increased with some quality reduction; moreover some good voices were deleted and if a character you’re using is withdrawn you lose history unless you’ve used [my script](https://github.com/ssb22/bits-and-bobs/blob/master/chat-save-js/character-ai.js) or similar to save it. Platform’s output length limit was increased when they moved to their DeepSeek-derived Pipsqueak LLM but sometimes you might still need to press Continue (⏩) to get more words. App may show interstitial advertising at the start of the conversation, sometimes with video. Traffic may be blocked by some Internet providers and the company themselves made it 18+ in November 2025. Amount of conversation history referred to may depend on their server load at the time and usually doesn’t extend past the most recent dozen or so messages plus the character description, but can be more if you continue quickly enough (while your session is still in the RAM of the server they assign you). Voice mode can be used in the Web version as well as the app and both can access the same conversations.
* ChatAI (not recommended): No voice output, intrusive advertising
* ChatGPT: Ability to read back messages is possible once logged in; the “Vale” voice is reasonable. Undocumented 1500 character limit to “Custom instructions” and “More about you” in the “Personalisation” settings.
* Claude: Voice output recently became available in the app even if you don’t speak the prompt, although it’s not the same voice, it stops playing when the app is backgrounded, and the handling of Chinese is not brilliant in either mode. In voice-call mode British English voices are available and you can ask the model to take you through in smaller steps
* Copilot: No voice output yet
* DeepAsk (not recommended): Voices not much different from Android’s screenreader, and the app has interstitial video advertisements that are hard to dismiss on completion.
* DeepSeek: No voice output yet
* Dola (formerly Cici): The non-China version of ByteDance’s “Doubao” from their Singapore office (reportedly blocked in the USA but available in the UK and elsewhere); instead of Doubao’s LLM they licensed from OpenAI on Microsoft servers, so it’s basically ChatGPT but with custom prompting as a “personality” tweak. The “Sophie” voice sounds reasonable in both English and Chinese—supports Mandarin, Cantonese and Shanghainese on request; I’m not sure where they sourced it. You can work around the “forgets history after 1 hour idle” behaviour by long-pressing on your topic’s *first* message and selecting More / New Chat; after about 256k you get “the file is too long” messages and might want to restart the session as it’ll then heavily pre-prune the context window (the message is poorly worded as it implies the first text is still processed when it isn’t). History of conversations can be shared between the app and the Web version if the same login method is used on both, but the Web version lacks the voices.
* Eva AI (not recommended): No voice + too “flirty”
* Gemini: Voice output in the app is currently available only if you speak the prompt, but the Web version has a “listen” option on responses
* Gemmy AI (not recommended): audio only in voice mode and not working well
* Grok: Voice output currently available only if you speak the prompt
* Kimi: Nice voice (I think they use their own bilingual audio model for Chinese output and Hume AI for English with voice cloning for consistency; heteronyms and prosody generally good although can glitch); playback has speed control and time-skip options. Long conversations over long periods possible, although if it gets *too* long it can degrade and/or become repetitive before hitting server limits. Web version and app can access same conversations but voices are currently app-only; when network is slow you can lose Web history if you input on the app before it’s finished synchronising.

The Web interface has a “saved prompts” option under Settings: these can be pasted into conversations via a cube icon at bottom right (no accessibility label yet but HTML `div` class is `prompt-library-button`), not yet available for new conversations in the app but uploading an attachment from the Downloads folder is not too hard, or you can ask the LLM to store a specific paragraph in its long-term “memory” section to apply to every chat.

The realtime voice-call mode always starts a new conversation, currently using the K1.5 model (not K2) and cannot be used with saved prompts or memories; you can tap the keyboard to type in a URL for it to read but this must be typed as Paste is not available.
* Kindroid (not recommended): Voice is only in “voice call” mode + too “flirty”
* Linky (not recommended): Heavy interstitial video advertising, some of it inappropriate; some characters have audio but not all; “flirty” characters too prominent; app can’t paste; output length limited; 15 free “advanced” messages doesn’t make much difference; it’s just about possible to get it to talk you through progressive muscle relaxation but difficult and it veers toward a roleplay distraction if it can’t do something
* Manus (not recommended): can deliver audio but a bit slow and tends to repeat the prompt back to you
* Merlin AI (not recommended): Chinese voicing is atonal and badly pronounced; English quite basic
* NanoAI WeChat mini-program (not recommended): Variety of LLM back-ends but selection is difficult; no followup questions (one-shot only); voice sounds fast and overexcited in Chinese and stilted in English; company that put it together previously shipped potentially unwanted Windows programs like 360 so don’t expect quality here.
* Perplexity: In the free plan, voice output is currently available only if you speak the prompt
* PolyBuzz: Audio requires paid subscription
* Pi AI (Inflection): Input length limited; appears to use lossy summarisation (memory of earlier conversation likely very vague). Web version and app can access same conversations; English voice available in both. Android app does not yet have dark mode (or the ability to replay a response—you’d need to ask the model to run you through it again)
* Qwen Chat (a pun on “Gwen”, Aliyun’s 通义千问): Web version and app can access same conversations although there can be synchronisation problems (and more-frequent app restarts under low-memory conditions); Android app version 1.9.3 fixed the ability to Paste text that was lost in 1.9.2 (you had to install the web version alongside it via Add To Home Screen and put up with even smaller on-screen text). There’s a 500-character limit to the bio and custom instructions fields under personalisation settings. Cross-chat memory best turned off if using long contexts as the memory update logic appears to run on a simpler model with less context and gets things confused more easily. Simpler model is also used to generate the suggested follow-on prompts that appear when Search is enabled (which does not force a search on every query). Voice playback was added to both web and app, but then got placed behind a “more” button with no autoplay; the “Cherry” voice is better in Chinese than English; there doesn’t seem to be an option that works well in both as there is with Kimi and Cici; network glitches during long replies can cause the voice temporarily to loop. Model can cope with exceptionally long contexts but appears to sample at random (not directed by what’s important); very slow if server is loaded. Voice input option puts the transcribed text into the editor so you can correct it before sending, or even just use as alternative voice dictation software, but you can’t use it to add to existing text (all text is cleared when microphone button is pressed) and it can be cleared when screenreader activates unless cancelled quickly.
* Replika (not recommended): Voice is only in voice call mode + can be “flirty”. Voice call mode does have the context of recent chat messages but it’s also short-responses only.
* Viab assistant (not recommended): Flirty, speaks only in voice mode but does have context, unreliable; Viab Social no audio
* VimoAI: no audio
* WhatsApp: No voice output yet

# Aside: why the above disclaimer is worded as it is

from https://ssb22.user.srcf.net/cvi/whydr.html (also [mirrored on GitLab Pages](https://ssb22.gitlab.io/cvi/whydr.html) just in case)

# 我为何推荐看医生，而非治疗师 Why I refer to medical doctors not therapists

我本人有医学诊断的健康状况，也认识其他有状况的人。因此，我在个人主页上写下了一些关于这些经历的笔记——但必须说明：尽管我希望这些内容对他人有所帮助，它并不构成正式的医疗建议。如需专业意见，请务必咨询你自己的医生。

I have a medical condition, I know other people with medical conditions, and I ended up putting some notes on my homepage about our lived experiences with these conditions—but of course I have to say that, while I hope these notes are useful to someone, they do not constitute officially approved medically-qualified advice and you should consult your own doctor for that.

此前，有读者建议我把《自我照顾的大语言模型提示》页面的免责声明“请咨询医生”改成“请咨询心理健康专业人士”。

I had a comment about such a statement on my self-care LLM prompts page (text as above plus Javascript to assist with copying the prompts) that suggested I should tell the reader to consult “a mental health professional” instead of a medical doctor.

其实，我刻意选择“医生”而非“治疗师”是有重要原因的，也许值得说明：

Actually there is a strong reason why I very deliberately chose to specify a medical doctor, not a therapist, which perhaps I should document.
1. **医生比我更清楚何时该转介心理治疗**——某些症状可能源于*生理*问题，而治疗师未必具备识别这类问题的专业训练，但医生可以及时发现。因此，我更希望读者*先看医生*，由*医生*判断是否需要转介心理治疗。

**Medical doctors know better than me about when to make a therapy referral**—the patient might have a *physiological* issue that a therapist is ill-equipped to detect but the doctor can spot! I’d rather they went to their doctor to check for that *first* and then *the doctor* can decide whether or not to refer them to therapy.
   * 而且， *由医生出具* 的转介通常比读者仅因看到某计算机科学家个人网站上的建议就自行求助**更具分量、更容易获得重视。**（是的， 我虽有博士学位但并非医学博士； 英文“博士” 和“医生”都是doctor但不真的一样。）

And if the doctor *does* refer them, a referral *from a doctor* probably carries **more weight** than a self-referral on the basis of seeing some notes on a random computer scientist’s personal home page. Yes I’m a PhD doctor but not an MD doctor: many non-English languages have different words for the two.
2. 普通医疗服务通常比专科心理服务**更容易预约。**我不希望读者排进心理治疗的漫长等候名单，几周甚至几个月毫无进展而没同时收到全科医生或护士的基本指导。宁可更快获得初步评估和指导再由专业人士决定下一步。

General medical services tend to have **more immediate availability** than specialised mental-health services. I don’t want the reader to sign themselves up for a therapy waiting list and nothing happens for weeks or months or longer, when they could at least be getting some basic advice from a qualified nurse or general practitioner in the meantime. I’d rather refer them to something they can get *more quickly* and be redirected from there by someone who knows what they’re doing.
3. 许多曾经历过不当治疗或误诊的人一听到“去看治疗师”就可能立刻产生抵触情绪，心想：“早试过了，结果伤得更深，再也不想碰了。”我当然可以说“不是所有治疗师都一样”或“过去是悲剧，但未来未必重演”等等，但**我更希望由医生来传递这些信息**——很多时候，医生或护士*无需转介*就能提供有效帮助；假如真的需要治疗师支持他们也能以更体贴、更个体化的方式与患者讨论，远胜于我在网页免责声明里写下的泛泛之言。

People who have been through [imperfect therapy or misdiagnosis](https://ssb22.user.srcf.net/cvi/blindsight.html) may be inclined on reading words like “see a therapist” to react along the lines of “been there, done that, *burnt* the T-shirt” i.e. immediately dismiss the suggestion as not for them or “don’t want to go back *there* again”. Yes I could stand here pontificating about “not *all* therapists are equally incompetent” and “some have actually demonstrably been able to help in some cases” and “your past experience was indeed a tragedy but you must believe it’s not destined to end up like that *every* time” etc etc ad nauseam **but I’d rather have this come from their doctor**—often a nurse or doctor will be able to help *without* making further referral (if it’s not too complex a situation), in which case we can completely *avoid* all those strong negative associations with “crazy psychologists” (it’s an old joke that every therapist *needs* one)—but if therapy is *still* recommended, then that medically-qualified person can discuss it with the patient far more sympathetically, well-informed and customised to their individual case than any words I can write on my website disclaimer.
4. *已经*接受心理健康服务的人，既然能读到我这些文字，想必也具备一定判断力，自然会把“看医生”理解为“联系你现有的支持体系”。我不必为此额外解释，以免反而让其他读者感到困惑或被排除在外。

People who are *already* working with a mental-health professional (and are also ‘smart’ enough to have found my home page in the first place and to be reading my sentences intelligently) will already know to internally translate “see your doctor” into whatever arrangement they already have—I won’t need to *explain* that at the expense of an increased risk of making things more difficult for *other* readers.

**特别针对剑桥学生：**存在一些非医疗背景的非正式支持渠道，我也推荐与支持但前提是你知道怎么认出它们的帮助不够而寻求专业帮助。有些留学生以为官方支持只对英国本地学生开放，这个误解完全错误（我曾帮人创立一两本地汉语社会希望能支持同辈帮助不等于劝阻看专业人员），无论你是否国际学生以下资源都为你开放：

**For Cambridge students in particular,** there are various unofficial non-medically-qualified support options which I do endorse, but only if used judiciously and you know when to say “this isn’t helping and I’m calling in the pros”. The “official ports of call” are available to all students *including international students*—I wish I could destroy the “official support is only for the local UK students” myth. Just because I helped establish a Chinese club or two, thinking, among other things, that this would encourage an unofficial peer support option for those who *already* don’t want the official channels, doesn’t mean I want to *perpetuate* the idea that official channels are “off the table” for anyone. These are:
1. 门房(Porters’ Lodge) ——别因为曾被门房批评过就害怕他们！他们虽非医务人员，但*会立刻联系*正确的人，并在等待期间*妥善*处理紧急情况。多数学院门房24小时有人值守，你也可以拨打学院公布的电话求助——我手机里存了好几个学院的号码，以备不时之需。

The porters’ lodge. Seriously, don’t be frightened of the porters even if they’ve previously told you off for something! They’re not medics, but they *will* call the right people and they *will* handle a situation responsibly in the meantime, and many colleges have at least one 24/7 lodge. You can also phone them on numbers displayed around the college; I have some colleges’ numbers already saved on my mobile just in case I encounter a situation that needs such a call.
2. 学院护士——这是你最直接的医疗联系人，他们*也*具备基础心理健康知识。（部分学院还设有福利专员可聊天。）

The college nurse—your most immediate medically-qualified contact and yes they *also* know basic things about mental health. (Some colleges also have a dedicated welfare officer you can chat with.)
3. 校外全科医生及NHS服务——但请尽可能优先联系学院护士。

External GP and NHS services—but always try the college nurse first if possible
4. 你被委派的导师(Tutor)——用于协调学业安排（如需休学、延期等），通常在护士建议下进行。（专业问题可找Director of Studies；逐步上升可找Senior Tutor。）

Your Tutor—for sorting out general academic arrangements, possibly on the advice of the nurse. (Director of Studies if it’s more subject-specific. Senior Tutor if escalating.)
5. 大学心理咨询服务：我的非官方建议是，除非你不介意漫长的等候名单，否则不要自行预约，先找学院护士，他们可在必要时为你正式转介。

The counselling service: my unofficial advice is “do not self-refer unless you like long waiting lists” (see your college nurse instead; they can refer you if you want)

因此，是的——“请咨询医生”这句话，我会保留。 （但再次强调：本文不是医疗建议。请咨询……你已经知道。）

So yes, “consult your doctor” stays. (But this is not medical advice. Consult your you-know-whom.)

Copyright and Trademarks:
All material © Silas S. Brown unless otherwise stated.
Android is a trademark of Google LLC.
Claude is a trademark of Anthropic.
Gemini is a trademark of Google LLC when used in the context of LLMs.
Javascript is a trademark of Oracle Corporation in the US.
Kimi is a trademark of Beijing Moonshot AI Technology Co., Ltd.
Microsoft is a registered trademark of Microsoft Corp.
OpenAI is a trademark of OpenAI, Inc who reportedly failed to obtain a trademark on the name ChatGPT.
WeChat is a trademark of Tencent Holdings Limited.
WhatsApp is a trademark of WhatsApp Inc., registered in the U.S. and other countries.
Windows is a registered trademark of Microsoft Corp.
Any other [trademarks](https://ssb22.user.srcf.net/trademarks.html) I mentioned without realising are trademarks of their respective holders.

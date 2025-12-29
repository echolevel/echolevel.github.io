---
layout: post
type: blog
title: "ARM vs x86 memory ordering in Unreal Engine"
date: 2025-10-31
description:
tags: []
image:
external_image:
youtube:
pinned: -1
---

I thought I'd write up the most infuriating bug I've had to deal with lately - how it manifested; the many things that could've caused it (but didn't); what actually did cause it; and how I fixed it.

Metron, our realtime dynamic music middleware, is a portable C++ replayer core which is wrapped by a tracker-style DAW interface and can be used standalone or as a plugin for Unreal Engine. Writing Metron is effectively how I migrated my Java skills to C++ and it's been a very rewarding experience on the whole. UE4's Audio Mixer gave me a great sandbox in which to learn how to create DSP effects and synths, while breaking Metron out to raw C++ has in turn been a wild ride of learning to cope without all the safety nets UE gives you. 

Learning realtime programming, you very quickly run into the various issues that certain well-established golden rules exist to prevent: to generalise, they mostly boil down to *“do not cause or allow anything to happen if you don’t know exactly how long it will take”*. With realtime audio, you're not doing all your work 60 or 120 times per second like the graphics and gameplay folks are. You have to do it 48,000 times per second - and if you can't, your game's unplayable. People will forgive minor visual glitches a lot more willingly than stuttering audio. This means you have a tight time budget that you can calculate by estimating an idealised maximum time that your per-buffer DSP work can take before buffer underruns occur, e.g. 
```
(512 / 48000) * 1000 = 10.67ms
```
and then ensuring that you do all your work in slightly less than that time headroom - ideally a LOT less that time.

Keeping to this budget means you can't have your core DSP loop sprinkled with calls to anything that happens in unbounded time, which is...actually quite a lot of stuff if you want your code to form part of any interactive application, game or VST plugin. So your core loop needs to be free of potentially latent or expensive things such as memory allocation (including vector/TArray resizing, which does memory allocation under the hood), UI updates, networking calls, input polling and so on; all those things need to be run on a different thread, and synchronisation between your realtime thread and your 'everything else' thread (let's call it the UI thread) should be very carefully managed so it doesn't a) happen way more often than it absolutely needs to and b) doesn't happen in such a way that causes - *or could potentially cause due to factors outside your control* - a buffer underrun.
---
layout: post
type: work
title: "GlueMidi"
description: "A MIDI routing app"
output: true
image: "assets/img/gluemidi-screenshot.png"
showmediapreview: true
---

### [https://github.com/echolevel/gluemidi](https://github.com/echolevel/gluemidi)

A tiny app for Windows that lives in the system tray and routes MIDI messages from multiple hardware or virtual ports to a single output device or port.

I wrote this to replace MIDI-OX in my own studio workflow. MIDI-OX is a very venerable MIDI utility that does loads of stuff I don't need, but often crashes when doing the one thing I DO need. GlueMidi is a lot more robust for my purposes (merging multiple hardware inputs into one virtual port that Reaper can see) - not just because it never randomly crashes, but also because it can release, refresh and renew its device enumerations without running out of memory making it easier to hotswap devices while a DAW project is up and running.

The system tray icon is animated (inspired by MIDI-OX) - a little DIN-plug whose 5 pins illuminate per incoming MIDI message, so you can see at a glance if the hardware control you're moving is being recognised.

By default the app starts minimised to tray, and minimises to tray on close, but both features are optional. When the app is open, you can view, toggle and pause/resume all inputs; choose an output; and monitor all incoming MIDI messages (both 7bit and 14bit) with some handy filters. 

I've made a lot of weird, niche tools that I rarely use but this one is in use all day, every day, and it might be the thing I'm most proud of...
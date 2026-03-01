---
layout: post
type: work
title: "AmigaPal"
description: "A sample converter for preparing audio samples to use on the Commodore Amiga"
output: true # Don't generate an URL stub for this - just link directly to external_url from projects index
image: "assets/img/amigapal-screenshot.png"
external_image:
youtube:
    id: e4vkSAM88Po
    playlist:
showmediapreview: true # Don't display image or video in item-preview, even if present
---

### [https://github.com/echolevel/AmigaPal](https://github.com/echolevel/AmigaPal)

A sample converter for preparing audio samples to use on the Commodore Amiga.

AmigaPal can load samples; apply some limiting, trimming, low and high filter cuts and a desired target root note (which effectively corresponds to sample rate in Protracker); and export 8SVX (for Amiga) or 8bit WAV (for various retro samplers). 

You can preview the end result using tracker-style QWERTY piano keys and a realtime DSP approximation of how the sample will sound after bit reduction, sample reduction, limiting/compression and filtering. 

You can batch-convert a big list of samples, tweaking individual ones if you need to, and it'll optionally export 128kb 8SVX rather than limiting to 64kb now that modern Protracker versions by 8bitbubsy support the increased size limit. It'll even optionally create a Protracker .MOD file with your converted samples placed in the sample slots, with a filename and title of your choice.

This currently works on Windows but the MacOS version may be broken (and even if it works, it hasn't been notarised and I no longer have the means to do so). It hasn't seen much love for a while since I haven't had the time, but also it's a very elderly codebase that uses an old version of AngularJS with an equally old version of Electron. 

If I was writing it from scratch now (which perhaps some day I'll do), AmigaPal would be a ~4MB Win32 app in C++, not a ~300MB monstrosity with nodejs and a web browser living inside it.
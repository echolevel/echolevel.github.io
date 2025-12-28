---
type: work
layout: post
title: "MetronFX"
description: "MetronFX: free VST3 distortion and reverb effect"
external_url:
output: true # Don't generate an URL stub for this - just link directly to external_url from projects index
youtube: 
    id: 
image: "assets/img/metronfx-screenshot.png"
showmediapreview: true # Don't display image or video in item-preview, even if present
pinned: 1
---

MetronFX is a free VST3 effect plugin that allows some of the insert/buss effects from Metron Tracker to be used in a DAW.
Currently it offers a range of high gain guitar-style distortion models and Metron's efficient but characterful PS1-inspired reverb.

Metron is the music editor and middleware plugin I write and maintain at Cardboard Sword where we use it in our Unreal Engine games.
Its editor is a custom tracker DAW, which works both standalone and within Unreal Editor, and the music can be played back in-game
with realtime bidirectional sync between gameplay systems and musical events. 

Since Metron isn't quite ready for public release yet, this is a little taste of what it does in realtime in two of our games so far ( 
The Siege and The Sandfox; and Transmission: Shortwave). The fact that Metron runs very performantly on Meta Quest (mobile ARM) hardware 
should hopefully be reflected in the low CPU usage of this plugin in your DAW.

Windows only for now, but soon I'll set up a MacOS build chain and make an AU installer.

[Download MetronFX 1.2.2 beta installer](assets/downloads/MetronFX-windows.1.2.2.beta.exe)
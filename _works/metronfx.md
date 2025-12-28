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

Since Metron isn't quite ready for public release yet, this is a little taste of what it does in realtime in two of our games so far - Transmission: Shortwave and The Siege and The Sandfox. The fact that Metron runs very performantly on Meta Quest (mobile ARM) VR hardware 
should hopefully be reflected in the low CPU usage of this plugin in your DAW. I find it rarely creeps above 4% of RT CPU budget usage 
in Reaper with an armed external guitar input and all the most 'expensive' options ticked. That's on a Ryzen 7 5800X; please let me know on Bsky if your experience is wildly different! 

Windows only for now, but soon I'll set up a MacOS build chain and make an AU installer. (The usual disclaimer: this software is free, 'as-is', author
accepts no liability for anything you do with it and offers no warranty against anything going wrong. Copyright 2025 Brendan O'Callaghan Ratliff and Cardboard Sword, all rights reserved.)

**[Download MetronFX 1.2.2 beta installer](/assets/downloads/MetronFX-windows.1.2.2.beta.exe)**
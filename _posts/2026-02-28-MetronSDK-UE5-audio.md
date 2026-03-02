---
layout: post
type: blog
title: "Metron SDK"
date: 2026-02-28
description:
tags: []
image:
external_image:
youtube:
pinned: -1
---

Metron is a dynamic music system for games that I've been developing over the last few years as an in-house audio tool at Cardboard Sword. It comprises a tracker-style DAW editor for composing and exporting music assets, and a static SDK library for playing that music back at runtime in a games engine. Crucially, the music is synthesised in realtime rather than rendered to a 'flat' audio format like WAV or MP3 which means that all of the individual notes, expression controls and arrangement events are available to the game as rich data for bi-directional sync. 

That means you can:
* sync game events to the music's beat, or fractions of a beat
* play/mute/modify individual instruments or sounds when game events occur
* bind visual state to a particular instrument's characteristics continuously in realtime (e.g. material emissiveness follows the kick drum volume envelope, or colour value follows a filter sweep)
* smoothly transpose or tempo-adjust the music according to some narrative state
* swap one instrument or sound with another on the fly
* control a song's mix state or arrangement position via player achievements

and so on - there's potential for incredibly finely controlled granular stuff as well as zooming out for hands-off, logic-driven dynamic music.

<br/>
<figure class="post-video">
  <video
    controls
    playsinline
    preload="metadata"
    poster="/assets/video/metron_sdk_example.jpg"
  >
    <source src="/assets/video/metron_sdk_example.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>

  <figcaption class="post-caption">
    A basic example of Metron Tracker to MetronUE workflow in Unreal Engine 5
  </figcaption>
</figure>


#### Trackers (a very brief history)

Why haven't games always been doing this? Well, they used to! The first publicly available music tracker was The Ultimate Soundtracker written for the Commodore Amiga in the 1980s by Karsten Obarski, and an overwhelming majority of games for that platform used his .MOD format (or something similar) to exploit the Amiga's then-revolutionary ability to play 4 simultaneous channels of decent quality sampledata in complex arrangements for almost zero CPU cost, thanks to the Amiga's fast DMA and custom chipset. In the 90s as the format expanded on the PC, and as PCs began to be fitted with sound cards like the SoundBlaster 16, evolutions of the 4-channel .MOD format to 8 and 32-channel varieties with extended capabilities became popular as an alternative to MIDI or flat-rendered CD-ROM audio for games such as Crusader: No Remorse, Unreal Tournament, One Must Fall and Deus Ex. 

Not all games took full advantage of the possibilities for using the rich data that tracked music replayer routines emitted as a by-product of playing the music, but where the choice was made to use these formats even into the early 00s, it was often due to one or more of these factors:
* vastly less storage footprint than PCM/WAV, because whereas a tracker module stores e.g. a drum sample once and can play it a thousand times at no extra storage cost, a rendered song would effectively have to store it a thousand times sequentially on disk; a 5 minute song might be 30MB as an uncompressed, low-samplerate WAV but 3MB as a tracker module
* vastly less CPU usage to play and render in realtime versus then-nascent decompression algorithms for MP3 and similar
* lots of composers in the games industry were fluent in the tracker paradigm, especially if they'd been active in the Amiga/PC demoscene in Europe and various tracker scenes in the US
* it was often considered preferable to MIDI music which - while fondly remembered and also incredibly efficient for storage and CPU - targeted a wildly fragmented range of consumer-side hardware, all of which sounded different (lucky owners of a Roland MT-32 had a far superior Monkey Island experience to those who had to make to do with whatever crappy General MIDI synth was on their unbranded Soundblaster clone). Lots of composers didn't want to roll the dice on how their music would sound to the player, and sampled sound can be _anything_, not just a fixed preset in a General MIDI synth.

(There's a whole lot more that could be written about how in-house European and Japanese game developers wrote music 'drivers' for console platforms with dedicated sound synthesis chips, or combined the sampledata and MIDI approaches into proprietary systems on a per-game basis right up until the PlayStation 2 era, but this article's getting too long already.)

That only gets us up to the turn of the century... These days, in the 2020s, games often ship with a 60GB+ footprint where even a gargantuan quantity of music assets is a drop in the ocean. They can also be heavily compressed with mature codecs like OGG and Bink then decompressed at runtime on modern multi-core platforms without hitching the game thread, and usually without a player ever noticing a dip in framerate. Most composers work in the studio with exceptionally high quality synths, sample libraries and often real orchestras to produce arrangements and mixes that would still be prohibitively expensive to recreate in realtime on end-user platforms (especially while those platforms are already going flat-out trying to run the game itself) so for a lot of games, especially big-budget franchises, the correct strategy is to have music rendered into flat stems so that mixes and arrangements can be adjusted dynamically.

{% include lightbox-image.html src="/assets/img/metron/MetronScreen00.png" alt="Metron Tracker's pattern editor screen" %}

#### Why use tracker music in games in 2026? 

Plenty of reasons! Musical aesthetics play a part: modern tracked music _can_ sound indistinguishable from 'traditional' flat-rendered stems (indeed, Metron can cheerfully play back those assets like any other modern dynamic music system), but it can also lean into a whole range of experimental, eccentric or nostalgic vibes. But by far the most compelling reason is to exploit the data-richness of a music format which _is_ its own project file; the file (or module, in oldschool parlance) is a bunch of sampledata plus a bunch of binary musical event data. There's no one-way lossy encoding - the sounds carry with them all the instructions required for them to be played back correctly. 

We released two games in 2026 - The Siege and The Sandfox, for PC, and Transmission: Shortwave on Meta Quest 3. Both used Metron, and both exploited the data-rich bidirectional sync it offers. In Sandfox (a stealth-based metroidvania) we had tension risers, enemy proximity heartbeats and combat state percussion layers being triggered and modulated by gameplay state, quantised to correct musical time within the song, and dynamically participating in the score in a musical way that felt natural and atmospheric while also telegraphing crucial information to the player. Proximity to an enemy controlled the filter cutoff on a 'warning' bass throb; enemy suspicion states dictated the volume and complexity of percussion polyrhythms; audible stings for pickups or telegraphing safe/dangerous areas were incorporated into the music itself - recognisable enough to be consistent, but subtly pitched and timed to keep them in the right musical key and correctly quantised to the beat.

Transmission: Shortwave, a retro-futuristic VR delivery courier driving game with an emphasis on low stakes and chillout vibes, leant even more into Metron's potential as the 'clock' of a rhythm game by syncing colours, geometry scale, car indicators and horn, even skybox star twinkling to the 90s jungle/drum and bass soundtrack. We set it up in a fully automated, fire-and-forget way to start with, but later one of our designers hand-authored specific assets' sync responders to complement the characteristics of each song - a breakbeat here, a Reese bass there, hi-hats all over the place - and the result is a rhythmic environment where human curation keeps things feeling good, _breathing_ to the beat, rather than allowing everything to go haywire.

Other proof-of-concept systems that'll make it into future games include gameplay states and achievements moving song transport in and out of 'loop traps', where various rules can dictate how the game conducts the music; gameplay systems like weather states actually being directed by the score (because music shouldn't always be subordinate to gameplay!); pickup/weapon/impact sounds being instantiated as melodic sequences in the currently-playing song, transposed to remain musically coherent (actually we do that in Sandfox, but it could go further).

{% include lightbox-image.html src="/assets/img/metron/MetronScreen01.png" alt="Metron Tracker's multisample instrument editor" %}

#### So...what _is_ Metron?

Initially Metron was a Blueprint in Unreal Engine 4. Actually, about a dozen enormous spaghetti-Blueprints. It proved the concept and taught me a lot about Unreal Engine and its then-new Audio Mixer, but ran very inefficiently - not least because it was doing heavy string-comparison operations per tick on the game thread in a system that's really not designed for that kind of thing. I'm quite proud that it actually ran, though! The sample instrument was very rudimentary and a lot of the music was being generated by Unreal Synth Components - a few of which are provided as examples by Epic Games in the engine. 

It was cool, and (usually) more fun than aggravating, but it was butting up against some hard constraints of UE's Audio Mixer pipeline - constraints that exist for extremely good reason (to keep the pipeline efficient and reliable for the insane demands that modern games place upon it) but which meant that the way Metron's sound generators, effects chains and mix stages had to be structured was far too fragile and wonky to ship.

Some day I'll write up the iteration process in full, because it was a wild ride (I had to teach myself C++ and the joys of threading along the way), but here's the short version:
1. A bunch of Blueprints, built-in synth components, effects presets; UMG/Slate editing interface - no custom code or engine modifications
2. A bunch of Blueprints, some custom synth components and effects, some C++ to instantiate a better effects/mix buss structure on the fly
3. A Metron plugin for UE4: one enormous custom synth component containing all the music sequencer logic; instanced synth components and sample players; a _proper_ tracker interface in Dear ImGui allowing music to be edited _in game_ via a semi-transparent overlay (pretty cool! But not _that_ useful!)
4. Some profound refactoring to bring _ALL_ DSP work inside the synth component, giving me proper performance metrics and allowing me to segment buffer-block processing for extremely tight timing
5. A new standalone Metron tracker in C++/Cmake, completely separate from Unreal Engine(!), with all aspects of the Metron music system modularised into e.g. core, I/O, UI and with build profiles split into 'standalone' and SDK
6. ... then a _new_ Unreal Engine plugin that can wrap the SDK, import music files saved by the standalone editor, and integrate them easily into a game

{% include lightbox-image.html src="/assets/img/metron/MetronScreen02.png" alt="Metron Tracker's audio mixer section" %}

Right now, Metron Music System exists in two parts: a standalone tracker DAW app for Win32, MacOS and potentially Linux (I try to keep the codebase cross-platform); and an SDK consisting of static libraries for metron_core, metron_io and metron_log. 

The standalone tracker is a 2.5MB executable that any composer with some experience of trackers (or none!) can use to write some music, save out that music, and send it to the game devs as a deliverable asset. This beats requiring a composer to download and install 50GB of Unreal Engine plus ~20GB of project, build it all, then run the entire game editor just to tweak some notes. 

The SDK contains all the header includes necessary to write a wrapper for the game engine of your choice. I've made a wrapper for UE since that's what we mostly use at Cardboard Sword. A wrapper for Unity or Godot should be straightforward too - as long as you can parse the Metron file format (a zip containing JSON data and PCM data) and pass that data to the core, then use the core to fill an audio callback buffer, you'll be able to play the music and get all the realtime sync data you want in a threadsafe way.

Yeah, it _was_ cool to have the tracker editor running in a Slate tab in UE, and as an overlay during PIE (Play In Editor) sessions and even in packaged builds, but iterating compositions in the standalone editor is a way better workflow, especially if you're contracting the music out to freelancers.

So the very short version is that it's a music middleware system, in-house to Cardboard Sword for the time being, but proven in two shipped titles and being actively developed.

Here's yet another set of bullet points with some cool features of Metron:
* The default instrument type is the SampleVoice - actually a multisampler with Kontakt-style key zones and velocity zones, FastTracker-style multistage volume/pitch/pan envelopes plus an assignable effect parameter envelope, internal phrase sequencers, plus the usual range of sample mangling pitch-and-time effects you'd expect from a tracker: sub-tick note cuts, microtiming, timestretching, retrigger, and so on.
* The custom synth engines are a hybrid 4-operator FM/PD synth; a Karplus-Strong string modelling synth; and a bit-accurate Atari YM2149 soundchip synth built on the ayumi AY chip emulator
* There's a full suite of discrete DSP effects that I wrote from scratch to be as efficient as possible, but with enough flexibility to allow for comprehensive master buss chains, creative time/modulation chains and extensive realtime automation. They can be used in the same way as VST plugins in a variety of contexts and routing paths, but unlike most VST plugins they're optimised for use in games where system resources are at a premium, and audio is not the sole priority like it is in a conventional DAW
* There are three fixed send effects (delay, reverb and chorus) that can be used by all instruments and group busses
* The group buss system allows an effects chain to be built on a group buss so that any channel's output can be routed through it
* The master effects chain allows all channels, sends and group busses to be processed through e.g. compressors, EQs and limiters (or indeed anything you want)
* Polyphony is dictated by the channel count - since performance is critical, it's important not to let polyphony run away from you, but also this means you can arbitrarily route an instrument to and from group busses by triggering them in different channels
* Obviously because this is all runtime sequence data and realtime DSP, transposing the pitch of a song without altering the tempo is essentially free in terms of CPU; while adjusting the tempo without altering the pitch is equally free.
* Aggressive optimisations throughout mean that, for example, _Transmission: Shortwave_'s soundtrack of reasonably complex 6 to 8 channel 90s jungle tunes with reverb, delay, chorus, compressor, limiter, EQ and some filters use an average of 8% of audio CPU budget on Meta Quest 3 hardware (ARM, Snapdragon XR2 Gen 2). Similar arrangements under Windows on a Ryzen 7 5800X are closer to 4%.

#### Epilogue

Thanks for reading! If you've been following Metron's progress, you'll know I'd like for Metron to be available to everyone in some way, at some point, but I've never made any promises or predictions because there are various things to figure out first (and there's so rarely enough time to figure things out). I always appreciate the support and interest it gets when I post or talk about it, and even if I can't immediately invite people to try it out and enjoy it, I hope that my occasional deep-dives on the development experience are of some use to others who are trying to do cool stuff in game audio generally, and Unreal Engine's fantastic Audio Mixer in particular.
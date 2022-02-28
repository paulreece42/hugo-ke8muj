---
title: "Every Setting on the FT-891, Explained"
date: 2021-11-15T23:03:10-05:00
draft: true
---

The following is distilled from months of research

First, some terms:

- Band: The band you're on. 40m, 20m
- Passband: what you hear coming from your speaker is the part of the _band_ that's in your _passband_.
- Bandwidth: How wide your _passband_ is. For single sideband (SSB), this is 2400 Hz.

Using a SDR is the easiest way to show these, Paul stop being lazy and make a video and add it here before posting.

[<img src="" >]

FUNCTION-1

- TNR: Tuner, for use with an automatic tuner like the FC-50. This must be enabled in the main settings menu (F long press). Once it's setup there, I see TNR on my main VFO screen, and it automatically tunes as expected, automatically. 
- VOX: VOX is pretty standard in radios, it's a hands-free mode that presses the PTT for you when it hears audio. Useful also for digital modes, can automatically key-up when your computer starts talking. I prefer having my computer manually control the PTT via the USB, your mileage may vary.
- PRC: Voice processor. This "compresses" your voice on single-sideband, a level from 1-100, and gives you more average power, reducing the peaks and valleys effect of human speech, at the tradeoff of sounding more robotic.
- MON: Monitor function - routes your transmit audio through your speakers. Useful for listening to your computer squawk packets, or for hearing how your voice sounds when configured with the equalizer or PRC setting above.
- SPL: Split function - listen on the A VFO, but transmit on the B VFO. Useful for 50 MHz repeaters, and some digital modes.
- IPO: Preamp off. I forget what IPO stands for according to Yaesu, but it's a silly acronym. Forget that, it means "preamp off".
- ATT: Attenuator. Minus several dB to all signals, signal and noise alike. 
- NAR: Narrow the bandwidth of the passband. Normal SSB for example is 2400 Hz wide, this makes it narrower than that. Works with AM mode (WDH does not). Can sometimes increase your signal to noise ratio when you have heavy interference.
- NB: Noise blanker. I'm a young ham, so this one is confusing to me. As far as I can tell, this would reduce many short "spikes" of interference, which used to be a problem with car ignition switches or something. Since cars don't use this anymore... I dunno, might be useful if a neighbor decides to throw a [lightswitch rave](https://www.youtube.com/watch?v=JwZwkk7q25I)? Or maybe I'll go to the [Woodward Dream Cruise](http://www.woodwarddreamcruise.com/) next year and report back?
- SFT: Shift your passband. The Yaesu manual actually has a great diagram of this one:
- WDH: Change the width of your passband. This is similar to the NAR / narrow setting, but can also be used to make it wider - up to 3000 Hz. Useful for digital modes like FT-8.
- NCH: Notch filter. Introduce a notch along your passband, useful in manually filtering carrier-type interference, when you have a continuous "buzzing" in your recieved audio. The notch can be put right over that "line o' noise" and filter it out.

FUNCTION-2:

- MTR: Change which thinghy you want to display as your main meter - SWR, Power transmitted, ALC
  - SWR: Standing wave ratio, if you don't know what this is, don't hit transmit, you can break your radio![^1]
  - 
- SCP: Scope. Supposed to be like a scope / panadapter, etc. This feature was a huge disappointment to me on the FT-891, the LCD and fact it mutes/steals your audio when tuning and slow refresh rate make it mostly useless, IMO, use a $20 RTL-SDR configured as a panadapter instead... (TODO: Find/make good link for this) 
- AGC: Automatic gain control, automatically adjusts your RF gain, such that if you tune to a loud signal, it lowers the RF gain.
- DNR: Digital Noise Reduction, an MVP function on this radio. Does just what it sounds, uses algorithms to filter out noise, leaving just the voice signal. Higher levels give you that "underwater" sound, but at lower levels with moderate noise, can make listening much more enjoyable.
- DNF: Digital notch filter. Just like the notch filter in FUNCTION-1 menu, but automatically applied to the hopefully correct place in your passband, by a friendly robot living inside your radio.
- CNT: ... Contour. A less sharp notch filter, over more of the passband. (And... Yaesu... we need to talk about some of these acronyms, please consult a millennial before making any more)
- MOX: 
- TXW: Switch transmit and recieve on TX and RX when operating split operation. Listen on your TX. Useful for trying to hear someone near you who can't make a repeater you're both using.
- MEQ: 
- QMB: Quick memory book. Book of memories for your frequencies. 

CW SETTING:

- SPEED: lol idk
- ZIN: Zero In, sometimes called zero beat on other radios. While another station is transmitting CW, smash that ZIN button to zero your VFO right on top of their exact frequency[^2]
- APF: 
- PITCH: 
- KEYER: 
- BK-IN: Transmit. This means TRANSMIT.

FM SETTING:

- T/DCS: Tones for accessing repeaters
- TONE: ""
- DCS: ""
- RPT: 
- REV: 

REC SETTING:

- DEC: 
- PB: 
- MEM: 
- CH1-5: 

[^1]: If you didn't know this already, check out hamstudy.org, it's free. I make sure my own transmissions are legal; that's my business and I mind it well. That said, if you don't know enough and try to transmit, you might break your radio, bud. So, hamstudy.org is your friend!
[^2]: this is a bit hard to explain if you haven't operated CW but the passband can be set very very narrow, you'd generally hit the ZIN, then turn on NAR, then zoom your width (WDH) wayyyy down until you've just got like 500 Hz around their CW signal... VERY good at eliminating QRM. Like, mind-blowingly good. Using this exact feature and seeing how much noise I could eliminate from a CW signal was what made me interested in learning CW... seriously...

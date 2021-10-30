---
title: "Stratum 1 NTP Server From WWV/H or CHU"
date: 2021-10-30T08:46:10-04:00
draft: false
---

The first time I heard a time station broadcasting the time, I thought "wouldn't it be useful if my computer could set its clock off that?"

So, I did some digging into it.

ntpd, the network time protocol daemon, has several little-documented features, and it turns out using the audio signal from [WWV/H](https://en.wikipedia.org/wiki/WWV_(radio_station)) or [CHU](https://en.wikipedia.org/wiki/CHU_(radio_station)) is one of them, but the code is very old and written for OSS and not ALSA, let alone PulseAudio.

To set this up, I took my Yaesu FT-891, a SignaLink USB[^1], and a Raspberry Pi 3

First tried with Rasbian Linux, and got pretty close with the alsa-oss wrappers, but in the end had no luck. Not sure why, it appeared to be working, but I just never got a clear read on a crystal-clear singal from CHU. YMMV.

Tried again with FreeBSD 13.0 on the pi, and the configuration was pretty much plug and play:

![screenshot showing my laptop synced with my Raspberry Pi using CHU as a source](https://mackmyra.static.mojocloud.com/screenshots/eeb45e5b-2392-40a7-b997-8cf8c5ca1382.png)

That's my laptop syncing with my Raspberry Pi @ 192.168.18.189, left that overnight with CHU tuned on 80 meters (3.33 MHz UPPER Sideband) and I'm keeping pace with NIST's official servers :) 

Configuration is simple, and the documentation is good... but you do have to [read the code](https://github.com/ntp-project/ntp/blob/master-no-authorname/ntpd/refclock_chu.c) 

/etc/ntp.conf:

    server 127.127.7.0
    fudge 127.127.7.0 time1 0.14


14 milliseconds is the time delay I get from CHU. In Detroit, I'm about 418 miles from the CHU transmitters in Ottawa in a straight line, which is only about 2ms of radio delay (1ms per 300km - speed of light). My guess is ~12msec is how long it takes the audio signal to be transferred through the soundcard, and processed in the NTP drivers for CHU.

The way I got 14 milliseconds is letting another computer use my Raspberry Pi as a server, along with other known very reliable NTP servers, such as those from NIST and JRC. I picked the number 14 because it looked right, comparing it off the other offsets. Accurate enough for the servers in my basement, no rocket surgery needed :)

Doing this with WWV is just as easy, you'd want to use 127.127.36.0 instead of the third octet being 7.

127.127.7.0 = CHU

127.127.36.0 = WWV

...It's just how ntp.conf works, don't ask me why. The 1990s were a wild time, I guess.

If you have multiple sound cards (FreeBSD didn't automatically detect/load the module for the onboard Pi sound card), you'd want to set up a /etc/ntp.audio file, something like this, to use the second sound card:

    idev /dev/dsp2


Both audio drivers (CHU and WWV/H) also support tuning an ICOM radio via the serial port, to switch around to other known signals for CHU or WWV/H if it loses signal on one band. According to the code, the baud rate is set to 9600. I tried symlinking my radio's USB COM port for CAT control to /dev/icom, which looks like it should work... but when running the program, I don't even see any attempts to access /dev/icom, using strace or truss. Using FreeBSD's ports system to recompile it, there's no option to "--enable-icom", and icom support appears to be hard-enabled from first glance at the code. More digging will be needed here.


Definitely going to poke at this more in any event[^2]

More on this story as it develops 

Further reading:

- [refclock_chu.c](https://github.com/ntp-project/ntp/blob/master-no-authorname/ntpd/refclock_chu.c)
- [refclock_wwv.c](https://github.com/ntp-project/ntp/blob/master-no-authorname/ntpd/refclock_wwv.c)


[^1]: though likely, any modern cheap $10 USB soundcard would work, or probably even the onboard line-in on a normal computer's motherboard
[^2]: Fun project ideas, maybe in the future when I get some time: port these drivers to work with an RTL-SDR in direct sampled mode. Then a $20 Raspberry Pi, a $20 RTL-SDR, and a low noise, recieve only Loop-on-Ground antenna could give you a pretty reliable and cheap stratum-1 reference clock. For now this is just a fun toy as I'm not going to tie up an expensive HF radio 24x7x365, just to know what time it is, but something like an RTL-SDR would bring this into the realm of practicality.


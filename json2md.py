#!/bin/env python3

import requests
import jinja2
import datetime
import sys

t = jinja2.Template("""---
title: "SSTV Cam"
date: {{now}}
draft: false
---

MFJ-2012 @ 50 feet EN82kk, Detroit MI USA

Ancient Windows 7 laptop running MMSSTV, 14.230 MHz


These images are uploaded automatically by people around the world, and may contain unintended offensive content[^1]

| SSTV | CAMS |
|------|------|
| ![{{foo[0]['link']}}]({{foo[0]['link']}}) | ![{{foo[1]['link']}}]({{foo[1]['link']}}) |
| {{foo[0]['uploadtime']}} | {{foo[1]['uploadtime']}} |
| ![{{foo[2]['link']}}]({{foo[2]['link']}}) | ![{{foo[3]['link']}}]({{foo[3]['link']}}) |
| {{foo[2]['uploadtime']}} | {{foo[3]['uploadtime']}} |
| ![{{foo[4]['link']}}]({{foo[4]['link']}}) | ![{{foo[5]['link']}}]({{foo[5]['link']}}) |
| {{foo[4]['uploadtime']}} | {{foo[5]['uploadtime']}} |
| ![{{foo[6]['link']}}]({{foo[6]['link']}}) | ![{{foo[7]['link']}}]({{foo[7]['link']}}) |
| {{foo[6]['uploadtime']}} | {{foo[7]['uploadtime']}} |
| ![{{foo[8]['link']}}]({{foo[6]['link']}}) | ![{{foo[7]['link']}}]({{foo[9]['link']}}) |
| {{foo[8]['uploadtime']}} | {{foo[9]['uploadtime']}} |

Page: [0](http://ke8muj.net/sstv/0/) [1](http://ke8muj.net/sstv/1/) [2](http://ke8muj.net/sstv/2/) [3](http://ke8muj.net/sstv/3/) [4](http://ke8muj.net/sstv/4/) [5](http://ke8muj.net/sstv/5/) [6](http://ke8muj.net/sstv/6/) [7](http://ke8muj.net/sstv/7/) [8](http://ke8muj.net/sstv/8/) [9](http://ke8muj.net/sstv/9/)

[^1]:Mostly just hilairously retro nude pictures, probably scanned in from Playboy circa 1970. Oh, you hams. Y'all know we have like, _entire websites_ for that now, right?


    If you see any, be sure to send me an email, I wanna see!!
""")

try:
    page = sys.argv[1]
    r = requests.get('http://hackdetroit.city:14230/sstv/%s' % page, headers={'Bearer' : 'foobarbaz' })
except:
    r = requests.get('http://hackdetroit.city:14230/sstv/0', headers={'Bearer' : 'foobarbaz' })

foo = r.json()

now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S-00:00')

try:
    print(t.render(foo=foo['data'], now=now))
except:
    pass

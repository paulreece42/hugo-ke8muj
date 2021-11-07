---
title: "Serverless SSTV LiveCam for the 2020s"
date: 2021-11-07T10:46:10-05:00
draft: false
---

On Halloween, I had a blast listening to pirate radio stations, mostly Radio Genix and Outhouse Radio

One of the neat things was they had intermittent SSTV mixed in with their music, and I recieved many cool Halloween-themed pictures. Pumkins, ghosts, and so on. The ones from Outhouse Radio were just really cool pictures, hard to describe.

Luckily, [I recorded it!](/posts/halloween-pirates/)


All was well, until one day last week I left MMSSTV running with my radio tuned to 14.230 and went to work. I came back from work to look at what I'd captured, propagation was very good that day, and...

OH, NO.

By default, MMSSTV only stores 32 pictures, using a sort of ring-buffer to overwrite the oldest one > 32. Clearly, I had to find a solution to this! With 18TB+ hard drives easily available in 2021, storage of small images is practically free these days, there's very little reason to ever delete old ones. I've seen a lot of people have their SSTV rigs upload to FTP, and update a website. I could do that, but with S3-compatible object storage! Better yet, I'll do it in Golang, that's the hot trendy programming language all the cool kids use these days! Maybe make it all serverless, run it on Kubernetes, all the ["I'ma cool dude Silicon Valley trendy VC trender IPO startup series C funding FAANG"](https://news.ycombinator.com/)  technologies! [^1]

So, I did:

[https://github.com/paulreece42/sstv-uploader](https://github.com/paulreece42/sstv-uploader)

Let me first say: there are a million easier ways to accomplish setting up a SSTV cam. If you somehow ended up here Googling how to do this, buddy, _this is not the way_[^2]. This is a pointlessly complex way of doing it, that I did for fun, to brush up on some tech skills and maybe show off a bit. 

Not that I'm doing a good job showing off, the code's a bit of a mess currently because this was all written in a few hours, I know I should go back and split a lot of things off into their own functions, and at least write some unit tests, but it's the weekend and I also have to do household chores at some point. This was my first Go script, and I have to say that it's a really nice language to work with, it lives up to its hype so far.

Anyways, what that little API does, is lets you POST images using curl (or some similar HTTP-protocol manipulation tool or library) with a simple bearer-token to the API endpoint, it then takes those images, generates a UUID for them, converts them from bitmap format (MMSSTV is a _very_ old program...) to png, and uploads them to any S3-compatible object storage, gets a md5sum of the image somewhere along the way to prevent duplicates and double-posting, and stores all this in PostgreSQL table

You can also query the API with a GET, and get a json listing of uploaded SSTV images

Then I just wrote a simple little [python/jinja2 wrapper](https://github.com/paulreece42/hugo-ke8muj/blob/main/json2md.py), to query this API when I build Hugo, and give me some SSTV blog posts

Hugo then builds all of this into a static-HTML website, which can then be uploaded either to a traditional webserver, or object storage using the s3website API. Using object storage and running a Hugo build pipeline and the SSTV uploader container in k8s (or AWS lambda, or whatever), you end up with a "serverless" solution.

Finally, I use a [PowerShell script](https://github.com/paulreece42/sstv-uploader/blob/main/monitor_mmsstv.ps1) to monitor MMSSTV's History folder for changes, and POST the changed .bmp file to my API

I really wanted to integrate this with some ML image recognition technologies like AWS Rekognition, at least to try to pull call signs off of recieved images, but the static just absolutely destroys the ability of ML to recognize and categorize images, and SSTV certainly isn't a popular enough hobby to train my own datasets. Digital/PAL-SSTV shows a lot more promise for that, but in days of occasional listening on 14.233, I haven't heard a single Digital/PAL-SSTV broadcast yet. Though to be fair, I have a very noisy QTH - I live in the middle of a major city

In the near-future, I want to get QSSTV running on a Raspberry Pi, drawing from a RTL-SDR[^3], and ideally I'll also add the frequency the SSTV was recieved to the data I upload and display. 





[^1]: Actually, I think the language for this is Rust, these days. Golang was like 5 years ago, but people are still using it fairly often, so I finally took notice as it's survived the test of time.
[^2]: If you did get here from Google, you're probably asking "okay then, what _is_ the way!?" Honestly, I have no idea. I didn't even look into it, I just saw the oppourtunity to make something pointlessly complex and jumped at it, sorry... probably "something with FTP" is my guess of what most people use?
[^3]: I say "RasPi + RTL-SDR" a lot. I imagine my ham shack in a few years just growing to be a veritable server rack of dozens of RasPis with RTL-SDR dongles :) 

# yor


Creating a Discord bot using the [interactions](https://discord-py-slash-command.readthedocs.io/en/latest/) Python API. I am NOT a developer whatsoever. 

You should not use this code even if it ends up working. Every single function I reckon is only ever useful to me.

## But I wanna use it

In case you really want to use this bot. Just make sure to `pip install` every requirements listed in the imports (if they don't come by default) and set all the environmental variables you need (defined in helpers.py) on your system. I reccomend doing all of this in a Python `venv`.

The initial commit works.


## Why this League of Comic Book Geeks thing?

LOCG is extremely useful to me and my community, we love looking at which new comic books come out every week and talk about it. Unfortunately it's not that fun when we have to manually link the website and everyone has to get out of Discord to look at it and then come back and forth to talk about the new comics.

It is also unfortunate that the developer (that I talked to) on LOCG has refused to release a public API in fear of 'people stealing my work', which I find absolutely idiotic. So I decided to grab the public GET calls their website uses and just parse their terrifying JSON and use some regex to match what I need from an entire HTML.

It's REALLY bad but it's what I have to do until I find a better way or the developer decides to not be so offstandish about something that the entire world does.

I have all of this and more working on Node-Red, so I decided to move it away from that clusterfuck and learn python while I was at it.
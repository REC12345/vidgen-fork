# vidgen (video generator) ❤️‍🩹

Algorithmically generate those videos you see all over TikTok, where some AI voice is reading out popular reddit posts while the background is some dopamine-rush mobile game footage.  This program has the goal of educating the user on how this type of content is made and just how easy it is to produce it.

### How It Works

1. Scrape popular online forums(Reddit, Qoura, etc...) for viral posts and save them to a JSON file.

2. Send each post through a text to speech program to produce an audio file.

3. Generate subtitles by transcribing each audio file.
   
   (we need to re-transcribe the audio because we don't know how fast the text to speech is talking.)

4. Get free-to-use satisfying game footage off YouTube.

5. Combine the audio, subtitles, and game footage into the final video.



### Usage

#### Directory structure

The program kind of expects the following directory structure under `data/`.

This means you're gonna want to provide a font.ttf and gonna need to provide background footage.

There are two sections, input and output.  Input includes the desired font, online post and background footage while output includes the final video, final audio and, subtitles.

`input` contains
+ `ttf/` stores the desired font(A default font is provided for convinence).
+ `posts/` stores reddit posts.
+ `background/` stores background footage.

`output/` contains
+ `subtitles/` stores the generated subtitles.
+ `audio/` stores text-to-speech output files.
+ `video/` stores the final video.

`config` contains
+ `dicts.py`, which are some dictionaries used to sanitize the reddit posts and, importantly, the list of subreddits used (currently: `r/tifu`, `r/amitheasshole`, `r/relationship_advice` and `r/confession`) and the method to query them (currently: `rss` or `web` -- as in RSS or web-scraping)
+ `structure.py`, which defines some directories and the font path, name and size.

Remember, garbage in is garbage out...

`tree` output:

```
vidgen
│
├── trashcan
│   ├── garbageIn_MM_DD_YYYY
│   │   ├── font.ttf
│   │   ├── post.json
│   │   └── background.mp4
│   │
│   ├── garbageIn_MM_DD_YYYY
│   │   ├── font.ttf
│   │   ├── post.json
│   │   └── background.mp4
│   │
│   └── garbageIn_MM_DD_YYYY
│       ├── font.ttf
│       ├── post.json
│       └── background.mp4
│  
├── dumpster
│   ├── garbageOut_MM_DD_YYYY
│   │   ├── subtitles.srt
│   │   ├── audio.mp3
│   │   └── video.mp4
│   │
│   ├── garbageOut_MM_DD_YYYY
│   │   ├── subtitles.srt
│   │   ├── audio.mp3
│   │   └── video.mp4
│   │
│   └── garbageOut_MM_DD_YYYY
│       ├── subtitles.srt
│       ├── audio.mp3
│       └── video.mp4
│  
└── config
    ├── dicts.py
    └── structure.py
```

#### main.py

`main.py` provides a convenient way to use the program. By default:
1. it downloads the daily top posts from the subreddits provided in `config/dicts.py`, 
2. saves them into the DB, then, 
3. for each one, it generates a text-to-speech audio file, 
4. a subtitles `.srt` file, 
5. composes the audio with a random background video from `video/bg/random_folder/random_file`,
6. burns subtitles onto the composed file
7. cuts up that video into 50-second chunks (so they can be uploaded as YouTube shorts, for example.) 
8. (Planned) automatically uploads the parts to configured platforms

It takes the following options from the command line:

+ `--no-web`: Do not save new posts from the web
+ `--no-audio`: Do not generate audios
+ `--no-subtitles`: Do not generate subtitles
+ `--no-video`: Do not compose videos
+ `--no-youtube-upload`: Do not upload to YouTube (currently irrelevant)
+ `--quick`: Work on a limited number of posts only
+ `--quick-limit`: Set the limit used in `--quick`, default: 1

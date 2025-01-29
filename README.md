# vidgen (video generator) ❤️‍🩹

This is a tool to algorithmically generate those videos you see all over TikTok, where some AI voice is reading out popular reddit posts while the background is some dopamine-rush mobile game footage.

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

This means you're gonna want to provide a font.ttf and gonna need to provide background footage (for your convenience, by default, a libre font is provided.)

`audio/` is used for the text-to-speech output files

`db/` is populated with an sqlite3 database to store reddit posts

`subtitles/` is used for .srt files to store the generated subtitles

`ttf/` contains the font to be used

`video` contains
+ `bg/` which contains individual folders whichthen contain your background footage
+ `done/` which is populated with the generated videos

`config` contains
+ `dicts.py`, which are some dictionaries used to sanitize the reddit posts and, importantly, the list of subreddits used (currently: `r/tifu`, `r/amitheasshole`, `r/relationship_advice` and `r/confession`) and the method to query them (currently: `rss` or `web` -- as in RSS or web-scraping)
+ `structure.py`, which defines some directories and the font path, name and size.


`tree` output:

```
vidgen
│
├── config
│   ├── dicts.py
│   └── structure.py
│
├── audio
│   └── (filled by vidgen)
├── db
│   └── (filled by vidgen)
├── subtitles
│   └── (filled by vidgen)
├── ttf
│   └── subtitle_font.ttf
└── video
    ├── bg
    │   ├── gta_gameplay
    │   │   └── gta_footage.mp4
    │   └── some_other_background_footage
    │       └── some_other_footage.mp4
    └── done
        └── (filled by vidgen)
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

### Planned features

+ Automatically uploading generated videos to platforms such as YouTube (shorts), TikTok or Instagram (reels)
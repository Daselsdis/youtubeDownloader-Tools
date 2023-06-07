# youtubeDownloader-Tools
Youtube downloader tools, separated into single and playlist scripts for convenience.
Not that proud of the programming in this, but it's a good centralized resource to a problem it took me some weeks to find a good mend to, so, proud of that part.

## Big important stuff
Youtube playlists and mixes (Mix) are a different thing, you cannot directly download mixes from just the link.
As an example, a playlist's link's Id is in my experience 34 chars long, and can take the form: "https://www.youtube.com/playlist?list="+Id. Mixes on the other hand have shorter playlist's link's Id, in my experience 13 chars long, and can take the form: "https://www.youtube.com/watch?v=VIDEOID&list=MIXID".
You can only download playlist, and I suspect only Public or Occult ones from your channel or whoever's if they are accessible from the outside via link.

## MORE EVEN MORE IMPORTANT STUFF:
How to solve this: I found this answer on reddit and I will credit it at the end, the trick is to load the mix, and next, add to queue a random video(be careful, delete it later or you will download it too). Now you don't have a mix, you have a queue of videos, now you can make a playlist out of this. Make sure to make it Public or Occult, now that playlist's link should follow what's said above and you are good to go :D.
 Credit where credits due: https://www.reddit.com/r/youtube/comments/b33ecs/comment/hj74ays/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button. Moreover, all the pytube library resources have been an amazing tool and for any doubt feel free to ask me the author or check those docs.
 
 Even more moreover, thanks to all those who contribute, this will evolve a bit over time and everybody is welcome. Special thanks to Ja1m33m for making it more verbose with dl location and making input more user friendly.
 
## Have an amazing time, yours truly: Daselsdis
_Also, feel free to tinker with this stuff, it has MIT license, free code :D (I wouldn't have made it this far without it)._

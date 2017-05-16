# getAniList
Inspired by discord bots that fetched data from MAL I made getAniList for my own discord bot.

getAniList is used only to read data from AniList. It uses the client credentials grant type and so it cannot add, edit, or delete user data.

# Using getAniList
```
from getAniList import getAniList

instance = getAniList(client_id, client_secret)
```

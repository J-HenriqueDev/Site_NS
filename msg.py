import requests
import auth

def send_msg(bot, lib, prefix, user, pos, content, time):
        text = {
                "content":content["msg"] ,
                "embed": {
                "url": "https://discordapp.com",
                "color": 4367861,
                "footer": {
                "icon_url": "https://i.imgur.com/MEMM7yB.png",
                "text": time
                },
                "thumbnail": {
                "url": "https://cdn.discordapp.com/avatars/"+bot["id"]+"/"+bot["avatar"]+".png"
                },
                "author": {
                "name": content["event"],
                "icon_url": "https://cdn.discordapp.com/avatars/499321522578522112/5905702619021955b2246eba83d09897.png"
                },
                "fields": [
                {
                        "name": "<:tags:571703384164401172> Tag",
                        "value": "``"+bot["username"]+"#"+bot["discriminator"]+" ("+bot["id"]+")``",
                        "inline": True
                },
                {
                        "name": "<:users:571703383774461972> Dono",
                        "value": "``"+user["username"]+"#"+user["discriminator"]+" ("+user["id"]+")``",
                        "inline": True
                },
                
                {
                        "name": "<:book:571703384185503784> Livraria",
                        "value": "``"+lib+"``",
                        "inline": True
                },
                {
                        "name": "<:hastag:571703384277778462> Prefix",
                        "value": "``"+prefix+"``",
                        "inline": True
                },
                {
                        "name": "<:ranking:571703383510220811> Posição",
                        "value": "``"+pos+"``",
                        "inline": True

                },
                {
                        "name": "<:link:573715713122893839> Link",
                        "value": "[link]("+auth.home+"bot/"+bot["id"]+")",
                        "inline": True

                }
                ]
                }
                }
        API_BASE_URL = 'https://discordapp.com/api/v6'
        CREATE_MESSAGE_URL = API_BASE_URL + '/channels/{}/messages'
        TOKEN = "Bot NTc3NjA3MjcyODYwMDkwMzcz.XNwXHQ.q5g1XdHrz9_gjFuMipcH2eh-Eo0"
        CHANNEL = "571046221121060894"
        requests.post(CREATE_MESSAGE_URL.format(CHANNEL),headers={'Authorization': TOKEN},json=text) 
def send_msg_tt(content):
        text = {"content":content}
        API_BASE_URL = 'https://discordapp.com/api/v6'
        CREATE_MESSAGE_URL = API_BASE_URL + '/channels/{}/messages'
        TOKEN = "Bot NTc3NjA3MjcyODYwMDkwMzcz.XNwXHQ.q5g1XdHrz9_gjFuMipcH2eh-Eo0"
        CHANNEL = "571046221121060894"
        requests.post(CREATE_MESSAGE_URL.format(CHANNEL),headers={'Authorization': TOKEN},json=text)             
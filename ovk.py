import requests as r
import time
import telebot

channel = '@ochvk'
bottoken = '1496637502:AAHFcXZe_usN8jBOMhZC9vWmfPAoeeow1Ck'
vktoken ='f5cc7ce4f5cc7ce4f5cc7ce41cf5b95ce2ff5ccf5cc7ce4aa7142796427ee98587840e7'
version = 5.126
domain = 'ochvk'
bot = telebot.TeleBot(bottoken)

def get_post():
    count = 2
    offset = {'offset' : 0}
    response = r.get('https://api.vk.com/method/wall.get', 
                params = {
                    'access_token' : vktoken,
                    'v' : version,
                    'domain' : domain,
                    'count' : count,
                    'offset' : offset['offset']
                    })
    pinind = response.json()['response']['items'][0]['is_pinned']
    if pinind == 1:
        newid = response.json()['response']['items'][1]['id']
        data = response.json()['response']['items'][1]['attachments'][0]['photo']['sizes'][-1]['url']
        post = [newid, data]
        return post
    elif pinind == 0:
        newid = response.json()['response']['items'][0]['id']
        data = response.json()['response']['items'][0]['attachments'][0]['photo']['sizes'][-1]['url']
        post = [newid, data]
        return post
        
def send_post(postid):
    
    if get_post()[0] > postid['id']:
        bot.send_photo(channel, get_post()[1])

def main():
    postid = {'id': 1966}
    while True:
        get_post()
        send_post(postid)
        postid['id'] = get_post()[0]
        time.sleep(30)

if __name__ == "__main__":
    main()



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
        
def send_post():
    with open('id.txt', 'r+') as ids:
        idlist = []
        for i in ids:
            idlist.append(i)
        postid = int(idlist[-1])  
        if get_post()[0] > postid:
            bot.send_photo(channel, get_post()[1])
            ids.write('\n' + str(get_post()[0]))
        

def main():
    while True:
        get_post()
        send_post()     
        time.sleep(15)

if __name__ == "__main__":
    main()



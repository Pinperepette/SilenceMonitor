#!/usr/bin/env python
import json
import requests
import urllib.parse
from twitter_client import TwitterClient
import time

def send_message(message, telegram_token, telegram_chat_id):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}&text={urllib.parse.quote(message)}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Errore durante l'invio del messaggio Telegram: {response.status_code}, {response.text}")

def main():
    with open('config.json', 'r') as file:
        config = json.load(file)
        
    client = TwitterClient(config)
    
    telegram_token = config.get("telegram_token")
    telegram_chat_id = config.get("telegram_chat_id")

    trending_topics = client.get_trends()
    print("Trending Topics ottenuti:", trending_topics)

    for trend in trending_topics:
        if not trend.startswith('#'):
            trend = f'#{trend}'
        
        print(f"Searching for trend: {trend}")
        time.sleep(60)
        try:
            results = client.search(query=trend, count=20)
            #print(results)
            
            if 'errors' in results:
                for error in results['errors']:

                    print(f"Errore trovato per il trend '{trend}': {error['message']}")
                    
                    if 'denylisted' in error['message']:
                        error_message = f"Errore trovato per il trend '{trend}': {error['message']}"
                        send_message(error_message, telegram_token, telegram_chat_id)
                        break  

        except Exception as e:
            error_message = f"Errore durante la ricerca del trend '{trend}': {str(e)}"
            print(error_message)
            send_message(error_message, telegram_token, telegram_chat_id)

if __name__ == "__main__":
    main()

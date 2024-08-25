#!/usr/bin/env python

import requests
import json
from bs4 import BeautifulSoup

class TwitterClient:
    def __init__(self, config):
        self.cookies = config['cookies']
        self.headers = config['headers']
        self.base_url = 'https://x.com/i/api/graphql/UN1i3zUiCWa-6r-Uaho4fw/SearchTimeline'
    
    def search(self, query, count=20):
        params = {
            'variables': json.dumps({
                "rawQuery": query,
                "count": count,
                "querySource": "recent_search_click",
                "product": "Top"
            }),
            'features': json.dumps({
                "rweb_tipjar_consumption_enabled": True,
                "responsive_web_graphql_exclude_directive_enabled": True,
                "verified_phone_label_enabled": False,
                "creator_subscriptions_tweet_preview_api_enabled": True,
                "responsive_web_graphql_timeline_navigation_enabled": True,
                "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                "communities_web_enable_tweet_community_results_fetch": True,
                "c9s_tweet_anatomy_moderator_badge_enabled": True,
                "articles_preview_enabled": True,
                "responsive_web_edit_tweet_api_enabled": True,
                "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
                "view_counts_everywhere_api_enabled": True,
                "longform_notetweets_consumption_enabled": True,
                "responsive_web_twitter_article_tweet_consumption_enabled": True,
                "tweet_awards_web_tipping_enabled": False,
                "creator_subscriptions_quote_tweet_preview_enabled": False,
                "freedom_of_speech_not_reach_fetch_enabled": True,
                "standardized_nudges_misinfo": True,
                "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
                "rweb_video_timestamps_enabled": True,
                "longform_notetweets_rich_text_read_enabled": True,
                "longform_notetweets_inline_media_enabled": True,
                "responsive_web_enhance_cards_enabled": False
            })
        }
        
        response = requests.get(
            self.base_url,
            params=params,
            cookies=self.cookies,
            headers=self.headers
        )
        
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}, {response.text}")
        
        return response.json()

    def get_trends(self):
        url = 'https://twitter-trends.iamrohit.in/italy'
        response = requests.get(url, cookies=self.cookies, headers=self.headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('tr')
            
            trending_topics = []
            
            for row in rows:
                columns = row.find_all('th')
                if len(columns) > 1:
                    link_tag = columns[1].find('a')
                    if link_tag:
                        trend = link_tag.text.strip()
                        trending_topics.append(trend)
            
            return trending_topics
        else:
            raise Exception(f"Errore nella richiesta: {response.status_code}")


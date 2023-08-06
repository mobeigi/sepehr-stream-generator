from .sepehr_channel import SepehrChannel

import mechanicalsoup
import string
import random
from time import time

class Browser:
    BASE_API_URL = "https://sepehrapi.sepehrtv.ir"

    def __init__(self):
        """ Initialize browser as needed """
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

    def generate_oauth_authorization_field(self):
        """ Generate data for OAuth Authorization header """
        timestamp = int(time())
        oauth_nonce = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32)) # nonce is seemingly random 32 length string
        return f'OAuth oauth_consumer_key="84ALFkdjpBX0DSR3DsaLo364lKs1hTGq", oauth_nonce="{oauth_nonce}", oauth_signature="OGUzYWY4NGE2ZTE2YzRmOTJjMmY3YTA0MTFmZjc3ODUzNjIwMTJhZg%3D%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="{timestamp}", oauth_token="b49255684ad9347386d890a04a642bfa7052d69ca568938b622ca7d84ed93972", oauth_version="1.0"'

    def get_all_sepehr_channels(self):
        """ Get all of Sepehrs channel list"""
        SEPEHR_API_ALL_CHANNELS_URL = f'{self.BASE_API_URL}/v3/channels/1?page_size=1000&page=1&include_media_resources=true&include_details=true'
        
        headers = {
            'Authorization': self.generate_oauth_authorization_field() 
        }
        response = self.browser.get(SEPEHR_API_ALL_CHANNELS_URL, headers=headers)

        if response.status_code != 200:
            raise SystemError

        # Check we received the listing data we needed
        json = response.json()
        if 'list' not in json or json['list'] is None or len(json['list']) == 0:
            raise SystemError
        
        sepehr_channels = []
        for channel in json["list"]:
            if 'streams' not in channel or channel['streams'] is None or len(channel['streams']) == 0 or 'src' not in channel['streams'][0]:
                # TODO: Log error
                continue

            sepehr_channel = SepehrChannel(
                channel['id'],
                channel['uid'],
                channel['name'],
                channel['type'],
                channel['icon'],
                channel['streams'][0]['src'],
            )
            sepehr_channels.append(sepehr_channel)

        return sepehr_channels

    def get_sepehr_channel_by_id(self, id):
        """ Get channel using channel id (numeric) """
        SEPEHR_API_CHANNELS_URL = f'{self.BASE_API_URL}/v3/channels/?list={id}&include_media_resources=true&include_details=true'
        return self.get_sepehr_channel(SEPEHR_API_CHANNELS_URL)
        
    def get_sepehr_channel_by_uid(self, uid):
        """ Get channel using channel uid (string) """
        SEPEHR_API_CHANNELS_URL = f'{self.BASE_API_URL}/v3/channels/?key={uid}&include_media_resources=true&include_details=true'
        return self.get_sepehr_channel(SEPEHR_API_CHANNELS_URL)

    def get_sepehr_channel(self, url):
        """ Get channel using API channel url """
        
        # Send request
        headers = {
            'Authorization': self.generate_oauth_authorization_field() 
        }
        response = self.browser.get(url, headers=headers)

        if response.status_code != 200:
            raise SystemError

        # Check we received the listing data we needed
        json = response.json()
        if 'list' not in json or json['list'] is None or len(json['list']) == 0:
            raise SystemError

        channel = response.json()['list'][0]

        if 'streams' not in channel or channel['streams'] is None or len(channel['streams']) == 0 or 'src' not in channel['streams'][0]:
            # TODO: Log error
            raise SystemError

        return SepehrChannel(
            channel['id'],
            channel['uid'],
            channel['name'],
            channel['type'],
            channel['icon'],
            channel['streams'][0]['src'],
        )

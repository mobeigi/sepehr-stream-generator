import mechanicalsoup
import re
import urllib

class Browser:
    def __init__(self):
        """ Initialize browser as needed """
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

    def get_csrf_token(self, channel):
        """ Get authorization token (CSRF protection token) that must be included in all requests """
        SEPEHR_TV_PAGE = f'https://sepehr.irib.ir/?idc=32&idt=tv&idv={channel}'
        home_page = self.browser.get(SEPEHR_TV_PAGE)

        if home_page.status_code != 200:
            raise SystemError

        return self.get_csrf_token_helper(home_page.text)


    def get_csrf_token_helper(self, text):
        """ Parse CSRF token from html """
        TOKEN_REGEXP_STRING = r'<meta name="csrf-token" content="(.*?)"'
        regexp = re.compile(TOKEN_REGEXP_STRING, re.MULTILINE)

        matches = regexp.search(text)

        if not matches or len(matches.groups()) != 1:
            raise SystemError

        return matches[1]

    def get_sepehr_link(self, channel):
        """ Get link for the provided channel """
        SEPEHR_GET_LINK_URL = f'https://sepehr.irib.ir/getLink/{channel}/tv'

        headers = {
            'X-CSRF-TOKEN': self.get_csrf_token(channel),
        }

        response = self.browser.post(SEPEHR_GET_LINK_URL, headers=headers)

        if response.status_code != 200:
            raise SystemError
        
        return response.json()

    def get_jjtvn_sepehr_frame(self, channel):
        """ Get frame for the provided channel. Must be done befroee requesting link for frame. """
        SEPEHR_GET_LINK_FRAME_URL = f'https://sepehr.irib.ir/frame/t/{channel}'

        headers = {
            'Referer': 'http://www.jjtvn.ir/'
        }

        frame = self.browser.get(SEPEHR_GET_LINK_FRAME_URL, headers=headers)

        if frame.status_code != 200:
            raise SystemError

        return frame


    def get_jjtvn_link_for_frame(self, channel, frame):
        """ Get link for frame for the provided channel """
        SEPEHR_GET_LINK_FRAME_URL = f'https://sepehr.irib.ir/getLinkFrame/{channel}'

        csrf_token = self.get_csrf_token_helper(frame.text)

        headers = {
            'X-CSRF-TOKEN': csrf_token
        }

        response = self.browser.post(SEPEHR_GET_LINK_FRAME_URL, headers=headers)
        
        if frame.status_code != 200:
            raise SystemError

        return response.json()

# -*- coding: utf-8 -*-
'''
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Subscribe to see which companies asked this question.
'''
class Codec:
    def __init__(self):
        self.s_url_prefix = 'http://d.toutiao.com/'
        self.urls = list()
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        lenth = len(self.urls)
        subfix = hex(lenth)
        s_url = self.s_url_prefix + subfix
        return s_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        subfix = shortUrl.split('/')[-1]
        index = int(subfix, 16)
        return self.urls[index-1]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

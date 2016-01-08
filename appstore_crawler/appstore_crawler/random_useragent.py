
import random
from scrapy import log
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class RandomUserAgentMiddleware(UserAgentMiddleware):
    """docstring for ClassName"""

    def __init__(self, settings, user_agent='Scrapy'):
        super(RandomUserAgentMiddleware, self).__init__()
        self.user_agent = user_agent
    
    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)

        # Add desired logging message here.   
        request.headers.setdefault('User-Agent', ua)
        spider.log(
            u'User-Agent: {} {}'.format(ua, request),
            level=log.DEBUG
        )
        """
        
        """

           #the default user_agent_list composes chrome,IE,firefox,Mozilla,opera,netscape
    #for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    ]

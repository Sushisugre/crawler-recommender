
import random
from scrapy import log
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

class RandomProxyMiddleware(HttpProxyMiddleware):
    """docstring for ClassName"""

    def __init__(self, settings):
        super(RandomProxyMiddleware, self).__init__()
        self.proxies = proxy_list
    
    def process_request(self, request, spider):
        nporxy = random.choice(self.proxy_list)

        # Add desired logging message here.   
        request.headers.setdefault('proxy', nporxy)
        spider.log(
            u'Proxy: {} {}'.format(nporxy, request),
            level=log.DEBUG
        )
        """
        
        """

           #the default user_agent_list composes chrome,IE,firefox,Mozilla,opera,netscape
    #for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    proxy_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    ]

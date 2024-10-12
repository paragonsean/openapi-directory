from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def g_etv1_scrape_emails_format(request: web.Request, website, must_include=None) -> web.Response:
    """Returns a list of emails scraped by priority (ie. e-mails appear on top level pages are first). Please note that subsequent calls to the same url will be fetched from the &lt;b&gt;cache&lt;/b&gt; (14 day flush). &lt;br/&gt;&lt;br/&gt;Will also parse patterns such as hello[at]site.com, hello[at]site[dot]com, hello(at)site.com, hello(at)site(dot)com, hello @ site.com, hello @ site . com. &lt;br/&gt;&lt;br/&gt;Please do note we cannot parse sites that require a login (for now), so for some Facebook pages it is not possible at the moment to fetch the e-mail.&lt;br/&gt;&lt;br/&gt;Finally, please note that the api will fetch links for up to 2 minutes. After that time it will start analysing the pages which have been scraped. &lt;b&gt;Therefore&lt;/b&gt; please ensure that your client has a timeout of at least &lt;b&gt;150 seconds&lt;/b&gt; (2 mins to fetch and the rest to parse). &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Please note&lt;/b&gt; that due to the fact that the api goes out to fetch the pages, the server allows only 1 concurrent request/ip. Requests which are made while the 1 request is still processing will result in a 429 code.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Please note&lt;/b&gt; that as of May 25, 2014, the main mechanism of tracking usage will be done via Mashape. You can get the free calls by signing up with the FREE plan.&lt;br/&gt;&lt;br/&gt;Please visit &lt;a href&#x3D;&#39;https://www.mashape.com/tommytcchan/scrape-website-email&#39;&gt;https://www.mashape.com/tommytcchan/scrape-website-email&lt;/a&gt;.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;There is now a limit of 5 requests per day using this sample interface.&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;

    

    :param website: &lt;p&gt;The website (ie. www.soundflair.com)&lt;/p&gt; 
    :type website: str
    :param must_include: &lt;table&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;Optional. The word(s) that the webpage must include (otherwise it will skip scraping that page). Good if you want to scrape only contact pages. Takes regex (ie. about&lt;/td&gt;       &lt;td&gt;contact).&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; 
    :type must_include: str

    """
    return web.Response(status=200)

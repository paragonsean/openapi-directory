from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def g_etv1_scrape_store_links_format(request: web.Request, website) -> web.Response:
    """Attempts to grab the google store url or the ios store url for a site, after searching through the site.

    

    :param website: &lt;p&gt;The website (ie. www.soundflair.com)&lt;/p&gt; 
    :type website: str

    """
    return web.Response(status=200)

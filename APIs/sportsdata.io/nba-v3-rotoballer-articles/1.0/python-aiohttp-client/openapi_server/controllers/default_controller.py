from typing import List, Dict
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server import util


async def rotoballer_articles(request: web.Request, format) -> web.Response:
    """RotoBaller Articles

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def rotoballer_articles_by_date(request: web.Request, format, _date) -> web.Response:
    """RotoBaller Articles by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the news. &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def rotoballer_articles_by_player(request: web.Request, format, playerid) -> web.Response:
    """RotoBaller Articles by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;10000507&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)

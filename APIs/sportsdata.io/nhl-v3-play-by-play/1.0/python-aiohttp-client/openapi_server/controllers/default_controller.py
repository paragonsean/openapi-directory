from typing import List, Dict
from aiohttp import web

from openapi_server.models.play_by_play import PlayByPlay
from openapi_server import util


async def play_by_play(request: web.Request, format, gameid) -> web.Response:
    """Play By Play

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param gameid: The GameID of an NHL game.  GameIDs can be found in the Games API.  Valid entries are &lt;code&gt;14620&lt;/code&gt; or &lt;code&gt;16905&lt;/code&gt;
    :type gameid: str

    """
    return web.Response(status=200)


async def play_by_play_delta(request: web.Request, format, _date, minutes) -> web.Response:
    """Play By Play Delta

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-JAN-31&lt;/code&gt;, &lt;code&gt;2017-OCT-01&lt;/code&gt;.
    :type _date: str
    :param minutes: Only returns plays that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt; ... &lt;code&gt;all&lt;/code&gt;.
    :type minutes: str

    """
    return web.Response(status=200)

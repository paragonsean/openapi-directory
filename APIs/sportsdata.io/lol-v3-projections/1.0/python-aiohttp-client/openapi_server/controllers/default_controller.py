from typing import List, Dict
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.player_game_projection import PlayerGameProjection
from openapi_server import util


async def dfs_slates_by_date(request: web.Request, format, _date) -> web.Response:
    """Dfs Slates By Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_date(request: web.Request, format, _date) -> web.Response:
    """Projected Player Game Stats by Date

    Projected Player Game Stats by Date

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Example: &lt;code&gt;2019-01-20&lt;/code&gt;
    :type _date: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_player(request: web.Request, format, _date, playerid) -> web.Response:
    """Projected Player Game Stats by Player

    Projected Player Game Stats by Date

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Example: &lt;code&gt;2019-01-20&lt;/code&gt;
    :type _date: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;100001500&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)

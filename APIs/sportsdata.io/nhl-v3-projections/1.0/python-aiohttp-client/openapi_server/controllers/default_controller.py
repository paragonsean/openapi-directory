from typing import List, Dict
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.player import Player
from openapi_server.models.player_game_projection import PlayerGameProjection
from openapi_server.models.starting_goaltenders import StartingGoaltenders
from openapi_server import util


async def dfs_slates_by_date(request: web.Request, format, _date) -> web.Response:
    """DFS Slates by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-DEC-01&lt;/code&gt;, &lt;code&gt;2018-FEB-15&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def injured_players(request: web.Request, format) -> web.Response:
    """Injured Players

    This endpoint provides all currently injured NHL players, along with injury details.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_date_w_injuries_dfs_salaries(request: web.Request, format, _date) -> web.Response:
    """Projected Player Game Stats by Date (w/ Injuries, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s).  &lt;br&gt;Examples: &lt;code&gt;2018-JAN-31&lt;/code&gt;, &lt;code&gt;2017-OCT-01&lt;/code&gt;.  
    :type _date: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_player_w_injuries_dfs_salaries(request: web.Request, format, _date, playerid) -> web.Response:
    """Projected Player Game Stats by Player (w/ Injuries, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s).  &lt;br&gt;Examples: &lt;code&gt;2018-JAN-31&lt;/code&gt;, &lt;code&gt;2017-OCT-01&lt;/code&gt;.  
    :type _date: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;30000378&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def starting_goaltenders_by_date(request: web.Request, format, _date) -> web.Response:
    """Starting Goaltenders by Date

    This endpoint provides the projected &amp; confirmed starting goaltenders for NHL games on a given date.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2021-OCT-12&lt;/code&gt;, &lt;code&gt;2021-DEC-09&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)

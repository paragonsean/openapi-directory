from typing import List, Dict
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.player import Player
from openapi_server.models.player_game_projection import PlayerGameProjection
from openapi_server.models.player_season_projection import PlayerSeasonProjection
from openapi_server.models.starting_lineups import StartingLineups
from openapi_server.models.team_depth_chart import TeamDepthChart
from openapi_server import util


async def depth_charts(request: web.Request, format) -> web.Response:
    """Depth Charts

    This endpoint provides a depth chart for each NBA team.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


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

    This endpoint provides all currently injured NBA players, along with injury details.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_date_w_injuries_dfs_salaries(request: web.Request, format, _date) -> web.Response:
    """Projected Player Game Stats by Date (w/ Injuries, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_player_w_injuries_dfs_salaries(request: web.Request, format, _date, playerid) -> web.Response:
    """Projected Player Game Stats by Player (w/ Injuries, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s).&lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;.
    :type _date: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;20000571&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def projected_player_season_stats(request: web.Request, format, season) -> web.Response:
    """Projected Player Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str

    """
    return web.Response(status=200)


async def projected_player_season_stats_by_player(request: web.Request, format, season, playerid) -> web.Response:
    """Projected Player Season Stats by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;20000571&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def projected_player_season_stats_by_team(request: web.Request, format, season, team) -> web.Response:
    """Projected Player Season Stats by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str
    :param team: The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;MIA&lt;/code&gt;, &lt;code&gt;PHI&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def starting_lineups_by_date(request: web.Request, format, _date) -> web.Response:
    """Starting Lineups by Date

    This endpoint provides the projected &amp; confirmed starting lineups for NBA games on a given date.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt; Examples: &lt;code&gt;2021-OCT-12&lt;/code&gt;, &lt;code&gt;2021-DEC-09&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)

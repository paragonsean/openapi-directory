from typing import List, Dict
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.player import Player
from openapi_server.models.player_game_projection import PlayerGameProjection
from openapi_server import util


async def dfs_slates_by_date(request: web.Request, format, _date) -> web.Response:
    """Dfs Slates By Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2020-02-18&lt;/code&gt; 
    :type _date: str

    """
    return web.Response(status=200)


async def injured_players_by_competition(request: web.Request, format, competition) -> web.Response:
    """Injured Players By Competition

    This endpoint provides all currently injured soccer players by competition, along with injury details.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param competition: An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: &lt;code&gt;EPL&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;MLS&lt;/code&gt;, &lt;code&gt;8&lt;/code&gt;, etc.
    :type competition: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_competition_w_dfs_salaries(request: web.Request, format, competition, _date) -> web.Response:
    """Projected Player Game Stats by Competition (w/ DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param competition: An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: &lt;code&gt;EPL&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;MLS&lt;/code&gt;, &lt;code&gt;8&lt;/code&gt;, etc.
    :type competition: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_date_w_dfs_salaries(request: web.Request, format, _date) -> web.Response:
    """Projected Player Game Stats by Date (w/ DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_player_w_dfs_salaries(request: web.Request, format, _date, playerid) -> web.Response:
    """Projected Player Game Stats by Player (w/ DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;.
    :type _date: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;90026231&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def upcoming_dfs_slates_by_competition(request: web.Request, format, competition_id) -> web.Response:
    """Upcoming Dfs Slates By Competition

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param competition_id: The Competition Id. &lt;br&gt;Examples: &lt;code&gt;3&lt;/code&gt;
    :type competition_id: str

    """
    return web.Response(status=200)

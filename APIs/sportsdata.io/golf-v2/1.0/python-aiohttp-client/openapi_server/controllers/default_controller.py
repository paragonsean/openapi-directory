from typing import List, Dict
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.injury import Injury
from openapi_server.models.leaderboard import Leaderboard
from openapi_server.models.news import News
from openapi_server.models.player import Player
from openapi_server.models.player_season import PlayerSeason
from openapi_server.models.player_tournament import PlayerTournament
from openapi_server.models.player_tournament_projection import PlayerTournamentProjection
from openapi_server.models.season import Season
from openapi_server.models.tournament import Tournament
from openapi_server import util


async def current_season(request: web.Request, format) -> web.Response:
    """Current Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def dfs_slates(request: web.Request, format, tournamentid) -> web.Response:
    """DFS Slates

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param tournamentid: The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc.
    :type tournamentid: str

    """
    return web.Response(status=200)


async def injuries(request: web.Request, format) -> web.Response:
    """Injuries

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def injuries_historical(request: web.Request, format) -> web.Response:
    """Injuries (Historical)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def leaderboard(request: web.Request, format, tournamentid) -> web.Response:
    """Leaderboard

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param tournamentid: The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc.
    :type tournamentid: str

    """
    return web.Response(status=200)


async def news(request: web.Request, format) -> web.Response:
    """News

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def news_by_date(request: web.Request, format, _date) -> web.Response:
    """News by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def news_by_player(request: web.Request, format, playerid) -> web.Response:
    """News by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player(request: web.Request, format, playerid) -> web.Response:
    """Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_season_stats_w_world_golf_rankings(request: web.Request, format, season) -> web.Response:
    """Player Season Stats (w/ World Golf Rankings)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def player_tournament_projected_stats_w_draftkings_salaries(request: web.Request, format, tournamentid) -> web.Response:
    """Player Tournament Projected Stats (w/ DraftKings Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param tournamentid: The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;78&lt;/code&gt;, &lt;code&gt;79&lt;/code&gt;, &lt;code&gt;80&lt;/code&gt;, etc.
    :type tournamentid: str

    """
    return web.Response(status=200)


async def player_tournament_stats_by_player(request: web.Request, format, tournamentid, playerid) -> web.Response:
    """Player Tournament Stats By Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param tournamentid: The TournamentID of a tournament.  TournamentIDs can be found in the Tournaments API.  Valid entries are &lt;code&gt;58&lt;/code&gt;, &lt;code&gt;61&lt;/code&gt;, etc.
    :type tournamentid: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;40000019&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def players(request: web.Request, format) -> web.Response:
    """Players

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def schedule(request: web.Request, format) -> web.Response:
    """Schedule

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def schedule_by_season(request: web.Request, format, season) -> web.Response:
    """Schedule by Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)

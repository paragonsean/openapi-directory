from typing import List, Dict
from aiohttp import web

from openapi_server.models.game import Game
from openapi_server.models.news import News
from openapi_server.models.player import Player
from openapi_server.models.player_basic import PlayerBasic
from openapi_server.models.referee import Referee
from openapi_server.models.schedule_basic import ScheduleBasic
from openapi_server.models.score_basic import ScoreBasic
from openapi_server.models.season import Season
from openapi_server.models.stadium import Stadium
from openapi_server.models.standing import Standing
from openapi_server.models.team import Team
from openapi_server.models.team_depth_chart import TeamDepthChart
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_season import TeamSeason
from openapi_server import util


async def are_games_in_progress(request: web.Request, format) -> web.Response:
    """Are Games In Progress

    Returns &lt;code&gt;true&lt;/code&gt; if there is at least one game being played at the time of the request or &lt;code&gt;false&lt;/code&gt; if there are none.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def current_season(request: web.Request, format) -> web.Response:
    """Current Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def depth_charts(request: web.Request, format) -> web.Response:
    """Depth Charts

    Returns the full list of NBA Referees.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def games_by_date(request: web.Request, format, _date) -> web.Response:
    """Games by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def games_by_date_basic(request: web.Request, format, _date) -> web.Response:
    """Games by Date (Basic)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;.
    :type _date: str

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
    :param _date: The date of the news. &lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def news_by_player(request: web.Request, format, playerid) -> web.Response:
    """News by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;10000507&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_details_by_active(request: web.Request, format) -> web.Response:
    """Player Details by Active

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_free_agent(request: web.Request, format) -> web.Response:
    """Player Details by Free Agent

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_player(request: web.Request, format, playerid) -> web.Response:
    """Player Details by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;20000571&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def players_by_team(request: web.Request, format, team) -> web.Response:
    """Players by Team

    This endpoint provides active player details by team.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param team: The abbreviation of the requested team.&lt;br&gt;Examples: &lt;code&gt;PHI&lt;/code&gt;, &lt;code&gt;BKN&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def players_by_team_basic(request: web.Request, format, team) -> web.Response:
    """Players by Team (Basic)

    This endpoint provides active player details by team.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param team: The abbreviation of the requested team.&lt;br&gt;Examples: &lt;code&gt;PHI&lt;/code&gt;, &lt;code&gt;BKN&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def referees(request: web.Request, format) -> web.Response:
    """Referees

    Returns the full list of NBA Referees.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def schedules(request: web.Request, format, season) -> web.Response:
    """Schedules

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str

    """
    return web.Response(status=200)


async def schedules_basic(request: web.Request, format, season) -> web.Response:
    """Schedules (Basic)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str

    """
    return web.Response(status=200)


async def stadiums(request: web.Request, format) -> web.Response:
    """Stadiums

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def standings(request: web.Request, format, season) -> web.Response:
    """Standings

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def team_game_logs_by_season(request: web.Request, format, season, teamid, numberofgames) -> web.Response:
    """Team Game Logs By Season

    Game by game log of total team statistics.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt;
    :type season: str
    :param teamid: Unique ID of team.  Example &lt;code&gt; 8 &lt;/code&gt;
    :type teamid: str
    :param numberofgames: How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt;
    :type numberofgames: str

    """
    return web.Response(status=200)


async def team_game_stats_by_date(request: web.Request, format, _date) -> web.Response:
    """Team Game Stats by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2015-JUL-31&lt;/code&gt;, &lt;code&gt;2015-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def team_season_stats(request: web.Request, format, season) -> web.Response:
    """Team Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def teams_active(request: web.Request, format) -> web.Response:
    """Teams (Active)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def teams_all(request: web.Request, format) -> web.Response:
    """Teams (All)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.conference import Conference
from openapi_server.models.game import Game
from openapi_server.models.player import Player
from openapi_server.models.player_basic import PlayerBasic
from openapi_server.models.schedule_basic import ScheduleBasic
from openapi_server.models.season import Season
from openapi_server.models.stadium import Stadium
from openapi_server.models.team import Team
from openapi_server.models.team_basic import TeamBasic
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_season import TeamSeason
from openapi_server import util


async def are_games_in_progress(request: web.Request, format) -> web.Response:
    """Are Games In Progress

    Returns &lt;code&gt;true&lt;/code&gt; if there is at least one game being played at the time of the request or &lt;code&gt;false&lt;/code&gt; if there are none.

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def conference_hierarchy_with_teams(request: web.Request, format) -> web.Response:
    """Conference Hierarchy (with Teams)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def current_season(request: web.Request, format) -> web.Response:
    """Current Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def current_season_details(request: web.Request, format) -> web.Response:
    """Current Season Details

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def current_seasontype(request: web.Request, format) -> web.Response:
    """Current SeasonType

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def current_week(request: web.Request, format) -> web.Response:
    """Current Week

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def games_by_date(request: web.Request, format, _date) -> web.Response:
    """Games by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str
    :param _date:            The date of the game(s).           &lt;br&gt;Examples: &lt;code&gt;2016-SEP-01&lt;/code&gt;, &lt;code&gt;2017-SEP-10&lt;/code&gt;.         
    :type _date: str

    """
    return web.Response(status=200)


async def games_by_week(request: web.Request, format, season, week) -> web.Response:
    """Games by Week

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season.           &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;, etc.         
    :type season: str
    :param week:            The week of the game(s).           &lt;br&gt;Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc.         
    :type week: str

    """
    return web.Response(status=200)


async def games_by_week_basic(request: web.Request, format, season, week) -> web.Response:
    """Games by Week (Basic)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season.           &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;, etc.         
    :type season: str
    :param week:            The week of the game(s).           &lt;br&gt;Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc.         
    :type week: str

    """
    return web.Response(status=200)


async def injured_players(request: web.Request, format) -> web.Response:
    """Injured Players

    This endpoint provides all currently injured college football players, along with injury details.

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_active(request: web.Request, format) -> web.Response:
    """Player Details By Active

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_player(request: web.Request, format, playerid) -> web.Response:
    """Player Details By Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid:            Unique FantasyData Player ID.           Example:&lt;code&gt;50002016&lt;/code&gt;.         
    :type playerid: str

    """
    return web.Response(status=200)


async def player_details_by_team(request: web.Request, format, team) -> web.Response:
    """Player Details by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param team:            The abbreviation of the requested team.           &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.         
    :type team: str

    """
    return web.Response(status=200)


async def players_by_team_basic(request: web.Request, format, team) -> web.Response:
    """Players by Team (Basic)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param team:            The abbreviation of the requested team.           &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.         
    :type team: str

    """
    return web.Response(status=200)


async def schedules(request: web.Request, format, season) -> web.Response:
    """Schedules

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str

    """
    return web.Response(status=200)


async def schedules_basic(request: web.Request, format, season) -> web.Response:
    """Schedules (Basic)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str

    """
    return web.Response(status=200)


async def stadiums(request: web.Request, format) -> web.Response:
    """Stadiums

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def team_game_logs_by_season(request: web.Request, format, season, teamid, numberofgames) -> web.Response:
    """Team Game Logs By Season

    Game by game log of total team statistics.

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str
    :param season: Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt;        
    :type season: str
    :param teamid: Unique ID of team.  Example &lt;code&gt; 1 &lt;/code&gt;
    :type teamid: str
    :param numberofgames: How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt;
    :type numberofgames: str

    """
    return web.Response(status=200)


async def team_game_stats_by_week(request: web.Request, format, season, week) -> web.Response:
    """Team Game Stats by Week

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season.           &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;, etc.         
    :type season: str
    :param week:            The week of the game(s).           &lt;br&gt;Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc.         
    :type week: str

    """
    return web.Response(status=200)


async def team_season_stats_standings(request: web.Request, format, season) -> web.Response:
    """Team Season Stats &amp; Standings

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2017POST&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def teams(request: web.Request, format) -> web.Response:
    """Teams

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def teams_basic(request: web.Request, format) -> web.Response:
    """Teams (Basic)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;xml&lt;/code&gt; or &lt;code&gt;json&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)

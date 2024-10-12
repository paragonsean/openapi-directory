from typing import List, Dict
from aiohttp import web

from openapi_server.models.box_score import BoxScore
from openapi_server.models.conference import Conference
from openapi_server.models.game import Game
from openapi_server.models.player import Player
from openapi_server.models.player_game import PlayerGame
from openapi_server.models.player_game_projection import PlayerGameProjection
from openapi_server.models.player_season import PlayerSeason
from openapi_server.models.season import Season
from openapi_server.models.stadium import Stadium
from openapi_server.models.team import Team
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_season import TeamSeason
from openapi_server.models.tournament import Tournament
from openapi_server import util


async def are_games_in_progress(request: web.Request, format) -> web.Response:
    """Are Games In Progress

    Returns &lt;code&gt;true&lt;/code&gt; if there is at least one game being played at the time of the request or &lt;code&gt;false&lt;/code&gt; if there are none.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def box_score(request: web.Request, format, gameid) -> web.Response:
    """Box Score

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param gameid: The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are &lt;code&gt;14620&lt;/code&gt; or &lt;code&gt;16905&lt;/code&gt;
    :type gameid: str

    """
    return web.Response(status=200)


async def box_scores_by_date(request: web.Request, format, _date) -> web.Response:
    """Box Scores by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def box_scores_by_date_delta(request: web.Request, format, _date, minutes) -> web.Response:
    """Box Scores by Date Delta

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;.
    :type _date: str
    :param minutes: Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are: &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.
    :type minutes: str

    """
    return web.Response(status=200)


async def current_season(request: web.Request, format) -> web.Response:
    """Current Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def games_by_date(request: web.Request, format, _date) -> web.Response:
    """Games by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def injured_players(request: web.Request, format) -> web.Response:
    """Injured Players

    This endpoint provides all currently injured college basketball players, along with injury details.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def league_hierarchy(request: web.Request, format) -> web.Response:
    """League Hierarchy

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_active(request: web.Request, format) -> web.Response:
    """Player Details by Active

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_player(request: web.Request, format, playerid) -> web.Response:
    """Player Details by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;60003802&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_details_by_team(request: web.Request, format, team) -> web.Response:
    """Player Details by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param team: The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def player_game_logs_by_season(request: web.Request, format, season, playerid, numberofgames) -> web.Response:
    """Player Game Logs By Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt;
    :type season: str
    :param playerid: Unique FantasyData Player ID.Example:&lt;code&gt;60008094&lt;/code&gt;.
    :type playerid: str
    :param numberofgames: How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt;
    :type numberofgames: str

    """
    return web.Response(status=200)


async def player_game_stats_by_date(request: web.Request, format, _date) -> web.Response:
    """Player Game Stats by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def player_game_stats_by_player(request: web.Request, format, _date, playerid) -> web.Response:
    """Player Game Stats by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;.
    :type _date: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;60003802&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_season_stats(request: web.Request, format, season) -> web.Response:
    """Player Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def player_season_stats_by_player(request: web.Request, format, season, playerid) -> web.Response:
    """Player Season Stats By Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;.
    :type season: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;60003802&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_season_stats_by_team(request: web.Request, format, season, team) -> web.Response:
    """Player Season Stats by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;.
    :type season: str
    :param team: The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_date(request: web.Request, format, _date) -> web.Response:
    """Projected Player Game Stats by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_player(request: web.Request, format, _date, playerid) -> web.Response:
    """Projected Player Game Stats by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;.
    :type _date: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;60003802&lt;/code&gt;.
    :type playerid: str

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


async def stadiums(request: web.Request, format) -> web.Response:
    """Stadiums

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def team_game_logs_by_season(request: web.Request, format, season, teamid, numberofgames) -> web.Response:
    """Team Game Logs By Season

    Game by game log of total team statistics.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt;
    :type season: str
    :param teamid: Unique ID of team.  Example &lt;code&gt; 1 &lt;/code&gt;
    :type teamid: str
    :param numberofgames: How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt;
    :type numberofgames: str

    """
    return web.Response(status=200)


async def team_game_stats_by_date(request: web.Request, format, _date) -> web.Response:
    """Team Game Stats by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-FEB-27&lt;/code&gt;, &lt;code&gt;2017-DEC-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def team_season_stats(request: web.Request, format, season) -> web.Response:
    """Team Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def teams(request: web.Request, format) -> web.Response:
    """Teams

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def tournament_hierarchy(request: web.Request, format, season) -> web.Response:
    """Tournament Hierarchy

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.box_score import BoxScore
from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.game import Game
from openapi_server.models.news import News
from openapi_server.models.player import Player
from openapi_server.models.player_game import PlayerGame
from openapi_server.models.player_season import PlayerSeason
from openapi_server.models.season import Season
from openapi_server.models.stadium import Stadium
from openapi_server.models.standing import Standing
from openapi_server.models.team import Team
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


async def batter_vs_pitcher_stats(request: web.Request, format, hitterid, pitcherid) -> web.Response:
    """Batter vs. Pitcher Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param hitterid: Unique FantasyData Player ID. Example:&lt;code&gt;10000031&lt;/code&gt;.
    :type hitterid: str
    :param pitcherid: Unique FantasyData Player ID. Example:&lt;code&gt;10000618&lt;/code&gt;.
    :type pitcherid: str

    """
    return web.Response(status=200)


async def box_score(request: web.Request, format, gameid) -> web.Response:
    """Box Score

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param gameid: The GameID of an MLB game.  GameIDs can be found in the Games API.  Valid entries are &lt;code&gt;14620&lt;/code&gt; or &lt;code&gt;16905&lt;/code&gt;
    :type gameid: str

    """
    return web.Response(status=200)


async def box_scores_by_date(request: web.Request, format, _date) -> web.Response:
    """Box Scores by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def box_scores_by_date_delta(request: web.Request, format, _date, minutes) -> web.Response:
    """Box Scores by Date Delta

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
    :type _date: str
    :param minutes: Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back. Valid entries are: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt; ... &lt;code&gt;all&lt;/code&gt;.
    :type minutes: str

    """
    return web.Response(status=200)


async def current_season(request: web.Request, format) -> web.Response:
    """Current Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def dfs_slates_by_date(request: web.Request, format, _date) -> web.Response:
    """DFS Slates by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the slates. &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def games_by_date(request: web.Request, format, _date) -> web.Response:
    """Games by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
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
    :param _date: The date of the news. &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
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


async def player_details_by_free_agents(request: web.Request, format) -> web.Response:
    """Player Details by Free Agents

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_player(request: web.Request, format, playerid) -> web.Response:
    """Player Details by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;10000507&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_game_logs_by_season(request: web.Request, format, season, playerid, numberofgames) -> web.Response:
    """Player Game Logs By Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt;
    :type season: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;10001365&lt;/code&gt;.
    :type playerid: str
    :param numberofgames: How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt;
    :type numberofgames: str

    """
    return web.Response(status=200)


async def player_game_stats_by_date(request: web.Request, format, _date) -> web.Response:
    """Player Game Stats by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def player_game_stats_by_player(request: web.Request, format, _date, playerid) -> web.Response:
    """Player Game Stats by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
    :type _date: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;10000507&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_season_away_stats(request: web.Request, format, season) -> web.Response:
    """Player Season Away Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def player_season_home_stats(request: web.Request, format, season) -> web.Response:
    """Player Season Home Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def player_season_split_stats(request: web.Request, format, season, split) -> web.Response:
    """Player Season Split Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
    :type season: str
    :param split: The desired split of stats. Currently, we support vs. Left/Right/Switch handed pitchers/hitters. Possible values are: &lt;code&gt;L&lt;/code&gt;, &lt;code&gt;R&lt;/code&gt; and &lt;code&gt;S&lt;/code&gt;
    :type split: str

    """
    return web.Response(status=200)


async def player_season_stats(request: web.Request, format, season) -> web.Response:
    """Player Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def player_season_stats_by_player(request: web.Request, format, season, playerid) -> web.Response:
    """Player Season Stats By Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
    :type season: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;10000507&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_season_stats_by_team(request: web.Request, format, season, team) -> web.Response:
    """Player Season Stats by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;. 
    :type season: str
    :param team: The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def player_season_stats_split_by_team(request: web.Request, format, season) -> web.Response:
    """Player Season Stats Split By Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def players_by_team(request: web.Request, format, team) -> web.Response:
    """Players by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param team: The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.
    :type team: str

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


async def standings(request: web.Request, format, season) -> web.Response:
    """Standings

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
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
    :param teamid: Unique ID of team.  Example &lt;code&gt; 12 &lt;/code&gt;
    :type teamid: str
    :param numberofgames: How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt;
    :type numberofgames: str

    """
    return web.Response(status=200)


async def team_game_stats_by_date(request: web.Request, format, _date) -> web.Response:
    """Team Game Stats by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def team_hitting_vs_starting_pitcher(request: web.Request, format, gameid, team) -> web.Response:
    """Team Hitting vs. Starting Pitcher

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param gameid: The GameID of an MLB game.  GameIDs can be found in the Games API.  Valid entries are &lt;code&gt;14620&lt;/code&gt; or &lt;code&gt;16905&lt;/code&gt;
    :type gameid: str
    :param team: The abbreviation of the requested team. &lt;br&gt;Examples: &lt;code&gt;SF&lt;/code&gt;, &lt;code&gt;NYY&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def team_season_stats(request: web.Request, format, season) -> web.Response:
    """Team Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2017&lt;/code&gt;, &lt;code&gt;2018&lt;/code&gt;.
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

from typing import List, Dict
from aiohttp import web

from openapi_server.models.box_score import BoxScore
from openapi_server.models.game import Game
from openapi_server.models.game_media import GameMedia
from openapi_server.models.game_weather import GameWeather
from openapi_server.models.player_game import PlayerGame
from openapi_server.models.scoreboard_game import ScoreboardGame
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_record import TeamRecord
from openapi_server.models.week import Week
from openapi_server import util


async def get_advanced_box_score(request: web.Request, game_id) -> web.Response:
    """Advanced box scores

    Get advanced box score data

    :param game_id: Game id parameters
    :type game_id: int

    """
    return web.Response(status=200)


async def get_calendar(request: web.Request, year) -> web.Response:
    """Season calendar

    Get calendar of weeks by season

    :param year: Year filter
    :type year: int

    """
    return web.Response(status=200)


async def get_game_media(request: web.Request, year, week=None, season_type=None, team=None, conference=None, media_type=None, classification=None) -> web.Response:
    """Game media information and schedules

    Game media information (TV, radio, etc)

    :param year: Year filter
    :type year: int
    :param week: Week filter
    :type week: int
    :param season_type: Season type filter (regular, postseason, or both)
    :type season_type: str
    :param team: Team filter
    :type team: str
    :param conference: Conference filter
    :type conference: str
    :param media_type: Media type filter (tv, radio, web, ppv, or mobile)
    :type media_type: str
    :param classification: Division classification filter (fbs/fcs/ii/iii)
    :type classification: str

    """
    return web.Response(status=200)


async def get_game_weather(request: web.Request, game_id=None, year=None, week=None, season_type=None, team=None, conference=None, classification=None) -> web.Response:
    """Game weather information (Patreon only)

    Weather information for the hour of kickoff

    :param game_id: Game id filter (required if no year)
    :type game_id: int
    :param year: Year filter (required if no game id)
    :type year: int
    :param week: Week filter
    :type week: int
    :param season_type: Season type filter (regular, postseason, or both)
    :type season_type: str
    :param team: Team filter
    :type team: str
    :param conference: Conference filter
    :type conference: str
    :param classification: Division classification filter (fbs/fcs/ii/iii)
    :type classification: str

    """
    return web.Response(status=200)


async def get_games(request: web.Request, year, week=None, season_type=None, team=None, home=None, away=None, conference=None, division=None, id=None) -> web.Response:
    """Games and results

    Get game results

    :param year: Year/season filter for games
    :type year: int
    :param week: Week filter
    :type week: int
    :param season_type: Season type filter (regular or postseason)
    :type season_type: str
    :param team: Team
    :type team: str
    :param home: Home team filter
    :type home: str
    :param away: Away team filter
    :type away: str
    :param conference: Conference abbreviation filter
    :type conference: str
    :param division: Division classification filter (fbs/fcs/ii/iii)
    :type division: str
    :param id: id filter for querying a single game
    :type id: int

    """
    return web.Response(status=200)


async def get_player_game_stats(request: web.Request, year, week=None, season_type=None, team=None, conference=None, category=None, game_id=None) -> web.Response:
    """Player game stats

    Player stats broken down by game

    :param year: Year/season filter for games
    :type year: int
    :param week: Week filter
    :type week: int
    :param season_type: Season type filter (regular or postseason)
    :type season_type: str
    :param team: Team filter
    :type team: str
    :param conference: Conference abbreviation filter
    :type conference: str
    :param category: Category filter (e.g defensive)
    :type category: str
    :param game_id: Game id filter
    :type game_id: int

    """
    return web.Response(status=200)


async def get_scoreboard(request: web.Request, classification=None, conference=None) -> web.Response:
    """Live game results (Patreon only)

    Get live game results

    :param classification: Classification filter (fbs, fcs, ii, or iii). Defaults to fbs.
    :type classification: str
    :param conference: Conference abbreviation filter.
    :type conference: str

    """
    return web.Response(status=200)


async def get_team_game_stats(request: web.Request, year, week=None, season_type=None, team=None, conference=None, game_id=None, classification=None) -> web.Response:
    """Team game stats

    Team stats broken down by game

    :param year: Year/season filter for games
    :type year: int
    :param week: Week filter
    :type week: int
    :param season_type: Season type filter (regular or postseason)
    :type season_type: str
    :param team: Team filter
    :type team: str
    :param conference: Conference abbreviation filter
    :type conference: str
    :param game_id: Game id filter
    :type game_id: int
    :param classification: Division classification filter (fbs/fcs/ii/iii)
    :type classification: str

    """
    return web.Response(status=200)


async def get_team_records(request: web.Request, year=None, team=None, conference=None) -> web.Response:
    """Team records

    Get team records by year

    :param year: Year filter
    :type year: int
    :param team: Team filter
    :type team: str
    :param conference: Conference filter
    :type conference: str

    """
    return web.Response(status=200)

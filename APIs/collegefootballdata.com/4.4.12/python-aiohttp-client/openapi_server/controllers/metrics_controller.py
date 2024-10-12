from typing import List, Dict
from aiohttp import web

from openapi_server.models.game_ppa import GamePPA
from openapi_server.models.play_wp import PlayWP
from openapi_server.models.player_game_ppa import PlayerGamePPA
from openapi_server.models.player_season_ppa import PlayerSeasonPPA
from openapi_server.models.predicted_points import PredictedPoints
from openapi_server.models.pregame_wp import PregameWP
from openapi_server.models.team_ppa import TeamPPA
from openapi_server import util


async def get_game_ppa(request: web.Request, year, week=None, team=None, conference=None, exclude_garbage_time=None, season_type=None) -> web.Response:
    """Team Predicated Points Added (PPA/EPA) by game

    Predicted Points Added (PPA) by game

    :param year: Year filter
    :type year: int
    :param week: Week filter
    :type week: int
    :param team: Team filter
    :type team: str
    :param conference: Conference filter
    :type conference: str
    :param exclude_garbage_time: Filter to remove garbage time plays from calculations
    :type exclude_garbage_time: bool
    :param season_type: Season type filter (regular or postseason)
    :type season_type: str

    """
    return web.Response(status=200)


async def get_player_game_ppa(request: web.Request, year=None, week=None, team=None, position=None, player_id=None, threshold=None, exclude_garbage_time=None, season_type=None) -> web.Response:
    """Player Predicated Points Added (PPA/EPA) broken down by game

    Predicted Points Added (PPA) by player game

    :param year: Year filter
    :type year: int
    :param week: Week filter
    :type week: int
    :param team: Team filter
    :type team: str
    :param position: Position abbreviation filter
    :type position: str
    :param player_id: Player id filter
    :type player_id: int
    :param threshold: Minimum play threshold filter
    :type threshold: str
    :param exclude_garbage_time: Filter to remove garbage time plays from calculations
    :type exclude_garbage_time: bool
    :param season_type: Season type filter (regular or postseason)
    :type season_type: str

    """
    return web.Response(status=200)


async def get_player_season_ppa(request: web.Request, year=None, team=None, conference=None, position=None, player_id=None, threshold=None, exclude_garbage_time=None) -> web.Response:
    """Player Predicated Points Added (PPA/EPA) broken down by season

    Predicted Points Added (PPA) by player season

    :param year: Year filter
    :type year: int
    :param team: Team filter
    :type team: str
    :param conference: Conference abbreviation filter
    :type conference: str
    :param position: Position abbreviation filter
    :type position: str
    :param player_id: Player id filter
    :type player_id: int
    :param threshold: Minimum play threshold filter
    :type threshold: str
    :param exclude_garbage_time: Filter to remove garbage time plays from calculations
    :type exclude_garbage_time: bool

    """
    return web.Response(status=200)


async def get_predicted_points(request: web.Request, down, distance) -> web.Response:
    """Predicted Points (i.e. Expected Points or EP)

    Predicted Points

    :param down: Down filter
    :type down: int
    :param distance: Distance filter
    :type distance: int

    """
    return web.Response(status=200)


async def get_pregame_win_probabilities(request: web.Request, year=None, week=None, team=None, season_type=None) -> web.Response:
    """Pregame win probability data

    Pregame win probabilities

    :param year: Year filter
    :type year: int
    :param week: Week filter
    :type week: int
    :param team: Team filter
    :type team: str
    :param season_type: regular or postseason
    :type season_type: str

    """
    return web.Response(status=200)


async def get_team_ppa(request: web.Request, year=None, team=None, conference=None, exclude_garbage_time=None) -> web.Response:
    """Predicted Points Added (PPA/EPA) data by team

    Predicted Points Added (PPA)

    :param year: Year filter (required if team not specified)
    :type year: int
    :param team: Team filter (required if year not specified)
    :type team: str
    :param conference: Conference filter
    :type conference: str
    :param exclude_garbage_time: Filter to remove garbage time plays from calculations
    :type exclude_garbage_time: bool

    """
    return web.Response(status=200)


async def get_win_probability_data(request: web.Request, game_id) -> web.Response:
    """Win probability chart data

    Win probability data

    :param game_id: Game id filter
    :type game_id: int

    """
    return web.Response(status=200)

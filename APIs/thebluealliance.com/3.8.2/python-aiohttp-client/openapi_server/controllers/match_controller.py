from typing import List, Dict
from aiohttp import web

from openapi_server.models.match import Match
from openapi_server.models.match_simple import MatchSimple
from openapi_server.models.zebra import Zebra
from openapi_server import util


async def get_event_match_timeseries_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_match_timeseries_0

    Gets an array of Match Keys for the given event key that have timeseries data. Returns an empty array if no matches have timeseries data. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_matches_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_matches_0

    Gets a list of matches for the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_matches_keys_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_matches_keys_0

    Gets a list of match keys for the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_matches_simple_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_matches_simple_0

    Gets a short-form list of matches for the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_match(request: web.Request, match_key, if_none_match=None) -> web.Response:
    """get_match

    Gets a &#x60;Match&#x60; object for the given match key.

    :param match_key: TBA Match Key, eg &#x60;2016nytr_qm1&#x60;
    :type match_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_match_simple(request: web.Request, match_key, if_none_match=None) -> web.Response:
    """get_match_simple

    Gets a short-form &#x60;Match&#x60; object for the given match key.

    :param match_key: TBA Match Key, eg &#x60;2016nytr_qm1&#x60;
    :type match_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_match_timeseries(request: web.Request, match_key, if_none_match=None) -> web.Response:
    """get_match_timeseries

    Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if not available. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.

    :param match_key: TBA Match Key, eg &#x60;2016nytr_qm1&#x60;
    :type match_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_match_zebra(request: web.Request, match_key, if_none_match=None) -> web.Response:
    """get_match_zebra

    Gets Zebra MotionWorks data for a Match for the given match key.

    :param match_key: TBA Match Key, eg &#x60;2016nytr_qm1&#x60;
    :type match_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches_1(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches_1

    Gets a list of matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches_keys_1(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches_keys_1

    Gets a list of match keys for matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches_simple_1(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches_simple_1

    Gets a short-form list of matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_matches_by_year_0(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_matches_by_year_0

    Gets a list of matches for the given team and year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_matches_by_year_keys_0(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_matches_by_year_keys_0

    Gets a list of match keys for matches for the given team and year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_matches_by_year_simple_0(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_matches_by_year_simple_0

    Gets a short-form list of matches for the given team and year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)

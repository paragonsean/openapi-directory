from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_list import DistrictList
from openapi_server.models.district_ranking import DistrictRanking
from openapi_server.models.event import Event
from openapi_server.models.event_district_points import EventDistrictPoints
from openapi_server.models.event_simple import EventSimple
from openapi_server.models.team import Team
from openapi_server.models.team_simple import TeamSimple
from openapi_server import util


async def get_district_events(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events

    Gets a list of events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_events_keys(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events_keys

    Gets a list of event keys for events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_events_simple(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events_simple

    Gets a short-form list of events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_rankings(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_rankings

    Gets a list of team district rankings for the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams

    Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams_keys(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams_keys

    Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams_simple(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams_simple

    Gets a short-form list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_districts_by_year(request: web.Request, year, if_none_match=None) -> web.Response:
    """get_districts_by_year

    Gets a list of districts and their corresponding district key, for the given year.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_district_points_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_district_points_0

    Gets a list of team rankings for the Event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_districts_0(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_districts_0

    Gets an array of districts representing each year the team was in a district. Will return an empty array if the team was never in a district.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.district_ranking import DistrictRanking
from openapi_server.models.event import Event
from openapi_server.models.event_simple import EventSimple
from openapi_server.models.team import Team
from openapi_server.models.team_event_status import TeamEventStatus
from openapi_server.models.team_simple import TeamSimple
from openapi_server import util


async def get_district_events_1(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events_1

    Gets a list of events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_events_keys_1(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events_keys_1

    Gets a list of event keys for events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_events_simple_1(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events_simple_1

    Gets a short-form list of events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_rankings_1(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_rankings_1

    Gets a list of team district rankings for the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams_1(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams_1

    Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams_keys_1(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams_keys_1

    Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams_simple_1(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams_simple_1

    Gets a short-form list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_1(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_1

    Gets a list of &#x60;Team&#x60; objects that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_keys_1(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_keys_1

    Gets a list of &#x60;Team&#x60; keys that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_simple_1(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_simple_1

    Gets a short-form list of &#x60;Team&#x60; objects that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_statuses_1(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_statuses_1

    Gets a key-value list of the event statuses for teams competing at the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_events_by_year_0(request: web.Request, year, if_none_match=None) -> web.Response:
    """get_events_by_year_0

    Gets a list of events in the given year.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_events_by_year_keys_0(request: web.Request, year, if_none_match=None) -> web.Response:
    """get_events_by_year_keys_0

    Gets a list of event keys in the given year.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_events_by_year_simple_0(request: web.Request, year, if_none_match=None) -> web.Response:
    """get_events_by_year_simple_0

    Gets a short-form list of events in the given year.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_statuses_by_year(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_statuses_by_year

    Gets a key-value list of the event statuses for events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_0(request: web.Request, page_num, if_none_match=None) -> web.Response:
    """get_teams_0

    Gets a list of &#x60;Team&#x60; objects, paginated in groups of 500.

    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_by_year_0(request: web.Request, year, page_num, if_none_match=None) -> web.Response:
    """get_teams_by_year_0

    Gets a list of &#x60;Team&#x60; objects that competed in the given year, paginated in groups of 500.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_by_year_keys_0(request: web.Request, year, page_num, if_none_match=None) -> web.Response:
    """get_teams_by_year_keys_0

    Gets a list Team Keys that competed in the given year, paginated in groups of 500.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_by_year_simple_0(request: web.Request, year, page_num, if_none_match=None) -> web.Response:
    """get_teams_by_year_simple_0

    Gets a list of short form &#x60;Team_Simple&#x60; objects that competed in the given year, paginated in groups of 500.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_keys_0(request: web.Request, page_num, if_none_match=None) -> web.Response:
    """get_teams_keys_0

    Gets a list of Team keys, paginated in groups of 500. (Note, each page will not have 500 teams, but will include the teams within that range of 500.)

    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_simple_0(request: web.Request, page_num, if_none_match=None) -> web.Response:
    """get_teams_simple_0

    Gets a list of short form &#x60;Team_Simple&#x60; objects, paginated in groups of 500.

    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)

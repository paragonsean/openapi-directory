from typing import List, Dict
from aiohttp import web

from openapi_server.models.award import Award
from openapi_server.models.elimination_alliance import EliminationAlliance
from openapi_server.models.event import Event
from openapi_server.models.event_district_points import EventDistrictPoints
from openapi_server.models.event_insights import EventInsights
from openapi_server.models.event_oprs import EventOPRs
from openapi_server.models.event_ranking import EventRanking
from openapi_server.models.event_simple import EventSimple
from openapi_server.models.match import Match
from openapi_server.models.match_simple import MatchSimple
from openapi_server.models.team import Team
from openapi_server.models.team_event_status import TeamEventStatus
from openapi_server.models.team_simple import TeamSimple
from openapi_server import util


async def get_district_events_0(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events_0

    Gets a list of events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_events_keys_0(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events_keys_0

    Gets a list of event keys for events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_events_simple_0(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_events_simple_0

    Gets a short-form list of events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event

    Gets an Event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_alliances(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_alliances

    Gets a list of Elimination Alliances for the given Event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_awards(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_awards

    Gets a list of awards from the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_district_points(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_district_points

    Gets a list of team rankings for the Event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_insights(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_insights

    Gets a set of Event-specific insights for the given Event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_match_timeseries(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_match_timeseries

    Gets an array of Match Keys for the given event key that have timeseries data. Returns an empty array if no matches have timeseries data. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_matches(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_matches

    Gets a list of matches for the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_matches_keys(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_matches_keys

    Gets a list of match keys for the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_matches_simple(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_matches_simple

    Gets a short-form list of matches for the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_oprs(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_oprs

    Gets a set of Event OPRs (including OPR, DPR, and CCWM) for the given Event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_predictions(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_predictions

    Gets information on TBA-generated predictions for the given Event. Contains year-specific information. *WARNING* This endpoint is currently under development and may change at any time.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_rankings(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_rankings

    Gets a list of team rankings for the Event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_simple(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_simple

    Gets a short-form Event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams

    Gets a list of &#x60;Team&#x60; objects that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_keys(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_keys

    Gets a list of &#x60;Team&#x60; keys that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_simple(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_simple

    Gets a short-form list of &#x60;Team&#x60; objects that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_statuses(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_statuses

    Gets a key-value list of the event statuses for teams competing at the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_events_by_year(request: web.Request, year, if_none_match=None) -> web.Response:
    """get_events_by_year

    Gets a list of events in the given year.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_events_by_year_keys(request: web.Request, year, if_none_match=None) -> web.Response:
    """get_events_by_year_keys

    Gets a list of event keys in the given year.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_events_by_year_simple(request: web.Request, year, if_none_match=None) -> web.Response:
    """get_events_by_year_simple

    Gets a short-form list of events in the given year.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_awards_0(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_awards_0

    Gets a list of awards the given team won at the given event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches_0(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches_0

    Gets a list of matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches_keys_0(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches_keys_0

    Gets a list of match keys for matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches_simple_0(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches_simple_0

    Gets a short-form list of matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_status_0(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_status_0

    Gets the competition rank and status of the team at the given event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_0(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_events_0

    Gets a list of all events this team has competed at.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_by_year_0(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_by_year_0

    Gets a list of events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_by_year_keys_0(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_by_year_keys_0

    Gets a list of the event keys for events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_by_year_simple_0(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_by_year_simple_0

    Gets a short-form list of events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_keys_0(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_events_keys_0

    Gets a list of the event keys for all events this team has competed at.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_simple_0(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_events_simple_0

    Gets a short-form list of all events this team has competed at.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_statuses_by_year_1(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_statuses_by_year_1

    Gets a key-value list of the event statuses for events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)

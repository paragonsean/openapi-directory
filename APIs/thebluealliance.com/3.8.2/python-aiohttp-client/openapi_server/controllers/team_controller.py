from typing import List, Dict
from aiohttp import web

from openapi_server.models.award import Award
from openapi_server.models.district_list import DistrictList
from openapi_server.models.district_ranking import DistrictRanking
from openapi_server.models.event import Event
from openapi_server.models.event_simple import EventSimple
from openapi_server.models.match import Match
from openapi_server.models.match_simple import MatchSimple
from openapi_server.models.media import Media
from openapi_server.models.team import Team
from openapi_server.models.team_event_status import TeamEventStatus
from openapi_server.models.team_robot import TeamRobot
from openapi_server.models.team_simple import TeamSimple
from openapi_server import util


async def get_district_rankings_0(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_rankings_0

    Gets a list of team district rankings for the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams_0(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams_0

    Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams_keys_0(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams_keys_0

    Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_district_teams_simple_0(request: web.Request, district_key, if_none_match=None) -> web.Response:
    """get_district_teams_simple_0

    Gets a short-form list of &#x60;Team&#x60; objects that competed in events in the given district.

    :param district_key: TBA District Key, eg &#x60;2016fim&#x60;
    :type district_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_0

    Gets a list of &#x60;Team&#x60; objects that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_keys_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_keys_0

    Gets a list of &#x60;Team&#x60; keys that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_simple_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_simple_0

    Gets a short-form list of &#x60;Team&#x60; objects that competed in the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_event_teams_statuses_0(request: web.Request, event_key, if_none_match=None) -> web.Response:
    """get_event_teams_statuses_0

    Gets a key-value list of the event statuses for teams competing at the given event.

    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team

    Gets a &#x60;Team&#x60; object for the team referenced by the given key.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_awards(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_awards

    Gets a list of awards the given team has won.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_awards_by_year(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_awards_by_year

    Gets a list of awards the given team has won in a given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_districts(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_districts

    Gets an array of districts representing each year the team was in a district. Will return an empty array if the team was never in a district.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_awards(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_awards

    Gets a list of awards the given team won at the given event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches

    Gets a list of matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches_keys(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches_keys

    Gets a list of match keys for matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_matches_simple(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_matches_simple

    Gets a short-form list of matches for the given team and event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_event_status(request: web.Request, team_key, event_key, if_none_match=None) -> web.Response:
    """get_team_event_status

    Gets the competition rank and status of the team at the given event.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param event_key: TBA Event Key, eg &#x60;2016nytr&#x60;
    :type event_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_events

    Gets a list of all events this team has competed at.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_by_year(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_by_year

    Gets a list of events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_by_year_keys(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_by_year_keys

    Gets a list of the event keys for events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_by_year_simple(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_by_year_simple

    Gets a short-form list of events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_keys(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_events_keys

    Gets a list of the event keys for all events this team has competed at.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_simple(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_events_simple

    Gets a short-form list of all events this team has competed at.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_events_statuses_by_year_0(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_events_statuses_by_year_0

    Gets a key-value list of the event statuses for events this team has competed at in the given year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_matches_by_year(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_matches_by_year

    Gets a list of matches for the given team and year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_matches_by_year_keys(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_matches_by_year_keys

    Gets a list of match keys for matches for the given team and year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_matches_by_year_simple(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_matches_by_year_simple

    Gets a short-form list of matches for the given team and year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_media_by_tag(request: web.Request, team_key, media_tag, if_none_match=None) -> web.Response:
    """get_team_media_by_tag

    Gets a list of Media (videos / pictures) for the given team and tag.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param media_tag: Media Tag which describes the Media.
    :type media_tag: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_media_by_tag_year(request: web.Request, team_key, media_tag, year, if_none_match=None) -> web.Response:
    """get_team_media_by_tag_year

    Gets a list of Media (videos / pictures) for the given team, tag and year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param media_tag: Media Tag which describes the Media.
    :type media_tag: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_media_by_year(request: web.Request, team_key, year, if_none_match=None) -> web.Response:
    """get_team_media_by_year

    Gets a list of Media (videos / pictures) for the given team and year.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_robots(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_robots

    Gets a list of year and robot name pairs for each year that a robot name was provided. Will return an empty array if the team has never named a robot.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_simple(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_simple

    Gets a &#x60;Team_Simple&#x60; object for the team referenced by the given key.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_social_media(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_social_media

    Gets a list of Media (social media) for the given team.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_team_years_participated(request: web.Request, team_key, if_none_match=None) -> web.Response:
    """get_team_years_participated

    Gets a list of years in which the team participated in at least one competition.

    :param team_key: TBA Team Key, eg &#x60;frc254&#x60;
    :type team_key: str
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams(request: web.Request, page_num, if_none_match=None) -> web.Response:
    """get_teams

    Gets a list of &#x60;Team&#x60; objects, paginated in groups of 500.

    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_by_year(request: web.Request, year, page_num, if_none_match=None) -> web.Response:
    """get_teams_by_year

    Gets a list of &#x60;Team&#x60; objects that competed in the given year, paginated in groups of 500.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_by_year_keys(request: web.Request, year, page_num, if_none_match=None) -> web.Response:
    """get_teams_by_year_keys

    Gets a list Team Keys that competed in the given year, paginated in groups of 500.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_by_year_simple(request: web.Request, year, page_num, if_none_match=None) -> web.Response:
    """get_teams_by_year_simple

    Gets a list of short form &#x60;Team_Simple&#x60; objects that competed in the given year, paginated in groups of 500.

    :param year: Competition Year (or Season). Must be 4 digits.
    :type year: int
    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_keys(request: web.Request, page_num, if_none_match=None) -> web.Response:
    """get_teams_keys

    Gets a list of Team keys, paginated in groups of 500. (Note, each page will not have 500 teams, but will include the teams within that range of 500.)

    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_teams_simple(request: web.Request, page_num, if_none_match=None) -> web.Response:
    """get_teams_simple

    Gets a list of short form &#x60;Team_Simple&#x60; objects, paginated in groups of 500.

    :param page_num: Page number of results to return, zero-indexed
    :type page_num: int
    :param if_none_match: Value of the &#x60;ETag&#x60; header in the most recently cached response by the client.
    :type if_none_match: str

    """
    return web.Response(status=200)

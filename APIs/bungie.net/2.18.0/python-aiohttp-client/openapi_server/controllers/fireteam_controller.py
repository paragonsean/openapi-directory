from typing import List, Dict
from aiohttp import web

from openapi_server.models.destiny2_equip_item200_response import Destiny2EquipItem200Response
from openapi_server.models.fireteam_get_available_clan_fireteams200_response import FireteamGetAvailableClanFireteams200Response
from openapi_server.models.fireteam_get_clan_fireteam200_response import FireteamGetClanFireteam200Response
from openapi_server.models.fireteam_get_my_clan_fireteams200_response import FireteamGetMyClanFireteams200Response
from openapi_server import util


async def fireteam_get_active_private_clan_fireteam_count(request: web.Request, group_id) -> web.Response:
    """fireteam_get_active_private_clan_fireteam_count

    Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

    :param group_id: The group id of the clan.
    :type group_id: int

    """
    return web.Response(status=200)


async def fireteam_get_available_clan_fireteams(request: web.Request, activity_type, date_range, group_id, page, platform, public_only, slot_filter, exclude_immediate=None, lang_filter=None) -> web.Response:
    """fireteam_get_available_clan_fireteams

    Gets a listing of all of this clan&#39;s fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

    :param activity_type: The activity type to filter by.
    :type activity_type: int
    :param date_range: The date range to grab available fireteams.
    :type date_range: int
    :param group_id: The group id of the clan.
    :type group_id: int
    :param page: Zero based page
    :type page: int
    :param platform: The platform filter.
    :type platform: int
    :param public_only: Determines public/private filtering.
    :type public_only: int
    :param slot_filter: Filters based on available slots
    :type slot_filter: int
    :param exclude_immediate: If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
    :type exclude_immediate: bool
    :param lang_filter: An optional language filter.
    :type lang_filter: str

    """
    return web.Response(status=200)


async def fireteam_get_clan_fireteam(request: web.Request, fireteam_id, group_id) -> web.Response:
    """fireteam_get_clan_fireteam

    Gets a specific fireteam.

    :param fireteam_id: The unique id of the fireteam.
    :type fireteam_id: int
    :param group_id: The group id of the clan.
    :type group_id: int

    """
    return web.Response(status=200)


async def fireteam_get_my_clan_fireteams(request: web.Request, group_id, include_closed, page, platform, group_filter=None, lang_filter=None) -> web.Response:
    """fireteam_get_my_clan_fireteams

    Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

    :param group_id: The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).
    :type group_id: int
    :param include_closed: If true, return fireteams that have been closed.
    :type include_closed: bool
    :param page: Deprecated parameter, ignored.
    :type page: int
    :param platform: The platform filter.
    :type platform: int
    :param group_filter: If true, filter by clan. Otherwise, ignore the clan and show all of the user&#39;s fireteams.
    :type group_filter: bool
    :param lang_filter: An optional language filter.
    :type lang_filter: str

    """
    return web.Response(status=200)


async def fireteam_search_public_available_clan_fireteams(request: web.Request, activity_type, date_range, page, platform, slot_filter, exclude_immediate=None, lang_filter=None) -> web.Response:
    """fireteam_search_public_available_clan_fireteams

    Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

    :param activity_type: The activity type to filter by.
    :type activity_type: int
    :param date_range: The date range to grab available fireteams.
    :type date_range: int
    :param page: Zero based page
    :type page: int
    :param platform: The platform filter.
    :type platform: int
    :param slot_filter: Filters based on available slots
    :type slot_filter: int
    :param exclude_immediate: If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
    :type exclude_immediate: bool
    :param lang_filter: An optional language filter.
    :type lang_filter: str

    """
    return web.Response(status=200)

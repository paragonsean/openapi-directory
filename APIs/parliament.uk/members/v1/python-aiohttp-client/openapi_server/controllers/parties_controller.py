from typing import List, Dict
from aiohttp import web

from openapi_server.models.house import House
from openapi_server.models.lords_by_type_members_service_search_result import LordsByTypeMembersServiceSearchResult
from openapi_server.models.party_members_service_search_result import PartyMembersServiceSearchResult
from openapi_server.models.party_seat_count_members_service_search_result import PartySeatCountMembersServiceSearchResult
from openapi_server import util


async def api_parties_get_active_house_get(request: web.Request, house) -> web.Response:
    """Returns a list of current parties with at least one active member.

    

    :param house: Current parties by house
    :type house: dict | bytes

    """
    house = .from_dict(house)
    return web.Response(status=200)


async def api_parties_lords_by_type_for_date_get(request: web.Request, for_date) -> web.Response:
    """Returns the composition of the House of Lords by peerage type.

    

    :param for_date: Composition of the Lords for date specified.
    :type for_date: str

    """
    for_date = util.deserialize_datetime(for_date)
    return web.Response(status=200)


async def api_parties_state_of_the_parties_house_for_date_get(request: web.Request, house, for_date) -> web.Response:
    """Returns current state of parties

    

    :param house: State of parties in Commons or Lords.
    :type house: dict | bytes
    :param for_date: State of parties for the date specified
    :type for_date: str

    """
    house = .from_dict(house)
    for_date = util.deserialize_datetime(for_date)
    return web.Response(status=200)

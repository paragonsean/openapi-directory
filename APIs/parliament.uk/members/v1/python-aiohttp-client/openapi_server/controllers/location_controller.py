from typing import List, Dict
from aiohttp import web

from openapi_server.models.constituency_item import ConstituencyItem
from openapi_server.models.constituency_members_service_search_result import ConstituencyMembersServiceSearchResult
from openapi_server.models.constituency_representation_list_item import ConstituencyRepresentationListItem
from openapi_server.models.election_result_item import ElectionResultItem
from openapi_server.models.election_result_list_item import ElectionResultListItem
from openapi_server.models.location_item import LocationItem
from openapi_server.models.location_type import LocationType
from openapi_server.models.string_item import StringItem
from openapi_server import util


async def api_location_browse_location_type_location_name_get(request: web.Request, location_type, location_name) -> web.Response:
    """Returns a list of locations, both parent and child

    

    :param location_type: Location by type of location
    :type location_type: dict | bytes
    :param location_name: Location by name specified
    :type location_name: str

    """
    location_type = .from_dict(location_type)
    return web.Response(status=200)


async def api_location_constituency_id_election_result_election_id_get(request: web.Request, id, election_id) -> web.Response:
    """Returns an election result by constituency and election id

    

    :param id: Election result by constituency id
    :type id: int
    :param election_id: Election result by election id
    :type election_id: int

    """
    return web.Response(status=200)


async def api_location_constituency_id_election_result_latest_get(request: web.Request, id) -> web.Response:
    """Returns latest election result by constituency id

    

    :param id: Latest election result by constituency id
    :type id: int

    """
    return web.Response(status=200)


async def api_location_constituency_id_election_results_get(request: web.Request, id) -> web.Response:
    """Returns a list of election results by constituency ID

    

    :param id: Elections results by constituency ID
    :type id: int

    """
    return web.Response(status=200)


async def api_location_constituency_id_geometry_get(request: web.Request, id) -> web.Response:
    """Returns geometry by constituency ID

    

    :param id: Geometry by constituency ID
    :type id: int

    """
    return web.Response(status=200)


async def api_location_constituency_id_get(request: web.Request, id) -> web.Response:
    """Returns a constituency by ID

    

    :param id: Constituency by ID
    :type id: int

    """
    return web.Response(status=200)


async def api_location_constituency_id_representations_get(request: web.Request, id) -> web.Response:
    """Returns a list of representations by constituency ID

    

    :param id: Representations by constituency ID
    :type id: int

    """
    return web.Response(status=200)


async def api_location_constituency_id_synopsis_get(request: web.Request, id) -> web.Response:
    """Returns a synopsis by constituency ID

    

    :param id: Synopsis by constituency ID
    :type id: int

    """
    return web.Response(status=200)


async def api_location_constituency_search_get(request: web.Request, search_text=None, skip=None, take=None) -> web.Response:
    """Returns a list of constituencies

    

    :param search_text: Constituencies containing serach term in their name
    :type search_text: str
    :param skip: The number of records to skip from the first, default is 0
    :type skip: int
    :param take: The number of records to return, default is 20. Maximum is 20
    :type take: int

    """
    return web.Response(status=200)

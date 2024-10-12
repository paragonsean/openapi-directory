from typing import List, Dict
from aiohttp import web

from openapi_server.models.members_interests_members_service_search_result import MembersInterestsMembersServiceSearchResult
from openapi_server.models.members_staff_members_service_search_result import MembersStaffMembersServiceSearchResult
from openapi_server import util


async def api_lords_interests_register_get(request: web.Request, search_term=None, page=None, include_deleted=None) -> web.Response:
    """Returns a list of registered interests

    

    :param search_term: Registered interests containing search term
    :type search_term: str
    :param page: Page of results to return, default 0. Results per page 20.
    :type page: int
    :param include_deleted: Registered interests that have been deleted
    :type include_deleted: bool

    """
    return web.Response(status=200)


async def api_lords_interests_staff_get(request: web.Request, search_term=None, page=None) -> web.Response:
    """Returns a list of staff

    

    :param search_term: Staff containing search term
    :type search_term: str
    :param page: Page of results to return, default 0. Results per page 20.
    :type page: int

    """
    return web.Response(status=200)

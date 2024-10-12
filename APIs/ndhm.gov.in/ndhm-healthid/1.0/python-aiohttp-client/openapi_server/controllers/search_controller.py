from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_by_health_id_request import SearchByHealthIdRequest
from openapi_server.models.search_by_mobile_request import SearchByMobileRequest
from openapi_server.models.search_response_single import SearchResponseSingle
from openapi_server import util


async def search_user_by_account_using_post(request: web.Request, search_request, accept_language=None) -> web.Response:
    """Search a user by Health ID Number.

    

    :param search_request: searchRequest
    :type search_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    search_request = SearchByHealthIdRequest.from_dict(search_request)
    return web.Response(status=200)


async def search_user_by_mobile_using_post(request: web.Request, search_request, accept_language=None) -> web.Response:
    """Search users with a mobile number.

    

    :param search_request: searchRequest
    :type search_request: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    search_request = SearchByMobileRequest.from_dict(search_request)
    return web.Response(status=200)


async def search_user_by_userid_using_post(request: web.Request, search_dto, accept_language=None) -> web.Response:
    """Search a user by Health IDs.

    

    :param search_dto: searchDTO
    :type search_dto: dict | bytes
    :param accept_language: 
    :type accept_language: str

    """
    search_dto = SearchByHealthIdRequest.from_dict(search_dto)
    return web.Response(status=200)

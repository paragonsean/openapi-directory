from typing import List, Dict
from aiohttp import web

from openapi_server.models.end_user_agreement import EndUserAgreement
from openapi_server.models.end_user_agreement_request import EndUserAgreementRequest
from openapi_server.models.enduser_acceptance_details_request import EnduserAcceptanceDetailsRequest
from openapi_server.models.paginated_end_user_agreement_list import PaginatedEndUserAgreementList
from openapi_server import util


async def accept_eua(request: web.Request, id, body) -> web.Response:
    """accept_eua

    Accept an end-user agreement via the API

    :param id: A UUID string identifying this end user agreement.
    :type id: str
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnduserAcceptanceDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def create_eua_v2(request: web.Request, body) -> web.Response:
    """create_eua_v2

    API endpoints related to end-user agreements.

    :param body: 
    :type body: dict | bytes

    """
    body = EndUserAgreementRequest.from_dict(body)
    return web.Response(status=200)


async def delete_eua_by_id_v2(request: web.Request, id) -> web.Response:
    """delete_eua_by_id_v2

    Delete an end user agreement

    :param id: A UUID string identifying this end user agreement.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def retrieve_all_euas_for_an_end_user_v2(request: web.Request, limit=None, offset=None) -> web.Response:
    """retrieve_all_euas_for_an_end_user_v2

    API endpoints related to end-user agreements.

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def retrieve_eua_by_id_v2(request: web.Request, id) -> web.Response:
    """retrieve_eua_by_id_v2

    Retrieve end user agreement by ID

    :param id: A UUID string identifying this end user agreement.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)

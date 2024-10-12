from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.offers_get200_response import OffersGet200Response
from openapi_server.models.offers_offer_id_get200_response import OffersOfferIdGet200Response
from openapi_server.models.offers_post_request import OffersPostRequest
from openapi_server import util


async def offers_get(request: web.Request, ) -> web.Response:
    """View list of offers

    


    """
    return web.Response(status=200)


async def offers_offer_id_delete(request: web.Request, offer_id) -> web.Response:
    """Delete an offer

    

    :param offer_id: 
    :type offer_id: str

    """
    return web.Response(status=200)


async def offers_offer_id_get(request: web.Request, offer_id) -> web.Response:
    """View offer

    

    :param offer_id: 
    :type offer_id: str

    """
    return web.Response(status=200)


async def offers_offer_id_put(request: web.Request, offer_id, status=None) -> web.Response:
    """Edit an offer

    

    :param offer_id: 
    :type offer_id: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)


async def offers_post(request: web.Request, body=None) -> web.Response:
    """Add new offer

    

    :param body: 
    :type body: dict | bytes

    """
    body = OffersPostRequest.from_dict(body)
    return web.Response(status=200)

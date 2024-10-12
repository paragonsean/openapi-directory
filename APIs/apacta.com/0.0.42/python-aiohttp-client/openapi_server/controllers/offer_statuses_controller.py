from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server.models.offer_statuses_get200_response import OfferStatusesGet200Response
from openapi_server.models.offer_statuses_offer_status_id_get200_response import OfferStatusesOfferStatusIdGet200Response
from openapi_server.models.offer_statuses_post_request import OfferStatusesPostRequest
from openapi_server import util


async def offer_statuses_bulk_delete_delete(request: web.Request, body) -> web.Response:
    """Bulk delete offer statuses

    

    :param body: Offer statuses ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def offer_statuses_get(request: web.Request, ) -> web.Response:
    """Get list of offer statuses

    


    """
    return web.Response(status=200)


async def offer_statuses_offer_status_id_delete(request: web.Request, offer_status_id) -> web.Response:
    """Delete a offer status

    

    :param offer_status_id: 
    :type offer_status_id: str
    :type offer_status_id: str

    """
    return web.Response(status=200)


async def offer_statuses_offer_status_id_get(request: web.Request, offer_status_id) -> web.Response:
    """Get a single offer status

    

    :param offer_status_id: 
    :type offer_status_id: str

    """
    return web.Response(status=200)


async def offer_statuses_offer_status_id_put(request: web.Request, offer_status_id) -> web.Response:
    """Edit a offer status

    

    :param offer_status_id: 
    :type offer_status_id: str

    """
    return web.Response(status=200)


async def offer_statuses_post(request: web.Request, body) -> web.Response:
    """Create a new offer status

    

    :param body: 
    :type body: dict | bytes

    """
    body = OfferStatusesPostRequest.from_dict(body)
    return web.Response(status=200)

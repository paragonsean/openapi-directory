from typing import List, Dict
from aiohttp import web

from openapi_server.models.discount_request import DiscountRequest
from openapi_server.models.discount_response import DiscountResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def create_discount(request: web.Request, organization_uuid, body=None) -> web.Response:
    """Create a discount

    Creates a single discount entity. The location of the newly created discount will be available in the successful response as a HttpHeaders.LOCATION header

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = DiscountRequest.from_dict(body)
    return web.Response(status=200)


async def delete_discount(request: web.Request, organization_uuid, discount_uuid) -> web.Response:
    """Delete a single discount 

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param discount_uuid: 
    :type discount_uuid: str
    :type discount_uuid: str

    """
    return web.Response(status=200)


async def get_all_discounts(request: web.Request, organization_uuid) -> web.Response:
    """Retrieve all discounts

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str

    """
    return web.Response(status=200)


async def get_discount(request: web.Request, organization_uuid, discount_uuid, if_none_match=None) -> web.Response:
    """Retrieve a single discount

    Get the full discount with the provided UUID. The method supports conditional GET through providing a HttpHeaders.IF_NONE_MATCH header. If the conditional prerequisite is fullfilled, the full discount is returned: otherwise a 304 not modified will be returned with an empty body.

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param discount_uuid: 
    :type discount_uuid: str
    :type discount_uuid: str
    :param if_none_match: 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def update_discount(request: web.Request, organization_uuid, discount_uuid, body, if_match=None) -> web.Response:
    """Update a single discount

    Updates a discount entity using JSON merge patch (https://tools.ietf.org/html/rfc7386). This means that only included fields will be changed: null values removes the field on the target entity, and other values updates the field. Conditional updates are supported through the HttpHeaders.IF_MATCH header. If the conditional prerequisite is fullfilled, the discount is updated: otherwise a 412 precondition failed will be returned with an empty body.

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param discount_uuid: 
    :type discount_uuid: str
    :type discount_uuid: str
    :param body: 
    :type body: dict | bytes
    :param if_match: 
    :type if_match: str

    """
    body = DiscountRequest.from_dict(body)
    return web.Response(status=200)

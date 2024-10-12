from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_body import RequestBody
from openapi_server.models.v_custom_prices_rules_post200_response import VCustomPricesRulesPost200Response
from openapi_server.models.v_custom_prices_rules_post_request import VCustomPricesRulesPostRequest
from openapi_server import util


async def v_custom_prices_rules_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create price association

    Creates a new price association for a shopping scenario

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = VCustomPricesRulesPostRequest.from_dict(body)
    return web.Response(status=200)


async def v_custom_prices_rules_price_association_id_delete(request: web.Request, content_type, accept, price_association_id) -> web.Response:
    """Disassociate price association by ID

    Disassociates a price association from a shopping scenario by its ID

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    :type accept: str
    :param price_association_id: Price Association unique identifier
    :type price_association_id: int

    """
    return web.Response(status=200)


async def v_custom_prices_rules_price_association_id_get(request: web.Request, content_type, accept, price_association_id) -> web.Response:
    """Get price association by ID

    Retrieves price association for a shopping scenario by its ID

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    :type accept: str
    :param price_association_id: Price Association unique identifier
    :type price_association_id: int

    """
    return web.Response(status=200)


async def v_custom_prices_rules_price_association_id_put(request: web.Request, content_type, accept, price_association_id, body=None) -> web.Response:
    """Update price association by ID

    Updates a price association for a shopping scenario by its ID

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    :type accept: str
    :param price_association_id: Price Association unique identifier
    :type price_association_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_seller200_response import CreateSeller200Response
from openapi_server.models.create_seller_request import CreateSellerRequest
from openapi_server.models.get_sellerby_id200_response import GetSellerbyId200Response
from openapi_server.models.get_sellersby_id200_response import GetSellersbyId200Response
from openapi_server.models.update_seller200_response import UpdateSeller200Response
from openapi_server.models.update_seller_request import UpdateSellerRequest
from openapi_server import util


async def create_seller(request: web.Request, content_type, accept, body) -> web.Response:
    """Create Seller

    Creates a new seller.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateSellerRequest.from_dict(body)
    return web.Response(status=200)


async def get_sellerby_id(request: web.Request, content_type, accept, seller_id) -> web.Response:
    """Get Seller by ID

    Retrieves the seller&#39;s details by its ID.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str

    """
    return web.Response(status=200)


async def get_sellersby_id(request: web.Request, content_type, accept, seller_id) -> web.Response:
    """Get Seller by ID

    Retrieves the seller&#39;s details by its ID.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str

    """
    return web.Response(status=200)


async def seller_list(request: web.Request, content_type, accept, sc=None, seller_type=None, is_better_scope=None) -> web.Response:
    """Get Seller List

    Retrieves the seller&#39;s details by its ID.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sc: Trade policy ID.
    :type sc: int
    :param seller_type: Seller type.
    :type seller_type: int
    :param is_better_scope: If the seller is better scope.
    :type is_better_scope: bool

    """
    return web.Response(status=200)


async def update_seller(request: web.Request, content_type, accept, body) -> web.Response:
    """Update Seller

    Updates a seller.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSellerRequest.from_dict(body)
    return web.Response(status=200)

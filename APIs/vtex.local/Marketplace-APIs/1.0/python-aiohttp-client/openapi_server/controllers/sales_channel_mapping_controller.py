from typing import List, Dict
from aiohttp import web

from openapi_server.models.upsert_mapping_request import UpsertMappingRequest
from openapi_server import util


async def retrieve_mapping(request: web.Request, content_type, accept, account_name, environment, an, seller_id) -> web.Response:
    """Get Sales Channel Mapping Data

    Retrieves information about the mapping between marketplace&#39;s sales channels and a specific seller.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param account_name: Name of the VTEX account that belongs to the marketplace. Used as part of the URL
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param an: Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path.
    :type an: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str

    """
    return web.Response(status=200)


async def upsert_mapping(request: web.Request, content_type, accept, account_name, environment, an, seller_id, body) -> web.Response:
    """Upsert Sales Channel Mapping

    This endpoint allows the marketplace to map its sales channels with a seller&#39;s [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187). The seller can have multiple sales channels associated with the same marketplace, by creating different affiliates. The mapping enables the seller to segment catalog, prices, inventory, logistics, and payments in the marketplace.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param account_name: Name of the VTEX account that belongs to the marketplace. Used as part of the URL.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param an: Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path.
    :type an: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [UpsertMappingRequest.from_dict(d) for d in body]
    return web.Response(status=200)

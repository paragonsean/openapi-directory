from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_upsert_seller_commissions_request import BulkUpsertSellerCommissionsRequest
from openapi_server.models.upsert_seller_commissions_request import UpsertSellerCommissionsRequest
from openapi_server import util


async def bulk_upsert_seller_commissions(request: web.Request, account_name, environment, accept, content_type, seller_id, body) -> web.Response:
    """Upsert Seller Commissions in Bulk

    This endpoint is used by marketplace operators to define comissions for multiple categories.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [BulkUpsertSellerCommissionsRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def list_seller_commissions(request: web.Request, account_name, environment, seller_id, accept, content_type) -> web.Response:
    """List Seller Commissions by seller ID

    This endpoint retrieves all comissions configured for a specific seller.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def remove_seller_commissions(request: web.Request, account_name, environment, accept, content_type, seller_id, category_id) -> web.Response:
    """Remove Seller Commissions by Category ID

    This endpoint removes a seller comission on the selected category.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param category_id: ID of the category in which the comission was applied
    :type category_id: str

    """
    return web.Response(status=200)


async def retrieve_seller_commissions(request: web.Request, account_name, environment, accept, content_type, seller_id, category_id) -> web.Response:
    """Get Seller Commissions by Category ID

    This endpoint retrieves seller comissions applied to the selected category.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param category_id: ID of the category in which the comission was applied
    :type category_id: str

    """
    return web.Response(status=200)


async def upsert_seller_commissions(request: web.Request, account_name, environment, seller_id, category_id, accept, content_type, body) -> web.Response:
    """Upsert Seller Commissions by Category ID

    This endpoint is used by marketplace operators to define comissions for a single category, by ID.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    :type seller_id: str
    :param category_id: ID of the category in which the comission will be applied.
    :type category_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpsertSellerCommissionsRequest.from_dict(body)
    return web.Response(status=200)

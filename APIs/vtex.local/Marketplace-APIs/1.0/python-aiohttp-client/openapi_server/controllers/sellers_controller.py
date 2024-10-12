from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_body_inner import RequestBodyInner
from openapi_server.models.upsert_seller_request import UpsertSellerRequest
from openapi_server import util


async def get_list_sellers(request: web.Request, account_name, environment, accept, content_type, _from=None, to=None, keyword=None, integration=None, group_=None, is_active=None, is_better_scope=None, is_vtex=None, sc=None, seller_type=None, sort=None) -> web.Response:
    """List Sellers

    This endpoint lists all Sellers. This call&#39;s results can be filtered by [trade policies](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data) through the &#x60;sc&#x60; query param.

    :param account_name: Name of the VTEX account that belongs to the marketplace.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param _from: The start number of pagination, being &#x60;0&#x60; the default value.
    :type _from: 
    :param to: The end number of pagination, being &#x60;100&#x60; the default value.
    :type to: 
    :param keyword: Search sellers by a keyword in &#x60;sellerId&#x60; or &#x60;sellerName&#x60;.
    :type keyword: str
    :param integration: Filters sellers by the name of who made the integration, if VTEX or an external hub. The possible values for VTEX integrations are: &#x60;vtex-sellerportal&#x60;, &#x60;vtex-seller&#x60; and &#x60;vtex-franchise&#x60;.
    :type integration: str
    :param group_: Groups are defined by keywords that group sellers into categories defined by the marketplace.
    :type group_: str
    :param is_active: Enables to filter sellers that are active (&#x60;true&#x60;) or unactive (&#x60;false&#x60;) in the marketplace.
    :type is_active: bool
    :param is_better_scope: The flag &#x60;isBetterScope&#x60; is used by the VTEX Checkout to simulate shopping carts, products, and shipping only in sellers with the field set as &#x60;true&#x60;, avoiding performance issues. When used as a query param, &#x60;isBetterScope&#x60; filters sellers that have the flag set as &#x60;true&#x60; or &#x60;false&#x60;.
    :type is_better_scope: bool
    :param is_vtex: When set as &#x60;true&#x60;, the list returned will be of sellers who have a VTEX store configured. When set as &#x60;false&#x60;, the list will be of sellers who do not have a VTEX store configured.
    :type is_vtex: bool
    :param sc: Filters sellers available for the marketplace&#39;s sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) indicated in this field.
    :type sc: str
    :param seller_type: Filters sellers by their type, which can be regular seller (&#x60;1&#x60;) or whitelabel seller (&#x60;2&#x60;).
    :type seller_type: int
    :param sort: Narrow the search filtering by the fields: &#x60;id&#x60;, &#x60;name&#x60; or &#x60;pendingoffers&#x60;. The list retrieved can be organized in an ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order. The standardized format is &#x60;{field}:{order}&#x60;, and the default value is &#x60;id:asc&#x60;.
    :type sort: str

    """
    return web.Response(status=200)


async def get_retrieve_seller(request: web.Request, account_name, environment, seller_id, accept, content_type, sc=None) -> web.Response:
    """Get Seller data by ID

    Marketplace operator may call this endpoint to retrieve information about a specific seller by filtering by ID. It is also possible to filter results by sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) through the &#x60;sc&#x60; query param.

    :param account_name: Name of the VTEX account that belongs to the marketplace.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace
    :type seller_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param sc: Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) associated to the seller account created.
    :type sc: str

    """
    return web.Response(status=200)


async def update_seller(request: web.Request, account_name, environment, accept, content_type, seller_id, body=None) -> web.Response:
    """Update Seller by Seller ID

    This endpoint allows marketplace operators to update the information of sellers connected to their account. You can replace a path&#39;s value with another value in order to update that single information. There is no need to fill all the body params available, only the one you wish to update.

    :param account_name: Name of the VTEX account that belongs to the marketplace.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace
    :type seller_id: str
    :param body: array of objects
    :type body: list | bytes

    """
    body = [RequestBodyInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def upsert_seller_request(request: web.Request, account_name, environment, accept, content_type, body) -> web.Response:
    """Configure Seller Account

    This endpoint is used by marketplace operators to configure the accounts of sellers that have already accepted the invitation to join their marketplaces.   For marketplaces to [add sellers](https://help.vtex.com/en/tutorial/adding-a-seller--tutorials_392) without the [Seller Invite](https://help.vtex.com/en/tutorial/marketplace-invited-sellers--6rb2FkcslmDueJ689Ulb9A) feature, call this endpoint directly.   This call includes all the information a seller needs to activate their account.

    :param account_name: Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpsertSellerRequest.from_dict(body)
    return web.Response(status=200)

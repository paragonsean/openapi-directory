from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_order_deals_request import AddOrderDealsRequest
from openapi_server.models.add_order_deals_response import AddOrderDealsResponse
from openapi_server.models.delete_order_deals_request import DeleteOrderDealsRequest
from openapi_server.models.delete_order_deals_response import DeleteOrderDealsResponse
from openapi_server.models.edit_all_order_deals_request import EditAllOrderDealsRequest
from openapi_server.models.edit_all_order_deals_response import EditAllOrderDealsResponse
from openapi_server.models.get_order_deals_response import GetOrderDealsResponse
from openapi_server import util


async def adexchangebuyer_marketplacedeals_delete(request: web.Request, proposal_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adexchangebuyer_marketplacedeals_delete

    Delete the specified deals from the proposal

    :param proposal_id: The proposalId to delete deals from.
    :type proposal_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteOrderDealsRequest.from_dict(body)
    return web.Response(status=200)


async def adexchangebuyer_marketplacedeals_insert(request: web.Request, proposal_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adexchangebuyer_marketplacedeals_insert

    Add new deals for the specified proposal

    :param proposal_id: proposalId for which deals need to be added.
    :type proposal_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddOrderDealsRequest.from_dict(body)
    return web.Response(status=200)


async def adexchangebuyer_marketplacedeals_list(request: web.Request, proposal_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, pql_query=None) -> web.Response:
    """adexchangebuyer_marketplacedeals_list

    List all the deals for a given proposal

    :param proposal_id: The proposalId to get deals for. To search across all proposals specify order_id &#x3D; &#39;-&#39; as part of the URL.
    :type proposal_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param pql_query: Query string to retrieve specific deals.
    :type pql_query: str

    """
    return web.Response(status=200)


async def adexchangebuyer_marketplacedeals_update(request: web.Request, proposal_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adexchangebuyer_marketplacedeals_update

    Replaces all the deals in the proposal with the passed in deals

    :param proposal_id: The proposalId to edit deals on.
    :type proposal_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditAllOrderDealsRequest.from_dict(body)
    return web.Response(status=200)

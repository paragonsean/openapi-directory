from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_order_notes_request import AddOrderNotesRequest
from openapi_server.models.add_order_notes_response import AddOrderNotesResponse
from openapi_server.models.get_order_notes_response import GetOrderNotesResponse
from openapi_server import util


async def adexchangebuyer_marketplacenotes_insert(request: web.Request, proposal_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adexchangebuyer_marketplacenotes_insert

    Add notes to the proposal

    :param proposal_id: The proposalId to add notes for.
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
    body = AddOrderNotesRequest.from_dict(body)
    return web.Response(status=200)


async def adexchangebuyer_marketplacenotes_list(request: web.Request, proposal_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, pql_query=None) -> web.Response:
    """adexchangebuyer_marketplacenotes_list

    Get all the notes associated with a proposal

    :param proposal_id: The proposalId to get notes for. To search across all proposals specify order_id &#x3D; &#39;-&#39; as part of the URL.
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
    :param pql_query: Query string to retrieve specific notes. To search the text contents of notes, please use syntax like \&quot;WHERE note.note &#x3D; \&quot;foo\&quot; or \&quot;WHERE note.note LIKE \&quot;%bar%\&quot;
    :type pql_query: str

    """
    return web.Response(status=200)

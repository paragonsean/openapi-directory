from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_private_auction_proposal_request import UpdatePrivateAuctionProposalRequest
from openapi_server import util


async def adexchangebuyer_marketplaceprivateauction_updateproposal(request: web.Request, private_auction_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adexchangebuyer_marketplaceprivateauction_updateproposal

    Update a given private auction proposal

    :param private_auction_id: The private auction id to be updated.
    :type private_auction_id: str
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
    body = UpdatePrivateAuctionProposalRequest.from_dict(body)
    return web.Response(status=200)

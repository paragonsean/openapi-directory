from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.offer_details_response import OfferDetailsResponse
from openapi_server import util


async def offerdetails_get(request: web.Request, fid, user_token, offer_id) -> web.Response:
    """Returns Information on an Offer

    This resource returns extended information for the requested offer, typically used to display a detail view. 

    :param fid: Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    :type fid: str
    :param user_token: Session identifier as returned by the UserToken resource.
    :type user_token: str
    :param offer_id: System-wide identifier for the campaign, not intended for end-user display.
    :type offer_id: str

    """
    return web.Response(status=200)

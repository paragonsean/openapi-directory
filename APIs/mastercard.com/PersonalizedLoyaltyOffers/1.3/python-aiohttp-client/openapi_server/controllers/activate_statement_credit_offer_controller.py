from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_offer_response import ActivateOfferResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def activatestatementcreditoffer_post(request: web.Request, fid, user_token, offer_id) -> web.Response:
    """Make Statement Credit Offer Available Redeemable

    This resource is used to make a statement credit offer available for redemption. 

    :param fid: Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    :type fid: str
    :param user_token: Session identifier as returned by the UserToken resource.
    :type user_token: str
    :param offer_id: System-wide identifier for the campaign, not intended for end-user display.
    :type offer_id: str

    """
    return web.Response(status=200)

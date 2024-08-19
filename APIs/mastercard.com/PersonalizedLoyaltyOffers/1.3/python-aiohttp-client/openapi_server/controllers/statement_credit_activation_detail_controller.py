from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.statement_credit_activation_response import StatementCreditActivationResponse
from openapi_server import util


async def statementcreditactivationdetail_get(request: web.Request, fid, user_token, activation_id) -> web.Response:
    """Returns Information About Redeemable Postpaid Credit Offer

    This resource returns extended information about the specified activated postpaid credit offer. 

    :param fid: Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    :type fid: str
    :param user_token: Session identifier as returned by the UserToken resource.
    :type user_token: str
    :param activation_id: Distinct identifier for the offer being available for redemption by the user as returned by Activate Statement Credit Offer or Redeemed Offers, not intended for end-user display.
    :type activation_id: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.funding_reversal144_wrapper import FundingReversal144Wrapper
from openapi_server.models.transfer145_wrapper import Transfer145Wrapper
from openapi_server import util


async def create_funding_reversal(request: web.Request, partner_id, transfer_id, transaction_id, funding_reversal=None) -> web.Response:
    """Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account.

    Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account.

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param transfer_id: Valid transfer id
    :type transfer_id: str
    :param transaction_id: Valid transaction id
    :type transaction_id: str
    :param funding_reversal: Contains the details of the request message.
    :type funding_reversal: dict | bytes

    """
    funding_reversal = FundingReversal144Wrapper.from_dict(funding_reversal)
    return web.Response(status=200)

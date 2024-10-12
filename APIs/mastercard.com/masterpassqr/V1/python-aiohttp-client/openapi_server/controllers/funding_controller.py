from typing import List, Dict
from aiohttp import web

from openapi_server.models.funding_transfer118_wrapper import FundingTransfer118Wrapper
from openapi_server.models.transfer129_wrapper import Transfer129Wrapper
from openapi_server import util


async def create_funding(request: web.Request, partner_id, funding_transfer=None) -> web.Response:
    """The Funding Transaction enables the &#39;pull&#39; of money from the sender&#39;s card to the Transaction Originator who is providing the Person to Merchant service. The amount that is debited from the Funding Account (sending consumer&#39;s account) will be the amount &#39;pushed&#39; to the recipient via a payment transfer request.  Funds can be transferred from Mastercard® or Maestro® debit card accounts. To initiate the funding transaction, users can provide the sending consumer&#39;s Primary Account Number (PAN) or a unique identifier previously mapped to the sending consumer&#39;s account.

    The Funding Transaction enables the &#39;pull&#39; of money from the sender&#39;s card to the Transaction Originator who is providing the Person to Merchant service. The amount that is debited from the Funding Account (sending consumer&#39;s account) will be the amount &#39;pushed&#39; to the recipient via a payment transfer request.  Funds can be transferred from Mastercard® or Maestro® debit card accounts. To initiate the funding transaction, users can provide the sending consumer&#39;s Primary Account Number (PAN) or a unique identifier previously mapped to the sending consumer&#39;s account.

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param funding_transfer: Contains the details of the request message.
    :type funding_transfer: dict | bytes

    """
    funding_transfer = FundingTransfer118Wrapper.from_dict(funding_transfer)
    return web.Response(status=200)

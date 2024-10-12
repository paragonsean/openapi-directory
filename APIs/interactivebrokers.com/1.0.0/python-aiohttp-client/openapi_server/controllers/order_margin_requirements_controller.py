from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_account_order_impact_post200_response import AccountsAccountOrderImpactPost200Response
from openapi_server.models.accounts_account_order_impact_post_request import AccountsAccountOrderImpactPostRequest
from openapi_server import util


async def accounts_account_order_impact_post(request: web.Request, account, body) -> web.Response:
    """Return margin impact info

    This endpoint allows the consumer to check the impact that an order would have on the account, including margin, NLV and estimated commission costs. To specify the contract, you provide a value for the ContractId field, OR Ticker/ListingExchange/InstrumentType&#x3D;STK for stocks OR Ticker/Currency/InstrumentType&#x3D;CASH for FX. 

    :param account: Account Number
    :type account: str
    :param body: Order Parameters
    :type body: dict | bytes

    """
    body = AccountsAccountOrderImpactPostRequest.from_dict(body)
    return web.Response(status=200)

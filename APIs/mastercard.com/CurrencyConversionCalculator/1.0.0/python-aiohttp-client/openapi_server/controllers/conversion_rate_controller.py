from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversion_rate_request import ConversionRateRequest
from openapi_server import util


async def get_conversion_detail_using_get(request: web.Request, fx_date, trans_curr, crdhld_bill_curr, trans_amt, bank_fee=None) -> web.Response:
    """Get the currency conversion rate details.

    Get the currency conversion rate details.

    :param fx_date: Date of the requested FX rates.
    :type fx_date: str
    :param trans_curr: Currency of the transaction.
    :type trans_curr: str
    :param crdhld_bill_curr: Cardholder billing currency.
    :type crdhld_bill_curr: str
    :param trans_amt: Amount in the transaction currency.
    :type trans_amt: float
    :param bank_fee: Additional fees imposed by the bank.
    :type bank_fee: float

    """
    return web.Response(status=200)

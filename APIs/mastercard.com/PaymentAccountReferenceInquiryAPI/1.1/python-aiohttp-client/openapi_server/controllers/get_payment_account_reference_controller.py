from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_payment_account_reference_request_schema import GetPaymentAccountReferenceRequestSchema
from openapi_server.models.get_payment_account_reference_response_schema import GetPaymentAccountReferenceResponseSchema
from openapi_server import util


async def par_paymentaccountreference10_get_payment_account_reference_post(request: web.Request, get_payment_account_reference_request_schema=None) -> web.Response:
    """Submit an encrypted PAN to obtain the PAR linked to the account.

    The API performs a PAR query into the PAR Vault with the supplied PAN. When a PAR is returned from the PAR vault the API will encrypt it using the wrapped encryption method with the  Mastercard Customer?s Encryption Public Key and include it in the API response. 

    :param get_payment_account_reference_request_schema: Contains the details of the get PAR API request message.
    :type get_payment_account_reference_request_schema: dict | bytes

    """
    get_payment_account_reference_request_schema = GetPaymentAccountReferenceRequestSchema.from_dict(get_payment_account_reference_request_schema)
    return web.Response(status=200)

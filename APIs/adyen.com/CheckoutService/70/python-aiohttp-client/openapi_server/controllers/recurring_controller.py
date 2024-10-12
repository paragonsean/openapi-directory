from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_stored_payment_methods_response import ListStoredPaymentMethodsResponse
from openapi_server import util


async def delete_stored_payment_methods_stored_payment_method_id(request: web.Request, stored_payment_method_id, shopper_reference, merchant_account) -> web.Response:
    """Delete a token for stored payment details

    Deletes the token identified in the path. The token can no longer be used with payment requests.

    :param stored_payment_method_id: The unique identifier of the token.
    :type stored_payment_method_id: str
    :param shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address.
    :type shopper_reference: str
    :param merchant_account: Your merchant account.
    :type merchant_account: str

    """
    return web.Response(status=200)


async def get_stored_payment_methods(request: web.Request, shopper_reference=None, merchant_account=None) -> web.Response:
    """Get tokens for stored payment details

    Lists the tokens for stored payment details for the shopper identified in the path, if there are any available. The token ID can be used with payment requests for the shopper&#39;s payment. A summary of the stored details is included.  

    :param shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address.
    :type shopper_reference: str
    :param merchant_account: Your merchant account.
    :type merchant_account: str

    """
    return web.Response(status=200)

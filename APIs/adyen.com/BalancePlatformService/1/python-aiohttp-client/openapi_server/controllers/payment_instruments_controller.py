from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_instrument import PaymentInstrument
from openapi_server.models.payment_instrument_info import PaymentInstrumentInfo
from openapi_server.models.payment_instrument_reveal_info import PaymentInstrumentRevealInfo
from openapi_server.models.payment_instrument_update_request import PaymentInstrumentUpdateRequest
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.transaction_rules_response import TransactionRulesResponse
from openapi_server.models.update_payment_instrument import UpdatePaymentInstrument
from openapi_server import util


async def get_payment_instruments_id(request: web.Request, id) -> web.Response:
    """Get a payment instrument

    Returns the details of a payment instrument.

    :param id: The unique identifier of the payment instrument.
    :type id: str

    """
    return web.Response(status=200)


async def get_payment_instruments_id_reveal(request: web.Request, id) -> web.Response:
    """Get the PAN of a payment instrument

    Returns the primary account number (PAN) of a payment instrument.  To make this request, your API credential must have the following [role](https://docs.adyen.com/issuing/manage-access/api-credentials-web-service#api-permissions):  * Balance Platform BCL PCI role

    :param id: The unique identifier of the payment instrument.
    :type id: str

    """
    return web.Response(status=200)


async def get_payment_instruments_id_transaction_rules(request: web.Request, id) -> web.Response:
    """Get all transaction rules for a payment instrument

    Returns a list of transaction rules associated with a payment instrument.

    :param id: The unique identifier of the payment instrument.
    :type id: str

    """
    return web.Response(status=200)


async def patch_payment_instruments_id(request: web.Request, id, body=None) -> web.Response:
    """Update a payment instrument

    Updates a payment instrument. Once a payment instrument is already active, you can only update its status. However, for cards created with **inactive** status, you can still update the balance account associated with the card.

    :param id: The unique identifier of the payment instrument.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentInstrumentUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def post_payment_instruments(request: web.Request, body=None) -> web.Response:
    """Create a payment instrument

    Creates a payment instrument to issue a physical card, a virtual card, or a business account to your user.   For more information, refer to [Issue cards](https://docs.adyen.com/issuing/create-cards) or [Issue business accounts](https://docs.adyen.com/marketplaces-and-platforms/business-accounts).

    :param body: 
    :type body: dict | bytes

    """
    body = PaymentInstrumentInfo.from_dict(body)
    return web.Response(status=200)

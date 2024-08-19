from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_instrument_group import PaymentInstrumentGroup
from openapi_server.models.payment_instrument_group_info import PaymentInstrumentGroupInfo
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.transaction_rules_response import TransactionRulesResponse
from openapi_server import util


async def get_payment_instrument_groups_id(request: web.Request, id) -> web.Response:
    """Get a payment instrument group

    Returns the details of a payment instrument group.

    :param id: The unique identifier of the payment instrument group.
    :type id: str

    """
    return web.Response(status=200)


async def get_payment_instrument_groups_id_transaction_rules(request: web.Request, id) -> web.Response:
    """Get all transaction rules for a payment instrument group

    Returns a list of all the transaction rules associated with a payment instrument group.

    :param id: The unique identifier of the payment instrument group.
    :type id: str

    """
    return web.Response(status=200)


async def post_payment_instrument_groups(request: web.Request, body=None) -> web.Response:
    """Create a payment instrument group

    Creates a payment instrument group to associate and group payment instrument resources together. You can apply a transaction rule to a payment instrument group.

    :param body: 
    :type body: dict | bytes

    """
    body = PaymentInstrumentGroupInfo.from_dict(body)
    return web.Response(status=200)

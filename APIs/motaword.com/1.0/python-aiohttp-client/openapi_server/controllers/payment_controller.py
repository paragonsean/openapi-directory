from typing import List, Dict
from aiohttp import web

from openapi_server.models.credit_card import CreditCard
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server import util


async def delete_credit_card(request: web.Request, card_id) -> web.Response:
    """Delete credit card

    

    :param card_id: Credit Card ID
    :type card_id: int

    """
    return web.Response(status=200)


async def get_credit_card(request: web.Request, card_id) -> web.Response:
    """View saved credit card

    

    :param card_id: Credit Card ID
    :type card_id: int

    """
    return web.Response(status=200)


async def reset_card_payment_code(request: web.Request, card_id) -> web.Response:
    """Reset credit card payment code

    Reset the payment code used to bypass credit card payment. This will invalidate your current payment code and your users should be aware of this change while ordering translations.

    :param card_id: Credit Card ID
    :type card_id: int

    """
    return web.Response(status=200)


async def reset_corporate_payment_code(request: web.Request, ) -> web.Response:
    """Reset payment code

    Reset your corporate account&#39;s payment code to bypass credit card payment. This will invalidate your current payment code and your users should be aware of this change while ordering translations.


    """
    return web.Response(status=200)


async def toggle_corporate_auto_charge(request: web.Request, ) -> web.Response:
    """Manage automatic charges on your credit card

    Toggle (enable/disable) automatic charges on the credit card on file.


    """
    return web.Response(status=200)

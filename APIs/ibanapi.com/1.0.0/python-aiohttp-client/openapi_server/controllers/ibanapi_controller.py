from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_response import BalanceResponse
from openapi_server.models.iban_result import IBANResult
from openapi_server.models.iban_result_basic import IBANResultBasic
from openapi_server.models.model400 import Model400
from openapi_server.models.model401 import Model401
from openapi_server.models.model403 import Model403
from openapi_server.models.model422 import Model422
from openapi_server import util


async def get_balance(request: web.Request, ) -> web.Response:
    """Get Account Balance

    Returns the account balance and expiry


    """
    return web.Response(status=200)


async def validate_iban(request: web.Request, iban) -> web.Response:
    """Validate IBAN

    Returns the validation results

    :param iban: The IBAN
    :type iban: str

    """
    return web.Response(status=200)


async def validate_iban_basic(request: web.Request, iban) -> web.Response:
    """Validate IBAN Basic

    Returns the basic validation results

    :param iban: The IBAN
    :type iban: str

    """
    return web.Response(status=200)

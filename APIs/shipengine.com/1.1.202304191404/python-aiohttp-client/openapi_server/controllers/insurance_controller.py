from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_funds_to_insurance_request_body import AddFundsToInsuranceRequestBody
from openapi_server.models.add_funds_to_insurance_response_body import AddFundsToInsuranceResponseBody
from openapi_server.models.connect_insurer_request_body import ConnectInsurerRequestBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_insurance_balance_response_body import GetInsuranceBalanceResponseBody
from openapi_server import util


async def add_funds_to_insurance(request: web.Request, body) -> web.Response:
    """Add Funds To Insurance

    You may need to auto fund your account from time to time. For example, if you don&#39;t normally ship items over $100, and may want to add funds to insurance rather than keeping the account funded. 

    :param body: 
    :type body: dict | bytes

    """
    body = AddFundsToInsuranceRequestBody.from_dict(body)
    return web.Response(status=200)


async def connect_insurer(request: web.Request, body) -> web.Response:
    """Connect a Shipsurance Account

    Connect a Shipsurance Account

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectInsurerRequestBody.from_dict(body)
    return web.Response(status=200)


async def disconnect_insurer(request: web.Request, ) -> web.Response:
    """Disconnect a Shipsurance Account

    Disconnect a Shipsurance Account


    """
    return web.Response(status=200)


async def get_insurance_balance(request: web.Request, ) -> web.Response:
    """Get Insurance Funds Balance

    Retrieve the balance of your Shipsurance account.


    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.dates import Dates
from openapi_server import util


async def get_account(request: web.Request, authorization) -> web.Response:
    """get_account

    Returns a list of all the accounts owned by the user

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str

    """
    return web.Response(status=200)


async def get_account_balance(request: web.Request, authorization, account_no) -> web.Response:
    """get_account_balance

    Returns details about a specific account

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str
    :param account_no: Account id
    :type account_no: str

    """
    return web.Response(status=200)


async def get_transactions(request: web.Request, authorization, account_no, body) -> web.Response:
    """get_transactions

    Return transactions between 2 specific dates

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str
    :param account_no: Account id
    :type account_no: str
    :param body: A start date and an end date
    :type body: dict | bytes

    """
    body = Dates.from_dict(body)
    return web.Response(status=200)


async def show_last_ten_transactions(request: web.Request, authorization, account_no) -> web.Response:
    """show_last_ten_transactions

    Returns the last 10 transactions attached to an account

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str
    :param account_no: Account id
    :type account_no: str

    """
    return web.Response(status=200)

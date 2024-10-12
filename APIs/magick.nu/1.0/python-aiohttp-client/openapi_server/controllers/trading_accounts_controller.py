from typing import List, Dict
from aiohttp import web

from openapi_server.models.password_dto import PasswordDTO
from openapi_server.models.trading_account import TradingAccount
from openapi_server import util


async def post_trading_accounts(request: web.Request, body) -> web.Response:
    """Add a Trading Account

    

    :param body: 
    :type body: dict | bytes

    """
    body = TradingAccount.from_dict(body)
    return web.Response(status=200)


async def put_trading_accounts_password_username_brokerserver_mt4username(request: web.Request, username, brokerserver, mt4username, body) -> web.Response:
    """Update MT4 Account Password

    

    :param username: 
    :type username: str
    :param brokerserver: 
    :type brokerserver: str
    :param mt4username: 
    :type mt4username: str
    :param body: 
    :type body: dict | bytes

    """
    body = PasswordDTO.from_dict(body)
    return web.Response(status=200)

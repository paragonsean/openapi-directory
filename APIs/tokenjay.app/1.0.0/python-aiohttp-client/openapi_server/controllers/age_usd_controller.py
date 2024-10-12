from typing import List, Dict
from aiohttp import web

from openapi_server.models.age_usd_exchange_info import AgeUsdExchangeInfo
from openapi_server.models.age_usd_info import AgeUsdInfo
from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.token_price import TokenPrice
from openapi_server import util


async def calc_sigma_rsv_exchange(request: web.Request, amount) -> web.Response:
    """Calculates SigRSV exchange

    

    :param amount: 
    :type amount: int

    """
    return web.Response(status=200)


async def calc_sigma_usd_exchange(request: web.Request, amount) -> web.Response:
    """Calculates SigUSD exchange

    

    :param amount: 
    :type amount: int

    """
    return web.Response(status=200)


async def do_sigma_rsv_exchange(request: web.Request, amount, address, check_rate=None, execution_fee=None) -> web.Response:
    """Builds ErgoPayRequest for SigRSV exchange

    

    :param amount: 
    :type amount: int
    :param address: 
    :type address: str
    :param check_rate: 
    :type check_rate: int
    :param execution_fee: 
    :type execution_fee: int

    """
    return web.Response(status=200)


async def do_sigma_usd_exchange(request: web.Request, amount, address, check_rate=None, execution_fee=None) -> web.Response:
    """Builds ErgoPayRequest for SigUSD exchange

    

    :param amount: 
    :type amount: int
    :param address: 
    :type address: str
    :param check_rate: 
    :type check_rate: int
    :param execution_fee: 
    :type execution_fee: int

    """
    return web.Response(status=200)


async def get_age_usd_info(request: web.Request, ) -> web.Response:
    """Returns state of AgeUSD at this moment

    


    """
    return web.Response(status=200)


async def get_sigma_rsv_price(request: web.Request, ) -> web.Response:
    """Lists price and available volume for SigmaRSV

    


    """
    return web.Response(status=200)


async def get_sigma_usd_price(request: web.Request, ) -> web.Response:
    """Lists price and available volume for SigmaUSD

    


    """
    return web.Response(status=200)

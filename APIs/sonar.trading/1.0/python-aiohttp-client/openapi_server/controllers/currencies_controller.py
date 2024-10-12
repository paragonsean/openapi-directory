from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def convert_get(request: web.Request, _from, to, amount=None, decimal_places=None) -> web.Response:
    """Convert a currency amount to multiple other currencies

    

    :param _from: Currency you want to convert. For example, EUR
    :type _from: str
    :param to: Comma separated list of currencies codes. For example, USD
    :type to: str
    :param amount: This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed.
    :type amount: str
    :param decimal_places: This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 12 is assumed.
    :type decimal_places: str

    """
    return web.Response(status=200)


async def country_currencies_get(request: web.Request, language=None) -> web.Response:
    """Return a list of all currencies of countries, available via service

    

    :param language: Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language.
    :type language: str

    """
    return web.Response(status=200)


async def digital_currencies_get(request: web.Request, language=None) -> web.Response:
    """Return a list of all digital currencies, available via service

    

    :param language: Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language.
    :type language: str

    """
    return web.Response(status=200)


async def history_get(request: web.Request, _from, to, _date, amount=None, decimal_places=None) -> web.Response:
    """Return a historic rate for a currencies

    

    :param _from: Currency you want to convert. For example, EUR
    :type _from: str
    :param to: Comma separated list of currencies codes. For example, USD
    :type to: str
    :param _date: UTC date should be in the form of YYYY-MM-DD, for example, 2018-06-20. Data available from 2018-06-19 only.
    :type _date: str
    :param amount: This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed.
    :type amount: str
    :param decimal_places: This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 4 is assumed.
    :type decimal_places: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def iatu_balance_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key) -> web.Response:
    """Account balance

    Returns a JSON of the account balance.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str

    """
    return web.Response(status=200)

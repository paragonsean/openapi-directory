from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_connection import DataConnection
from openapi_server import util


async def create_partner_expense_connection(request: web.Request, company_id) -> web.Response:
    """Create Partner Expense connection

    Creates a Partner Expense data connection

    :param company_id: 
    :type company_id: str
    :type company_id: str

    """
    return web.Response(status=200)

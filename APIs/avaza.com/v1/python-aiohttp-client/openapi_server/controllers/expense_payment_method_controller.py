from typing import List, Dict
from aiohttp import web

from openapi_server.models.expense_payment_method_dropdown_list import ExpensePaymentMethodDropdownList
from openapi_server import util


async def expense_payment_method_lookup(request: web.Request, ) -> web.Response:
    """Gets minimal list of Expense Payment Methods.

    


    """
    return web.Response(status=200)

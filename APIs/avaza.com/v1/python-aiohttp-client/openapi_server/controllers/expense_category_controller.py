from typing import List, Dict
from aiohttp import web

from openapi_server.models.expense_category_list import ExpenseCategoryList
from openapi_server import util


async def expense_category_get(request: web.Request, is_enabled=None) -> web.Response:
    """Gets list of Expense Categories

    The default sort order is by Name asc

    :param is_enabled: Optional filter on for enabled/disabled categories. Defaults to true.
    :type is_enabled: bool

    """
    return web.Response(status=200)

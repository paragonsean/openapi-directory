from typing import List, Dict
from aiohttp import web

from openapi_server.models.expense_group_dropdown_list import ExpenseGroupDropdownList
from openapi_server import util


async def expense_group_lookup(request: web.Request, page_size=None, page_number=None, search=None) -> web.Response:
    """Gets minimal list of Expense Groups.

    Expense Groups are for adhoc grouping of reported expenses. e.g. for expenses incurred on a Trip

    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param search: Search string to match against Expense Group Name
    :type search: str

    """
    return web.Response(status=200)

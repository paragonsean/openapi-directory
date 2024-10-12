from typing import List, Dict
from aiohttp import web

from openapi_server.models.expense_type_model import ExpenseTypeModel
from openapi_server.models.expense_types_model import ExpenseTypesModel
from openapi_server import util


async def expense_types_get_by_country(request: web.Request, country) -> web.Response:
    """expense_types_get_by_country

    Description: This operation retrieves all Expense Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Expense Types including id and type description.

    :param country: The country used to filter Expense Types
    :type country: str

    """
    return web.Response(status=200)


async def expense_types_get_by_id(request: web.Request, id) -> web.Response:
    """expense_types_get_by_id

    Description: This operation retrieves all Expense Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Expense Types including id and type description.

    :param id: The ID of Expense Type used to retreive the Expense Type information
    :type id: int

    """
    return web.Response(status=200)

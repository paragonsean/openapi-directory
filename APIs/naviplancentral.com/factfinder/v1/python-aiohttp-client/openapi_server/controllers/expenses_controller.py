from typing import List, Dict
from aiohttp import web

from openapi_server.models.expense_model import ExpenseModel
from openapi_server.models.expense_with_id_model import ExpenseWithIdModel
from openapi_server.models.expenses_model import ExpensesModel
from openapi_server import util


async def expenses_delete_by_id(request: web.Request, id) -> web.Response:
    """expenses_delete_by_id

    Description: The operation removes an Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Expense from a Fact Finder.

    :param id: The Expense ID used to identify which Expense to remove
    :type id: int

    """
    return web.Response(status=200)


async def expenses_get_by_id(request: web.Request, id) -> web.Response:
    """expenses_get_by_id

    Description: This operation retrieves a single Expense for the specified Expense ID.&lt;br /&gt;                Purpose: Provides access to the Expense including description and Expense type.

    :param id: The ID of the Expense used to retreive the Expense
    :type id: int

    """
    return web.Response(status=200)


async def expenses_get_expenses_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """expenses_get_expenses_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Expenses for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Expenses including description and Expense type.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Expenses
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def expenses_post_by_model(request: web.Request, model) -> web.Response:
    """expenses_post_by_model

    Description: The operation creates an Expense.&lt;br /&gt;                Purpose: Allows for creation of Expenses on a Fact Finder.

    :param model: The Expense to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = ExpenseModel.from_dict(model)
    return web.Response(status=200)


async def expenses_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """expenses_put_by_id_model

    Description: The operation updates an Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of an Expense on a Fact Finder. &lt;br /&gt;&lt;br /&gt;                Note: Expense type cannot be changed for expenses prepopulated from NaviPlan.

    :param id: The existing Expense ID used to identify which Expense to update
    :type id: int
    :param model: The Expense to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = ExpenseModel.from_dict(model)
    return web.Response(status=200)

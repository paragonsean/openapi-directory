from typing import List, Dict
from aiohttp import web

from openapi_server.models.income_model import IncomeModel
from openapi_server.models.income_with_id_model import IncomeWithIdModel
from openapi_server.models.incomes_model import IncomesModel
from openapi_server import util


async def incomes_delete_by_id(request: web.Request, id) -> web.Response:
    """incomes_delete_by_id

    Description: The operation removes an Income tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Income from a Fact Finder.

    :param id: The Income ID used to identify which Income to remove
    :type id: int

    """
    return web.Response(status=200)


async def incomes_get_by_id(request: web.Request, id) -> web.Response:
    """incomes_get_by_id

    Description: This operation retrieves a single Income for the specified Income ID.&lt;br /&gt;                Purpose: Provides access to the Income including annual amount and start date.

    :param id: The ID of the Income used to retreive the Income
    :type id: int

    """
    return web.Response(status=200)


async def incomes_get_incomes_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """incomes_get_incomes_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Incomes for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Incomes including annual amount and start date.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Incomes
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def incomes_post_by_model(request: web.Request, model) -> web.Response:
    """incomes_post_by_model

    Description: The operation creates an Income.&lt;br /&gt;                Purpose: Allows for creation of Incomes on a Fact Finder.

    :param model: The Income to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = IncomeModel.from_dict(model)
    return web.Response(status=200)


async def incomes_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """incomes_put_by_id_model

    Description: The operation updates an Income.&lt;br /&gt;                Purpose: Allows for complete replacement of an Income on a Fact Finder.

    :param id: The existing Income ID used to identify which Income to update
    :type id: int
    :param model: The Income to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = IncomeModel.from_dict(model)
    return web.Response(status=200)

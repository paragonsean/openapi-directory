from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def fact_delete(request: web.Request, id) -> web.Response:
    """fact_delete

    Delete a Fact entry identified by the id.

    :param id: Fact ID
    :type id: str

    """
    return web.Response(status=200)


async def fact_get_0(request: web.Request, id=None) -> web.Response:
    """fact_get_0

    Get a Fact belonging to the id.

    :param id: ID of the fact to fetch
    :type id: str

    """
    return web.Response(status=200)


async def fact_put(request: web.Request, fact, category, subcategory, tags) -> web.Response:
    """fact_put

    Add a Fact entry to the database (private collection).

    :param fact: Fact Text
    :type fact: str
    :param category: Category of the fact
    :type category: str
    :param subcategory: Sub Category of the fact
    :type subcategory: str
    :param tags: Tags
    :type tags: str

    """
    return web.Response(status=200)

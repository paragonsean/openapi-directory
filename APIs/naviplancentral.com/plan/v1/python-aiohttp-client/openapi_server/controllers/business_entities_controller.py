from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_entities_model import BusinessEntitiesModel
from openapi_server.models.business_entity_model import BusinessEntityModel
from openapi_server import util


async def business_entities_get_by_id_planid(request: web.Request, id, plan_id) -> web.Response:
    """Retrieve a business entity

    This operation retrieves a business entity from the plan.

    :param id: ID of business entity to retrieve
    :type id: int
    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)


async def business_entities_get_by_planid(request: web.Request, plan_id) -> web.Response:
    """Retrieve business entities

    This operation retrieves a list of all of the business entities in the plan.

    :param plan_id: Id of the plan to retrieve data from (e.g. 1001-11-3).
    :type plan_id: str

    """
    return web.Response(status=200)

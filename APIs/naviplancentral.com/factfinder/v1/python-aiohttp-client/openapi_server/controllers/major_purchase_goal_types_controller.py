from typing import List, Dict
from aiohttp import web

from openapi_server.models.major_purchase_goal_type_model import MajorPurchaseGoalTypeModel
from openapi_server.models.major_purchase_goal_types_model import MajorPurchaseGoalTypesModel
from openapi_server import util


async def major_purchase_goal_types_get_by_country(request: web.Request, country) -> web.Response:
    """major_purchase_goal_types_get_by_country

    Description: This operation retrieves all Major Purchase Goal Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Major Purchase Goal Types including id and type description.

    :param country: The country used to filter Major Purchase Goal Types
    :type country: str

    """
    return web.Response(status=200)


async def major_purchase_goal_types_get_by_id(request: web.Request, id) -> web.Response:
    """major_purchase_goal_types_get_by_id

    Description: This operation retrieves the Major Purchase Goal Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Major Purchase Goal Types including id and type description.

    :param id: The ID of Major Purchase Goal Type used to retreive the Major Purchase Goal Type information
    :type id: int

    """
    return web.Response(status=200)

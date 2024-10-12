from typing import List, Dict
from aiohttp import web

from openapi_server.models.households_model import HouseholdsModel
from openapi_server import util


async def households_get_by_householdid(request: web.Request, household_id=None) -> web.Response:
    """Retrieve all Households associated with the user

    This operation retrieves a list of households the current user has access to or one household specified by a householdId parameter

    :param household_id: The Id of the specific household to retrieve
    :type household_id: int

    """
    return web.Response(status=200)

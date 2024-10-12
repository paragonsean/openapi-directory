from typing import List, Dict
from aiohttp import web

from openapi_server.models.advisor_model import AdvisorModel
from openapi_server.models.advisors_model import AdvisorsModel
from openapi_server import util


async def advisors_get(request: web.Request, ) -> web.Response:
    """Retrieve Advisors

    This operation retrieves a list of all of the Advisors in the plan.


    """
    return web.Response(status=200)


async def advisors_get_by_householdid_clientid(request: web.Request, household_id, client_id) -> web.Response:
    """Retrieve Advisors for a Client

    This operation retrieves a list of all of the Advisors for the client.

    :param household_id: Integer id of the household
    :type household_id: int
    :param client_id: Guid id of the client.
    :type client_id: str

    """
    return web.Response(status=200)


async def advisors_get_by_id(request: web.Request, id) -> web.Response:
    """Retrieve an Advisor

    This operation retrieves an Advisor from the plan.

    :param id: Guid id of the advisor
    :type id: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_staff_model import ApplicationStaffModel
from openapi_server.models.application_staff_model_results import ApplicationStaffModelResults
from openapi_server import util


async def v2_tier2_short_name_staff_staff_application_staff_idget(request: web.Request, short_name, application_staff_id) -> web.Response:
    """Get a specific application staff given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param application_staff_id: The unique ID of the ApplicationStaff
    :type application_staff_id: str

    """
    return web.Response(status=200)


async def v2_tier2_short_name_staff_staff_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all the staff members linked to a specific company

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)

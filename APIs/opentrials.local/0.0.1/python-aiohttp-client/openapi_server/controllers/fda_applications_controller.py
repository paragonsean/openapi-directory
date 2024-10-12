from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.fda_application import FDAApplication
from openapi_server.models.fda_application_list import FDAApplicationList
from openapi_server import util


async def get_fda_application(request: web.Request, id) -> web.Response:
    """get_fda_application

    Returns an FDA application details

    :param id: ID of the FDA application
    :type id: str

    """
    return web.Response(status=200)


async def list_fda_applications(request: web.Request, page=None, per_page=None) -> web.Response:
    """list_fda_applications

    Returns FDA applications

    :param page: The page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)

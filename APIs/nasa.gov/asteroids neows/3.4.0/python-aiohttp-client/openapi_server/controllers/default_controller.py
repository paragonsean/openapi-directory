from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_projects_format_get200_response import ApiProjectsFormatGet200Response
from openapi_server.models.project import Project
from openapi_server import util


async def api_get(request: web.Request, ) -> web.Response:
    """api_get

    Returns the swagger specification for the API.


    """
    return web.Response(status=200)


async def api_projects_format_get(request: web.Request, updated_since, format, format2) -> web.Response:
    """api_projects_format_get

    Returns a list of available technology project IDs.

    :param updated_since: ISO 8601 full-date in the format YYYY-MM-DD. Filters the list of available ID values by their lastUpdated parameter.
    :type updated_since: str
    :param format: The response type desired.
    :type format: str
    :param format2: Automatically added
    :type format2: str

    """
    updated_since = util.deserialize_date(updated_since)
    return web.Response(status=200)


async def api_projects_id_format_get(request: web.Request, id, format, format2) -> web.Response:
    """api_projects_id_format_get

    Returns information about a specific technology project.

    :param id: ID of project to fetch
    :type id: int
    :param format: The response type desired.
    :type format: str
    :param format2: Automatically added
    :type format2: str

    """
    return web.Response(status=200)

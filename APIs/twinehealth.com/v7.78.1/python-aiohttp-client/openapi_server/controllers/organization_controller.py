from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_organization_response import FetchOrganizationResponse
from openapi_server import util


async def fetch_organization(request: web.Request, id) -> web.Response:
    """Get an organization

    Get an organization record by id.

    :param id: Organization identifier
    :type id: str

    """
    return web.Response(status=200)

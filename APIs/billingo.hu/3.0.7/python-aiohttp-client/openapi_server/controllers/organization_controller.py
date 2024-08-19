from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.organization_data import OrganizationData
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse
from openapi_server import util


async def get_organization_data(request: web.Request, ) -> web.Response:
    """Retrieve a organization data.

    Retrieves the data of organization.


    """
    return web.Response(status=200)

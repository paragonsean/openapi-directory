from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_data_role_interface import CompanyDataRoleInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_role_repository_v1_delete_delete(request: web.Request, role_id) -> web.Response:
    """company/role/{roleId}

    Delete a role.

    :param role_id: 
    :type role_id: int

    """
    return web.Response(status=200)


async def company_role_repository_v1_get_get(request: web.Request, role_id) -> web.Response:
    """company/role/{roleId}

    Returns the list of permissions for a specified role.

    :param role_id: 
    :type role_id: int

    """
    return web.Response(status=200)

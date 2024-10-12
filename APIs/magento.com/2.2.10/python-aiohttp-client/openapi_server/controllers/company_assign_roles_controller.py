from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_acl_v1_assign_roles_put_request import CompanyAclV1AssignRolesPutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_acl_v1_assign_roles_put(request: web.Request, body=None) -> web.Response:
    """company/assignRoles

    Change a role for a company user.

    :param body: 
    :type body: dict | bytes

    """
    body = CompanyAclV1AssignRolesPutRequest.from_dict(body)
    return web.Response(status=200)

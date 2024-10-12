from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_acl_v1_get_users_by_role_id_get(request: web.Request, role_id) -> web.Response:
    """company/role/{roleId}/users

    View the list of company users assigned to a specified role.

    :param role_id: 
    :type role_id: int

    """
    return web.Response(status=200)

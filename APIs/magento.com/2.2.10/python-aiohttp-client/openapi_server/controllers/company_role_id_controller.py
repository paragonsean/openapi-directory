from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_data_role_interface import CompanyDataRoleInterface
from openapi_server.models.company_role_repository_v1_save_post_request import CompanyRoleRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_role_repository_v1_save_put(request: web.Request, id, body=None) -> web.Response:
    """company/role/{id}

    Create or update a role for a selected company.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyRoleRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)

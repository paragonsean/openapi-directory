from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_data_hierarchy_interface import CompanyDataHierarchyInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_company_hierarchy_v1_get_company_hierarchy_get(request: web.Request, id) -> web.Response:
    """hierarchy/{id}

    Returns the list of teams and company users in the company structure.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)

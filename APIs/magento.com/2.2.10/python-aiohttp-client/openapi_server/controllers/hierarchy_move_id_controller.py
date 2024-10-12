from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_company_hierarchy_v1_move_node_put_request import CompanyCompanyHierarchyV1MoveNodePutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_company_hierarchy_v1_move_node_put(request: web.Request, id, body=None) -> web.Response:
    """hierarchy/move/{id}

    Moves teams and users within the company structure.

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyCompanyHierarchyV1MoveNodePutRequest.from_dict(body)
    return web.Response(status=200)

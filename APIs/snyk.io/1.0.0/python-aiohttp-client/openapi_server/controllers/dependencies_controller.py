from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_all_dependencies200_response import ListAllDependencies200Response
from openapi_server.models.list_all_dependencies_request import ListAllDependenciesRequest
from openapi_server import util


async def list_all_dependencies(request: web.Request, org_id, sort_by=None, order=None, page=None, per_page=None, body=None) -> web.Response:
    """List all dependencies

    

    :param org_id: The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param sort_by: The field to sort results by.
    :type sort_by: str
    :param order: The direction to sort results by.
    :type order: str
    :param page: The page of results to fetch.
    :type page: 
    :param per_page: The number of results to fetch per page (maximum is 1000).
    :type per_page: 
    :param body: 
    :type body: dict | bytes

    """
    body = ListAllDependenciesRequest.from_dict(body)
    return web.Response(status=200)

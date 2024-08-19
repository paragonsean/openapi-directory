from typing import List, Dict
from aiohttp import web

from openapi_server.models.breadcrumbs_api_models_pathfinder_pathfinder_request import BreadcrumbsAPIModelsPathfinderPathfinderRequest
from openapi_server.models.breadcrumbs_api_models_pathfinder_pathfinder_response import BreadcrumbsAPIModelsPathfinderPathfinderResponse
from openapi_server.models.breadcrumbs_response_unauthorized_response import BreadcrumbsResponseUnauthorizedResponse
from openapi_server.models.breadcrumbs_response_unprocessable_response import BreadcrumbsResponseUnprocessableResponse
from openapi_server import util


async def pathfinder_post(request: web.Request, body=None) -> web.Response:
    """Automatically find path between crypto addresses

    

    :param body: 
    :type body: dict | bytes

    """
    body = BreadcrumbsAPIModelsPathfinderPathfinderRequest.from_dict(body)
    return web.Response(status=200)

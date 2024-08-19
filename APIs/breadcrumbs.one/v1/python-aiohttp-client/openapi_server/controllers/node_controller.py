from typing import List, Dict
from aiohttp import web

from openapi_server.models.breadcrumbs_api_models_node_node_request import BreadcrumbsAPIModelsNodeNodeRequest
from openapi_server.models.breadcrumbs_api_models_node_node_response import BreadcrumbsAPIModelsNodeNodeResponse
from openapi_server.models.breadcrumbs_response_unauthorized_response import BreadcrumbsResponseUnauthorizedResponse
from openapi_server.models.breadcrumbs_response_unprocessable_response import BreadcrumbsResponseUnprocessableResponse
from openapi_server import util


async def node_post(request: web.Request, body=None) -> web.Response:
    """Shows the incoming and outgoing transactions from blockchain address

    

    :param body: 
    :type body: dict | bytes

    """
    body = BreadcrumbsAPIModelsNodeNodeRequest.from_dict(body)
    return web.Response(status=200)

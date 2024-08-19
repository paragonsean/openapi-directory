from typing import List, Dict
from aiohttp import web

from openapi_server.models.breadcrumbs_api_models_sanction_sanctioned_request import BreadcrumbsAPIModelsSanctionSanctionedRequest
from openapi_server.models.breadcrumbs_api_models_sanction_sanctioned_response import BreadcrumbsAPIModelsSanctionSanctionedResponse
from openapi_server.models.breadcrumbs_response_unauthorized_response import BreadcrumbsResponseUnauthorizedResponse
from openapi_server.models.breadcrumbs_response_unprocessable_response import BreadcrumbsResponseUnprocessableResponse
from openapi_server import util


async def sanctioned_address_post(request: web.Request, body=None) -> web.Response:
    """Verify if the addresses provided are in our sanctioned lists

    

    :param body: 
    :type body: list | bytes

    """
    body = [BreadcrumbsAPIModelsSanctionSanctionedRequest.from_dict(d) for d in body]
    return web.Response(status=200)

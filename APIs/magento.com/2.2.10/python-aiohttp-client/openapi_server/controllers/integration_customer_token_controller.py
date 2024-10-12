from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.integration_admin_token_service_v1_create_admin_access_token_post_request import IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest
from openapi_server import util


async def integration_customer_token_service_v1_create_customer_access_token_post(request: web.Request, body=None) -> web.Response:
    """integration/customer/token

    Create access token for admin given the customer credentials.

    :param body: 
    :type body: dict | bytes

    """
    body = IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v1_apps_post200_response import ApiV1AppsPost200Response
from openapi_server.models.api_v1_apps_post_request import ApiV1AppsPostRequest
from openapi_server.models.application import Application
from openapi_server.models.error import Error
from openapi_server import util


async def api_v1_apps_post(request: web.Request, body=None) -> web.Response:
    """api_v1_apps_post

    Create a new application to obtain OAuth2 credentials.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1AppsPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_apps_verify_credentials_get(request: web.Request, ) -> web.Response:
    """api_v1_apps_verify_credentials_get

    Confirm that the app&#39;s OAuth2 credentials work.


    """
    return web.Response(status=200)

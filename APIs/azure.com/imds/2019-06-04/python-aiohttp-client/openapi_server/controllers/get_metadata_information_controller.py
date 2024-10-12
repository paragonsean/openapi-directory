from typing import List, Dict
from aiohttp import web

from openapi_server.models.identity_error_response import IdentityErrorResponse
from openapi_server.models.identity_info_response import IdentityInfoResponse
from openapi_server import util


async def identity_get_info(request: web.Request, metadata, api_version) -> web.Response:
    """identity_get_info

    Get information about AAD Metadata

    :param metadata: This must be set to &#39;true&#39;.
    :type metadata: str
    :param api_version: This is the API version to use.
    :type api_version: str

    """
    return web.Response(status=200)

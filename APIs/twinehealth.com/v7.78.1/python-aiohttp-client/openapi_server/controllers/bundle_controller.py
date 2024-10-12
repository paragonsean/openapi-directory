from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_bundle_request import CreateBundleRequest
from openapi_server.models.create_bundle_response import CreateBundleResponse
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_bundle_response import FetchBundleResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.update_bundle_request import UpdateBundleRequest
from openapi_server.models.update_bundle_response import UpdateBundleResponse
from openapi_server import util


async def create_bundle(request: web.Request, body) -> web.Response:
    """Create bundle

    Create a bundle in a patient&#39;s plan

    :param body: 
    :type body: dict | bytes

    """
    body = CreateBundleRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_bundle(request: web.Request, id) -> web.Response:
    """Get a bundle

    Get a bundle from a patient&#39;s plan.

    :param id: Bundle identifier
    :type id: str

    """
    return web.Response(status=200)


async def update_bundle(request: web.Request, id, body) -> web.Response:
    """Update a bundle

    Updte a bundle from a patient&#39;s plan.

    :param id: Bundle identifier
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateBundleRequest.from_dict(body)
    return web.Response(status=200)

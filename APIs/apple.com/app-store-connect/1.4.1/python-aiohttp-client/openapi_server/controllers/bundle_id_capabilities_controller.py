from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_id_capability_create_request import BundleIdCapabilityCreateRequest
from openapi_server.models.bundle_id_capability_response import BundleIdCapabilityResponse
from openapi_server.models.bundle_id_capability_update_request import BundleIdCapabilityUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_id_capabilities_create_instance(request: web.Request, body) -> web.Response:
    """bundle_id_capabilities_create_instance

    

    :param body: BundleIdCapability representation
    :type body: dict | bytes

    """
    body = BundleIdCapabilityCreateRequest.from_dict(body)
    return web.Response(status=200)


async def bundle_id_capabilities_delete_instance(request: web.Request, id) -> web.Response:
    """bundle_id_capabilities_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def bundle_id_capabilities_update_instance(request: web.Request, id, body) -> web.Response:
    """bundle_id_capabilities_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: BundleIdCapability representation
    :type body: dict | bytes

    """
    body = BundleIdCapabilityUpdateRequest.from_dict(body)
    return web.Response(status=200)

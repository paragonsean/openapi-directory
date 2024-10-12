from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.registry_configuration import RegistryConfiguration
from openapi_server.models.registry_configuration_request import RegistryConfigurationRequest
from openapi_server import util


async def create_registry(request: web.Request, body, validate=None, x_anchore_account=None) -> web.Response:
    """Add a new registry

    Adds a new registry to the system

    :param body: 
    :type body: dict | bytes
    :param validate: flag to determine whether or not to validate registry/credential at registry add time
    :type validate: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    body = RegistryConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_registry(request: web.Request, registry, x_anchore_account=None) -> web.Response:
    """Delete a registry configuration

    Delete a registry configuration record from the system. Does not remove any images.

    :param registry: 
    :type registry: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_registry(request: web.Request, registry, x_anchore_account=None) -> web.Response:
    """Get a specific registry configuration

    Get information on a specific registry

    :param registry: 
    :type registry: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def list_registries(request: web.Request, x_anchore_account=None) -> web.Response:
    """List configured registries

    List all configured registries the system can/will watch

    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def update_registry(request: web.Request, registry, body, validate=None, x_anchore_account=None) -> web.Response:
    """Update/replace a registry configuration

    Replaces an existing registry record with the given record

    :param registry: 
    :type registry: str
    :param body: 
    :type body: dict | bytes
    :param validate: flag to determine whether or not to validate registry/credential at registry update time
    :type validate: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    body = RegistryConfigurationRequest.from_dict(body)
    return web.Response(status=200)

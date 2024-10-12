from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.deleted import Deleted
from openapi_server.models.error_template import ErrorTemplate
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.service import Service
from openapi_server.models.target import Target
from openapi_server import util


async def all_services(request: web.Request, ) -> web.Response:
    """Get all services

    Get all services


    """
    return web.Response(status=200)


async def create_service(request: web.Request, body=None) -> web.Response:
    """Create a new service descriptor

    Create a new service descriptor

    :param body: 
    :type body: dict | bytes

    """
    body = Service.from_dict(body)
    return web.Response(status=200)


async def create_service_template(request: web.Request, service_id, body=None) -> web.Response:
    """Create a service descriptor error template

    Update a service descriptor targets

    :param service_id: The service id
    :type service_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ErrorTemplate.from_dict(body)
    return web.Response(status=200)


async def delete_service(request: web.Request, service_id) -> web.Response:
    """Delete a service descriptor

    Delete a service descriptor

    :param service_id: The service id
    :type service_id: str

    """
    return web.Response(status=200)


async def delete_service_template(request: web.Request, service_id) -> web.Response:
    """Delete a service descriptor error template

    Delete a service descriptor error template

    :param service_id: The service id
    :type service_id: str

    """
    return web.Response(status=200)


async def patch_service(request: web.Request, service_id, body=None) -> web.Response:
    """Update a service descriptor with a diff

    Update a service descriptor with a diff

    :param service_id: The service id
    :type service_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def service(request: web.Request, service_id) -> web.Response:
    """Get a service descriptor

    Get a service descriptor

    :param service_id: The service id
    :type service_id: str

    """
    return web.Response(status=200)


async def service_add_target(request: web.Request, service_id, body=None) -> web.Response:
    """Add a target to a service descriptor

    Add a target to a service descriptor

    :param service_id: The service id
    :type service_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Target.from_dict(body)
    return web.Response(status=200)


async def service_delete_target(request: web.Request, service_id) -> web.Response:
    """Delete a service descriptor target

    Delete a service descriptor target

    :param service_id: The service id
    :type service_id: str

    """
    return web.Response(status=200)


async def service_group_services(request: web.Request, service_group_id) -> web.Response:
    """Get all services descriptor for a group

    Get all services descriptor for a group

    :param service_group_id: The service group id
    :type service_group_id: str

    """
    return web.Response(status=200)


async def service_targets(request: web.Request, service_id) -> web.Response:
    """Get a service descriptor targets

    Get a service descriptor targets

    :param service_id: The service id
    :type service_id: str

    """
    return web.Response(status=200)


async def service_template(request: web.Request, service_id) -> web.Response:
    """Get a service descriptor error template

    Get a service descriptor error template

    :param service_id: The service id
    :type service_id: str

    """
    return web.Response(status=200)


async def update_service(request: web.Request, service_id, body=None) -> web.Response:
    """Update a service descriptor

    Update a service descriptor

    :param service_id: The service id
    :type service_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Service.from_dict(body)
    return web.Response(status=200)


async def update_service_targets(request: web.Request, service_id, body=None) -> web.Response:
    """Update a service descriptor targets

    Update a service descriptor targets

    :param service_id: The service id
    :type service_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_service_template(request: web.Request, service_id, body=None) -> web.Response:
    """Update an error template to a service descriptor

    Update an error template to a service descriptor

    :param service_id: The service id
    :type service_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ErrorTemplate.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.deleted import Deleted
from openapi_server.models.group import Group
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.quotas import Quotas
from openapi_server import util


async def all_api_keys(request: web.Request, ) -> web.Response:
    """Get all api keys

    Get all api keys


    """
    return web.Response(status=200)


async def api_key(request: web.Request, service_id, client_id) -> web.Response:
    """Get an api key

    Get an api key for a specified service descriptor

    :param service_id: The api key service id
    :type service_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def api_key_from_group(request: web.Request, group_id, client_id) -> web.Response:
    """Get an api key

    Get an api key for a specified service group

    :param group_id: The api key group id
    :type group_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def api_key_from_group_quotas(request: web.Request, group_id, client_id) -> web.Response:
    """Get the quota state of an api key

    Get the quota state of an api key

    :param group_id: The api key group id
    :type group_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def api_key_group(request: web.Request, service_id, client_id) -> web.Response:
    """Get the group of an api key

    Get the group of an api key

    :param service_id: The api key service id
    :type service_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def api_key_quotas(request: web.Request, service_id, client_id) -> web.Response:
    """Get the quota state of an api key

    Get the quota state of an api key

    :param service_id: The api key service id
    :type service_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def api_keys(request: web.Request, service_id) -> web.Response:
    """Get all api keys for the group of a service

    Get all api keys for the group of a service

    :param service_id: The api key service id
    :type service_id: str

    """
    return web.Response(status=200)


async def api_keys_from_group(request: web.Request, group_id) -> web.Response:
    """Get all api keys for the group of a service

    Get all api keys for the group of a service

    :param group_id: The api key group id
    :type group_id: str

    """
    return web.Response(status=200)


async def create_api_key(request: web.Request, service_id, body=None) -> web.Response:
    """Create a new api key for a service

    

    :param service_id: The api key service id
    :type service_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def create_api_key_from_group(request: web.Request, group_id, body=None) -> web.Response:
    """Create a new api key for a group

    Create a new api key for a group

    :param group_id: The api key group id
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def delete_api_key(request: web.Request, service_id, client_id) -> web.Response:
    """Delete an api key

    Delete an api key for a specified service descriptor

    :param service_id: The api key service id
    :type service_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def delete_api_key_from_group(request: web.Request, group_id, client_id) -> web.Response:
    """Delete an api key

    Delete an api key for a specified service group

    :param group_id: The api key group id
    :type group_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def patch_api_key(request: web.Request, service_id, client_id, body=None) -> web.Response:
    """Update an api key with a diff

    Update an api key for a specified service descriptor with a diff

    :param service_id: The api key service id
    :type service_id: str
    :param client_id: the api key id
    :type client_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def patch_api_key_from_group(request: web.Request, group_id, client_id, body=None) -> web.Response:
    """Update an api key with a diff

    Update an api key for a specified service descriptor with a diff

    :param group_id: The api key group id
    :type group_id: str
    :param client_id: the api key id
    :type client_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def reset_api_key_from_group_quotas(request: web.Request, group_id, client_id) -> web.Response:
    """Reset the quota state of an api key

    Reset the quota state of an api key

    :param group_id: The api key group id
    :type group_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def reset_api_key_quotas(request: web.Request, service_id, client_id) -> web.Response:
    """Reset the quota state of an api key

    Reset the quota state of an api key

    :param service_id: The api key service id
    :type service_id: str
    :param client_id: the api key id
    :type client_id: str

    """
    return web.Response(status=200)


async def update_api_key(request: web.Request, service_id, client_id, body=None) -> web.Response:
    """Update an api key

    Update an api key for a specified service descriptor

    :param service_id: The api key service id
    :type service_id: str
    :param client_id: the api key id
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def update_api_key_from_group(request: web.Request, group_id, client_id, body=None) -> web.Response:
    """Update an api key

    Update an api key for a specified service group

    :param group_id: The api key group id
    :type group_id: str
    :param client_id: the api key id
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.redis_create_or_update_parameters import RedisCreateOrUpdateParameters
from openapi_server.models.redis_list_keys_result import RedisListKeysResult
from openapi_server.models.redis_list_result import RedisListResult
from openapi_server.models.redis_reboot_parameters import RedisRebootParameters
from openapi_server.models.redis_regenerate_key_parameters import RedisRegenerateKeyParameters
from openapi_server.models.redis_resource import RedisResource
from openapi_server.models.redis_resource_with_access_key import RedisResourceWithAccessKey
from openapi_server import util


async def redis_create_or_update(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """redis_create_or_update

    Create a Redis cache, or replace (overwrite/recreate, with potential downtime) an existing cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Redis operation.
    :type parameters: dict | bytes

    """
    parameters = RedisCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def redis_delete(request: web.Request, resource_group_name, name, api_version, subscription_id) -> web.Response:
    """redis_delete

    Deletes a Redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_force_reboot(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """redis_force_reboot

    Reboot specified Redis node(s). This operation requires write permission to the cache resource. There can be potential data loss.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Specifies which Redis node(s) to reboot.
    :type parameters: dict | bytes

    """
    parameters = RedisRebootParameters.from_dict(parameters)
    return web.Response(status=200)


async def redis_get(request: web.Request, resource_group_name, name, api_version, subscription_id) -> web.Response:
    """redis_get

    Gets a Redis cache (resource description).

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """redis_list

    Gets all Redis caches in the specified subscription.

    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """redis_list_by_resource_group

    Gets all Redis caches in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_list_keys(request: web.Request, resource_group_name, name, api_version, subscription_id) -> web.Response:
    """redis_list_keys

    Retrieve a Redis cache&#39;s access keys. This operation requires write permission to the cache resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_regenerate_key(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """redis_regenerate_key

    Regenerate the access keys for a Redis cache. This operation requires write permission to the cache resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Specifies which key to reset.
    :type parameters: dict | bytes

    """
    parameters = RedisRegenerateKeyParameters.from_dict(parameters)
    return web.Response(status=200)

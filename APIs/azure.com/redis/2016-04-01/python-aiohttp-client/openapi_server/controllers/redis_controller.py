from typing import List, Dict
from aiohttp import web

from openapi_server.models.export_rdb_parameters import ExportRDBParameters
from openapi_server.models.import_rdb_parameters import ImportRDBParameters
from openapi_server.models.redis_access_keys import RedisAccessKeys
from openapi_server.models.redis_create_parameters import RedisCreateParameters
from openapi_server.models.redis_firewall_rule import RedisFirewallRule
from openapi_server.models.redis_firewall_rule_list_result import RedisFirewallRuleListResult
from openapi_server.models.redis_force_reboot_response import RedisForceRebootResponse
from openapi_server.models.redis_list_result import RedisListResult
from openapi_server.models.redis_patch_schedule import RedisPatchSchedule
from openapi_server.models.redis_reboot_parameters import RedisRebootParameters
from openapi_server.models.redis_regenerate_key_parameters import RedisRegenerateKeyParameters
from openapi_server.models.redis_resource import RedisResource
from openapi_server.models.redis_update_parameters import RedisUpdateParameters
from openapi_server import util


async def firewall_rules_list(request: web.Request, api_version, subscription_id, resource_group_name, cache_name) -> web.Response:
    """firewall_rules_list

    Gets all firewall rules in the specified redis cache.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str

    """
    return web.Response(status=200)


async def patch_schedules_create_or_update(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """patch_schedules_create_or_update

    Create or replace the patching schedule for Redis cache (requires Premium SKU).

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to set the patching schedule for Redis cache.
    :type parameters: dict | bytes

    """
    parameters = RedisPatchSchedule.from_dict(parameters)
    return web.Response(status=200)


async def patch_schedules_delete(request: web.Request, resource_group_name, name, api_version, subscription_id) -> web.Response:
    """patch_schedules_delete

    Deletes the patching schedule of a redis cache (requires Premium SKU).

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def patch_schedules_get(request: web.Request, resource_group_name, name, api_version, subscription_id) -> web.Response:
    """patch_schedules_get

    Gets the patching schedule of a redis cache (requires Premium SKU).

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_create(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """redis_create

    Create or replace (overwrite/recreate, with potential downtime) an existing Redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create Redis operation.
    :type parameters: dict | bytes

    """
    parameters = RedisCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def redis_delete(request: web.Request, resource_group_name, name, api_version, subscription_id) -> web.Response:
    """redis_delete

    Deletes a Redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_export_data(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """redis_export_data

    Export data from the redis cache to blobs in a container.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters for Redis export operation.
    :type parameters: dict | bytes

    """
    parameters = ExportRDBParameters.from_dict(parameters)
    return web.Response(status=200)


async def redis_firewall_rule_create_or_update(request: web.Request, resource_group_name, cache_name, rule_name, api_version, subscription_id, parameters) -> web.Response:
    """redis_firewall_rule_create_or_update

    Create or update a redis cache firewall rule

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str
    :param rule_name: The name of the firewall rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update redis firewall rule operation.
    :type parameters: dict | bytes

    """
    parameters = RedisFirewallRule.from_dict(parameters)
    return web.Response(status=200)


async def redis_firewall_rule_delete(request: web.Request, resource_group_name, cache_name, rule_name, api_version, subscription_id) -> web.Response:
    """redis_firewall_rule_delete

    Deletes a single firewall rule in a specified redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str
    :param rule_name: The name of the firewall rule.
    :type rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_firewall_rule_get(request: web.Request, resource_group_name, cache_name, rule_name, api_version, subscription_id) -> web.Response:
    """redis_firewall_rule_get

    Gets a single firewall rule in a specified redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cache_name: The name of the Redis cache.
    :type cache_name: str
    :param rule_name: The name of the firewall rule.
    :type rule_name: str
    :param api_version: Client Api Version.
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
    :param api_version: Client Api Version.
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
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_import_data(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """redis_import_data

    Import data into Redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters for Redis import operation.
    :type parameters: dict | bytes

    """
    parameters = ImportRDBParameters.from_dict(parameters)
    return web.Response(status=200)


async def redis_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """redis_list

    Gets all Redis caches in the specified subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """redis_list_by_resource_group

    Lists all Redis caches in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
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
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def redis_regenerate_key(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """redis_regenerate_key

    Regenerate Redis cache&#39;s access keys. This operation requires write permission to the cache resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Specifies which key to regenerate.
    :type parameters: dict | bytes

    """
    parameters = RedisRegenerateKeyParameters.from_dict(parameters)
    return web.Response(status=200)


async def redis_update(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """redis_update

    Update an existing Redis cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the Redis cache.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update Redis operation.
    :type parameters: dict | bytes

    """
    parameters = RedisUpdateParameters.from_dict(parameters)
    return web.Response(status=200)

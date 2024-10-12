from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.trigger_list_response import TriggerListResponse
from openapi_server.models.trigger_resource import TriggerResource
from openapi_server.models.trigger_run_list_response import TriggerRunListResponse
from openapi_server import util


async def triggers_create_or_update(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version, trigger, if_match=None) -> web.Response:
    """triggers_create_or_update

    Creates or updates a trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str
    :param trigger: Trigger resource definition.
    :type trigger: dict | bytes
    :param if_match: ETag of the trigger entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    :type if_match: str

    """
    trigger = TriggerResource.from_dict(trigger)
    return web.Response(status=200)


async def triggers_delete(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version) -> web.Response:
    """triggers_delete

    Deletes a trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def triggers_list_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """triggers_list_by_factory

    Lists triggers.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def triggers_list_runs(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version, start_time, end_time) -> web.Response:
    """triggers_list_runs

    List trigger runs.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str
    :param start_time: Start time for trigger runs.
    :type start_time: str
    :param end_time: End time for trigger runs.
    :type end_time: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def triggers_start(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version) -> web.Response:
    """triggers_start

    Starts a trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def triggers_stop(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version) -> web.Response:
    """triggers_stop

    Stops a trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)

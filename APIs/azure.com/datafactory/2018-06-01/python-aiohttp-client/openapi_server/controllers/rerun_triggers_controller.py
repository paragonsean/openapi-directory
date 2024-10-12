from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.rerun_trigger_list_response import RerunTriggerListResponse
from openapi_server.models.rerun_tumbling_window_trigger_action_parameters import RerunTumblingWindowTriggerActionParameters
from openapi_server.models.trigger_resource import TriggerResource
from openapi_server import util


async def rerun_triggers_cancel(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, rerun_trigger_name, api_version) -> web.Response:
    """rerun_triggers_cancel

    Cancels a trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param rerun_trigger_name: The rerun trigger name.
    :type rerun_trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def rerun_triggers_create(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, rerun_trigger_name, api_version, rerun_tumbling_window_trigger_action_parameters) -> web.Response:
    """rerun_triggers_create

    Creates a rerun trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param rerun_trigger_name: The rerun trigger name.
    :type rerun_trigger_name: str
    :param api_version: The API version.
    :type api_version: str
    :param rerun_tumbling_window_trigger_action_parameters: Rerun tumbling window trigger action parameters.
    :type rerun_tumbling_window_trigger_action_parameters: dict | bytes

    """
    rerun_tumbling_window_trigger_action_parameters = RerunTumblingWindowTriggerActionParameters.from_dict(rerun_tumbling_window_trigger_action_parameters)
    return web.Response(status=200)


async def rerun_triggers_list_by_trigger(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version) -> web.Response:
    """rerun_triggers_list_by_trigger

    Lists rerun triggers by an original trigger name.

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


async def rerun_triggers_start(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, rerun_trigger_name, api_version) -> web.Response:
    """rerun_triggers_start

    Starts a trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param rerun_trigger_name: The rerun trigger name.
    :type rerun_trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def rerun_triggers_stop(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, rerun_trigger_name, api_version) -> web.Response:
    """rerun_triggers_stop

    Stops a trigger.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param trigger_name: The trigger name.
    :type trigger_name: str
    :param rerun_trigger_name: The rerun trigger name.
    :type rerun_trigger_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)

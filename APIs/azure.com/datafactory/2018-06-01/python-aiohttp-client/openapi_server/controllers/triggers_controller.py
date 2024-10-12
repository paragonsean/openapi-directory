from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.trigger_list_response import TriggerListResponse
from openapi_server.models.trigger_resource import TriggerResource
from openapi_server.models.trigger_subscription_operation_status import TriggerSubscriptionOperationStatus
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


async def triggers_get_event_subscription_status(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version) -> web.Response:
    """triggers_get_event_subscription_status

    Get a trigger&#39;s event subscription status.

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


async def triggers_subscribe_to_events(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version) -> web.Response:
    """triggers_subscribe_to_events

    Subscribe event trigger to events.

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


async def triggers_unsubscribe_from_events(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version) -> web.Response:
    """triggers_unsubscribe_from_events

    Unsubscribe event trigger from events.

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

from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.trigger_resource import TriggerResource
from openapi_server import util


async def triggers_get(request: web.Request, subscription_id, resource_group_name, factory_name, trigger_name, api_version, if_none_match=None) -> web.Response:
    """triggers_get

    Gets a trigger.

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
    :param if_none_match: ETag of the trigger entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    :type if_none_match: str

    """
    return web.Response(status=200)

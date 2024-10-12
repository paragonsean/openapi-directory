from typing import List, Dict
from aiohttp import web

from openapi_server.models.iot_hub_description import IotHubDescription
from openapi_server.models.tags_resource import TagsResource
from openapi_server import util


async def iot_hub_resource_update(request: web.Request, subscription_id, resource_group_name, resource_name, api_version, iot_hub_tags) -> web.Response:
    """Update an existing IoT Hubs tags.

    Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param resource_name: Name of iot hub to update.
    :type resource_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param iot_hub_tags: Updated tag information to set into the iot hub instance.
    :type iot_hub_tags: dict | bytes

    """
    iot_hub_tags = TagsResource.from_dict(iot_hub_tags)
    return web.Response(status=200)

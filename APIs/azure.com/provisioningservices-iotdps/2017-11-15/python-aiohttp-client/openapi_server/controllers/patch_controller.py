from typing import List, Dict
from aiohttp import web

from openapi_server.models.provisioning_service_description import ProvisioningServiceDescription
from openapi_server.models.tags_resource import TagsResource
from openapi_server import util


async def iot_dps_resource_update(request: web.Request, subscription_id, resource_group_name, provisioning_service_name, api_version, provisioning_service_tags) -> web.Response:
    """Update an existing provisioning service&#39;s tags.

    Update an existing provisioning service&#39;s tags. to update other fields use the CreateOrUpdate method

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param provisioning_service_name: Name of provisioning service to create or update.
    :type provisioning_service_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param provisioning_service_tags: Updated tag information to set into the provisioning service instance.
    :type provisioning_service_tags: dict | bytes

    """
    provisioning_service_tags = TagsResource.from_dict(provisioning_service_tags)
    return web.Response(status=200)

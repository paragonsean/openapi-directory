from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_security_group import ApplicationSecurityGroup
from openapi_server.models.application_security_groups_update_tags_request import ApplicationSecurityGroupsUpdateTagsRequest
from openapi_server import util


async def application_security_groups_update_tags(request: web.Request, resource_group_name, application_security_group_name, api_version, subscription_id, parameters) -> web.Response:
    """application_security_groups_update_tags

    Updates an application security group&#39;s tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_security_group_name: The name of the application security group.
    :type application_security_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update application security group tags.
    :type parameters: dict | bytes

    """
    parameters = ApplicationSecurityGroupsUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)

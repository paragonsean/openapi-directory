from typing import List, Dict
from aiohttp import web

from openapi_server.models.arm_template import ArmTemplate
from openapi_server.models.arm_template_list import ArmTemplateList
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def arm_templates_get(request: web.Request, subscription_id, resource_group_name, lab_name, artifact_source_name, name, api_version, expand=None) -> web.Response:
    """arm_templates_get

    Get azure resource manager template.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param artifact_source_name: The name of the artifact source.
    :type artifact_source_name: str
    :param name: The name of the azure resource manager template.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def arm_templates_list(request: web.Request, subscription_id, resource_group_name, lab_name, artifact_source_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """arm_templates_list

    List azure resource manager templates in a given artifact source.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param artifact_source_name: The name of the artifact source.
    :type artifact_source_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;)
    :type filter: str
    :param top: The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39;
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39;
    :type orderby: str

    """
    return web.Response(status=200)

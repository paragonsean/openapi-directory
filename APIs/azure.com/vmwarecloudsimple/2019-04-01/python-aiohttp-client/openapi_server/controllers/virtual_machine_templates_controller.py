from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.virtual_machine_template import VirtualMachineTemplate
from openapi_server.models.virtual_machine_template_list_response import VirtualMachineTemplateListResponse
from openapi_server import util


async def virtual_machine_templates_get(request: web.Request, subscription_id, region_id, pc_name, virtual_machine_template_name, api_version) -> web.Response:
    """Implements virtual machine template GET method

    Returns virtual machine templates by its name

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param virtual_machine_template_name: virtual machine template id (vsphereId)
    :type virtual_machine_template_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machine_templates_list(request: web.Request, subscription_id, api_version, pc_name, region_id, resource_pool_name) -> web.Response:
    """Implements list of available VM templates

    Returns list of virtual machine templates in region for private cloud

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param resource_pool_name: Resource pool used to derive vSphere cluster which contains VM templates
    :type resource_pool_name: str

    """
    return web.Response(status=200)

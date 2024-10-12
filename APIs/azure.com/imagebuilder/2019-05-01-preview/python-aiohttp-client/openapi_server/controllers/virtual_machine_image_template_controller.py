from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.image_template import ImageTemplate
from openapi_server.models.image_template_list_result import ImageTemplateListResult
from openapi_server.models.image_template_update_parameters import ImageTemplateUpdateParameters
from openapi_server.models.run_output import RunOutput
from openapi_server.models.run_output_collection import RunOutputCollection
from openapi_server import util


async def virtual_machine_image_templates_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, image_template_name, parameters) -> web.Response:
    """virtual_machine_image_templates_create_or_update

    Create or update a virtual machine image template

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_template_name: The name of the image Template
    :type image_template_name: str
    :param parameters: Parameters supplied to the CreateImageTemplate operation
    :type parameters: dict | bytes

    """
    parameters = ImageTemplate.from_dict(parameters)
    return web.Response(status=200)


async def virtual_machine_image_templates_delete(request: web.Request, api_version, subscription_id, resource_group_name, image_template_name) -> web.Response:
    """virtual_machine_image_templates_delete

    Delete a virtual machine image template

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_template_name: The name of the image Template
    :type image_template_name: str

    """
    return web.Response(status=200)


async def virtual_machine_image_templates_get(request: web.Request, api_version, subscription_id, resource_group_name, image_template_name) -> web.Response:
    """virtual_machine_image_templates_get

    Get information about a virtual machine image template

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_template_name: The name of the image Template
    :type image_template_name: str

    """
    return web.Response(status=200)


async def virtual_machine_image_templates_get_run_output(request: web.Request, api_version, subscription_id, resource_group_name, image_template_name, run_output_name) -> web.Response:
    """virtual_machine_image_templates_get_run_output

    Get the specified run output for the specified image template resource

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_template_name: The name of the image Template
    :type image_template_name: str
    :param run_output_name: The name of the run output
    :type run_output_name: str

    """
    return web.Response(status=200)


async def virtual_machine_image_templates_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """virtual_machine_image_templates_list

    Gets information about the VM image templates associated with the subscription.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machine_image_templates_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """virtual_machine_image_templates_list_by_resource_group

    Gets information about the VM image templates associated with the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_machine_image_templates_list_run_outputs(request: web.Request, api_version, subscription_id, resource_group_name, image_template_name) -> web.Response:
    """virtual_machine_image_templates_list_run_outputs

    List all run outputs for the specified Image Template resource

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_template_name: The name of the image Template
    :type image_template_name: str

    """
    return web.Response(status=200)


async def virtual_machine_image_templates_run(request: web.Request, api_version, subscription_id, resource_group_name, image_template_name) -> web.Response:
    """virtual_machine_image_templates_run

    Create artifacts from a existing image template

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_template_name: The name of the image Template
    :type image_template_name: str

    """
    return web.Response(status=200)


async def virtual_machine_image_templates_update(request: web.Request, subscription_id, resource_group_name, image_template_name, api_version, parameters) -> web.Response:
    """virtual_machine_image_templates_update

    Update the tags for this Virtual Machine Image Template

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_template_name: The name of the image Template
    :type image_template_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Additional parameters for Image Template update.
    :type parameters: dict | bytes

    """
    parameters = ImageTemplateUpdateParameters.from_dict(parameters)
    return web.Response(status=200)

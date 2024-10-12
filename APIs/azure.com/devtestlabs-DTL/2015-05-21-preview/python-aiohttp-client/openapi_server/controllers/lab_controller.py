from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.generate_upload_uri_parameter import GenerateUploadUriParameter
from openapi_server.models.generate_upload_uri_response import GenerateUploadUriResponse
from openapi_server.models.lab import Lab
from openapi_server.models.lab_virtual_machine import LabVirtualMachine
from openapi_server.models.response_with_continuation_lab import ResponseWithContinuationLab
from openapi_server.models.response_with_continuation_lab_vhd import ResponseWithContinuationLabVhd
from openapi_server import util


async def lab_create_environment(request: web.Request, subscription_id, resource_group_name, name, api_version, lab_virtual_machine) -> web.Response:
    """lab_create_environment

    Create virtual machines in a Lab. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_virtual_machine: 
    :type lab_virtual_machine: dict | bytes

    """
    lab_virtual_machine = LabVirtualMachine.from_dict(lab_virtual_machine)
    return web.Response(status=200)


async def lab_create_or_update_resource(request: web.Request, subscription_id, resource_group_name, name, api_version, lab) -> web.Response:
    """lab_create_or_update_resource

    Create or replace an existing Lab. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab: 
    :type lab: dict | bytes

    """
    lab = Lab.from_dict(lab)
    return web.Response(status=200)


async def lab_delete_resource(request: web.Request, subscription_id, resource_group_name, name, api_version) -> web.Response:
    """lab_delete_resource

    Delete lab. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def lab_generate_upload_uri(request: web.Request, subscription_id, resource_group_name, name, api_version, generate_upload_uri_parameter) -> web.Response:
    """lab_generate_upload_uri

    Generate a URI for uploading custom disk images to a Lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param generate_upload_uri_parameter: 
    :type generate_upload_uri_parameter: dict | bytes

    """
    generate_upload_uri_parameter = GenerateUploadUriParameter.from_dict(generate_upload_uri_parameter)
    return web.Response(status=200)


async def lab_get_resource(request: web.Request, subscription_id, resource_group_name, name, api_version) -> web.Response:
    """lab_get_resource

    Get lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def lab_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """lab_list_by_resource_group

    List labs.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)


async def lab_list_by_subscription(request: web.Request, subscription_id, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """lab_list_by_subscription

    List labs.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)


async def lab_list_vhds(request: web.Request, subscription_id, resource_group_name, name, api_version) -> web.Response:
    """lab_list_vhds

    List disk images available for custom image creation.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def lab_patch_resource(request: web.Request, subscription_id, resource_group_name, name, api_version, lab) -> web.Response:
    """lab_patch_resource

    Modify properties of labs.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab: 
    :type lab: dict | bytes

    """
    lab = Lab.from_dict(lab)
    return web.Response(status=200)

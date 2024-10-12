from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.export_resource_usage_parameters import ExportResourceUsageParameters
from openapi_server.models.generate_upload_uri_parameter import GenerateUploadUriParameter
from openapi_server.models.generate_upload_uri_response import GenerateUploadUriResponse
from openapi_server.models.lab import Lab
from openapi_server.models.lab_fragment import LabFragment
from openapi_server.models.lab_virtual_machine_creation_parameter import LabVirtualMachineCreationParameter
from openapi_server.models.response_with_continuation_lab import ResponseWithContinuationLab
from openapi_server.models.response_with_continuation_lab_vhd import ResponseWithContinuationLabVhd
from openapi_server import util


async def labs_claim_any_vm(request: web.Request, subscription_id, resource_group_name, name, api_version) -> web.Response:
    """labs_claim_any_vm

    Claim a random claimable virtual machine in the lab. This operation can take a while to complete.

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


async def labs_create_environment(request: web.Request, subscription_id, resource_group_name, name, api_version, lab_virtual_machine_creation_parameter) -> web.Response:
    """labs_create_environment

    Create virtual machines in a lab. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_virtual_machine_creation_parameter: Properties for creating a virtual machine.
    :type lab_virtual_machine_creation_parameter: dict | bytes

    """
    lab_virtual_machine_creation_parameter = LabVirtualMachineCreationParameter.from_dict(lab_virtual_machine_creation_parameter)
    return web.Response(status=200)


async def labs_create_or_update(request: web.Request, subscription_id, resource_group_name, name, api_version, lab) -> web.Response:
    """labs_create_or_update

    Create or replace an existing lab. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab: A lab.
    :type lab: dict | bytes

    """
    lab = Lab.from_dict(lab)
    return web.Response(status=200)


async def labs_delete(request: web.Request, subscription_id, resource_group_name, name, api_version) -> web.Response:
    """labs_delete

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


async def labs_export_resource_usage(request: web.Request, subscription_id, resource_group_name, name, api_version, export_resource_usage_parameters) -> web.Response:
    """labs_export_resource_usage

    Exports the lab resource usage into a storage account This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param export_resource_usage_parameters: The parameters of the export operation.
    :type export_resource_usage_parameters: dict | bytes

    """
    export_resource_usage_parameters = ExportResourceUsageParameters.from_dict(export_resource_usage_parameters)
    return web.Response(status=200)


async def labs_generate_upload_uri(request: web.Request, subscription_id, resource_group_name, name, api_version, generate_upload_uri_parameter) -> web.Response:
    """labs_generate_upload_uri

    Generate a URI for uploading custom disk images to a Lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param generate_upload_uri_parameter: Properties for generating an upload URI.
    :type generate_upload_uri_parameter: dict | bytes

    """
    generate_upload_uri_parameter = GenerateUploadUriParameter.from_dict(generate_upload_uri_parameter)
    return web.Response(status=200)


async def labs_get(request: web.Request, subscription_id, resource_group_name, name, api_version, expand=None) -> web.Response:
    """labs_get

    Get lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;defaultStorageAccount)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def labs_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """labs_list_by_resource_group

    List labs in a resource group.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;defaultStorageAccount)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def labs_list_by_subscription(request: web.Request, subscription_id, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """labs_list_by_subscription

    List labs in a subscription.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;defaultStorageAccount)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def labs_list_vhds(request: web.Request, subscription_id, resource_group_name, name, api_version) -> web.Response:
    """labs_list_vhds

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


async def labs_update(request: web.Request, subscription_id, resource_group_name, name, api_version, lab) -> web.Response:
    """labs_update

    Modify properties of labs.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param name: The name of the lab.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab: A lab.
    :type lab: dict | bytes

    """
    lab = LabFragment.from_dict(lab)
    return web.Response(status=200)

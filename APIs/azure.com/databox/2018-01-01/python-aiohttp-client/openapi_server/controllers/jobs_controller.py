from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancellation_reason import CancellationReason
from openapi_server.models.job_resource import JobResource
from openapi_server.models.job_resource_list import JobResourceList
from openapi_server.models.job_resource_update_parameter import JobResourceUpdateParameter
from openapi_server.models.shipment_pick_up_request import ShipmentPickUpRequest
from openapi_server.models.shipment_pick_up_response import ShipmentPickUpResponse
from openapi_server.models.unencrypted_credentials_list import UnencryptedCredentialsList
from openapi_server import util


async def jobs_book_shipment_pick_up(request: web.Request, subscription_id, resource_group_name, job_name, api_version, shipment_pick_up_request) -> web.Response:
    """jobs_book_shipment_pick_up

    Book shipment pick up.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type job_name: str
    :param api_version: The API Version
    :type api_version: str
    :param shipment_pick_up_request: Details of shipment pick up request.
    :type shipment_pick_up_request: dict | bytes

    """
    shipment_pick_up_request = ShipmentPickUpRequest.from_dict(shipment_pick_up_request)
    return web.Response(status=200)


async def jobs_cancel(request: web.Request, subscription_id, resource_group_name, job_name, api_version, cancellation_reason) -> web.Response:
    """jobs_cancel

    CancelJob.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type job_name: str
    :param api_version: The API Version
    :type api_version: str
    :param cancellation_reason: Reason for cancellation.
    :type cancellation_reason: dict | bytes

    """
    cancellation_reason = CancellationReason.from_dict(cancellation_reason)
    return web.Response(status=200)


async def jobs_create(request: web.Request, subscription_id, resource_group_name, job_name, api_version, job_resource) -> web.Response:
    """jobs_create

    Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type job_name: str
    :param api_version: The API Version
    :type api_version: str
    :param job_resource: Job details from request body.
    :type job_resource: dict | bytes

    """
    job_resource = JobResource.from_dict(job_resource)
    return web.Response(status=200)


async def jobs_delete(request: web.Request, subscription_id, resource_group_name, job_name, api_version) -> web.Response:
    """jobs_delete

    Deletes a job.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type job_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_get(request: web.Request, subscription_id, resource_group_name, job_name, api_version, expand=None) -> web.Response:
    """jobs_get

    Gets information about the specified job.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type job_name: str
    :param api_version: The API Version
    :type api_version: str
    :param expand: $expand is supported on details parameter for job, which provides details on the job stages.
    :type expand: str

    """
    return web.Response(status=200)


async def jobs_list(request: web.Request, subscription_id, api_version, skip_token=None) -> web.Response:
    """jobs_list

    Lists all the jobs available under the subscription.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param api_version: The API Version
    :type api_version: str
    :param skip_token: $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.
    :type skip_token: str

    """
    return web.Response(status=200)


async def jobs_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, skip_token=None) -> web.Response:
    """jobs_list_by_resource_group

    Lists all the jobs available under the given resource group.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param api_version: The API Version
    :type api_version: str
    :param skip_token: $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.
    :type skip_token: str

    """
    return web.Response(status=200)


async def jobs_list_credentials(request: web.Request, subscription_id, resource_group_name, job_name, api_version) -> web.Response:
    """jobs_list_credentials

    This method gets the unencrypted secrets related to the job.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type job_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_update(request: web.Request, subscription_id, resource_group_name, job_name, api_version, job_resource_update_parameter, if_match=None) -> web.Response:
    """jobs_update

    Updates the properties of an existing job.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type job_name: str
    :param api_version: The API Version
    :type api_version: str
    :param job_resource_update_parameter: Job update parameters from request body.
    :type job_resource_update_parameter: dict | bytes
    :param if_match: Defines the If-Match condition. The patch will be performed only if the ETag of the job on the server matches this value.
    :type if_match: str

    """
    job_resource_update_parameter = JobResourceUpdateParameter.from_dict(job_resource_update_parameter)
    return web.Response(status=200)

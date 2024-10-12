from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_bit_locker_keys_response import GetBitLockerKeysResponse
from openapi_server.models.job_response import JobResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.location import Location
from openapi_server.models.locations_response import LocationsResponse
from openapi_server.models.put_job_parameters import PutJobParameters
from openapi_server.models.update_job_parameters import UpdateJobParameters
from openapi_server import util


async def bit_locker_keys_list(request: web.Request, job_name, subscription_id, resource_group_name, api_version, accept_language=None) -> web.Response:
    """bit_locker_keys_list

    Returns the BitLocker Keys for all drives in the specified job.

    :param job_name: The name of the import/export job.
    :type job_name: str
    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param resource_group_name: The resource group name uniquely identifies the resource group within the user subscription.
    :type resource_group_name: str
    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    return web.Response(status=200)


async def jobs_create(request: web.Request, job_name, subscription_id, resource_group_name, api_version, body, accept_language=None, x_ms_client_tenant_id=None) -> web.Response:
    """jobs_create

    Creates a new job or updates an existing job in the specified subscription.

    :param job_name: The name of the import/export job.
    :type job_name: str
    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param resource_group_name: The resource group name uniquely identifies the resource group within the user subscription.
    :type resource_group_name: str
    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param body: The parameters used for creating the job
    :type body: dict | bytes
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str
    :param x_ms_client_tenant_id: The tenant ID of the client making the request.
    :type x_ms_client_tenant_id: str

    """
    body = PutJobParameters.from_dict(body)
    return web.Response(status=200)


async def jobs_delete(request: web.Request, job_name, subscription_id, resource_group_name, api_version, accept_language=None) -> web.Response:
    """jobs_delete

    Deletes an existing job. Only jobs in the Creating or Completed states can be deleted.

    :param job_name: The name of the import/export job.
    :type job_name: str
    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param resource_group_name: The resource group name uniquely identifies the resource group within the user subscription.
    :type resource_group_name: str
    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    return web.Response(status=200)


async def jobs_get(request: web.Request, job_name, subscription_id, resource_group_name, api_version, accept_language=None) -> web.Response:
    """jobs_get

    Gets information about an existing job.

    :param job_name: The name of the import/export job.
    :type job_name: str
    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param resource_group_name: The resource group name uniquely identifies the resource group within the user subscription.
    :type resource_group_name: str
    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    return web.Response(status=200)


async def jobs_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, top=None, filter=None, accept_language=None) -> web.Response:
    """jobs_list_by_resource_group

    Returns all active and completed jobs in a resource group.

    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param resource_group_name: The resource group name uniquely identifies the resource group within the user subscription.
    :type resource_group_name: str
    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param top: An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100.
    :type top: int
    :param filter: Can be used to restrict the results to certain conditions.
    :type filter: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    return web.Response(status=200)


async def jobs_list_by_subscription(request: web.Request, subscription_id, api_version, top=None, filter=None, accept_language=None) -> web.Response:
    """jobs_list_by_subscription

    Returns all active and completed jobs in a subscription.

    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param top: An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100.
    :type top: int
    :param filter: Can be used to restrict the results to certain conditions.
    :type filter: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    return web.Response(status=200)


async def jobs_update(request: web.Request, job_name, subscription_id, resource_group_name, api_version, body, accept_language=None) -> web.Response:
    """jobs_update

    Updates specific properties of a job. You can call this operation to notify the Import/Export service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also be used to cancel an existing job.

    :param job_name: The name of the import/export job.
    :type job_name: str
    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param resource_group_name: The resource group name uniquely identifies the resource group within the user subscription.
    :type resource_group_name: str
    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param body: The parameters to update in the job
    :type body: dict | bytes
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    body = UpdateJobParameters.from_dict(body)
    return web.Response(status=200)


async def locations_get(request: web.Request, location_name, api_version, accept_language=None) -> web.Response:
    """locations_get

    Returns the details about a location to which you can ship the disks associated with an import or export job. A location is an Azure region.

    :param location_name: The name of the location. For example, West US or westus.
    :type location_name: str
    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    return web.Response(status=200)


async def locations_list(request: web.Request, api_version, accept_language=None) -> web.Response:
    """locations_list

    Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region.

    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version, accept_language=None) -> web.Response:
    """operations_list

    Returns the list of operations supported by the import/export resource provider.

    :param api_version: Specifies the API version to use for this request.
    :type api_version: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str

    """
    return web.Response(status=200)

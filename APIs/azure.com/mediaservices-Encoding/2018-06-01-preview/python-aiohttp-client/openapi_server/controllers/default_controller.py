from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.job import Job
from openapi_server.models.job_collection import JobCollection
from openapi_server.models.transform import Transform
from openapi_server.models.transform_collection import TransformCollection
from openapi_server import util


async def jobs_cancel_job(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, job_name, api_version) -> web.Response:
    """Cancel Job

    Cancel a Job.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param job_name: The Job name.
    :type job_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_create(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, job_name, api_version, parameters) -> web.Response:
    """Create Job

    Creates a Job.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param job_name: The Job name.
    :type job_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = Job.from_dict(parameters)
    return web.Response(status=200)


async def jobs_delete(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, job_name, api_version) -> web.Response:
    """Delete Job

    Deletes a Job.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param job_name: The Job name.
    :type job_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_get(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, job_name, api_version) -> web.Response:
    """Get Job

    Gets a Job.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param job_name: The Job name.
    :type job_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def jobs_list(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, api_version, filter=None, top=None, skip=None) -> web.Response:
    """List Jobs

    Lists all of the Jobs for the Transform.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param filter: Restricts the set of items returned.
    :type filter: str
    :param top: Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    :type top: int
    :param skip: Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1.
    :type skip: int

    """
    return web.Response(status=200)


async def transforms_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, api_version, parameters) -> web.Response:
    """Create or Update Transform

    Creates or updates a new Transform.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = Transform.from_dict(parameters)
    return web.Response(status=200)


async def transforms_delete(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, api_version) -> web.Response:
    """Delete Transform

    Deletes a Transform.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def transforms_get(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, api_version) -> web.Response:
    """Get Transform

    Gets a Transform.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def transforms_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version, filter=None, top=None, skip=None) -> web.Response:
    """List Transforms

    Lists the Transforms in the account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param filter: Restricts the set of items returned.
    :type filter: str
    :param top: Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    :type top: int
    :param skip: Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1.
    :type skip: int

    """
    return web.Response(status=200)


async def transforms_update(request: web.Request, subscription_id, resource_group_name, account_name, transform_name, api_version, parameters) -> web.Response:
    """Update Transform

    Updates a Transform.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param transform_name: The Transform name.
    :type transform_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = Transform.from_dict(parameters)
    return web.Response(status=200)

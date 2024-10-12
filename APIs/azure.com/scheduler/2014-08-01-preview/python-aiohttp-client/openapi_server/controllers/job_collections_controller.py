from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_collection_definition import JobCollectionDefinition
from openapi_server.models.job_collection_list_result import JobCollectionListResult
from openapi_server import util


async def job_collections_create_or_update(request: web.Request, subscription_id, resource_group_name, job_collection_name, api_version, job_collection) -> web.Response:
    """job_collections_create_or_update

    Provisions a new job collection or updates an existing job collection.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param api_version: The API version.
    :type api_version: str
    :param job_collection: The job collection definition.
    :type job_collection: dict | bytes

    """
    job_collection = JobCollectionDefinition.from_dict(job_collection)
    return web.Response(status=200)


async def job_collections_delete(request: web.Request, subscription_id, resource_group_name, job_collection_name, api_version) -> web.Response:
    """job_collections_delete

    Deletes a job collection.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_collections_disable(request: web.Request, subscription_id, resource_group_name, job_collection_name, api_version) -> web.Response:
    """job_collections_disable

    Disables all of the jobs in the job collection.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_collections_enable(request: web.Request, subscription_id, resource_group_name, job_collection_name, api_version) -> web.Response:
    """job_collections_enable

    Enables all of the jobs in the job collection.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_collections_get(request: web.Request, subscription_id, resource_group_name, job_collection_name, api_version) -> web.Response:
    """job_collections_get

    Gets a job collection.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_collections_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """job_collections_list_by_resource_group

    Gets all job collections under specified resource group.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_collections_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """job_collections_list_by_subscription

    Gets all job collections under specified subscription.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_collections_patch(request: web.Request, subscription_id, resource_group_name, job_collection_name, api_version, job_collection) -> web.Response:
    """job_collections_patch

    Patches an existing job collection.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param job_collection_name: The job collection name.
    :type job_collection_name: str
    :param api_version: The API version.
    :type api_version: str
    :param job_collection: The job collection definition.
    :type job_collection: dict | bytes

    """
    job_collection = JobCollectionDefinition.from_dict(job_collection)
    return web.Response(status=200)

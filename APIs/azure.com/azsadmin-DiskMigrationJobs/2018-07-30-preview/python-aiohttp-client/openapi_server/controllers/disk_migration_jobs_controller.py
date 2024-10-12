from typing import List, Dict
from aiohttp import web

from openapi_server.models.disk_migration_jobs_create_request_inner import DiskMigrationJobsCreateRequestInner
from openapi_server.models.disk_migration_jobs_get200_response import DiskMigrationJobsGet200Response
from openapi_server.models.disk_migration_jobs_list200_response import DiskMigrationJobsList200Response
from openapi_server import util


async def disk_migration_jobs_cancel(request: web.Request, subscription_id, location, migration_id, api_version) -> web.Response:
    """disk_migration_jobs_cancel

    Cancel a disk migration job.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param migration_id: The migration job guid name.
    :type migration_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disk_migration_jobs_create(request: web.Request, subscription_id, location, migration_id, target_share, api_version, disks) -> web.Response:
    """disk_migration_jobs_create

    Create a disk migration job.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param migration_id: The migration job guid name.
    :type migration_id: str
    :param target_share: The target share name.
    :type target_share: str
    :param api_version: Client API Version.
    :type api_version: str
    :param disks: The parameters of disk list.
    :type disks: list | bytes

    """
    disks = [DiskMigrationJobsCreateRequestInner.from_dict(d) for d in disks]
    return web.Response(status=200)


async def disk_migration_jobs_get(request: web.Request, subscription_id, location, migration_id, api_version) -> web.Response:
    """disk_migration_jobs_get

    Returns the requested disk migration job.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param migration_id: The migration job guid name.
    :type migration_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def disk_migration_jobs_list(request: web.Request, subscription_id, location, api_version, status=None) -> web.Response:
    """disk_migration_jobs_list

    Returns a list of disk migration jobs.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param status: The parameters of disk migration job status.
    :type status: str

    """
    return web.Response(status=200)

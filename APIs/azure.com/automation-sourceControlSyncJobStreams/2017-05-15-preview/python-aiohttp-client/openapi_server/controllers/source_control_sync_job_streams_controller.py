from typing import List, Dict
from aiohttp import web

from openapi_server.models.source_control_sync_job_stream_by_id import SourceControlSyncJobStreamById
from openapi_server.models.source_control_sync_job_streams_list_by_sync_job import SourceControlSyncJobStreamsListBySyncJob
from openapi_server.models.source_control_sync_job_streams_list_by_sync_job_default_response import SourceControlSyncJobStreamsListBySyncJobDefaultResponse
from openapi_server import util


async def source_control_sync_job_streams_get(request: web.Request, resource_group_name, automation_account_name, source_control_name, source_control_sync_job_id, stream_id, subscription_id, api_version) -> web.Response:
    """source_control_sync_job_streams_get

    Retrieve a sync job stream identified by stream id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The source control name.
    :type source_control_name: str
    :param source_control_sync_job_id: The source control sync job id.
    :type source_control_sync_job_id: str
    :type source_control_sync_job_id: str
    :param stream_id: The id of the sync job stream.
    :type stream_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def source_control_sync_job_streams_list_by_sync_job(request: web.Request, resource_group_name, automation_account_name, source_control_name, source_control_sync_job_id, subscription_id, api_version, filter=None) -> web.Response:
    """source_control_sync_job_streams_list_by_sync_job

    Retrieve a list of sync job streams identified by sync job id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The source control name.
    :type source_control_name: str
    :param source_control_sync_job_id: The source control sync job id.
    :type source_control_sync_job_id: str
    :type source_control_sync_job_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)

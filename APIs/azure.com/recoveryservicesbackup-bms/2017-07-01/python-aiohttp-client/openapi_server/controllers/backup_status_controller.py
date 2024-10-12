from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_status_request import BackupStatusRequest
from openapi_server.models.backup_status_response import BackupStatusResponse
from openapi_server import util


async def backup_status_get(request: web.Request, api_version, azure_region, subscription_id, parameters) -> web.Response:
    """Get the container backup status

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param azure_region: Azure region to hit Api
    :type azure_region: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param parameters: Container Backup Status Request
    :type parameters: dict | bytes

    """
    parameters = BackupStatusRequest.from_dict(parameters)
    return web.Response(status=200)

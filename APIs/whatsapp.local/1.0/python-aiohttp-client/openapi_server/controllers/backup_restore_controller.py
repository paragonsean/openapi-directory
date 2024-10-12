from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_settings_request_body import BackupSettingsRequestBody
from openapi_server.models.backup_settings_response import BackupSettingsResponse
from openapi_server.models.restore_settings_request_body import RestoreSettingsRequestBody
from openapi_server import util


async def backup_settings(request: web.Request, body) -> web.Response:
    """Backup-Settings

    

    :param body: 
    :type body: dict | bytes

    """
    body = BackupSettingsRequestBody.from_dict(body)
    return web.Response(status=200)


async def restore_settings(request: web.Request, body) -> web.Response:
    """Restore-Settings

    

    :param body: 
    :type body: dict | bytes

    """
    body = RestoreSettingsRequestBody.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup import Backup
from openapi_server.models.backup_list import BackupList
from openapi_server.models.restore_options import RestoreOptions
from openapi_server import util


async def backups_get(request: web.Request, subscription_id, resource_group_name, location, backup, api_version) -> web.Response:
    """backups_get

    Returns a backup from a location based on name.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Name of the backup location.
    :type location: str
    :param backup: Name of the backup.
    :type backup: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def backups_list(request: web.Request, subscription_id, resource_group_name, location, api_version) -> web.Response:
    """backups_list

    Returns a list of backups from a location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Name of the backup location.
    :type location: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def backups_restore(request: web.Request, subscription_id, location, resource_group_name, backup, api_version, restore_options) -> web.Response:
    """backups_restore

    Restore a backup.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Name of the backup location.
    :type location: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param backup: Name of the backup.
    :type backup: str
    :param api_version: Client API version.
    :type api_version: str
    :param restore_options: Restore options.
    :type restore_options: dict | bytes

    """
    restore_options = RestoreOptions.from_dict(restore_options)
    return web.Response(status=200)

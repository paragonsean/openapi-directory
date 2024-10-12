from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_sync_status import CompanySyncStatus
from openapi_server import util


async def get_last_successful_sync(request: web.Request, company_id) -> web.Response:
    """Last successful sync

    Gets the status of the last successfull sync

    :param company_id: 
    :type company_id: str
    :type company_id: str

    """
    return web.Response(status=200)


async def get_latest_sync(request: web.Request, company_id) -> web.Response:
    """Latest sync status

    Gets the latest sync status

    :param company_id: 
    :type company_id: str
    :type company_id: str

    """
    return web.Response(status=200)


async def get_sync_by_id(request: web.Request, company_id, sync_id) -> web.Response:
    """Get Sync status

    Get the sync status for a specified sync

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param sync_id: Unique identifier for a sync.
    :type sync_id: str
    :type sync_id: str

    """
    return web.Response(status=200)


async def list_syncs(request: web.Request, company_id) -> web.Response:
    """List sync statuses

    Gets a list of sync statuses

    :param company_id: 
    :type company_id: str
    :type company_id: str

    """
    return web.Response(status=200)
